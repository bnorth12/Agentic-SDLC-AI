"""Route work packages to procedural, LangGraph, or ACP executors.

Now wired for PROCEDURAL mode using the new L2 ProceduralSkillExecutor (E1.1).
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

from .executor import run_procedural_skill


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
    """Select executor from gate registry or explicit work package mode.

    For PROCEDURAL: delegates to run_procedural_skill (parses SKILL.md,
    executes supported steps, returns evidence).
    """

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

        if mode == ExecutionMode.PROCEDURAL:
            if not package.skill_id:
                return {
                    "status": "error",
                    "mode": mode.value,
                    "package_id": package.id,
                    "error": "skill_id required for PROCEDURAL mode",
                }
            # Delegate to the new procedural executor
            result = run_procedural_skill(
                skill_id=package.skill_id,
                payload=package.payload,
            )
            result["package_id"] = package.id
            result["mode"] = mode.value
            return result

        # Still scaffold for other modes (LangGraph / ACP) — future work
        return {
            "status": "scaffold",
            "mode": mode.value,
            "package_id": package.id,
            "message": f"{mode.value} executor not yet wired (see L2 roadmap)",
        }