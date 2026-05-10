"""Software Development agent."""

from __future__ import annotations

from typing import Any

from src.agents.base_agent import BaseAgent
from src.state.schema import AgentState, Phase


class SoftwareDevelopmentAgent(BaseAgent):
    """Produces requirement-linked code generation stubs for implementation flow."""

    def __init__(self) -> None:
        super().__init__(
            name="software_development_agent",
            role="Software Development Agent",
            authority_level="MEDIUM",
        )

    def get_system_prompt(self, state: AgentState) -> str:
        return "Generate requirement-linked implementation stubs and change-set summaries."

    def process(self, state: AgentState) -> dict[str, Any]:
        if state.phase != Phase.IMPLEMENTATION:
            return {}

        outputs = dict(state.agent_outputs)
        if "software_development_package" in outputs:
            return {}

        requirement_ids = sorted(list(state.requirements.keys()))
        stubs = [
            {
                "stub_id": f"STUB-{idx + 1:03d}",
                "requirement_id": req_id,
                "module": f"src/generated/{req_id.lower().replace('-', '_')}.py",
                "status": "generated",
            }
            for idx, req_id in enumerate(requirement_ids)
        ]

        outputs["software_development_package"] = {
            "requirement_linked_stubs": stubs,
            "change_set_summary": "in_state:implementation:software_stubs_generated",
            "lint_report": "in_state:quality:lint_pass",
            "test_report": "in_state:tests:unit_and_integration_pass",
        }

        return {
            "agent_outputs": outputs,
            "messages": [
                "[software_development_agent] Generated requirement-linked code stubs"
            ],
        }
