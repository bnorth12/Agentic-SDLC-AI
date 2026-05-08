"""Program Manager Agent - Overall coordination and work assignment."""

from __future__ import annotations

from typing import Any

from src.agents.base_agent import BaseAgent
from src.config.prompts import PROGRAM_MANAGER_PROMPT
from src.state.schema import AgentState, Phase, WorkItem, WorkItemStatus


class ProgramManagerAgent(BaseAgent):
    """
    Program Manager responsible for:
    - Prioritizing work
    - Assigning tasks to specialist agents
    - Tracking program status
    - Managing stakeholder alignment
    """

    def __init__(self):
        super().__init__(
            name="program_manager",
            role="Program Manager",
            authority_level="HIGH",
        )

    def get_system_prompt(self, state: AgentState) -> str:
        """Generate system prompt for the Program Manager."""
        return PROGRAM_MANAGER_PROMPT.format(objective=state.objective)

    def process(self, state: AgentState) -> dict[str, Any]:
        """
        Process program management tasks:
        1. Review current objective and state
        2. Determine next phase if needed
        3. Create work items for specialist agents
        4. Track overall progress
        """
        updates: dict[str, Any] = {"messages": []}

        # Initial task decomposition
        if state.phase == Phase.INTAKE and state.objective:
            updates["messages"].append(
                f"[{self.name}] Received objective: {state.objective}"
            )

            # Move to requirements phase
            updates["phase"] = Phase.REQUIREMENTS

            # Create initial work items
            work_items = [
                WorkItem(
                    id="req-001",
                    title="Elicit and document stakeholder requirements",
                    description=f"Analyze objective and develop initial requirements: {state.objective}",
                    assigned_to="requirements_agent",
                    priority=1,
                    status=WorkItemStatus.IN_PROGRESS,
                ),
            ]

            updates["work_queue"] = work_items
            updates["messages"].append(
                f"[{self.name}] Transitioning to REQUIREMENTS phase and assigning work"
            )

        # Check for phase transitions
        elif state.phase == Phase.REQUIREMENTS:
            if len(state.requirements) > 0 and not state.active_board:
                # Requirements are ready for review
                updates["messages"].append(
                    f"[{self.name}] Requirements developed, requesting review"
                )
                updates["active_board"] = "requirements_review"

        return updates
