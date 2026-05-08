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
from src.utils.logging import get_logger

logger = get_logger(__name__)


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
    return agent(state)


def chief_engineer_node(state: AgentState) -> dict[str, Any]:
    """Execute chief engineer agent."""
    agent = ChiefEngineerAgent()
    return agent(state)


def requirements_node(state: AgentState) -> dict[str, Any]:
    """Execute requirements agent."""
    agent = RequirementsAgent()
    return agent(state)


def architecture_node(state: AgentState) -> dict[str, Any]:
    """Execute architecture agent."""
    agent = ArchitectureAgent()
    return agent(state)


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

    return updates


def human_approval_node(state: AgentState) -> dict[str, Any]:
    """
    Human approval gate (simplified - just auto-approves for now).

    In production, this would use HITL utilities to pause and wait for human input.
    """
    logger.info("Human approval checkpoint")

    # For now, auto-approve
    return {
        "requires_human_approval": False,
        "human_feedback": "Auto-approved for demo",
        "messages": ["[HUMAN] Approved"],
    }


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
