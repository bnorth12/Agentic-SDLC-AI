"""Base agent interface and implementation."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from langchain_core.language_models import BaseChatModel
from langchain_ollama import ChatOllama

from src.config import get_settings
from src.state.schema import AgentState
from src.utils.logging import AgentLogger


class BaseAgent(ABC):
    """Base class for all specialist agents."""

    def __init__(
        self,
        name: str,
        role: str,
        authority_level: str,
        model: BaseChatModel | None = None,
    ):
        """
        Initialize a base agent.

        Args:
            name: Agent identifier (e.g., "requirements_agent")
            role: Human-readable role (e.g., "Requirements Development Engineer")
            authority_level: Authority level (LOW, MEDIUM, HIGH, HIGHEST)
            model: Language model to use (defaults to configured Ollama model)
        """
        self.name = name
        self.role = role
        self.authority_level = authority_level
        self.logger = AgentLogger(name)

        settings = get_settings()

        # Get model for this agent's role
        if model is None:
            model_name = settings.get_model_for_role(name)
            self.model = ChatOllama(
                base_url=settings.ollama_base_url,
                model=model_name,
                temperature=settings.temperature,
            )
        else:
            self.model = model

    @abstractmethod
    def get_system_prompt(self, state: AgentState) -> str:
        """
        Generate the system prompt for this agent based on current state.

        Args:
            state: Current shared state

        Returns:
            Formatted system prompt
        """
        pass

    @abstractmethod
    def process(self, state: AgentState) -> dict[str, Any]:
        """
        Main processing logic for the agent.

        Args:
            state: Current shared state

        Returns:
            Dictionary of state updates to apply
        """
        pass

    def should_escalate(self, issue: str, state: AgentState) -> bool:
        """
        Determine if an issue should be escalated to leadership.

        Args:
            issue: Description of the issue
            state: Current shared state

        Returns:
            True if escalation is needed
        """
        # Default escalation logic - can be overridden
        escalation_keywords = [
            "unsafe",
            "critical risk",
            "requirement conflict",
            "design flaw",
            "security vulnerability",
        ]

        return any(keyword in issue.lower() for keyword in escalation_keywords)

    def request_review_board(
        self, board_name: str, item: str, rationale: str
    ) -> dict[str, Any]:
        """
        Request a review board evaluation.

        Args:
            board_name: Name of the board to convene
            item: Item to be reviewed
            rationale: Reason for requesting review

        Returns:
            State updates to trigger board review
        """
        self.logger.log_escalation(f"Requesting {board_name} review", board_name)

        return {
            "active_board": board_name,
            "requires_human_approval": True,
            "messages": [
                f"[{self.name}] Requesting {board_name} for: {item}\nRationale: {rationale}"
            ],
        }

    def __call__(self, state: AgentState) -> dict[str, Any]:
        """
        Execute the agent's processing logic.

        Args:
            state: Current shared state

        Returns:
            State updates
        """
        self.logger.log_start(f"Processing in phase: {state.phase}")

        try:
            updates = self.process(state)
            self.logger.log_complete("Processing", updates.keys())
            return updates
        except Exception as e:
            self.logger.log_error("Processing", e)
            return {
                "messages": [f"[{self.name}] Error: {str(e)}"],
            }
