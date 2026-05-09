"""State management for the Agentic SDLC system."""

from src.state.schema import (
    AgentState,
    BoardDecision,
    Decision,
    DecisionStatus,
    Phase,
    Requirement,
    Risk,
    StateMetadata,
    VerificationStatus,
    WorkItem,
    WorkItemStatus,
)

try:
    from src.state.persistence import PersistenceManager, get_persistence_manager
except ModuleNotFoundError:  # Optional dependency may not be installed in all environments.
    PersistenceManager = None  # type: ignore[assignment]

    def get_persistence_manager() -> None:
        """Placeholder when persistence extras are unavailable."""
        raise ModuleNotFoundError(
            "Persistence dependencies are unavailable. Install optional postgres "
            "checkpoint dependencies to use persistence features."
        )

__all__ = [
    "AgentState",
    "BoardDecision",
    "Decision",
    "DecisionStatus",
    "Phase",
    "PersistenceManager",
    "Requirement",
    "Risk",
    "StateMetadata",
    "VerificationStatus",
    "WorkItem",
    "WorkItemStatus",
    "get_persistence_manager",
]