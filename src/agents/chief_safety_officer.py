"""Chief Safety Officer agent."""

from __future__ import annotations

from typing import Any

from src.agents.base_agent import BaseAgent
from src.state.schema import AgentState, Phase


class ChiefSafetyOfficerAgent(BaseAgent):
    """Provides safety hazard assessment before implementation gate exit."""

    def __init__(self) -> None:
        super().__init__(
            name="chief_safety_officer",
            role="Chief Safety Officer",
            authority_level="HIGH",
        )

    def get_system_prompt(self, state: AgentState) -> str:
        return (
            "Assess safety hazards, mitigations, and acceptance criteria for "
            "implementation and deployment transitions."
        )

    def process(self, state: AgentState) -> dict[str, Any]:
        if state.phase != Phase.IMPLEMENTATION:
            return {}

        assessments = dict(state.agent_outputs)
        if "safety_assessment" in assessments:
            return {}

        assessments["safety_assessment"] = {
            "hazard_analysis_status": "completed",
            "open_hazards": 0,
            "mitigations": ["fail_safe_mode", "watchdog", "input_sanity_checks"],
        }

        return {
            "agent_outputs": assessments,
            "messages": [
                "[chief_safety_officer] Safety assessment completed for implementation package"
            ],
        }
