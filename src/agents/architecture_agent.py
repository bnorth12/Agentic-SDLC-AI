"""Architecture Agent - System architecture and design."""

from __future__ import annotations

from typing import Any

from src.agents.base_agent import BaseAgent
from src.config.prompts import ARCHITECTURE_AGENT_PROMPT
from src.state.schema import AgentState, Phase


class ArchitectureAgent(BaseAgent):
    """
    Systems Architect responsible for:
    - Developing system architecture
    - Creating architecture views and diagrams
    - Defining component interfaces
    - Ensuring architecture meets requirements
    """

    def __init__(self):
        super().__init__(
            name="architecture_agent",
            role="Systems Architect",
            authority_level="MEDIUM",
        )

    def get_system_prompt(self, state: AgentState) -> str:
        """Generate system prompt for the Architecture Agent."""
        return ARCHITECTURE_AGENT_PROMPT.format(objective=state.objective)

    def process(self, state: AgentState) -> dict[str, Any]:
        """
        Process architecture development tasks:
        1. Review requirements
        2. Develop architecture
        3. Document decisions
        4. Request review
        """
        updates: dict[str, Any] = {"messages": []}

        # Only process during architecture phase
        if state.phase != Phase.ARCHITECTURE:
            return updates

        # Check if we have approved requirements
        if not state.requirements:
            updates["messages"].append(
                f"[{self.name}] Waiting for approved requirements before developing architecture"
            )
            return updates

        # Develop architecture if not already done
        if not state.architecture:
            self.logger.log_start("Developing system architecture")

            # Simplified architecture generation
            architecture = {
                "overview": "Multi-agent orchestration system with persistent state",
                "components": [
                    {
                        "name": "Supervisor Graph",
                        "responsibility": "Coordinate agents and manage workflow",
                    },
                    {
                        "name": "Specialist Agents",
                        "responsibility": "Domain-specific work execution",
                    },
                    {
                        "name": "Review Boards",
                        "responsibility": "Governance and approval gates",
                    },
                    {
                        "name": "Persistence Layer",
                        "responsibility": "State management and checkpointing",
                    },
                ],
                "interfaces": ["LangGraph StateGraph API", "Ollama API", "PostgreSQL"],
                "traced_requirements": list(state.requirements.keys()),
            }

            updates["architecture"] = architecture
            updates["messages"].append(
                f"[{self.name}] Developed initial architecture with {len(architecture['components'])} components"
            )

            updates["active_board"] = "architecture_review"
            updates.update(
                self.build_governance_output(
                    gate="gate_3",
                    policy_ids=["ADP-001", "SEMP-001", "RMP-001"],
                    traceability_links=[
                        {
                            "requirement_id": req_id,
                            "artifacts": ["architecture_baseline_package"],
                        }
                        for req_id in state.requirements.keys()
                    ],
                    evidence_links={
                        "architecture_baseline_package": "in_state:architecture",
                        "requirement_architecture_trace_matrix": "in_state:architecture.traced_requirements",
                        "architecture_board_decision": "pending:architecture_review",
                    },
                    notes="Architecture baseline package prepared and submitted for ARB",
                )
            )

            self.logger.log_complete("Architecture development")

        return updates
