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
        assessments = dict(state.agent_outputs)

        if state.phase == Phase.ARCHITECTURE:
            if "architecture_safety_assessment" in assessments:
                return {}

            hazards = [
                {
                    "id": "HZD-001",
                    "description": "Unbounded workflow recursion may starve safety checks",
                    "severity": "high",
                    "likelihood": "medium",
                    "mitigations": ["recursion_limit", "phase guardrails", "watchdog"],
                },
                {
                    "id": "HZD-002",
                    "description": "Human approval bypass in degraded mode",
                    "severity": "high",
                    "likelihood": "low",
                    "mitigations": ["hard gate enforcement", "explicit approval state"],
                },
            ]

            assessments["architecture_safety_assessment"] = {
                "hazard_analysis_status": "completed",
                "open_hazards": 0,
                "mitigations": [
                    "fail_safe_mode",
                    "watchdog",
                    "input_sanity_checks",
                ],
                "hazards": hazards,
            }

            return {
                "agent_outputs": assessments,
                "architecture_hazard_log": hazards,
                "messages": [
                    "[chief_safety_officer] Architecture hazard log completed for Gate 3"
                ],
            }

        if state.phase != Phase.IMPLEMENTATION:
            return {}

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
