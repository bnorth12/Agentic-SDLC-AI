"""Implementation gate evaluation node."""

from __future__ import annotations

from typing import Any

from src.state.schema import AgentState, Phase
from src.tools.governance_validation import validate_outputs


def evaluate_implementation_gate(state: AgentState) -> dict[str, Any]:
    """Validate gate_4 evidence and transition to verification when ready."""
    if state.phase != Phase.IMPLEMENTATION:
        return {}

    output = state.agent_outputs.get("integration_manager")
    if not isinstance(output, dict):
        return {
            "messages": [
                "[implementation_gate] No integration manager governance payload found"
            ]
        }

    report = validate_outputs([output], expected_gate="gate_4", require_strict_ready=True)
    updates: dict[str, Any] = {
        "governance_validation": report,
        "messages": ["[implementation_gate] Evaluated gate_4 readiness"],
    }

    if report["gate_can_be_marked_ready"]:
        updates["phase"] = Phase.VERIFICATION
        updates["messages"].append(
            "[implementation_gate] gate_4 ready; transitioning to VERIFICATION"
        )
    else:
        updates["requires_human_approval"] = True
        updates["messages"].append(
            "[implementation_gate] gate_4 not ready; human review required"
        )

    return updates
