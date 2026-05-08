"""Shared state schema for the Agentic SDLC orchestration graph."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class AgentState(BaseModel):
    """Represents shared graph state exchanged across supervisor and specialist agents."""

    objective: str = ""
    phase: str = "intake"
    backlog: list[str] = Field(default_factory=list)
    artifacts: dict[str, Any] = Field(default_factory=dict)
    messages: list[str] = Field(default_factory=list)
    decisions: list[str] = Field(default_factory=list)
    requires_human_approval: bool = False
