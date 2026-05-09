"""Architecture gate evaluation node."""

from __future__ import annotations

from typing import Any

from src.state.schema import AgentState, Phase
from src.tools.governance_validation import validate_outputs


def evaluate_architecture_gate(state: AgentState) -> dict[str, Any]:
    """Validate gate_3 evidence and transition to design when ready."""
    if state.phase != Phase.ARCHITECTURE or not state.architecture:
        return {}

    output = state.agent_outputs.get("architecture_agent")
    if not isinstance(output, dict):
        return {
            "messages": [
                "[architecture_gate] No architecture agent governance payload found"
            ]
        }

    report = validate_outputs([output], expected_gate="gate_3", require_strict_ready=True)
    updates: dict[str, Any] = {
        "governance_validation": report,
        "messages": ["[architecture_gate] Evaluated gate_3 readiness"],
    }

    if report["gate_can_be_marked_ready"]:
        updates["phase"] = Phase.DESIGN
        updates["messages"].append(
            "[architecture_gate] gate_3 ready; transitioning to DESIGN"
        )
    else:
        updates["requires_human_approval"] = True
        updates["messages"].append(
            "[architecture_gate] gate_3 not ready; human review required"
        )

    return updates
