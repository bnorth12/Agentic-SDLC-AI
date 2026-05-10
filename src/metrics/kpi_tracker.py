"""KPI tracking and metrics aggregation for governance gates."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from src.utils.logging import get_logger

logger = get_logger(__name__)


class KPITracker:
    """Track Key Performance Indicators tied to gate outcomes."""

    def __init__(self):
        """Initialize KPI tracker with empty metrics."""
        self.metrics: dict[str, Any] = {
            "gate_pass_rate": 0.0,
            "gate_pass_count": 0,
            "gate_fail_count": 0,
            "gate_defer_count": 0,
            "gate_ready_on_first_attempt": 0.0,
            "gates_attempted": 0,
            "phase_transition_times": {},  # phase_name -> [time_in_seconds]
            "review_board_decision_times": {},  # board_name -> [time_in_seconds]
            "requirement_traceability_coverage": 0.0,
            "verified_requirements": 0,
            "total_requirements": 0,
            "agent_contribution_count": {},  # agent_name -> count
            "agent_execution_times": {},  # agent_name -> [duration_seconds]
            "model_routing_count_by_agent": {},  # agent_name -> count
            "model_usage_count": {},  # model_name -> count
            "model_fallback_count": 0,
            "model_performance": {},  # model_name -> {calls, errors, durations[]}
            "error_count": 0,
            "error_count_by_agent": {},  # agent_name -> count
            "checkpoint_snapshot_count": 0,
            "gate_evidence_completeness": {},  # gate_name -> score (0.0-1.0)
        }

    def record_gate_outcome(
        self,
        gate_name: str,
        status: str,
        evidence_completeness: float = 1.0,
        was_ready_on_first_attempt: bool = False,
    ) -> None:
        """Record the outcome of a gate evaluation."""
        self.metrics["gates_attempted"] += 1

        if status == "READY":
            self.metrics["gate_pass_count"] += 1
            if was_ready_on_first_attempt:
                self.metrics["gate_ready_on_first_attempt"] += 1
        elif status == "NOT_READY":
            self.metrics["gate_fail_count"] += 1
        elif status == "DEFERRED":
            self.metrics["gate_defer_count"] += 1

        # Update pass rate
        if self.metrics["gates_attempted"] > 0:
            self.metrics["gate_pass_rate"] = (
                self.metrics["gate_pass_count"] / self.metrics["gates_attempted"]
            )

        # Update first-attempt rate
        if self.metrics["gates_attempted"] > 0:
            self.metrics["gate_ready_on_first_attempt"] = (
                self.metrics["gate_ready_on_first_attempt"]
                / self.metrics["gates_attempted"]
            )

        # Track evidence completeness per gate
        self.metrics["gate_evidence_completeness"][gate_name] = evidence_completeness
        logger.info(
            f"Recorded gate {gate_name} outcome: {status} "
            f"(evidence_completeness={evidence_completeness:.2f})"
        )

    def record_phase_transition(
        self, from_phase: str, to_phase: str, duration_seconds: float
    ) -> None:
        """Record a phase transition with duration."""
        phase_key = f"{from_phase}_to_{to_phase}"
        if phase_key not in self.metrics["phase_transition_times"]:
            self.metrics["phase_transition_times"][phase_key] = []
        self.metrics["phase_transition_times"][phase_key].append(duration_seconds)
        logger.info(
            f"Recorded phase transition {phase_key}: {duration_seconds:.2f}s"
        )

    def record_review_board_decision(
        self, board_name: str, duration_seconds: float
    ) -> None:
        """Record review board decision time."""
        if board_name not in self.metrics["review_board_decision_times"]:
            self.metrics["review_board_decision_times"][board_name] = []
        self.metrics["review_board_decision_times"][board_name].append(
            duration_seconds
        )
        logger.info(f"Recorded {board_name} decision time: {duration_seconds:.2f}s")

    def record_requirement_traceability(
        self, total_requirements: int, verified_requirements: int
    ) -> None:
        """Record requirement traceability coverage."""
        self.metrics["total_requirements"] = total_requirements
        self.metrics["verified_requirements"] = verified_requirements
        if total_requirements > 0:
            self.metrics["requirement_traceability_coverage"] = (
                verified_requirements / total_requirements
            )
        logger.info(
            f"Recorded traceability: {verified_requirements}/{total_requirements} "
            f"({self.metrics['requirement_traceability_coverage']*100:.1f}%)"
        )

    def record_agent_contribution(self, agent_name: str, count: int = 1) -> None:
        """Record agent execution count."""
        if agent_name not in self.metrics["agent_contribution_count"]:
            self.metrics["agent_contribution_count"][agent_name] = 0
        self.metrics["agent_contribution_count"][agent_name] += count
        logger.debug(
            f"Recorded {agent_name} contribution: {self.metrics['agent_contribution_count'][agent_name]}"
        )

    def record_agent_execution(self, agent_name: str, duration_seconds: float) -> None:
        """Record agent execution duration and contribution count."""
        self.record_agent_contribution(agent_name)
        if agent_name not in self.metrics["agent_execution_times"]:
            self.metrics["agent_execution_times"][agent_name] = []
        self.metrics["agent_execution_times"][agent_name].append(duration_seconds)

    def record_error(self, agent_name: str) -> None:
        """Record an agent execution error."""
        self.metrics["error_count"] += 1
        if agent_name not in self.metrics["error_count_by_agent"]:
            self.metrics["error_count_by_agent"][agent_name] = 0
        self.metrics["error_count_by_agent"][agent_name] += 1

    def record_model_routing(
        self,
        agent_name: str,
        model_name: str,
        complexity: str,
        fallback_used: bool = False,
        duration_seconds: float | None = None,
        failed: bool = False,
    ) -> None:
        """Record model-routing telemetry for adaptive selection analysis."""
        if agent_name not in self.metrics["model_routing_count_by_agent"]:
            self.metrics["model_routing_count_by_agent"][agent_name] = 0
        self.metrics["model_routing_count_by_agent"][agent_name] += 1

        if model_name not in self.metrics["model_usage_count"]:
            self.metrics["model_usage_count"][model_name] = 0
        self.metrics["model_usage_count"][model_name] += 1

        if fallback_used:
            self.metrics["model_fallback_count"] += 1

        if model_name not in self.metrics["model_performance"]:
            self.metrics["model_performance"][model_name] = {
                "calls": 0,
                "errors": 0,
                "durations": [],
                "complexity_mix": {},
            }

        perf = self.metrics["model_performance"][model_name]
        perf["calls"] += 1
        if failed:
            perf["errors"] += 1
        if duration_seconds is not None:
            perf["durations"].append(duration_seconds)
        if complexity not in perf["complexity_mix"]:
            perf["complexity_mix"][complexity] = 0
        perf["complexity_mix"][complexity] += 1

    def record_checkpoint_snapshot(self) -> None:
        """Record a checkpoint snapshot creation."""
        self.metrics["checkpoint_snapshot_count"] += 1

    def get_metrics_report(self) -> dict[str, Any]:
        """Generate a comprehensive metrics report."""
        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "summary": {
                "gates_attempted": self.metrics["gates_attempted"],
                "gate_pass_rate": f"{self.metrics['gate_pass_rate']*100:.1f}%",
                "gate_pass_count": self.metrics["gate_pass_count"],
                "gate_fail_count": self.metrics["gate_fail_count"],
                "gate_defer_count": self.metrics["gate_defer_count"],
                "first_attempt_success_rate": f"{self.metrics['gate_ready_on_first_attempt']*100:.1f}%",
            },
            "requirements": {
                "total": self.metrics["total_requirements"],
                "verified": self.metrics["verified_requirements"],
                "traceability_coverage": f"{self.metrics['requirement_traceability_coverage']*100:.1f}%",
            },
            "agents": self.metrics["agent_contribution_count"],
            "errors": {
                "total": self.metrics["error_count"],
                "by_agent": self.metrics["error_count_by_agent"],
                "error_rate_per_gate": (
                    f"{(self.metrics['error_count'] / max(1, self.metrics['gates_attempted']))*100:.1f}%"
                ),
            },
            "checkpoints": self.metrics["checkpoint_snapshot_count"],
            "gate_evidence_completeness": {
                gate: f"{score*100:.1f}%"
                for gate, score in self.metrics["gate_evidence_completeness"].items()
            },
            "model_routing": {
                "by_agent": self.metrics["model_routing_count_by_agent"],
                "model_usage": self.metrics["model_usage_count"],
                "fallback_count": self.metrics["model_fallback_count"],
            },
        }

        # Add average phase transition times
        if self.metrics["phase_transition_times"]:
            avg_phase_times = {}
            for phase_key, times in self.metrics["phase_transition_times"].items():
                avg_phase_times[phase_key] = f"{sum(times) / len(times):.2f}s"
            report["average_phase_transition_times"] = avg_phase_times

        # Add average review board decision times
        if self.metrics["review_board_decision_times"]:
            avg_board_times = {}
            for board_name, times in self.metrics[
                "review_board_decision_times"
            ].items():
                avg_board_times[board_name] = f"{sum(times) / len(times):.2f}s"
            report["average_review_board_times"] = avg_board_times

        if self.metrics["agent_execution_times"]:
            avg_agent_times = {}
            for agent_name, times in self.metrics["agent_execution_times"].items():
                avg_agent_times[agent_name] = f"{sum(times) / len(times):.2f}s"
            report["average_agent_execution_times"] = avg_agent_times

        if self.metrics["model_performance"]:
            model_performance: dict[str, Any] = {}
            for model_name, perf in self.metrics["model_performance"].items():
                calls = perf["calls"]
                errors = perf["errors"]
                durations = perf["durations"]
                model_performance[model_name] = {
                    "calls": calls,
                    "errors": errors,
                    "error_rate": f"{((errors / max(1, calls)) * 100):.1f}%",
                    "avg_duration": (
                        f"{(sum(durations) / len(durations)):.2f}s"
                        if durations
                        else "n/a"
                    ),
                    "complexity_mix": perf["complexity_mix"],
                }
            report["model_performance"] = model_performance

        return report


def aggregate_gate_metrics(gate_outcomes: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Aggregate metrics from multiple gate evaluation outcomes.

    Args:
        gate_outcomes: List of gate validation result dictionaries

    Returns:
        Aggregated metrics dictionary
    """
    tracker = KPITracker()

    for outcome in gate_outcomes:
        gate_name = outcome.get("gate", "unknown")
        status = outcome.get("status", "UNKNOWN")
        evidence_completeness = outcome.get("evidence_completeness", 0.5)
        first_attempt = outcome.get("first_attempt", True)

        tracker.record_gate_outcome(
            gate_name=gate_name,
            status=status,
            evidence_completeness=evidence_completeness,
            was_ready_on_first_attempt=first_attempt,
        )

    return tracker.get_metrics_report()
