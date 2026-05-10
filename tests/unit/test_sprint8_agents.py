"""Unit tests for Sprint 8 specialist agents."""

from __future__ import annotations

import unittest

from src.agents.data_management_agent import DataManagementAgentStub
from src.agents.integration_and_test_agent import IntegrationAndTestAgentStub
from src.state.schema import AgentState, Phase


class IntegrationAndTestAgentTest(unittest.TestCase):
    def test_produces_integration_test_package_during_verification(self) -> None:
        agent = IntegrationAndTestAgentStub()
        state = AgentState(objective="Integration testing", phase=Phase.VERIFICATION)

        updates = agent(state)

        self.assertIn("agent_outputs", updates)
        self.assertIn("integration_test_package", updates["agent_outputs"])
        self.assertIn("messages", updates)

    def test_integration_package_includes_test_evidence(self) -> None:
        agent = IntegrationAndTestAgentStub()
        state = AgentState(objective="Integration testing", phase=Phase.VERIFICATION)

        updates = agent(state)
        pkg = updates["agent_outputs"]["integration_test_package"]

        self.assertIn("test_plan", pkg)
        self.assertIn("integration_test_cases", pkg)
        self.assertIn("coverage_tracking", pkg)
        self.assertGreater(len(pkg["integration_test_cases"]), 0)

    def test_includes_governance_output(self) -> None:
        agent = IntegrationAndTestAgentStub()
        state = AgentState(objective="Integration testing", phase=Phase.VERIFICATION)

        updates = agent(state)

        self.assertIn("gate_readiness", updates)
        self.assertIn("policy_compliance", updates)
        self.assertIn("evidence_links", updates)


class DataManagementAgentTest(unittest.TestCase):
    def test_produces_data_governance_package(self) -> None:
        agent = DataManagementAgentStub()
        state = AgentState(objective="Data governance")

        updates = agent(state)

        self.assertIn("agent_outputs", updates)
        self.assertIn("data_management_package", updates["agent_outputs"])

    def test_data_package_includes_inventory(self) -> None:
        agent = DataManagementAgentStub()
        state = AgentState(objective="Data governance")

        updates = agent(state)
        pkg = updates["agent_outputs"]["data_management_package"]

        self.assertIn("data_inventory", pkg)
        self.assertIn("access_control_matrix", pkg)
        self.assertGreater(len(pkg["data_inventory"]), 0)

    def test_data_package_includes_audit_trail(self) -> None:
        agent = DataManagementAgentStub()
        state = AgentState(objective="Data governance")

        updates = agent(state)
        pkg = updates["agent_outputs"]["data_management_package"]

        self.assertIn("audit_events", pkg)
        self.assertGreater(len(pkg["audit_events"]), 0)

    def test_includes_governance_output(self) -> None:
        agent = DataManagementAgentStub()
        state = AgentState(objective="Data governance")

        updates = agent(state)

        self.assertIn("gate_readiness", updates)
        self.assertIn("policy_compliance", updates)


if __name__ == "__main__":
    unittest.main()
