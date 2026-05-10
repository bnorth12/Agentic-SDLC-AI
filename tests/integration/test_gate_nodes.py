"""Integration tests for gate node transitions."""

from __future__ import annotations

import unittest

from src.gates.gate_architecture import evaluate_architecture_gate
from src.gates.gate_deployment import evaluate_deployment_gate
from src.gates.gate_implementation import evaluate_implementation_gate
from src.gates.gate_requirements import evaluate_requirements_gate
from src.state.schema import AgentState, Phase, Requirement


class GateNodeIntegrationTest(unittest.TestCase):
    def _build_state(self) -> AgentState:
        state = AgentState(objective="Sprint 2 gate flow validation")
        state.requirements = {
            "REQ-001": Requirement(
                id="REQ-001",
                text="System shall provide governed phase transitions",
                category="functional",
                priority="high",
                verification_method="test",
                created_by="test",
            )
        }
        return state

    def test_requirements_gate_transitions_to_architecture(self) -> None:
        state = self._build_state()
        state.phase = Phase.REQUIREMENTS
        state.agent_outputs["requirements_agent"] = {
            "agent": "requirements_agent",
            "policy_compliance": {"status": "PASS", "policies": ["RMP-001"]},
            "traceability_links": [
                {"requirement_id": "REQ-001", "artifacts": ["requirements_baseline"]}
            ],
            "gate_readiness": {"gate": "gate_2", "status": "READY"},
            "evidence_links": {
                "requirements_baseline": "in_state:requirements",
                "requirements_traceability_matrix": "in_state:rtm",
                "open_issues": "in_state:none",
            },
            "risks_or_blockers": [],
        }

        updates = evaluate_requirements_gate(state)

        self.assertEqual(updates["phase"], Phase.ARCHITECTURE)
        self.assertTrue(updates["governance_validation"]["gate_can_be_marked_ready"])

    def test_architecture_gate_transitions_to_design(self) -> None:
        state = self._build_state()
        state.phase = Phase.ARCHITECTURE
        state.architecture = {"components": ["supervisor", "agents"]}
        state.agent_outputs["architecture_security_assessment"] = {
            "threat_model_status": "completed"
        }
        state.agent_outputs["architecture_safety_assessment"] = {
            "hazard_analysis_status": "completed"
        }
        state.agent_outputs["architecture_reliability_assessment"] = {
            "reliability_analysis_status": "completed"
        }
        state.agent_outputs["architecture_agent"] = {
            "agent": "architecture_agent",
            "policy_compliance": {"status": "PASS", "policies": ["ADP-001"]},
            "traceability_links": [
                {
                    "requirement_id": "REQ-001",
                    "artifacts": ["architecture_baseline_package"],
                }
            ],
            "gate_readiness": {"gate": "gate_3", "status": "READY"},
            "evidence_links": {
                "architecture_baseline_package": "in_state:architecture",
                "requirement_architecture_trace_matrix": "in_state:trace_matrix",
                "architecture_board_decision": "in_state:arb:approve",
            },
            "risks_or_blockers": [],
        }

        updates = evaluate_architecture_gate(state)

        self.assertEqual(updates["phase"], Phase.DESIGN)
        self.assertTrue(updates["governance_validation"]["gate_can_be_marked_ready"])

    def test_implementation_gate_transitions_to_verification(self) -> None:
        state = self._build_state()
        state.phase = Phase.IMPLEMENTATION
        state.agent_outputs["integration_manager"] = {
            "agent": "integration_manager",
            "policy_compliance": {"status": "PASS", "policies": ["CCM-001"]},
            "traceability_links": [
                {"requirement_id": "REQ-001", "artifacts": ["implementation_package"]}
            ],
            "gate_readiness": {"gate": "gate_4", "status": "READY"},
            "evidence_links": {
                "change_set_summary": "in_state:change_set",
                "test_report": "in_state:test_report",
                "lint_report": "in_state:lint_report",
                "configuration_baseline_update": "in_state:baseline_v2",
            },
            "risks_or_blockers": [],
        }

        updates = evaluate_implementation_gate(state)

        self.assertEqual(updates["phase"], Phase.VERIFICATION)
        self.assertTrue(updates["governance_validation"]["gate_can_be_marked_ready"])

    def test_deployment_gate_transitions_to_maintenance(self) -> None:
        state = self._build_state()
        state.phase = Phase.DEPLOYMENT
        state.agent_outputs["operations_lead"] = {
            "agent": "operations_lead",
            "policy_compliance": {"status": "PASS", "policies": ["OPS-001"]},
            "traceability_links": [
                {"requirement_id": "REQ-001", "artifacts": ["deployment_package"]}
            ],
            "gate_readiness": {"gate": "gate_6", "status": "READY"},
            "evidence_links": {
                "security_assessment_report": "in_state:security_report",
                "safety_assessment_report": "in_state:safety_report",
            },
            "risks_or_blockers": [],
        }

        updates = evaluate_deployment_gate(state)

        self.assertEqual(updates["phase"], Phase.MAINTENANCE)
        self.assertTrue(updates["governance_validation"]["gate_can_be_marked_ready"])
