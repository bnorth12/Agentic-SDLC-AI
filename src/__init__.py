"""Agentic SDLC AI - Multi-agent systems engineering organization."""

__version__ = "0.1.0"
__author__ = "Agentic SDLC AI Contributors"

from src.graphs import build_supervisor_graph
from src.state import AgentState

__all__ = ["AgentState", "build_supervisor_graph", "__version__"]