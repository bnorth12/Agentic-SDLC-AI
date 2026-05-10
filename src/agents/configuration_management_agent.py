"""Configuration Management agent."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from src.agents.base_agent import BaseAgent
from src.state.schema import AgentState, Phase


class ConfigurationManagementAgent(BaseAgent):
    """Produces baseline register and change control evidence for Gate 4."""

    def __init__(self) -> None:
        super().__init__(
            name="configuration_management_agent",
            role="Configuration Management Agent",
            authority_level="MEDIUM",
        )

    def get_system_prompt(self, state: AgentState) -> str:
        return "Maintain baseline register, change log, and configuration tags."

    def process(self, state: AgentState) -> dict[str, Any]:
        if state.phase != Phase.IMPLEMENTATION:
            return {}

        outputs = dict(state.agent_outputs)
        if "configuration_management_package" in outputs:
            return {}

        baseline_version = "baseline_v2"
        change_log = {
            "change_id": "CHG-0001",
            "summary": "Initial implementation baseline update",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "approved_by": "configuration_management_agent",
        }

        outputs["configuration_management_package"] = {
            "configuration_baseline_update": f"in_state:cm:{baseline_version}",
            "baseline_register": {
                "active_baseline": baseline_version,
                "configuration_tags": ["impl-ready", "gate4-candidate"],
            },
            "change_control_log": [change_log],
        }

        return {
            "agent_outputs": outputs,
            "messages": [
                "[configuration_management_agent] Baseline register and change control log updated"
            ],
        }
