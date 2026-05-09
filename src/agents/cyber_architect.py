"""Cyber Architect agent."""

from __future__ import annotations

from typing import Any

from src.agents.base_agent import BaseAgent
from src.state.schema import AgentState, Phase


class CyberArchitectAgent(BaseAgent):
    """Builds security architecture views during design."""

    def __init__(self) -> None:
        super().__init__(
            name="cyber_architect",
            role="Cybersecurity Architect",
            authority_level="MEDIUM",
        )

    def get_system_prompt(self, state: AgentState) -> str:
        return (
            "Develop security architecture views, trust boundaries, and control "
            "allocation linked to requirements."
        )

    def process(self, state: AgentState) -> dict[str, Any]:
        if state.phase != Phase.DESIGN:
            return {}

        if state.architecture.get("cyber_security_view"):
            return {}

        architecture = dict(state.architecture)
        architecture["cyber_security_view"] = {
            "trust_boundaries": ["api_boundary", "data_store_boundary"],
            "security_controls": ["mTLS", "RBAC", "immutable_audit_log"],
            "threat_scenarios": ["unauthorized_access", "tampering", "dos"],
        }

        outputs = dict(state.agent_outputs)
        outputs["cyber_architecture"] = architecture["cyber_security_view"]

        return {
            "architecture": architecture,
            "agent_outputs": outputs,
            "phase": Phase.IMPLEMENTATION,
            "messages": [
                "[cyber_architect] Cyber architecture baseline completed; transitioning to IMPLEMENTATION"
            ],
        }
