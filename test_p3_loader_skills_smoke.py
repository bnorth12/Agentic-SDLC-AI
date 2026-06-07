"""P3 Slice 1 smoke: Manifest/Pack Loader + Skills Discovery.

Run:
  .\.venv\Scripts\python.exe test_p3_loader_skills_smoke.py

Focus (tiny slice):
- Extend PluginLoader with discover_skills() using entry.skills_dir + P1 frontmatter parsing.
- Returns id/pack_id/declared_tools etc.
- Live test: discover ide-platform skills, assert known ones + their tools (from P1 declarations).
- Tiny changes, dual ready (Python loader; PS helper next slice), trace to L4-001 / §5 / matrix.

This is the first small testable batch for P3 (Manifest / Pack Loader + Discovery Tool).
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.platform.plugins.loader import PluginLoader


def main() -> int:
    print("=== P3 Loader Skills Smoke (slice 1) ===")

    loader = PluginLoader()
    packs = loader.discover()
    pack_ids = {p.id for p in packs}
    print(f"discovered packs: {sorted(pack_ids)}")
    assert "ide-platform" in pack_ids
    print("  PASS: ide-platform pack discovered")

    skills = loader.discover_skills()
    skill_ids = {s["id"] for s in skills}
    print(f"discovered skills count: {len(skills)} (sample: {list(skill_ids)[:5]})")
    assert "ide-platform" in {s["pack_id"] for s in skills}
    assert "ide-hierarchy-taxonomy-steward" in skill_ids
    assert "ide-decision-record" in skill_ids  # has declared tools from P1
    print("  PASS: ide-platform skills discovered (including P1 ones)")

    # Check declared_tools from P1 frontmatter
    hier = next((s for s in skills if s["id"] == "ide-hierarchy-taxonomy-steward"), None)
    assert hier and "validate_hierarchy_metadata" in hier.get("declared_tools", [])
    print(f"  PASS: ide-hierarchy-taxonomy-steward has declared_tools (P1): {hier['declared_tools']}")

    dec = next((s for s in skills if s["id"] == "ide-decision-record"), None)
    assert dec and len(dec.get("declared_tools", [])) > 0
    print(f"  PASS: ide-decision-record declared_tools: {dec['declared_tools']}")

    print("\n=== P3 SLICE 1 SMOKE COMPLETE ===")
    print("Next slice: integrate loader into executor + registry population from manifests.")

    # P3 slice 2 integration check (live in this smoke for testability)
    from src.platform.orchestration.executor import run_procedural_skill
    from src.platform.tools.registry import get_registry
    res = run_procedural_skill("ide-hierarchy-taxonomy-steward")
    print(f"executor via loader: status={res.get('status')}, via_loader={res.get('discovered_via_loader')}, pack={res.get('pack_id')}")
    assert res.get("discovered_via_loader") is True
    assert res.get("pack_id") == "ide-platform"
    # status may be error/partial (doc-example pwsh -File steps in the SKILL); loader resolution + declared_tools are the P3 win
    outs = res.get("outputs", {})
    print(f"  declared_tools in outputs: {outs.get('declared_tools')}")
    assert "validate_hierarchy_metadata" in (outs.get("declared_tools") or [])
    print("  PASS: run_procedural_skill now uses loader discovery (P3) + declared_tools present")

    reg = get_registry()
    decl = getattr(reg, "_skill_declarations", {})
    print(f"registry skill_decls packs: {list(decl.keys())}")
    assert "ide-platform" in decl
    assert "ide-hierarchy-taxonomy-steward" in decl.get("ide-platform", {})
    print("  PASS: registry populated with skill declarations from manifests (P3)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
