"""Unit tests for KPI tracker metrics aggregation."""

from __future__ import annotations

import unittest

from src.metrics import KPITracker


class KPITrackerUnitTest(unittest.TestCase):
    def test_records_agent_execution_and_errors(self) -> None:
        tracker = KPITracker()

        tracker.record_agent_execution("program_manager", 0.25)
        tracker.record_agent_execution("program_manager", 0.75)
        tracker.record_error("program_manager")

        report = tracker.get_metrics_report()

        self.assertEqual(report["agents"]["program_manager"], 2)
        self.assertEqual(report["errors"]["total"], 1)
        self.assertEqual(report["errors"]["by_agent"]["program_manager"], 1)
        self.assertIn("average_agent_execution_times", report)

    def test_records_phase_transition_average(self) -> None:
        tracker = KPITracker()

        tracker.record_phase_transition("requirements", "architecture", 1.0)
        tracker.record_phase_transition("requirements", "architecture", 3.0)

        report = tracker.get_metrics_report()
        self.assertIn("average_phase_transition_times", report)
        self.assertEqual(
            report["average_phase_transition_times"]["requirements_to_architecture"],
            "2.00s",
        )


if __name__ == "__main__":
    unittest.main()
