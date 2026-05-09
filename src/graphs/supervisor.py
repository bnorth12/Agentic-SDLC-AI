"""Supervisor graph orchestrating the multi-agent system."""

from __future__ import annotations

from typing import Any

from langgraph.graph import StateGraph

from src.agents import (
    ArchitectureAgent,
    ChiefComplianceOfficerAgent,
    ChiefEngineerAgent,
    ChiefSafetyOfficerAgent,
    ChiefSecurityOfficerAgent,
    CyberArchitectAgent,
    IntegrationManagerAgent,
    OperationsLeadAgent,
    ProgramManagerAgent,
    QAManagerAgent,
    RequirementsAgent,
    SoftwareQualityManagerAgent,
)
from src.boards import ArchitectureReviewBoard
from src.gates import (
    evaluate_architecture_gate,
    evaluate_deployment_gate,
    evaluate_implementation_gate,
    evaluate_requirements_gate,
)
from src.metrics import KPITracker
from src.state.persistence import get_persistence_manager
from src.state.schema import AgentState, Phase
from src.tools.governance_validation import validate_outputs
from src.utils.logging import get_logger

logger = get_logger(__name__)


# Global KPI tracker instance
_kpi_tracker: KPITracker | None = None


def get_kpi_tracker() -> KPITracker:
    """Get the global KPI tracker instance."""
    global _kpi_tracker
    if _kpi_tracker is None:
        _kpi_tracker = KPITracker()
    return _kpi_tracker


def _save_checkpoint_snapshot(state: AgentState, updates: dict[str, Any]) -> None:
    """Persist a lightweight in-memory checkpoint snapshot for session resume."""
    session_id = state.metadata.session_id
    if not session_id:
        return

    try:
        payload = state.model_dump(mode="python")
        payload.update(updates)
        get_persistence_manager().save_checkpoint_snapshot(session_id, payload)
    except Exception as exc:  # pragma: no cover - defensive logging only
        logger.warning("Unable to save checkpoint snapshot: %s", exc)


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
        _save_checkpoint_snapshot(state, candidate)
        return candidate

    gate_status = str(gate_readiness.get("status", "")).upper()
    if gate_status != "READY":
        _save_checkpoint_snapshot(state, candidate)
        return candidate

    output = _build_governance_output(candidate, source_agent)
    stored_outputs = dict(state.agent_outputs)
    candidate_outputs = candidate.get("agent_outputs")
    if isinstance(candidate_outputs, dict):
        stored_outputs.update(candidate_outputs)
    stored_outputs[source_agent] = output
    candidate["agent_outputs"] = stored_outputs

    report = validate_outputs(
        [output],
        expected_gate=gate_readiness.get("gate"),
        require_strict_ready=True,
    )
    candidate["governance_validation"] = report

    # Record metrics for this gate evaluation
    gate_name = report["results"][0]["gate"] if report["results"] else "unknown"
    evidence_completeness = 1.0 - (
        len(report["results"][0]["missing_evidence_keys"])
        / max(1, len(report["results"][0].get("expected_evidence_keys", [])))
        if report["results"]
        else 0.0
    )
    get_kpi_tracker().record_gate_outcome(
        gate_name=gate_name,
        status="READY" if report["gate_can_be_marked_ready"] else "NOT_READY",
        evidence_completeness=evidence_completeness,
        was_ready_on_first_attempt=True,
    )
    get_kpi_tracker().record_checkpoint_snapshot()

    # Update governance metrics in state
    governance_metrics = dict(candidate.get("governance_metrics", {}))
    governance_metrics["last_gate_evaluation"] = {
        "gate": gate_name,
        "status": "READY" if report["gate_can_be_marked_ready"] else "NOT_READY",
        "evidence_completeness": evidence_completeness,
    }
    governance_metrics["kpi_report"] = get_kpi_tracker().get_metrics_report()
    candidate["governance_metrics"] = governance_metrics

    if report["gate_can_be_marked_ready"]:
        messages = _ensure_messages(candidate)
        messages.append(
            f"[governance_hook] {source_agent} passed validation for "
            f"{report['results'][0]['gate']}"
        )
        _save_checkpoint_snapshot(state, candidate)
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
    _save_checkpoint_snapshot(state, candidate)
    return candidate


def should_continue(state: AgentState) -> str:
    """
    Determine the next node in the graph.

    Args:
        state: Current state

    Returns:
        Next node name
    """
    if state.active_board:
        return "review_board"

    if state.requires_human_approval:
        return "human_approval"

    # Route based on phase with gate checkpoints.
    if state.phase == Phase.INTAKE:
        return "program_manager"

    if state.phase == Phase.REQUIREMENTS:
        if not state.requirements:
            return "requirements_agent"
        return "requirements_gate"

    if state.phase == Phase.ARCHITECTURE:
        if not state.architecture:
            return "architecture_agent"
        return "architecture_gate"

    if state.phase == Phase.DESIGN:
        return "cyber_architect"

    if state.phase == Phase.IMPLEMENTATION:
        assessments = state.agent_outputs
        if "security_assessment" not in assessments:
            return "chief_security_officer"
        if "safety_assessment" not in assessments:
            return "chief_safety_officer"
        if "compliance_assessment" not in assessments:
            return "chief_compliance_officer"
        if "implementation_package" not in assessments:
            return "integration_manager"
        return "implementation_gate"

    if state.phase == Phase.VERIFICATION:
        if "verification_package" not in state.agent_outputs:
            return "qa_manager"
        return "END"

    if state.phase == Phase.DEPLOYMENT:
        if "deployment_package" not in state.agent_outputs:
            return "operations_lead"
        return "deployment_gate"

    if state.phase == Phase.MAINTENANCE:
        if "maintenance_quality_package" not in state.agent_outputs:
            return "software_quality_manager"
        return "END"

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


def cyber_architect_node(state: AgentState) -> dict[str, Any]:
    """Execute cyber architect agent."""
    agent = CyberArchitectAgent()
    return apply_governance_gate_hook(state, agent(state), "cyber_architect")


def chief_security_officer_node(state: AgentState) -> dict[str, Any]:
    """Execute chief security officer agent."""
    agent = ChiefSecurityOfficerAgent()
    return apply_governance_gate_hook(state, agent(state), "chief_security_officer")


def chief_safety_officer_node(state: AgentState) -> dict[str, Any]:
    """Execute chief safety officer agent."""
    agent = ChiefSafetyOfficerAgent()
    return apply_governance_gate_hook(state, agent(state), "chief_safety_officer")


def chief_compliance_officer_node(state: AgentState) -> dict[str, Any]:
    """Execute chief compliance officer agent."""
    agent = ChiefComplianceOfficerAgent()
    return apply_governance_gate_hook(state, agent(state), "chief_compliance_officer")


def integration_manager_node(state: AgentState) -> dict[str, Any]:
    """Execute integration manager agent."""
    agent = IntegrationManagerAgent()
    return apply_governance_gate_hook(state, agent(state), "integration_manager")


def qa_manager_node(state: AgentState) -> dict[str, Any]:
    """Execute QA manager agent."""
    agent = QAManagerAgent()
    return apply_governance_gate_hook(state, agent(state), "qa_manager")


def operations_lead_node(state: AgentState) -> dict[str, Any]:
    """Execute operations lead agent."""
    agent = OperationsLeadAgent()
    return apply_governance_gate_hook(state, agent(state), "operations_lead")


def software_quality_manager_node(state: AgentState) -> dict[str, Any]:
    """Execute software quality manager agent."""
    agent = SoftwareQualityManagerAgent()
    return apply_governance_gate_hook(state, agent(state), "software_quality_manager")


def requirements_gate_node(state: AgentState) -> dict[str, Any]:
    """Execute requirements gate evaluation."""
    return apply_governance_gate_hook(
        state,
        evaluate_requirements_gate(state),
        "requirements_gate",
    )


def architecture_gate_node(state: AgentState) -> dict[str, Any]:
    """Execute architecture gate evaluation."""
    return apply_governance_gate_hook(
        state,
        evaluate_architecture_gate(state),
        "architecture_gate",
    )


def implementation_gate_node(state: AgentState) -> dict[str, Any]:
    """Execute implementation gate evaluation."""
    return apply_governance_gate_hook(
        state,
        evaluate_implementation_gate(state),
        "implementation_gate",
    )


def deployment_gate_node(state: AgentState) -> dict[str, Any]:
    """Execute deployment gate evaluation."""
    return apply_governance_gate_hook(
        state,
        evaluate_deployment_gate(state),
        "deployment_gate",
    )


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


def resume_from_checkpoint(state: AgentState) -> AgentState:
    """
    Resume execution from a checkpoint snapshot.

    If the state has a session_id, attempt to load the last saved checkpoint
    and restore the state to that point. This enables resuming work after
    interruptions or for incremental progress tracking.

    Args:
        state: Current state (may be initial or partial)

    Returns:
        Restored state from checkpoint, or original state if no checkpoint found
    """
    session_id = state.metadata.session_id
    if not session_id:
        logger.debug("No session_id in state metadata; skipping checkpoint restore")
        return state

    try:
        checkpoint = get_persistence_manager().load_checkpoint_snapshot(session_id)
        if checkpoint:
            logger.info(f"Restoring state from checkpoint for session {session_id}")
            # Reconstruct AgentState from checkpoint payload
            restored = AgentState(**checkpoint)
            logger.info(
                f"Restored state: phase={restored.phase}, "
                f"requirements={len(restored.requirements)}, "
                f"work_packages={len(restored.work_packages)}"
            )
            return restored
        else:
            logger.debug(
                f"No checkpoint found for session {session_id}; using current state"
            )
    except Exception as exc:  # pragma: no cover - defensive logging
        logger.warning(f"Unable to restore checkpoint: {exc}; using current state")

    return state


def build_supervisor_graph() -> StateGraph:
    """
    Build the supervisor graph that orchestrates all agents.

    Returns:
        Compiled StateGraph
    """
    workflow = StateGraph(AgentState)

    # Agent and gate nodes
    workflow.add_node("program_manager", program_manager_node)
    workflow.add_node("chief_engineer", chief_engineer_node)
    workflow.add_node("requirements_agent", requirements_node)
    workflow.add_node("architecture_agent", architecture_node)
    workflow.add_node("cyber_architect", cyber_architect_node)
    workflow.add_node("chief_security_officer", chief_security_officer_node)
    workflow.add_node("chief_safety_officer", chief_safety_officer_node)
    workflow.add_node("chief_compliance_officer", chief_compliance_officer_node)
    workflow.add_node("integration_manager", integration_manager_node)
    workflow.add_node("qa_manager", qa_manager_node)
    workflow.add_node("operations_lead", operations_lead_node)
    workflow.add_node("software_quality_manager", software_quality_manager_node)
    workflow.add_node("requirements_gate", requirements_gate_node)
    workflow.add_node("architecture_gate", architecture_gate_node)
    workflow.add_node("implementation_gate", implementation_gate_node)
    workflow.add_node("deployment_gate", deployment_gate_node)
    workflow.add_node("review_board", review_board_node)
    workflow.add_node("human_approval", human_approval_node)

    workflow.set_entry_point("program_manager")

    route_map = {
        "program_manager": "program_manager",
        "chief_engineer": "chief_engineer",
        "requirements_agent": "requirements_agent",
        "architecture_agent": "architecture_agent",
        "cyber_architect": "cyber_architect",
        "chief_security_officer": "chief_security_officer",
        "chief_safety_officer": "chief_safety_officer",
        "chief_compliance_officer": "chief_compliance_officer",
        "integration_manager": "integration_manager",
        "qa_manager": "qa_manager",
        "operations_lead": "operations_lead",
        "software_quality_manager": "software_quality_manager",
        "requirements_gate": "requirements_gate",
        "architecture_gate": "architecture_gate",
        "implementation_gate": "implementation_gate",
        "deployment_gate": "deployment_gate",
        "review_board": "review_board",
        "human_approval": "human_approval",
        "END": "__end__",
    }

    for node_name in [
        "program_manager",
        "chief_engineer",
        "requirements_agent",
        "architecture_agent",
        "cyber_architect",
        "chief_security_officer",
        "chief_safety_officer",
        "chief_compliance_officer",
        "integration_manager",
        "qa_manager",
        "operations_lead",
        "software_quality_manager",
        "requirements_gate",
        "architecture_gate",
        "implementation_gate",
        "deployment_gate",
        "review_board",
        "human_approval",
    ]:
        workflow.add_conditional_edges(node_name, should_continue, route_map)

    graph = workflow.compile()
    logger.info("Supervisor graph compiled successfully")
    return graph
