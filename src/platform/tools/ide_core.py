"""First core IDE-native tools for agents and skills (L2/L4).

These are the initial high-leverage tools to enable the Refactoring Agent,
Planning Agent, and generalized ide-* skills to operate on the new platform
model (editing .agent.md / SKILL.md, validating hierarchy, basic generalization
support, evidence helpers).

Exposed as Python-callable functions that can be invoked from the
ProceduralSkillExecutor or directly by agents.

Future: These will be registered in a tool registry (L4) and callable from
SKILL.md "tool" steps.
Priority 1 complete: see registry.py (get_registry() + bootstrap_core_tools auto-registers
these 4 on first use; parse_declared_tools supports frontmatter; executor wires declarations
and "tool:" steps). Dual: Python for L2 executor + future GUI runtime; PS wrapper for MVP terminal.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml


def read_ide_artifact(path: str | Path) -> dict[str, Any]:
    """Read a .agent.md or SKILL.md with frontmatter + body.

    Returns: {"frontmatter": dict, "body": str, "path": str}
    Safe for IDE artifacts (no arbitrary code execution).
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(str(p))

    content = p.read_text(encoding="utf-8")
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1]) or {}
            body = parts[2].strip()
            return {"frontmatter": fm, "body": body, "path": str(p)}

    # No frontmatter
    return {"frontmatter": {}, "body": content, "path": str(p)}


def write_ide_artifact(path: str | Path, frontmatter: dict[str, Any], body: str) -> str:
    """Write a .agent.md or SKILL.md with proper frontmatter.

    Returns the path written. Overwrites safely for IDE artifacts.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    fm_text = yaml.safe_dump(frontmatter, sort_keys=False, default_flow_style=False).strip()
    content = f"---\n{fm_text}\n---\n\n{body.strip()}\n"
    p.write_text(content, encoding="utf-8")
    return str(p)


def validate_hierarchy_metadata(artifact: dict[str, Any] | str | Path) -> dict[str, Any]:
    """Validate hierarchy metadata on an IDE artifact or dict.

    Expected fields (per IDE_REFACTOR_PLAN and structure docs):
    - Parent Capability
    - Child Function
    - Decomposition Level
    - Allocated Component/Module
    - Verification Method

    Returns report with "valid", "missing", "issues".
    This is the first version of the "hierarchy validator" tool.
    """
    if isinstance(artifact, (str, Path)):
        data = read_ide_artifact(artifact)
        text = data.get("body", "") + str(data.get("frontmatter", {}))
    else:
        text = str(artifact)

    required = [
        "Parent Capability",
        "Child Function",
        "Decomposition Level",
        "Allocated Component/Module",
        "Verification Method",
    ]

    found = {}
    issues = []

    for field in required:
        # Loose search (case-insensitive, common variants)
        pattern = re.compile(rf"{re.escape(field)}[:\s]*([^\n]+)", re.IGNORECASE)
        match = pattern.search(text)
        if match:
            found[field] = match.group(1).strip()
        else:
            issues.append(f"Missing: {field}")

    valid = len(issues) == 0
    return {
        "valid": valid,
        "found": found,
        "missing": [f for f in required if f not in found],
        "issues": issues,
        "score": f"{len(found)}/{len(required)}",
    }


def basic_generalize_stub(source_path: str | Path, target_pack: str = "ide-platform") -> dict[str, Any]:
    """Minimal stub for generalization helper tool.

    In real use this would do suffix stripping, path replacement,
    IDE surface injection, hierarchy addition, etc.

    For now: returns a plan of what would be done + a suggested target path.
    Used by ide-structural-refactoring skill procedures.
    """
    src = Path(source_path)
    name = src.stem.replace("-farmrtk", "").replace("requirements-implementation-auditor", "ide-requirements-implementation-auditor")

    if "agent" in src.suffixes or src.suffix == ".agent.md":
        target = f"plugins/packs/{target_pack}/agents/{name}.agent.md"
    else:
        target = f"plugins/packs/{target_pack}/skills/{name}/SKILL.md"

    return {
        "source": str(src),
        "suggested_target": target,
        "actions_planned": [
            "strip product suffix",
            "replace hard paths with manifest/gate references",
            "inject IDE surface awareness (editors, viewers, L0-L8)",
            "add PowerShell + gh examples",
            "ensure hierarchy metadata",
            "update Parent links to IDE_REFACTOR_PLAN + matrix",
        ],
        "status": "stub - real generalization still performed by Refactoring Agent + human for complex cases",
    }


# Convenience registry for the executor / future tool host
IDE_CORE_TOOLS = {
    "read_ide_artifact": read_ide_artifact,
    "write_ide_artifact": write_ide_artifact,
    "validate_hierarchy_metadata": validate_hierarchy_metadata,
    "basic_generalize_stub": basic_generalize_stub,
}
