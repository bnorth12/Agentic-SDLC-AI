"""Memory and RAG tools for long-term context."""

from __future__ import annotations

from src.utils.logging import get_logger

logger = get_logger(__name__)


class MemoryStore:
    """Simple in-memory store for agent context (production would use vector DB)."""

    def __init__(self):
        self._memories: dict[str, list[str]] = {}

    def add_memory(self, agent_name: str, memory: str) -> None:
        """
        Add a memory entry for an agent.

        Args:
            agent_name: Name of the agent
            memory: Memory content to store
        """
        if agent_name not in self._memories:
            self._memories[agent_name] = []

        self._memories[agent_name].append(memory)
        logger.debug(f"Added memory for {agent_name}")

    def get_memories(self, agent_name: str, limit: int = 10) -> list[str]:
        """
        Retrieve recent memories for an agent.

        Args:
            agent_name: Name of the agent
            limit: Maximum number of memories to retrieve

        Returns:
            List of recent memories
        """
        memories = self._memories.get(agent_name, [])
        return memories[-limit:]

    def search_memories(self, query: str, agent_name: str | None = None) -> list[str]:
        """
        Search memories by keyword (simplified - production would use embeddings).

        Args:
            query: Search query
            agent_name: Optional agent name to limit search

        Returns:
            List of matching memories
        """
        query_lower = query.lower()
        results = []

        if agent_name:
            memories = self._memories.get(agent_name, [])
            results = [m for m in memories if query_lower in m.lower()]
        else:
            for memories in self._memories.values():
                results.extend([m for m in memories if query_lower in m.lower()])

        logger.debug(f"Found {len(results)} memories matching '{query}'")
        return results

    def clear_agent_memories(self, agent_name: str) -> None:
        """
        Clear all memories for an agent.

        Args:
            agent_name: Name of the agent
        """
        if agent_name in self._memories:
            del self._memories[agent_name]
            logger.debug(f"Cleared memories for {agent_name}")


# Global memory store instance
_memory_store: MemoryStore | None = None


def get_memory_store() -> MemoryStore:
    """Get the global memory store instance."""
    global _memory_store
    if _memory_store is None:
        _memory_store = MemoryStore()
    return _memory_store
