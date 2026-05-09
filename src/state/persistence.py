"""Persistence management for LangGraph checkpointing."""

from __future__ import annotations

import logging
from typing import Any

try:
    from langgraph.checkpoint.postgres import PostgresSaver
except Exception:  # pragma: no cover - optional dependency
    PostgresSaver = Any  # type: ignore[assignment]

try:
    from psycopg import Connection
except Exception:  # pragma: no cover - optional dependency
    Connection = Any  # type: ignore[assignment]

from src.config import get_settings

logger = logging.getLogger(__name__)


class PersistenceManager:
    """Manages LangGraph checkpoint persistence."""

    def __init__(self):
        self.settings = get_settings()
        self._checkpointer: PostgresSaver | None = None
        self._connection: Connection | None = None
        self._checkpoint_cache: dict[str, dict[str, Any]] = {}

    def get_checkpointer(self) -> PostgresSaver:
        """Get or create the checkpoint saver."""
        if self._checkpointer is None:
            if not hasattr(PostgresSaver, "from_conn_string"):
                raise RuntimeError(
                    "langgraph postgres checkpoint dependencies are not installed"
                )
            self._checkpointer = PostgresSaver.from_conn_string(
                self.settings.postgres_url
            )
            logger.info("PostgreSQL checkpointer initialized")

        return self._checkpointer

    def setup_database(self) -> None:
        """Initialize database tables for checkpointing."""
        checkpointer = self.get_checkpointer()
        if not hasattr(checkpointer, "setup"):
            raise RuntimeError("Checkpoint saver does not support setup()")
        checkpointer.setup()
        logger.info("Database schema initialized")

    def save_checkpoint_snapshot(
        self,
        session_id: str,
        state_payload: dict[str, Any],
    ) -> None:
        """Cache the latest state payload for quick local resume support."""
        if not session_id:
            return

        self._checkpoint_cache[session_id] = dict(state_payload)
        logger.info("Checkpoint snapshot updated for session_id=%s", session_id)

    def load_checkpoint_snapshot(self, session_id: str) -> dict[str, Any] | None:
        """Load a cached state payload for session resume."""
        if not session_id:
            return None
        payload = self._checkpoint_cache.get(session_id)
        return dict(payload) if payload else None

    def list_checkpoint_sessions(self) -> list[str]:
        """List cached session identifiers available for local resume."""
        return sorted(self._checkpoint_cache.keys())

    def close(self) -> None:
        """Close database connections."""
        if self._connection:
            self._connection.close()
            logger.info("Database connection closed")


# Global persistence manager instance
_persistence_manager: PersistenceManager | None = None


def get_persistence_manager() -> PersistenceManager:
    """Get the global persistence manager instance."""
    global _persistence_manager
    if _persistence_manager is None:
        _persistence_manager = PersistenceManager()
    return _persistence_manager
