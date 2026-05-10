"""Integration tests for in-memory checkpoint snapshot helpers."""

from __future__ import annotations

import unittest

from src.state.persistence import PersistenceManager


class PersistenceSnapshotIntegrationTest(unittest.TestCase):
    def test_save_and_load_checkpoint_snapshot(self) -> None:
        manager = PersistenceManager()
        payload = {"phase": "requirements", "messages": ["hello"]}

        manager.save_checkpoint_snapshot("session-1", payload)
        loaded = manager.load_checkpoint_snapshot("session-1")

        self.assertEqual(loaded, payload)
        self.assertIsNot(loaded, payload)

    def test_list_checkpoint_sessions_sorted(self) -> None:
        manager = PersistenceManager()
        manager.save_checkpoint_snapshot("session-b", {"phase": "design"})
        manager.save_checkpoint_snapshot("session-a", {"phase": "architecture"})

        self.assertEqual(manager.list_checkpoint_sessions(), ["session-a", "session-b"])

    def test_resume_from_arbitrary_restore_point(self) -> None:
        manager = PersistenceManager()
        manager.save_checkpoint_snapshot(
            "session-restore",
            {"phase": "requirements", "messages": ["first"]},
            label="first",
        )
        manager.save_checkpoint_snapshot(
            "session-restore",
            {"phase": "architecture", "messages": ["second"]},
            label="second",
        )

        restore_points = manager.list_restore_points("session-restore")
        self.assertGreaterEqual(len(restore_points), 2)

        oldest = restore_points[-1]["snapshot_id"]
        restored = manager.load_checkpoint_snapshot("session-restore", resume_point=oldest)

        self.assertIsNotNone(restored)
        self.assertEqual(restored["phase"], "requirements")

    def test_rollback_to_restore_point_creates_new_snapshot(self) -> None:
        manager = PersistenceManager()
        manager.save_checkpoint_snapshot("session-rb", {"phase": "requirements"}, label="v1")
        manager.save_checkpoint_snapshot("session-rb", {"phase": "implementation"}, label="v2")

        restore_points = manager.list_restore_points("session-rb")
        target_snapshot = restore_points[-1]["snapshot_id"]

        rolled_back = manager.rollback_to_restore_point("session-rb", target_snapshot)
        self.assertIsNotNone(rolled_back)
        self.assertEqual(rolled_back["phase"], "requirements")

        latest = manager.load_checkpoint_snapshot("session-rb")
        self.assertEqual(latest["phase"], "requirements")

    def test_observability_events_round_trip(self) -> None:
        manager = PersistenceManager()
        manager.record_observability_event(
            "agent_execution",
            {"agent": "program_manager", "duration_seconds": 0.5},
            session_id="session-obs",
        )
        manager.record_observability_event(
            "health_snapshot",
            {"all_healthy": True},
        )

        all_events = manager.list_observability_events(limit=10)
        self.assertGreaterEqual(len(all_events), 2)

        filtered = manager.list_observability_events(
            event_type="agent_execution",
            session_id="session-obs",
            limit=10,
        )
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["payload"]["agent"], "program_manager")
