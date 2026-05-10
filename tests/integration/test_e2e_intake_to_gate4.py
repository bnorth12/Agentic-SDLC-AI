"""End-to-end integration test for intake through implementation Gate 4 readiness."""

from __future__ import annotations

import unittest

from src.graphs.supervisor import build_supervisor_graph
from src.state.schema import AgentState, Phase


class EndToEndIntakeToGate4Test(unittest.TestCase):
    """Validate Sprint 4 intake-to-Gate-4 flow with dev+CM evidence."""

    def test_intake_to_gate4_includes_dev_and_cm_packages(self) -> None:
        graph = build_supervisor_graph()
        initial_state = AgentState(objective="Build a governed autonomous SDLC workflow")

        final_state = graph.invoke(initial_state, config={"recursion_limit": 120})

        outputs = final_state.get("agent_outputs", {})
        self.assertIn("software_development_package", outputs)
        self.assertIn("configuration_management_package", outputs)
        self.assertIn("implementation_package", outputs)

        impl_package = outputs["implementation_package"]
        self.assertIn("change_set_summary", impl_package)
        self.assertIn("test_report", impl_package)
        self.assertIn("lint_report", impl_package)
        self.assertIn("configuration_baseline_update", impl_package)

        governance_validation = final_state.get("governance_validation", {})
        results = governance_validation.get("results", [])
        if results:
            self.assertTrue(str(results[0].get("gate", "")).startswith("gate_"))

        self.assertIn(
            final_state.get("phase"),
            [
                Phase.VERIFICATION,
                Phase.DEPLOYMENT,
                Phase.MAINTENANCE,
            ],
        )


if __name__ == "__main__":
    unittest.main()
