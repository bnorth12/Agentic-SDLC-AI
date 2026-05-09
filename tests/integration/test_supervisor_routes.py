"""Integration tests for supervisor routing decisions."""

from __future__ import annotations

import unittest

from src.graphs.supervisor import should_continue
from src.state.schema import AgentState, Phase, Requirement


class SupervisorRoutingIntegrationTest(unittest.TestCase):
    def test_requirements_with_artifacts_routes_gate(self) -> None:
        state = AgentState(objective="route test", phase=Phase.REQUIREMENTS)
        state.requirements = {
            "REQ-001": Requirement(
                id="REQ-001",
                text="System shall route requirements through gate checks",
                category="functional",
                priority="high",
                verification_method="test",
                created_by="test",
            )
        }

        self.assertEqual(should_continue(state), "requirements_gate")

    def test_implementation_routes_security_first(self) -> None:
        state = AgentState(objective="route test", phase=Phase.IMPLEMENTATION)

        self.assertEqual(should_continue(state), "chief_security_officer")

    def test_implementation_routes_gate_after_all_packages(self) -> None:
        state = AgentState(objective="route test", phase=Phase.IMPLEMENTATION)
        state.agent_outputs = {
            "security_assessment": {},
            "safety_assessment": {},
            "compliance_assessment": {},
            "implementation_package": {},
        }

        self.assertEqual(should_continue(state), "implementation_gate")

    def test_maintenance_routes_end_after_quality_package(self) -> None:
        state = AgentState(objective="route test", phase=Phase.MAINTENANCE)
        state.agent_outputs = {"maintenance_quality_package": {}}

        self.assertEqual(should_continue(state), "END")
