"""Operations Lead agent."""

from __future__ import annotations

from typing import Any

from src.agents.base_agent import BaseAgent
from src.state.schema import AgentState, Phase


class OperationsLeadAgent(BaseAgent):
    """Produces deployment readiness evidence for gate 6."""

    def __init__(self) -> None:
        super().__init__(
            name="operations_lead",
            role="Operations Lead",
            authority_level="MEDIUM",
        )

    def get_system_prompt(self, state: AgentState) -> str:
        return "Prepare operational readiness and deployment control evidence."

    def process(self, state: AgentState) -> dict[str, Any]:
        if state.phase != Phase.DEPLOYMENT:
            return {}

        outputs = dict(state.agent_outputs)
        if "deployment_package" in outputs:
            return {}

        outputs["deployment_package"] = {
            "security_assessment_report": "in_state:deployment:security_ready",
            "safety_assessment_report": "in_state:deployment:safety_ready",
        }

        updates = {
            "agent_outputs": outputs,
            "messages": ["[operations_lead] Deployment package assembled for gate_6"],
        }

        updates.update(
            self.build_governance_output(
                gate="gate_6",
                policy_ids=["OPS-001", "SEC-001", "SAF-001"],
                traceability_links=[
                    {
                        "requirement_id": req_id,
                        "artifacts": ["deployment_package"],
                    }
                    for req_id in state.requirements.keys()
                ],
                evidence_links=outputs["deployment_package"],
                notes="Deployment readiness evidence package prepared for gate_6",
            )
        )

        return updates
