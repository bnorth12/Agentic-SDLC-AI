"""Persistence management for LangGraph checkpointing."""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

try:
    from langgraph.checkpoint.postgres import PostgresSaver
except Exception:  # pragma: no cover - optional dependency
    PostgresSaver = Any  # type: ignore[assignment]

try:
    from psycopg import Connection
except Exception:  # pragma: no cover - optional dependency
    Connection = Any  # type: ignore[assignment]

try:
    import psycopg
except Exception:  # pragma: no cover - optional dependency
    psycopg = None

from src.config import get_settings

logger = logging.getLogger(__name__)


class PersistenceManager:
    """Manages LangGraph checkpoint persistence."""

    def __init__(self):
        self.settings = get_settings()
        self._checkpointer: PostgresSaver | None = None
        self._connection: Connection | None = None
        self._db_available: bool | None = None
        self._checkpoint_cache: dict[str, dict[str, Any]] = {}
        self._snapshot_history: dict[str, list[dict[str, Any]]] = {}
        self._observability_events: list[dict[str, Any]] = []

    def _get_connection(self) -> Connection | None:
        """Get or establish a PostgreSQL connection for optional persistence helpers."""
        if self._connection:
            return self._connection
        if self._db_available is False:
            return None
        if psycopg is None:
            self._db_available = False
            return None

        try:
            self._connection = psycopg.connect(
                self.settings.postgres_url,
                connect_timeout=2,
            )
            self._db_available = True
            return self._connection
        except Exception:
            self._db_available = False
            return None

    def _ensure_aux_tables(self) -> None:
        """Create snapshot history and observability event tables if possible."""
        conn = self._get_connection()
        if not conn:
            return

        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS workflow_snapshots (
                        id BIGSERIAL PRIMARY KEY,
                        session_id TEXT NOT NULL,
                        label TEXT,
                        state_payload JSONB NOT NULL,
                        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                    )
                    """
                )
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS observability_events (
                        id BIGSERIAL PRIMARY KEY,
                        event_type TEXT NOT NULL,
                        session_id TEXT,
                        payload JSONB NOT NULL,
                        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                    )
                    """
                )
            conn.commit()
        except Exception:
            conn.rollback()

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
        self._ensure_aux_tables()
        logger.info("Database schema initialized")

    def save_checkpoint_snapshot(
        self,
        session_id: str,
        state_payload: dict[str, Any],
        label: str | None = None,
    ) -> None:
        """Persist a checkpoint snapshot and append restore point history."""
        if not session_id:
            return

        payload = dict(state_payload)
        now = datetime.utcnow().isoformat()
        snapshot = {
            "snapshot_id": f"{session_id}:{len(self._snapshot_history.get(session_id, [])) + 1}",
            "session_id": session_id,
            "label": label or "auto",
            "created_at": now,
            "state": payload,
        }

        history = self._snapshot_history.setdefault(session_id, [])
        history.append(snapshot)
        self._checkpoint_cache[session_id] = payload

        conn = self._get_connection()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO workflow_snapshots (session_id, label, state_payload)
                        VALUES (%s, %s, %s)
                        """,
                        (session_id, snapshot["label"], payload),
                    )
                conn.commit()
            except Exception:
                conn.rollback()

        logger.info("Checkpoint snapshot updated for session_id=%s", session_id)

    def load_checkpoint_snapshot(
        self,
        session_id: str,
        resume_point: str | None = None,
    ) -> dict[str, Any] | None:
        """Load latest or specific restore point payload for session resume."""
        if not session_id:
            return None

        if resume_point:
            for snapshot in reversed(self._snapshot_history.get(session_id, [])):
                if snapshot["snapshot_id"] == resume_point:
                    return dict(snapshot["state"])

        payload = self._checkpoint_cache.get(session_id)
        if payload:
            return dict(payload)

        conn = self._get_connection()
        if not conn:
            return None

        try:
            with conn.cursor() as cur:
                if resume_point:
                    cur.execute(
                        """
                        SELECT state_payload
                        FROM workflow_snapshots
                        WHERE session_id = %s AND CONCAT(session_id, ':', id::text) = %s
                        ORDER BY id DESC
                        LIMIT 1
                        """,
                        (session_id, resume_point),
                    )
                else:
                    cur.execute(
                        """
                        SELECT state_payload
                        FROM workflow_snapshots
                        WHERE session_id = %s
                        ORDER BY id DESC
                        LIMIT 1
                        """,
                        (session_id,),
                    )
                row = cur.fetchone()
                if row and row[0]:
                    state_payload = dict(row[0])
                    self._checkpoint_cache[session_id] = dict(state_payload)
                    return state_payload
        except Exception:
            return None

        return None

    def list_checkpoint_sessions(self) -> list[str]:
        """List cached session identifiers available for local resume."""
        sessions = set(self._checkpoint_cache.keys())
        sessions.update(self._snapshot_history.keys())

        conn = self._get_connection()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT DISTINCT session_id FROM workflow_snapshots")
                    rows = cur.fetchall()
                for row in rows:
                    if row and row[0]:
                        sessions.add(str(row[0]))
            except Exception:
                pass

        return sorted(sessions)

    def list_restore_points(
        self, session_id: str, limit: int = 50
    ) -> list[dict[str, Any]]:
        """List available restore points for a session."""
        restore_points = []

        recent_snapshots = self._snapshot_history.get(session_id, [])[-limit:]
        for snapshot in reversed(recent_snapshots):
            restore_points.append(
                {
                    "snapshot_id": snapshot["snapshot_id"],
                    "label": snapshot["label"],
                    "created_at": snapshot["created_at"],
                }
            )

        conn = self._get_connection()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id, label, created_at
                        FROM workflow_snapshots
                        WHERE session_id = %s
                        ORDER BY id DESC
                        LIMIT %s
                        """,
                        (session_id, limit),
                    )
                    rows = cur.fetchall()
                if rows:
                    restore_points = [
                        {
                            "snapshot_id": f"{session_id}:{row[0]}",
                            "label": row[1] or "auto",
                            "created_at": row[2].isoformat() if row[2] else "",
                        }
                        for row in rows
                    ]
            except Exception:
                pass

        return restore_points

    def rollback_to_restore_point(
        self, session_id: str, snapshot_id: str
    ) -> dict[str, Any] | None:
        """Rollback the session cache to a selected restore point."""
        payload = self.load_checkpoint_snapshot(session_id, resume_point=snapshot_id)
        if not payload:
            return None

        self._checkpoint_cache[session_id] = dict(payload)
        self.save_checkpoint_snapshot(
            session_id,
            payload,
            label=f"rollback:{snapshot_id}",
        )
        return payload

    def record_observability_event(
        self,
        event_type: str,
        payload: dict[str, Any],
        session_id: str | None = None,
    ) -> None:
        """Persist observability event in memory and optional postgres store."""
        event = {
            "event_type": event_type,
            "session_id": session_id,
            "payload": dict(payload),
            "created_at": datetime.utcnow().isoformat(),
        }
        self._observability_events.append(event)

        conn = self._get_connection()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO observability_events (event_type, session_id, payload)
                        VALUES (%s, %s, %s)
                        """,
                        (event_type, session_id, payload),
                    )
                conn.commit()
            except Exception:
                conn.rollback()

    def list_observability_events(
        self,
        event_type: str | None = None,
        session_id: str | None = None,
        limit: int = 200,
    ) -> list[dict[str, Any]]:
        """List historical observability events."""
        events = [
            event
            for event in self._observability_events
            if (event_type is None or event["event_type"] == event_type)
            and (session_id is None or event["session_id"] == session_id)
        ]

        conn = self._get_connection()
        if conn:
            try:
                query = """
                    SELECT event_type, session_id, payload, created_at
                    FROM observability_events
                    WHERE (%s IS NULL OR event_type = %s)
                      AND (%s IS NULL OR session_id = %s)
                    ORDER BY id DESC
                    LIMIT %s
                """
                with conn.cursor() as cur:
                    cur.execute(
                        query,
                        (event_type, event_type, session_id, session_id, limit),
                    )
                    rows = cur.fetchall()
                return [
                    {
                        "event_type": row[0],
                        "session_id": row[1],
                        "payload": dict(row[2]) if row[2] else {},
                        "created_at": row[3].isoformat() if row[3] else "",
                    }
                    for row in rows
                ]
            except Exception:
                pass

        return events[-limit:]

    def close(self) -> None:
        """Close database connections."""
        if self._connection:
            self._connection.close()
            self._connection = None
            self._db_available = None
            logger.info("Database connection closed")


# Global persistence manager instance
_persistence_manager: PersistenceManager | None = None


def get_persistence_manager() -> PersistenceManager:
    """Get the global persistence manager instance."""
    global _persistence_manager
    if _persistence_manager is None:
        _persistence_manager = PersistenceManager()
    return _persistence_manager
