"""QA Manager agent."""

from __future__ import annotations

from typing import Any

from src.agents.base_agent import BaseAgent
from src.state.schema import AgentState, Phase


class QAManagerAgent(BaseAgent):
    """Produces verification evidence for gate 5."""

    def __init__(self) -> None:
        super().__init__(
            name="qa_manager",
            role="QA Manager",
            authority_level="MEDIUM",
        )

    def get_system_prompt(self, state: AgentState) -> str:
        return "Drive verification and validation evidence completeness for gate exit."

    def process(self, state: AgentState) -> dict[str, Any]:
        if state.phase != Phase.VERIFICATION:
            return {}

        outputs = dict(state.agent_outputs)
        if "verification_validation_package" not in outputs:
            return {
                "messages": ["[qa_manager] Waiting on verification validation package"]
            }

        if "verification_package" in outputs:
            return {}

        vv_package = outputs["verification_validation_package"]
        coverage = vv_package.get("coverage_tracking", {})
        coverage_percent = coverage.get("coverage_percent", 0.0)
        coverage_summary = f"in_state:vnv:coverage_{int(coverage_percent)}_percent"

        outputs["verification_package"] = {
            "verification_validation_report": "in_state:vnv:report_v2",
            "coverage_summary": coverage_summary,
            "defect_disposition_log": "in_state:vnv:defects_closed",
            "requirements_to_test_mapping": vv_package.get(
                "requirements_to_test_mapping", []
            ),
            "vnv_signoff": vv_package.get("vnv_signoff", {}),
        }

        updates = {
            "agent_outputs": outputs,
            "phase": Phase.DEPLOYMENT,
            "messages": [
                "[qa_manager] Verification package assembled for gate_5; transitioning to DEPLOYMENT"
            ],
        }

        updates.update(
            self.build_governance_output(
                gate="gate_5",
                policy_ids=["VVP-001", "QMP-001"],
                traceability_links=[
                    {
                        "requirement_id": req_id,
                        "artifacts": ["verification_package"],
                    }
                    for req_id in state.requirements.keys()
                ],
                evidence_links=outputs["verification_package"],
                notes="Verification evidence package prepared for gate_5",
            )
        )

        return updates
