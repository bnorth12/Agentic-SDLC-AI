"""Chief Engineer Agent - Technical authority and oversight."""

from __future__ import annotations

from typing import Any

from src.agents.base_agent import BaseAgent
from src.config.prompts import CHIEF_ENGINEER_PROMPT
from src.state.schema import AgentState, Phase


class ChiefEngineerAgent(BaseAgent):
    """
    Chief Engineer responsible for:
    - Technical authority for all engineering decisions
    - Chairing Architecture Review Boards
    - Resolving technical disputes
    - Ensuring engineering rigor
    """

    def __init__(self):
        super().__init__(
            name="chief_engineer",
            role="Chief Engineer",
            authority_level="HIGHEST",
        )

    def get_system_prompt(self, state: AgentState) -> str:
        """Generate system prompt for the Chief Engineer."""
        return CHIEF_ENGINEER_PROMPT.format(objective=state.objective)

    def process(self, state: AgentState) -> dict[str, Any]:
        """
        Process technical oversight tasks:
        1. Review technical decisions
        2. Provide technical guidance
        3. Approve or reject board recommendations
        4. Resolve technical issues
        """
        updates: dict[str, Any] = {"messages": []}

        # Monitor for technical risks
        high_risks = [
            risk for risk in state.risks.values() if risk.impact in ["high", "critical"]
        ]

        if high_risks and not state.active_board:
            updates["messages"].append(
                f"[{self.name}] Identified {len(high_risks)} high-impact risks requiring attention"
            )

        # Oversee architecture phase
        if state.phase == Phase.ARCHITECTURE:
            if state.architecture and not state.active_board:
                updates["messages"].append(
                    f"[{self.name}] Architecture ready for review, convening ARB"
                )
                updates["active_board"] = "architecture_review"

        return updates
