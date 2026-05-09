"""Requirements gate evaluation node."""

from __future__ import annotations

from typing import Any

from src.state.schema import AgentState, Phase
from src.tools.governance_validation import validate_outputs


def evaluate_requirements_gate(state: AgentState) -> dict[str, Any]:
    """Validate gate_2 evidence and transition to architecture when ready."""
    if state.phase != Phase.REQUIREMENTS or not state.requirements:
        return {}

    output = state.agent_outputs.get("requirements_agent")
    if not isinstance(output, dict):
        return {
            "messages": [
                "[requirements_gate] No requirements agent governance payload found"
            ]
        }

    report = validate_outputs([output], expected_gate="gate_2", require_strict_ready=True)
    updates: dict[str, Any] = {
        "governance_validation": report,
        "messages": ["[requirements_gate] Evaluated gate_2 readiness"],
    }

    if report["gate_can_be_marked_ready"]:
        updates["phase"] = Phase.ARCHITECTURE
        updates["messages"].append(
            "[requirements_gate] gate_2 ready; transitioning to ARCHITECTURE"
        )
    else:
        updates["requires_human_approval"] = True
        updates["messages"].append(
            "[requirements_gate] gate_2 not ready; human review required"
        )

    return updates
