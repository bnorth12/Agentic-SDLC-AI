"""Software Quality Manager agent."""

from __future__ import annotations

from typing import Any

from src.agents.base_agent import BaseAgent
from src.state.schema import AgentState, Phase


class SoftwareQualityManagerAgent(BaseAgent):
    """Tracks post-release quality evidence for gate 7."""

    def __init__(self) -> None:
        super().__init__(
            name="software_quality_manager",
            role="Software Quality Manager",
            authority_level="MEDIUM",
        )

    def get_system_prompt(self, state: AgentState) -> str:
        return "Collect post-release quality metrics and incident evidence."

    def process(self, state: AgentState) -> dict[str, Any]:
        if state.phase != Phase.MAINTENANCE:
            return {}

        outputs = dict(state.agent_outputs)
        if "maintenance_quality_package" in outputs:
            return {}

        outputs["maintenance_quality_package"] = {
            "post_release_metrics_summary": "in_state:maintenance:kpi_summary",
            "incident_problem_report": "in_state:maintenance:no_open_incidents",
            "updated_risk_register_action_plan": "in_state:maintenance:risk_plan_v1",
        }

        updates = {
            "agent_outputs": outputs,
            "messages": [
                "[software_quality_manager] Post-release quality package assembled for gate_7"
            ],
        }

        updates.update(
            self.build_governance_output(
                gate="gate_7",
                policy_ids=["QMP-001", "RMP-001"],
                traceability_links=[
                    {
                        "requirement_id": req_id,
                        "artifacts": ["maintenance_quality_package"],
                    }
                    for req_id in state.requirements.keys()
                ],
                evidence_links=outputs["maintenance_quality_package"],
                notes="Post-release quality evidence package prepared for gate_7",
            )
        )

        return updates
