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

    def test_architecture_routes_security_after_baseline(self) -> None:
        state = AgentState(objective="route test", phase=Phase.ARCHITECTURE)
        state.architecture = {"components": ["supervisor", "agents"]}

        self.assertEqual(should_continue(state), "chief_security_officer")

    def test_architecture_routes_safety_after_security(self) -> None:
        state = AgentState(objective="route test", phase=Phase.ARCHITECTURE)
        state.architecture = {"components": ["supervisor", "agents"]}
        state.agent_outputs = {
            "architecture_security_assessment": {
                "threat_model_status": "completed"
            }
        }

        self.assertEqual(should_continue(state), "chief_safety_officer")

    def test_architecture_routes_reliability_after_safety(self) -> None:
        state = AgentState(objective="route test", phase=Phase.ARCHITECTURE)
        state.architecture = {"components": ["supervisor", "agents"]}
        state.agent_outputs = {
            "architecture_security_assessment": {
                "threat_model_status": "completed"
            },
            "architecture_safety_assessment": {
                "hazard_analysis_status": "completed"
            },
        }

        self.assertEqual(should_continue(state), "chief_reliability_officer")

    def test_architecture_routes_gate_after_all_assessments(self) -> None:
        state = AgentState(objective="route test", phase=Phase.ARCHITECTURE)
        state.architecture = {"components": ["supervisor", "agents"]}
        state.agent_outputs = {
            "architecture_security_assessment": {
                "threat_model_status": "completed"
            },
            "architecture_safety_assessment": {
                "hazard_analysis_status": "completed"
            },
            "architecture_reliability_assessment": {
                "reliability_analysis_status": "completed"
            },
        }

        self.assertEqual(should_continue(state), "architecture_gate")

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
