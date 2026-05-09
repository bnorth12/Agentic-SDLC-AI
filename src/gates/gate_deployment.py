"""Deployment gate evaluation node."""

from __future__ import annotations

from typing import Any

from src.state.schema import AgentState, Phase
from src.tools.governance_validation import validate_outputs


def evaluate_deployment_gate(state: AgentState) -> dict[str, Any]:
    """Validate gate_6 evidence and transition to maintenance when ready."""
    if state.phase != Phase.DEPLOYMENT:
        return {}

    output = state.agent_outputs.get("operations_lead")
    if not isinstance(output, dict):
        return {
            "messages": [
                "[deployment_gate] No operations lead governance payload found"
            ]
        }

    report = validate_outputs([output], expected_gate="gate_6", require_strict_ready=True)
    updates: dict[str, Any] = {
        "governance_validation": report,
        "messages": ["[deployment_gate] Evaluated gate_6 readiness"],
    }

    if report["gate_can_be_marked_ready"]:
        updates["phase"] = Phase.MAINTENANCE
        updates["messages"].append(
            "[deployment_gate] gate_6 ready; transitioning to MAINTENANCE"
        )
    else:
        updates["requires_human_approval"] = True
        updates["messages"].append(
            "[deployment_gate] gate_6 not ready; human review required"
        )

    return updates
