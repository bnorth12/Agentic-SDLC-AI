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
