"""Agentic SDLC AI - Multi-agent systems engineering organization."""

__version__ = "0.1.0"
__author__ = "Agentic SDLC AI Contributors"

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
	from src.state.schema import AgentState as AgentState


def build_supervisor_graph(*args: Any, **kwargs: Any) -> Any:
	"""Build the supervisor graph using a lazy import."""
	from src.graphs import build_supervisor_graph as _build_supervisor_graph

	return _build_supervisor_graph(*args, **kwargs)


def __getattr__(name: str) -> Any:
	"""Lazily expose AgentState without importing optional persistence deps."""
	if name == "AgentState":
		from src.state.schema import AgentState as _AgentState

		return _AgentState
	raise AttributeError(f"module 'src' has no attribute {name!r}")

__all__ = ["AgentState", "build_supervisor_graph", "__version__"]