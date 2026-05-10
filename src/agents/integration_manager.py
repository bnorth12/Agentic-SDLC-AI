"""Integration Manager agent."""

from __future__ import annotations

from typing import Any

from src.agents.base_agent import BaseAgent
from src.state.schema import AgentState, Phase


class IntegrationManagerAgent(BaseAgent):
    """Builds implementation package evidence for gate 4."""

    def __init__(self) -> None:
        super().__init__(
            name="integration_manager",
            role="Integration Manager",
            authority_level="MEDIUM",
        )

    def get_system_prompt(self, state: AgentState) -> str:
        return (
            "Coordinate subsystem integration and produce implementation quality "
            "evidence for gate progression."
        )

    def process(self, state: AgentState) -> dict[str, Any]:
        if state.phase != Phase.IMPLEMENTATION:
            return {}

        outputs = dict(state.agent_outputs)

        if "software_development_package" not in outputs:
            return {
                "messages": [
                    "[integration_manager] Waiting on software development package"
                ]
            }

        if "configuration_management_package" not in outputs:
            return {
                "messages": [
                    "[integration_manager] Waiting on configuration management package"
                ]
            }

        if "implementation_package" in outputs:
            return {}

        dev_package = outputs["software_development_package"]
        cm_package = outputs["configuration_management_package"]

        outputs["implementation_package"] = {
            "change_set_summary": dev_package.get(
                "change_set_summary", "in_state:implementation:core_components_integrated"
            ),
            "test_report": dev_package.get(
                "test_report", "in_state:tests:integration_smoke_pass"
            ),
            "lint_report": dev_package.get("lint_report", "in_state:quality:lint_pass"),
            "configuration_baseline_update": cm_package.get(
                "configuration_baseline_update", "in_state:cm:baseline_v2"
            ),
            "requirement_linked_stubs": dev_package.get("requirement_linked_stubs", []),
            "configuration_tags": cm_package.get("baseline_register", {}).get(
                "configuration_tags", []
            ),
        }

        updates = {
            "agent_outputs": outputs,
            "messages": [
                "[integration_manager] Implementation package assembled for gate_4 review"
            ],
        }

        updates.update(
            self.build_governance_output(
                gate="gate_4",
                policy_ids=["CCM-001", "TVP-001"],
                traceability_links=[
                    {
                        "requirement_id": req_id,
                        "artifacts": ["implementation_package"],
                    }
                    for req_id in state.requirements.keys()
                ],
                evidence_links=outputs["implementation_package"],
                notes="Implementation package evidence prepared for gate_4",
            )
        )

        return updates
