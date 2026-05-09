"""Smoke tests for starter project modules."""

import unittest

from src.graphs.supervisor import build_supervisor_graph
from src.state.schema import AgentState, Phase, Requirement


class StarterModulesTest(unittest.TestCase):
    def test_agent_state_defaults(self) -> None:
        """Test AgentState initialization with defaults."""
        state = AgentState()
        self.assertEqual(state.phase, Phase.INTAKE)
        self.assertEqual(state.work_queue, [])
        self.assertFalse(state.requires_human_approval)
        self.assertEqual(state.requirements, {})

    def test_agent_state_with_objective(self) -> None:
        """Test AgentState with an objective."""
        objective = "Build a test application"
        state = AgentState(objective=objective)
        self.assertEqual(state.objective, objective)
        self.assertEqual(state.phase, Phase.INTAKE)

    def test_requirement_creation(self) -> None:
        """Test creating a Requirement."""
        req = Requirement(
            id="REQ-001",
            text="System shall do X",
            category="functional",
            priority="high",
            verification_method="test",
            created_by="test_agent",
        )
        self.assertEqual(req.id, "REQ-001")
        self.assertEqual(req.category, "functional")
        self.assertEqual(req.status, "draft")

    def test_supervisor_graph_builds(self) -> None:
        """Test that supervisor graph can be built."""
        graph = build_supervisor_graph()
        self.assertIsNotNone(graph)

    def test_supervisor_graph_execution(self) -> None:
        """Test basic supervisor graph execution."""
        graph = build_supervisor_graph()

        initial_state = AgentState(
            objective="Test objective for smoke test"
        )

        config = {"recursion_limit": 50}
        result = graph.invoke(initial_state, config=config)

        # Basic assertions
        self.assertIsNotNone(result)
        self.assertIn("objective", result)
        self.assertEqual(result["objective"], initial_state.objective)


if __name__ == "__main__":
    unittest.main()
