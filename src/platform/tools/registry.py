"""Minimal Tool Registry + Permission/Scoping Model (L2/L4 Priority 1).

Provides:
- ToolSpec (name, description, scopes, callable)
- ToolRegistry singleton with register / get / list / invoke
- Auto-bootstrap of ide_core tools on first use
- Frontmatter declaration support (tools: list, required_scopes)
- Basic evidence-friendly invoke (no hard enforcement in batch 1; declaration recorded for G1/G3)

Dual surface: Python callable for L2 executor / agents (and future GUI runtime);
thin PowerShell wrapper (Invoke-IdeTool.ps1) + python -c for PS-MVP terminal and future GUI integrated terminal.

Traceability: Satisfies TOOL-001, L4-001 in IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md
and E2.1 in NEXT_WAVE_02_CHARTER.md. References IDE_REFACTOR_PLAN §5 (L2+L4 tooling).
"""

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class ToolSpec(BaseModel):
    """Declaration for a platform tool (callable from skills/procedures or agents)."""
    name: str
    description: str = ""
    scopes: list[str] = Field(default_factory=list)  # e.g. ["ide.fs.read", "ide.hierarchy", "gh.evidence", "exec.ps"]
    func: Any = None  # Python callable; future: also ps_invoker path or module


class ToolRegistry:
    """Central registry. Lives in L4 but wired at L2 for procedural execution.

    Batch 1: permissive invoke (records declared intent). Future batches add caller
    context + scope intersection enforcement before dispatch.
    """

    def __init__(self) -> None:
        self._tools: dict[str, ToolSpec] = {}

    def register(self, spec: ToolSpec) -> None:
        if not spec.func:
            raise ValueError(f"Tool {spec.name} has no callable func")
        self._tools[spec.name] = spec

    def get(self, name: str) -> Optional[ToolSpec]:
        return self._tools.get(name)

    def list_tools(self, scope: str | None = None) -> list[str]:
        if scope is None:
            return sorted(self._tools.keys())
        return sorted(n for n, s in self._tools.items() if scope in (s.scopes or []))

    def invoke(self, name: str, **kwargs: Any) -> Any:
        spec = self.get(name)
        if not spec or spec.func is None:
            raise KeyError(f"Tool not registered or not callable: {name}")
        # Batch 1: declaration-based (caller SKILL frontmatter declares; evidence captures)
        # No runtime scope intersection yet — logged in result for G1 traceability.
        return spec.func(**kwargs)

    def bootstrap_core_tools(self) -> int:
        """Register the initial ide_core set (idempotent)."""
        from .ide_core import IDE_CORE_TOOLS  # local import to avoid circular at module load

        registered = 0
        for name, fn in IDE_CORE_TOOLS.items():
            if name in self._tools:
                continue
            doc = (fn.__doc__ or name).strip().splitlines()[0][:120]
            # Heuristic scopes for core tools
            scopes: list[str] = ["ide.general"]
            if any(k in name for k in ("artifact", "read", "write")):
                scopes = ["ide.fs.read", "ide.fs.write"]
            if "hierarchy" in name or "validate" in name:
                scopes = ["ide.hierarchy", "ide.fs.read"]
            if "generalize" in name:
                scopes = ["ide.fs.read", "ide.generalize"]
            self.register(ToolSpec(name=name, description=doc, scopes=scopes, func=fn))
            registered += 1
        return registered


# Singleton
_registry: ToolRegistry | None = None


def get_registry() -> ToolRegistry:
    global _registry
    if _registry is None:
        _registry = ToolRegistry()
        _registry.bootstrap_core_tools()
    return _registry


def reset_registry_for_tests() -> None:
    """Test helper only."""
    global _registry
    _registry = None


def parse_declared_tools(frontmatter: dict[str, Any] | BaseModel) -> list[str]:
    """Extract declared tool names from SKILL.md frontmatter (supports flat list or nested)."""
    if isinstance(frontmatter, BaseModel):
        fm = frontmatter.model_dump()
    else:
        fm = frontmatter or {}

    # Support common shapes seen in generalized skills:
    # tools: [ "validate_hierarchy_metadata", ... ]
    # or metadata.tools, or required_tools
    candidates = []
    for key in ("tools", "required_tools", "tool_names"):
        val = fm.get(key)
        if isinstance(val, list):
            candidates.extend([str(v) for v in val])
        elif isinstance(val, str):
            candidates.append(val)

    # Also look under a nested "metadata" or "tool" block if present (some skills use metadata:)
    meta = fm.get("metadata") or {}
    if isinstance(meta, dict):
        for key in ("tools", "required_tools"):
            val = meta.get(key)
            if isinstance(val, list):
                candidates.extend([str(v) for v in val])
        # Also support tools declared under metadata (as we did for P1 batch on steward)
        if "tools" in meta and isinstance(meta.get("tools"), list):
            candidates.extend(str(v) for v in meta["tools"])
        if "required_scopes" in meta and isinstance(meta.get("required_scopes"), list):
            # scopes handled by the other parser; for declared_tools we only want tool names here
            pass

    # Dedup preserve order
    seen = set()
    out = []
    for c in candidates:
        if c and c not in seen:
            seen.add(c)
            out.append(c)
    return out


def parse_required_scopes(frontmatter: dict[str, Any] | BaseModel) -> list[str]:
    if isinstance(frontmatter, BaseModel):
        fm = frontmatter.model_dump()
    else:
        fm = frontmatter or {}
    scopes: list[str] = []
    for key in ("required_scopes", "scopes", "tool_scopes"):
        val = fm.get(key)
        if isinstance(val, list):
            scopes.extend([str(v) for v in val])
    meta = fm.get("metadata") or {}
    if isinstance(meta, dict):
        for key in ("required_scopes", "scopes"):
            val = meta.get(key)
            if isinstance(val, list):
                scopes.extend(str(v) for v in val)
        if "required_scopes" in meta and isinstance(meta.get("required_scopes"), list):
            scopes.extend(str(v) for v in meta["required_scopes"])
    return list(dict.fromkeys(scopes))  # dedup order preserving


# Convenience re-export for executor / router consumers
__all__ = [
    "ToolSpec",
    "ToolRegistry",
    "get_registry",
    "reset_registry_for_tests",
    "parse_declared_tools",
    "parse_required_scopes",
]
