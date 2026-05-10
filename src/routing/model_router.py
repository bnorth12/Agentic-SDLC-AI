"""Adaptive model routing by role and task complexity."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from src.config import Settings, get_settings
from src.state.schema import AgentState, Phase


@dataclass
class ModelRoutingDecision:
    """Result of a model routing decision."""

    selected_model: str
    candidates: list[str]
    complexity: str
    fallback_used: bool = False
    reason: str = "policy_default"


class ModelRouter:
    """Resolve model selection policies for agent execution."""

    def __init__(self, settings: Settings | None = None):
        self.settings = settings or get_settings()

    def estimate_complexity(self, state: AgentState | None) -> str:
        """Estimate task complexity from active state signals."""
        if state is None:
            return "medium"

        score = 0
        if state.phase in {Phase.ARCHITECTURE, Phase.IMPLEMENTATION, Phase.VERIFICATION}:
            score += 2
        if state.requires_human_approval:
            score += 2

        score += min(3, len(state.requirements) // 5)
        score += min(2, len(state.risks) // 5)
        score += min(2, len(state.work_packages) // 5)
        score += min(2, len(state.agent_outputs) // 8)

        if score >= 6:
            return "high"
        if score >= 3:
            return "medium"
        return "low"

    def choose_model(
        self,
        role: str,
        state: AgentState | None,
        runtime_metrics: dict[str, dict[str, float | int]] | None = None,
    ) -> ModelRoutingDecision:
        """Choose a model for a role using policy and optional runtime metrics."""
        complexity = self.estimate_complexity(state)
        candidates = self.settings.get_model_candidates_for_role(role, complexity)
        selected = candidates[0]
        fallback_used = False
        reason = "policy_default"

        if self.settings.enable_adaptive_model_routing:
            adaptive = self._choose_adaptive_candidate(candidates, complexity, runtime_metrics)
            if adaptive is not None:
                adaptive_model, adaptive_reason = adaptive
                if adaptive_model != selected:
                    selected = adaptive_model
                    fallback_used = True
                    reason = adaptive_reason

        return ModelRoutingDecision(
            selected_model=selected,
            candidates=candidates,
            complexity=complexity,
            fallback_used=fallback_used,
            reason=reason,
        )

    def _choose_adaptive_candidate(
        self,
        candidates: list[str],
        complexity: str,
        runtime_metrics: dict[str, dict[str, float | int]] | None,
    ) -> tuple[str, str] | None:
        """Pick a healthier model candidate when telemetry suggests fallback."""
        if not runtime_metrics or len(candidates) < 2:
            return None

        first = candidates[0]
        first_metrics = runtime_metrics.get(first, {})
        first_calls = int(first_metrics.get("calls", 0))
        first_errors = int(first_metrics.get("errors", 0))
        first_error_rate = (first_errors / first_calls) if first_calls else 0.0

        if first_errors >= self.settings.adaptive_error_threshold or first_error_rate >= 0.5:
            for candidate in candidates[1:]:
                candidate_errors = int(runtime_metrics.get(candidate, {}).get("errors", 0))
                if candidate_errors < self.settings.adaptive_error_threshold:
                    return (candidate, "adaptive_error_fallback")

        if complexity == "low":
            best_model = first
            best_duration = float(first_metrics.get("avg_duration", float("inf")))
            for candidate in candidates[1:]:
                metrics = runtime_metrics.get(candidate, {})
                avg_duration = float(metrics.get("avg_duration", float("inf")))
                if avg_duration < best_duration:
                    best_duration = avg_duration
                    best_model = candidate

            if best_model != first and best_duration <= self.settings.adaptive_latency_threshold_seconds:
                return (best_model, "adaptive_latency_optimization")

        return None


def serialize_routing_payload(
    agent: str,
    decision: ModelRoutingDecision,
    duration_seconds: float,
    failed: bool,
) -> dict[str, Any]:
    """Convert routing decision into serializable telemetry payload."""
    return {
        "agent": agent,
        "selected_model": decision.selected_model,
        "candidates": decision.candidates,
        "complexity": decision.complexity,
        "fallback_used": decision.fallback_used,
        "reason": decision.reason,
        "duration_seconds": round(duration_seconds, 4),
        "failed": failed,
    }