"""Load .workspace.yaml manifests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class WorkspaceManifest(BaseModel):
    id: str
    maturity: str = "M1"
    repos: list[dict[str, Any]] = Field(default_factory=list)
    packs: list[str] = Field(default_factory=list)
    gates: dict[str, str] = Field(default_factory=dict)
    runtime: dict[str, Any] = Field(default_factory=dict)
    toolchains: list[str] = Field(default_factory=list)
    github: dict[str, Any] = Field(default_factory=dict)


def load_workspace(path: Path) -> WorkspaceManifest:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return WorkspaceManifest(**data)