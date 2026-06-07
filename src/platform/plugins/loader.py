"""Discover and load plugin manifests from plugins/packs/."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field

# P3: reuse for frontmatter + declared tools (from P1)
from ..tools.ide_core import read_ide_artifact
from ..tools.registry import parse_declared_tools


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

    def discover_skills(self) -> list[dict]:
        """P3 slice 1: discover SKILL.md under each pack's entry.skills_dir.
        Returns list of {id, pack_id, path, frontmatter, declared_tools}.
        Reuses P1 read_ide_artifact + parse_declared_tools for consistency.
        """
        found: list[dict] = []
        for pack in self.discover():
            entry = pack.entry or {}
            skills_dir_name = entry.get("skills_dir", "skills")
            base = pack.path or (self.plugins_root / pack.id)
            skills_dir = base / skills_dir_name
            if not skills_dir.exists() or not skills_dir.is_dir():
                continue
            for skill_dir in skills_dir.iterdir():
                if not skill_dir.is_dir():
                    continue
                skill_md = skill_dir / "SKILL.md"
                if not skill_md.exists():
                    continue
                try:
                    art = read_ide_artifact(skill_md)
                    fm = art.get("frontmatter", {})
                    tools = parse_declared_tools(fm)
                    found.append({
                        "id": fm.get("name", skill_dir.name),
                        "pack_id": pack.id,
                        "path": str(skill_md),
                        "frontmatter": fm,
                        "declared_tools": tools,
                    })
                except Exception:
                    continue
        return found