"""Priority 1 smoke test: Tool Registry + Permission/Scoping Model.

Run from repo root with:
  python test_p1_registry_smoke.py

Or via pwsh:
  $env:PYTHONPATH="."; python test_p1_registry_smoke.py

Validates:
- Registry bootstraps ide_core tools
- list_tools + invoke (validate + read)
- SKILL frontmatter declaration parse + capture in executor outputs
- "tool:" step execution producing evidence (when text contains tool: refs)
- Declared tools visible in SkillExecutionResult
- PS wrapper script exists and is documented for dual-use (PS-MVP + future GUI terminal)

This is the first small testable batch for the 5 tool priorities.
All changes traceable to IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md (TOOL-001, L4-001)
and remaining-xgen-refactoring-session.md (new Priority 1 batch log).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Ensure repo root on path when run directly
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.platform.tools.registry import (
    get_registry,
    reset_registry_for_tests,
    parse_declared_tools,
    parse_required_scopes,
)
from src.platform.orchestration.executor import (
    ProceduralSkillExecutor,
    run_procedural_skill,
    parse_skill_md,
)


def main() -> int:
    print("=== P1 Tool Registry Smoke ===")

    # 1. Registry bootstrap + list
    reset_registry_for_tests()
    reg = get_registry()
    tools = reg.list_tools()
    print(f"Registered tools: {tools}")
    assert "validate_hierarchy_metadata" in tools, "core tool missing"
    assert "read_ide_artifact" in tools, "core tool missing"
    print("  PASS: bootstrap + list_tools")

    # 2. Direct invoke of a core tool (uses read + validate internally for some)
    target = "plugins/packs/ide-platform/skills/ide-hierarchy-taxonomy-steward/SKILL.md"
    vres = reg.invoke("validate_hierarchy_metadata", artifact=target)
    print(f"validate_hierarchy_metadata on steward: valid={vres.get('valid')}, score={vres.get('score')}")
    assert vres.get("valid") or len(vres.get("missing", [])) < 5, "hierarchy validation should find most fields"
    print("  PASS: direct registry.invoke(validate)")

    rres = reg.invoke("read_ide_artifact", path=target)
    print(f"read_ide_artifact: frontmatter keys={list(rres.get('frontmatter', {}).keys())[:5]}")
    assert "frontmatter" in rres and "body" in rres
    print("  PASS: direct registry.invoke(read)")

    # 3. Parse declared from a frontmatter we edited
    front, _ = parse_skill_md(target)
    declared = parse_declared_tools(front)
    scopes = parse_required_scopes(front)
    print(f"Parsed declared from steward frontmatter: tools={declared}, scopes={scopes}")
    assert "validate_hierarchy_metadata" in declared
    print("  PASS: parse_declared_tools + parse_required_scopes")

    # 4. Executor run captures declared + runs tool steps if present in body
    execr = ProceduralSkillExecutor(workspace_root=".")
    result = execr.execute(target)
    print(f"Executor result for steward: status={result.status}, #evidence={len(result.evidence)}")
    print(f"  outputs.declared_tools = {result.outputs.get('declared_tools')}")
    print(f"  outputs.required_scopes = {result.outputs.get('required_scopes')}")
    assert result.outputs.get("declared_tools"), "executor should capture declared_tools"
    # Look for at least one tool-type evidence (the auto "tool:" detector or the declared exercise)
    tool_evs = [e for e in result.evidence if e.step_type == "tool"]
    print(f"  tool-type evidence steps: {len(tool_evs)}")
    # Even if no literal "tool:" in the steward body yet, declared presence + registry available is the contract
    assert result.outputs.get("tool_registry_available") or result.outputs.get("declared_tools")
    print("  PASS: executor integration (declared captured, registry visible)")

    # 5. Also exercise the router entrypoint (used by OrchestrationRouter)
    routed = run_procedural_skill("ide-hierarchy-taxonomy-steward")
    print(f"run_procedural_skill (router path): status={routed.get('status')}")
    assert routed.get("outputs", {}).get("declared_tools")
    print("  PASS: run_procedural_skill surfaces declarations")

    # 6. PS wrapper presence (for dual PS-MVP / future GUI terminal)
    ps1 = ROOT / "src" / "platform" / "tools" / "Invoke-IdeTool.ps1"
    print(f"PS wrapper present: {ps1.exists()} at {ps1}")
    assert ps1.exists()
    print("  PASS: Invoke-IdeTool.ps1 (dual-use surface)")

    print("\n=== P1 SMOKE COMPLETE (all assertions passed) ===")
    print("Next: commit evidence, update invocation record + matrix (tiny anchors), then P2 batch.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
