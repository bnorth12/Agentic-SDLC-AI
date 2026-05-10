"""End-to-end integration test for intake through verification Gate 5 readiness."""

from __future__ import annotations

import unittest

from src.graphs.supervisor import build_supervisor_graph
from src.state.schema import AgentState, Phase


class EndToEndIntakeToGate5Test(unittest.TestCase):
    """Validate Sprint 5 intake-to-Gate-5 flow with V&V evidence."""

    def test_intake_to_gate5_includes_traceability_and_coverage(self) -> None:
        graph = build_supervisor_graph()
        initial_state = AgentState(objective="Build a governed autonomous SDLC workflow")

        final_state = graph.invoke(initial_state, config={"recursion_limit": 140})

        outputs = final_state.get("agent_outputs", {})
        self.assertIn("verification_validation_package", outputs)
        self.assertIn("verification_package", outputs)

        vv_package = outputs["verification_validation_package"]
        coverage = vv_package.get("coverage_tracking", {})

        self.assertGreaterEqual(float(coverage.get("coverage_percent", 0.0)), 80.0)
        self.assertEqual(
            int(coverage.get("linked_requirement_count", 0)),
            int(coverage.get("requirement_count", 0)),
        )

        mapping = vv_package.get("requirements_to_test_mapping", [])
        self.assertGreater(len(mapping), 0)
        self.assertTrue(all(item.get("test_cases") for item in mapping))

        signoff = vv_package.get("vnv_signoff", {})
        self.assertEqual(signoff.get("status"), "approved")

        governance_validation = final_state.get("governance_validation", {})
        results = governance_validation.get("results", [])
        if results:
            self.assertTrue(str(results[0].get("gate", "")).startswith("gate_"))

        self.assertIn(
            final_state.get("phase"),
            [
                Phase.DEPLOYMENT,
                Phase.MAINTENANCE,
            ],
        )


if __name__ == "__main__":
    unittest.main()
