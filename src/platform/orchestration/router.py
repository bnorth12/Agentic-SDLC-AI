"""Route work packages to procedural, LangGraph, or ACP executors."""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class ExecutionMode(str, Enum):
    PROCEDURAL = "procedural"
    LANGGRAPH = "langgraph"
    ACP = "acp"


class WorkPackage(BaseModel):
    id: str
    gate_id: str | None = None
    skill_id: str | None = None
    plugin_id: str | None = None
    mode: ExecutionMode = ExecutionMode.PROCEDURAL
    payload: dict[str, Any] = Field(default_factory=dict)


class OrchestrationRouter:
    """Select executor from gate registry or explicit work package mode."""

    def resolve_mode(self, package: WorkPackage) -> ExecutionMode:
        if package.mode != ExecutionMode.PROCEDURAL:
            return package.mode
        if package.plugin_id:
            return ExecutionMode.LANGGRAPH
        if package.skill_id and package.skill_id.endswith("-acp"):
            return ExecutionMode.ACP
        return ExecutionMode.PROCEDURAL

    def execute(self, package: WorkPackage) -> dict[str, Any]:
        mode = self.resolve_mode(package)
        # Scaffold: wire to executors in R1
        return {
            "status": "scaffold",
            "mode": mode.value,
            "package_id": package.id,
            "message": "Executor not wired — see docs/charter/REFACTOR_TODO.md R1",
        }