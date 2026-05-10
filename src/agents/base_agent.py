"""Base agent interface and implementation."""

from __future__ import annotations

import time
from abc import ABC, abstractmethod
from typing import Any

from langchain_core.language_models import BaseChatModel
from langchain_ollama import ChatOllama

from src.config import get_settings
from src.routing import ModelRouter
from src.routing.model_router import ModelRoutingDecision, serialize_routing_payload
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
        self._settings = settings
        self._router = ModelRouter(settings)
        self._runtime_metrics: dict[str, dict[str, float | int]] = {}
        self._uses_custom_model = model is not None
        self._active_model_name = "custom"

        # Get model for this agent's role
        if model is None:
            decision = self._router.choose_model(name, None, self._runtime_metrics)
            model_name = decision.selected_model
            self._active_model_name = model_name
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
            "safety issue",
            "critical safety",
            "critical",
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

    def build_governance_output(
        self,
        gate: str,
        policy_ids: list[str],
        traceability_links: list[dict[str, Any]],
        evidence_links: dict[str, Any],
        risks_or_blockers: list[str] | None = None,
        status: str = "READY",
        notes: str = "",
    ) -> dict[str, Any]:
        """Build a governance output payload and top-level fields for gate validation."""
        payload = {
            "agent": self.name,
            "policy_compliance": {
                "status": "PASS" if status == "READY" else "CONDITIONAL",
                "policies": policy_ids,
            },
            "traceability_links": traceability_links,
            "gate_readiness": {
                "gate": gate,
                "status": status,
                "notes": notes,
            },
            "evidence_links": evidence_links,
            "risks_or_blockers": risks_or_blockers or [],
        }

        return {
            "current_gate": gate,
            "policy_compliance": payload["policy_compliance"],
            "traceability_links": payload["traceability_links"],
            "gate_readiness": payload["gate_readiness"],
            "evidence_links": payload["evidence_links"],
            "risks_or_blockers": payload["risks_or_blockers"],
            "governance_output": payload,
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
        routing_decision = self._resolve_model_for_state(state)
        started = time.perf_counter()

        try:
            updates = self.process(state)
            elapsed = time.perf_counter() - started
            if routing_decision is not None:
                self._record_runtime_result(routing_decision.selected_model, elapsed, False)
                self._attach_routing_metrics(
                    updates,
                    serialize_routing_payload(
                        agent=self.name,
                        decision=routing_decision,
                        duration_seconds=elapsed,
                        failed=False,
                    ),
                )
            self.logger.log_complete("Processing", updates.keys())
            return updates
        except Exception as e:
            elapsed = time.perf_counter() - started
            payload: dict[str, Any] | None = None
            if routing_decision is not None:
                self._record_runtime_result(routing_decision.selected_model, elapsed, True)
                payload = serialize_routing_payload(
                    agent=self.name,
                    decision=routing_decision,
                    duration_seconds=elapsed,
                    failed=True,
                )
            self.logger.log_error("Processing", e)
            error_updates = {
                "messages": [f"[{self.name}] Error: {str(e)}"],
            }
            if payload is not None:
                self._attach_routing_metrics(error_updates, payload)
            return error_updates

    def _resolve_model_for_state(
        self,
        state: AgentState,
    ) -> ModelRoutingDecision | None:
        """Resolve and activate model policy for this execution."""
        if self._uses_custom_model:
            return None

        decision = self._router.choose_model(self.name, state, self._runtime_metrics)
        if decision.selected_model != self._active_model_name:
            self.model = ChatOllama(
                base_url=self._settings.ollama_base_url,
                model=decision.selected_model,
                temperature=self._settings.temperature,
            )
            self._active_model_name = decision.selected_model
        return decision

    def _record_runtime_result(self, model_name: str, elapsed: float, failed: bool) -> None:
        """Maintain lightweight runtime telemetry used for adaptive routing."""
        metrics = self._runtime_metrics.setdefault(
            model_name,
            {
                "calls": 0,
                "errors": 0,
                "total_duration": 0.0,
                "avg_duration": 0.0,
            },
        )
        metrics["calls"] = int(metrics["calls"]) + 1
        metrics["total_duration"] = float(metrics["total_duration"]) + elapsed
        metrics["avg_duration"] = float(metrics["total_duration"]) / int(metrics["calls"])
        if failed:
            metrics["errors"] = int(metrics["errors"]) + 1

    def _attach_routing_metrics(
        self,
        updates: dict[str, Any],
        payload: dict[str, Any],
    ) -> None:
        """Attach model-routing telemetry to state updates for supervisor aggregation."""
        updates["model_routing"] = payload
        governance_metrics = dict(updates.get("governance_metrics", {}))
        governance_metrics["model_routing"] = payload
        updates["governance_metrics"] = governance_metrics
