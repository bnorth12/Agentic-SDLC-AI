"""Test fixtures for reusable test data."""

from src.state.schema import (
    AgentState,
    Decision,
    DecisionStatus,
    Phase,
    Requirement,
    Risk,
    WorkItem,
    WorkItemStatus,
)


def basic_state() -> AgentState:
    """Create a basic AgentState for testing."""
    return AgentState(objective="Test objective")


def state_with_requirements() -> AgentState:
    """Create an AgentState with sample requirements."""
    return AgentState(
        objective="Build a user management system",
        phase=Phase.ARCHITECTURE,
        requirements={
            "REQ-001": Requirement(
                id="REQ-001",
                text="System shall authenticate users via username and password",
                category="functional",
                priority="critical",
                verification_method="test",
                created_by="requirements_agent",
            ),
            "REQ-002": Requirement(
                id="REQ-002",
                text="System shall support role-based access control",
                category="functional",
                priority="high",
                verification_method="test",
                created_by="requirements_agent",
            ),
            "REQ-003": Requirement(
                id="REQ-003",
                text="System shall respond to requests within 200ms",
                category="non-functional",
                priority="medium",
                verification_method="analysis",
                created_by="requirements_agent",
            ),
        },
    )


def state_with_risks() -> AgentState:
    """Create an AgentState with sample risks."""
    return AgentState(
        objective="Build a distributed system",
        risks={
            "RISK-001": Risk(
                id="RISK-001",
                title="Network partition risk",
                description="System may experience network partitions in distributed deployment",
                category="technical",
                probability="medium",
                impact="high",
                mitigation="Implement consensus protocol with automatic failover",
                owner="architecture_agent",
                identified_by="safety_agent",
            ),
        },
    )
