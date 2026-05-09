"""Supervisor graph orchestrating the multi-agent system."""

from __future__ import annotations

from typing import Any

from langgraph.graph import StateGraph

from src.agents import (
    ArchitectureAgent,
    ChiefEngineerAgent,
    ProgramManagerAgent,
    RequirementsAgent,
)
from src.boards import ArchitectureReviewBoard
from src.state.schema import AgentState, Phase
from src.tools.governance_validation import validate_outputs
from src.utils.logging import get_logger

logger = get_logger(__name__)


def _ensure_messages(updates: dict[str, Any]) -> list[str]:
    """Ensure updates has a mutable messages list and return it."""
    messages = updates.get("messages")
    if not isinstance(messages, list):
        messages = []
        updates["messages"] = messages
    return messages


def _build_governance_output(
    updates: dict[str, Any], source_agent: str
) -> dict[str, Any]:
    """Build a governance output payload expected by the validator."""
    provided = updates.get("governance_output")
    if isinstance(provided, dict):
        payload = dict(provided)
        payload.setdefault("agent", source_agent)
        return payload

    return {
        "agent": source_agent,
        "policy_compliance": updates.get("policy_compliance"),
        "traceability_links": updates.get("traceability_links"),
        "gate_readiness": updates.get("gate_readiness"),
        "evidence_links": updates.get("evidence_links"),
        "risks_or_blockers": updates.get("risks_or_blockers", []),
    }


def apply_governance_gate_hook(
    state: AgentState,
    updates: dict[str, Any],
    source_agent: str,
) -> dict[str, Any]:
    """Validate gate readiness claims before allowing READY transitions."""
    if not updates:
        return updates

    candidate = dict(updates)
    gate_readiness = candidate.get("gate_readiness")
    if not isinstance(gate_readiness, dict):
        return candidate

    gate_status = str(gate_readiness.get("status", "")).upper()
    if gate_status != "READY":
        return candidate

    output = _build_governance_output(candidate, source_agent)
    report = validate_outputs(
        [output],
        expected_gate=gate_readiness.get("gate"),
        require_strict_ready=True,
    )
    candidate["governance_validation"] = report

    if report["gate_can_be_marked_ready"]:
        messages = _ensure_messages(candidate)
        messages.append(
            f"[governance_hook] {source_agent} passed validation for "
            f"{report['results'][0]['gate']}"
        )
        return candidate

    # Block READY transition and prevent associated phase transition.
    blocked_readiness = dict(gate_readiness)
    blocked_readiness["status"] = "NOT_READY"
    blocked_readiness["reason"] = "Governance evidence validation failed"
    candidate["gate_readiness"] = blocked_readiness
    candidate.pop("phase", None)
    candidate["requires_human_approval"] = True

    details = report["results"][0]
    issues: list[str] = []
    if details["missing_fields"]:
        issues.append("missing fields: " + ", ".join(details["missing_fields"]))
    if details["invalid_values"]:
        issues.append("invalid values: " + ", ".join(details["invalid_values"]))
    if details["missing_evidence_keys"]:
        issues.append(
            "missing evidence: " + ", ".join(details["missing_evidence_keys"])
        )

    messages = _ensure_messages(candidate)
    messages.append(
        "[governance_hook] READY transition blocked until governance evidence is complete"
    )
    if issues:
        messages.append("[governance_hook] " + " | ".join(issues))

    logger.warning(
        "Blocked READY transition for %s due to governance validation failure",
        source_agent,
    )
    return candidate


def should_continue(state: AgentState) -> str:
    """
    Determine the next node in the graph.

    Args:
        state: Current state

    Returns:
        Next node name
    """
    # Check for active board
    if state.active_board:
        return "review_board"

    # Check for human approval requirement
    if state.requires_human_approval:
        return "human_approval"

    # Stop if current phase artifacts are complete and no review is pending.
    if state.phase == Phase.REQUIREMENTS and state.requirements:
        return "END"
    if state.phase == Phase.ARCHITECTURE and state.architecture:
        return "END"

    # Route based on phase
    if state.phase == Phase.INTAKE:
        return "program_manager"
    elif state.phase == Phase.REQUIREMENTS:
        return "requirements_agent"
    elif state.phase == Phase.ARCHITECTURE:
        return "architecture_agent"
    else:
        return "END"


def program_manager_node(state: AgentState) -> dict[str, Any]:
    """Execute program manager agent."""
    agent = ProgramManagerAgent()
    return apply_governance_gate_hook(state, agent(state), "program_manager")


def chief_engineer_node(state: AgentState) -> dict[str, Any]:
    """Execute chief engineer agent."""
    agent = ChiefEngineerAgent()
    return apply_governance_gate_hook(state, agent(state), "chief_engineer")


def requirements_node(state: AgentState) -> dict[str, Any]:
    """Execute requirements agent."""
    agent = RequirementsAgent()
    return apply_governance_gate_hook(state, agent(state), "requirements_agent")


def architecture_node(state: AgentState) -> dict[str, Any]:
    """Execute architecture agent."""
    agent = ArchitectureAgent()
    return apply_governance_gate_hook(state, agent(state), "architecture_agent")


def review_board_node(state: AgentState) -> dict[str, Any]:
    """Execute review board."""
    if not state.active_board:
        return {}

    logger.info(f"Convening {state.active_board}")

    # Instantiate the appropriate board
    if state.active_board == "architecture_review":
        board = ArchitectureReviewBoard()
        decision = board.evaluate(state, state.architecture)
    else:
        # Placeholder for other boards
        logger.warning(f"Board {state.active_board} not implemented yet")
        return {"active_board": None}

    # Store board decision
    board_results = state.board_results.copy()
    board_results[state.active_board] = decision

    updates = {
        "board_results": board_results,
        "active_board": None,
        "requires_human_approval": True,  # Boards require human review
        "messages": [
            f"[{state.active_board}] Decision: {decision.decision}",
            f"Rationale: {decision.rationale}",
        ],
    }

    # If approved, transition to next phase
    if decision.decision == "approve":
        if state.phase == Phase.REQUIREMENTS:
            updates["phase"] = Phase.ARCHITECTURE
        elif state.phase == Phase.ARCHITECTURE:
            updates["phase"] = Phase.IMPLEMENTATION

    return apply_governance_gate_hook(state, updates, "review_board")


def human_approval_node(state: AgentState) -> dict[str, Any]:
    """
    Human approval gate (simplified - just auto-approves for now).

    In production, this would use HITL utilities to pause and wait for human input.
    """
    logger.info("Human approval checkpoint")

    # For now, auto-approve
    updates = {
        "requires_human_approval": False,
        "human_feedback": "Auto-approved for demo",
        "messages": ["[HUMAN] Approved"],
    }
    return apply_governance_gate_hook(state, updates, "human_approval")


def build_supervisor_graph() -> StateGraph:
    """
    Build the supervisor graph that orchestrates all agents.

    Returns:
        Compiled StateGraph
    """
    # Create graph
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("program_manager", program_manager_node)
    workflow.add_node("chief_engineer", chief_engineer_node)
    workflow.add_node("requirements_agent", requirements_node)
    workflow.add_node("architecture_agent", architecture_node)
    workflow.add_node("review_board", review_board_node)
    workflow.add_node("human_approval", human_approval_node)

    # Set entry point
    workflow.set_entry_point("program_manager")

    # Add conditional edges
    workflow.add_conditional_edges(
        "program_manager",
        should_continue,
        {
            "program_manager": "program_manager",
            "requirements_agent": "requirements_agent",
            "architecture_agent": "architecture_agent",
            "review_board": "review_board",
            "human_approval": "human_approval",
            "END": "__end__",
        },
    )

    workflow.add_conditional_edges(
        "requirements_agent",
        should_continue,
        {
            "program_manager": "program_manager",
            "requirements_agent": "requirements_agent",
            "review_board": "review_board",
            "human_approval": "human_approval",
            "END": "__end__",
        },
    )

    workflow.add_conditional_edges(
        "architecture_agent",
        should_continue,
        {
            "architecture_agent": "architecture_agent",
            "review_board": "review_board",
            "human_approval": "human_approval",
            "END": "__end__",
        },
    )

    workflow.add_conditional_edges(
        "review_board",
        should_continue,
        {
            "program_manager": "program_manager",
            "requirements_agent": "requirements_agent",
            "architecture_agent": "architecture_agent",
            "review_board": "review_board",
            "human_approval": "human_approval",
            "END": "__end__",
        },
    )

    workflow.add_conditional_edges(
        "human_approval",
        should_continue,
        {
            "program_manager": "program_manager",
            "requirements_agent": "requirements_agent",
            "architecture_agent": "architecture_agent",
            "END": "__end__",
        },
    )

    # Compile graph
    graph = workflow.compile()

    logger.info("Supervisor graph compiled successfully")

    return graph
