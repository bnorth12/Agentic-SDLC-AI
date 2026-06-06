"""Discover and load plugin manifests from plugins/packs/."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class PluginManifest(BaseModel):
    id: str
    version: str
    type: str
    name: str | None = None
    description: str | None = None
    entry: dict[str, Any] = Field(default_factory=dict)
    os: list[str] = Field(default_factory=list)
    languages: list[str] = Field(default_factory=list)
    dependencies: dict[str, list[str]] = Field(default_factory=dict)
    path: Path | None = None


class PluginLoader:
    def __init__(self, plugins_root: Path | None = None) -> None:
        root = Path(__file__).resolve().parents[3]
        self.plugins_root = plugins_root or root / "plugins" / "packs"

    def discover(self) -> list[PluginManifest]:
        found: list[PluginManifest] = []
        if not self.plugins_root.exists():
            return found
        for pack_dir in self.plugins_root.iterdir():
            if not pack_dir.is_dir() or pack_dir.name.startswith("_"):
                continue
            manifest_file = pack_dir / "plugin.manifest.yaml"
            if not manifest_file.exists():
                continue
            data = yaml.safe_load(manifest_file.read_text(encoding="utf-8"))
            m = PluginManifest(**data, path=pack_dir)
            found.append(m)
        return found