"""End-to-end integration test for intake through architecture Gate 3 readiness."""

from __future__ import annotations

import unittest

from src.graphs.supervisor import build_supervisor_graph
from src.state.schema import AgentState, Phase


class EndToEndIntakeToGate3Test(unittest.TestCase):
    """Validate Sprint 3 intake-to-Gate-3 flow with safety/security/reliability evidence."""

    def test_intake_to_gate3_includes_architecture_assessments(self) -> None:
        graph = build_supervisor_graph()
        initial_state = AgentState(objective="Build a governed autonomous SDLC workflow")

        final_state = graph.invoke(initial_state, config={"recursion_limit": 80})

        # Gate 3 path should produce architecture and architecture-phase assessments.
        self.assertIn("architecture", final_state)
        self.assertTrue(final_state.get("architecture"))

        outputs = final_state.get("agent_outputs", {})
        self.assertIn("architecture_security_assessment", outputs)
        self.assertIn("architecture_safety_assessment", outputs)
        self.assertIn("architecture_reliability_assessment", outputs)

        board_results = final_state.get("board_results", {})
        self.assertIn("architecture_review", board_results)
        self.assertIn(
            board_results["architecture_review"].decision,
            ["approve", "approve_with_conditions"],
        )

        # Governance validation should remain structurally valid throughout execution.
        governance_validation = final_state.get("governance_validation", {})
        results = governance_validation.get("results", [])
        if results:
            self.assertTrue(str(results[0].get("gate", "")).startswith("gate_"))

        # Once Gate 3 is ready, workflow should be past architecture.
        phase = final_state.get("phase")
        self.assertIn(
            phase,
            [
                Phase.DESIGN,
                Phase.IMPLEMENTATION,
                Phase.VERIFICATION,
                Phase.DEPLOYMENT,
                Phase.MAINTENANCE,
            ],
        )


if __name__ == "__main__":
    unittest.main()
