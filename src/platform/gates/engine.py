"""Gate registry loader and HITL policy evaluation."""

from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class GateMode(str, Enum):
    MANDATORY = "mandatory"
    OPTIONAL = "optional"
    WAIVED = "waived"
    MATURITY_GATED = "maturity-gated"


class GateDefinition(BaseModel):
    id: str
    name: str
    phase: str
    default_mode: GateMode
    executor: dict[str, Any] = Field(default_factory=dict)
    viewer: str | None = None
    enforce_at: list[str] = Field(default_factory=list)


class GateEngine:
    """Load platform/gates/registry.yaml and resolve effective mode per workspace."""

    def __init__(self, registry_path: Path | None = None) -> None:
        root = Path(__file__).resolve().parents[3]
        self.registry_path = registry_path or root / "platform" / "gates" / "registry.yaml"
        self._gates: dict[str, GateDefinition] = {}
        self._load()

    def _load(self) -> None:
        if not self.registry_path.exists():
            return
        data = yaml.safe_load(self.registry_path.read_text(encoding="utf-8"))
        for row in data.get("gates", []):
            g = GateDefinition(
                id=row["id"],
                name=row["name"],
                phase=row["phase"],
                default_mode=GateMode(row["default_mode"]),
                executor=row.get("executor", {}),
                viewer=row.get("viewer"),
                enforce_at=row.get("enforce_at", []),
            )
            self._gates[g.id] = g

    def list_gates(self) -> list[GateDefinition]:
        return list(self._gates.values())

    def effective_mode(
        self,
        gate_id: str,
        workspace_gates: dict[str, str] | None = None,
        maturity: str = "M1",
    ) -> GateMode:
        g = self._gates.get(gate_id)
        if not g:
            return GateMode.OPTIONAL
        if workspace_gates and gate_id in workspace_gates:
            return GateMode(workspace_gates[gate_id])
        if g.default_mode == GateMode.MATURITY_GATED:
            return GateMode.MANDATORY if maturity in ("M2", "M3", "M4") else GateMode.OPTIONAL
        return g.default_mode

    def requires_hitl(self, gate_id: str, **kwargs: Any) -> bool:
        return self.effective_mode(gate_id, **kwargs) == GateMode.MANDATORY