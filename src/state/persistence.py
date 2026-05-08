"""Persistence management for LangGraph checkpointing."""

from __future__ import annotations

import logging
from typing import Any

from langgraph.checkpoint.postgres import PostgresSaver
from psycopg import Connection

from src.config import get_settings

logger = logging.getLogger(__name__)


class PersistenceManager:
    """Manages LangGraph checkpoint persistence."""

    def __init__(self):
        self.settings = get_settings()
        self._checkpointer: PostgresSaver | None = None
        self._connection: Connection | None = None

    def get_checkpointer(self) -> PostgresSaver:
        """Get or create the checkpoint saver."""
        if self._checkpointer is None:
            self._checkpointer = PostgresSaver.from_conn_string(
                self.settings.postgres_url
            )
            logger.info("PostgreSQL checkpointer initialized")

        return self._checkpointer

    def setup_database(self) -> None:
        """Initialize database tables for checkpointing."""
        checkpointer = self.get_checkpointer()
        checkpointer.setup()
        logger.info("Database schema initialized")

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
