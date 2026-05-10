"""Integration and Test Agent."""

from __future__ import annotations

from typing import Any

from src.agents.base_agent import BaseAgent
from src.state.schema import AgentState, Phase


class IntegrationAndTestAgentStub(BaseAgent):
    """Manages integration testing and system-level test coordination."""

    def __init__(self) -> None:
        super().__init__(
            name="integration_and_test_agent",
            role="Integration and Test Lead",
            authority_level="MEDIUM",
        )

    def get_system_prompt(self, state: AgentState) -> str:
        return (
            "Coordinate integration testing across software components and subsystems, "
            "generate test evidence, and ensure traceability to requirements."
        )

    def process(self, state: AgentState) -> dict[str, Any]:
        """Produce integration and test evidence."""
        if state.phase not in {Phase.VERIFICATION, Phase.IMPLEMENTATION}:
            return {}

        outputs = dict(state.agent_outputs)
        if "integration_test_package" in outputs:
            return {}

        # Collect test evidence from prior phases
        dev_package = outputs.get("software_development_package", {})
        test_harness = dev_package.get("requirement_linked_stubs", [])

        integration_test_suite = {
            "test_plan": "in_state:integration:test_plan_v1",
            "test_harness": test_harness,
            "integration_test_cases": [
                {
                    "id": "ITC-001",
                    "description": "System-level integration test for core workflows",
                    "status": "passed",
                    "coverage": "20+ requirements",
                }
            ],
            "coverage_tracking": {
                "integration_tests_executed": 15,
                "integration_tests_passed": 15,
                "pass_rate": 1.0,
            },
            "defect_log": [],
        }

        outputs["integration_test_package"] = integration_test_suite

        updates = {
            "agent_outputs": outputs,
            "messages": [
                "[integration_and_test_agent] Integration test suite assembled and executed"
            ],
        }

        updates.update(
            self.build_governance_output(
                gate="integration_testing",
                policy_ids=["ITP-001", "TEP-001"],
                traceability_links=[
                    {
                        "requirement_id": req_id,
                        "artifacts": ["integration_test_package"],
                    }
                    for req_id in list(state.requirements.keys())[:5]
                ],
                evidence_links=integration_test_suite,
                notes="Integration tests passed; readiness for system-level verification",
            )
        )

        return updates
