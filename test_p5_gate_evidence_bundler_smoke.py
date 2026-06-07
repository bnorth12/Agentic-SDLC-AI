"""P5 Slice 1 smoke: Gate Evidence Bundler + Viewer Integration (core + registry).

Run:
  .\.venv\Scripts\python.exe test_p5_gate_evidence_bundler_smoke.py

Focus (tiny slice):
- gate_evidence_bundler.py: create_gate_evidence_bundle (collect from exec/gh sources), bundle_to_markdown, bundle_to_json.
- Schema for G1/G3/G4 bundles.
- Registered as 'bundle_gate_evidence' in ToolRegistry.
- Live smoke: mock SkillExecutionResult + gh result -> bundle -> md/json outputs. Registry invoke.
- Tiny changes. Live validation. Dual (Python; PS next). Trace to L3-001 / §5 / matrix.

This is the first small testable batch for P5.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.platform.tools.gate_evidence_bundler import (
    create_gate_evidence_bundle,
    bundle_to_markdown,
    bundle_to_json,
)
from src.platform.tools.registry import get_registry, reset_registry_for_tests


def main() -> int:
    print("=== P5 Gate Evidence Bundler Smoke (slice 1) ===")

    # 1. Mock sources: SkillExecutionResult-like + gh_evidence result (as in P2/P4)
    exec_source = {
        "type": "skill_execution",
        "id": "ide-hierarchy-taxonomy-steward",
        "result": {
            "status": "success",
            "evidence": [
                {"step_type": "pwsh", "status": "success", "stdout": "Hierarchy check passed"},
                {"step_type": "tool", "status": "success", "stdout": "validate_hierarchy_metadata: valid=True"},
            ],
            "outputs": {"declared_tools": ["validate_hierarchy_metadata"]},
        },
    }
    gh_source = {
        "type": "gh_evidence",
        "id": "issue#123",
        "result": {
            "status": "success",
            "stdout": "https://github.com/.../issues/123",
            "command": "gh issue create ...",
        },
    }

    # 2. Bundle for G4 (example)
    bundle = create_gate_evidence_bundle(
        gate_id="G4_independent_review",
        sources=[exec_source, gh_source],
        metadata={"maturity": "M2", "pack": "ide-platform"},
    )
    print(f"bundle: gate={bundle.gate_id}, sources={len(bundle.sources)}, evidence_items={len(bundle.evidence)}")
    assert bundle.gate_id == "G4_independent_review"
    assert len(bundle.evidence) >= 2
    print("  PASS: create_gate_evidence_bundle (G4)")

    # 3. Viewer-friendly outputs
    md = bundle_to_markdown(bundle)
    js = bundle_to_json(bundle)
    assert "# Gate Evidence Bundle: G4_independent_review" in md
    assert '"gate_id": "G4_independent_review"' in js
    print("  PASS: bundle_to_markdown + bundle_to_json (viewer-friendly)")

    # 4. Registry
    reset_registry_for_tests()
    reg = get_registry()
    tools = reg.list_tools()
    print(f"registry has bundle_gate_evidence: {'bundle_gate_evidence' in tools}")
    assert "bundle_gate_evidence" in tools
    inv = reg.invoke(
        "bundle_gate_evidence",
        gate_id="G1_traceability",
        sources=[{"type": "test", "id": "smoke", "result": {"status": "success", "evidence": [{"step_type": "test", "status": "success"}]}}],
    )
    print(f"registry invoke: gate={getattr(inv, 'gate_id', None)}")
    # Note: pydantic model returned; check gate_id
    assert getattr(inv, "gate_id", None) == "G1_traceability"
    print("  PASS: registered and invocable (P5)")

    print("\n=== P5 SLICE 1 SMOKE COMPLETE ===")
    print("Next slice: PS wrapper + integrate with executor/gates.")

    # Slice 2: PS wrapper sim (via python call to bundler, as PS wrapper does) + bundle from prior P2/P4 tools
    # Simulate sources from robust pwsh exec + gh_evidence (as produced in real runs)
    ps_sources = [
        {"type": "skill_execution", "id": "ide-decision-record", "result": {"status": "success", "evidence": [{"step_type": "pwsh", "status": "success", "stdout": "ADR scaffolded"}]}},
        {"type": "gh_evidence", "id": "pr#99", "result": {"status": "success", "stdout": "Evidence attached to PR", "command": "gh pr comment ..."}},
    ]
    ps_bundle = create_gate_evidence_bundle(gate_id="G3_hitl", sources=ps_sources)
    ps_md = bundle_to_markdown(ps_bundle)
    print(f"PS-sim bundle (from P2/P4 tools): gate={ps_bundle.gate_id}, items={len(ps_bundle.evidence)}, md_len={len(ps_md)}")
    assert ps_bundle.gate_id == "G3_hitl"
    assert "G3_hitl" in ps_md
    print("  PASS: bundle from prior tools (exec+gh) + viewer md (PS wrapper sim)")

    # Note: real PS call would be pwsh -File New-GateEvidenceBundle.ps1 -GateId G3_hitl -SourcesJson '...'
    print("  (PS wrapper New-GateEvidenceBundle.ps1 ready for dual use)")

    # Slice 3: full integration test (real executor on skill with gates in frontmatter + gh sim + GateEngine bundle + registry)
    from src.platform.orchestration.executor import ProceduralSkillExecutor
    from src.platform.gates.engine import GateEngine
    execr = ProceduralSkillExecutor(workspace_root=".")
    # Use a real skill that declares gates (e.g. G1/G4 from P1-era frontmatter)
    skill_res = execr.execute("plugins/packs/ide-platform/skills/ide-hierarchy-taxonomy-steward/SKILL.md")
    exec_source = {"type": "skill_execution", "id": "ide-hierarchy-taxonomy-steward", "result": skill_res.model_dump()}
    gh_sim = {"type": "gh_evidence", "id": "pr#evidence-42", "result": {"status": "success", "stdout": "Evidence attached", "command": "gh pr comment"}}
    sources = [exec_source, gh_sim]

    # Direct bundler + GateEngine
    engine = GateEngine()
    bundled = engine.bundle_evidence_for_gate("G4_independent_review", sources, metadata={"test": "slice3"})
    print(f"GateEngine bundle for G4: items={len(bundled['bundle']['evidence'])}, has_md={len(bundled['markdown'])>100}")
    assert "G4_independent_review" in bundled["markdown"]
    assert bundled["gate"] is not None

    # Via registry too
    reg_bundle = reg.invoke("bundle_gate_evidence", gate_id="G1_traceability", sources=sources)
    print(f"registry bundle G1: items={len(reg_bundle.evidence) if hasattr(reg_bundle, 'evidence') else 'n/a'}")
    print("  PASS: real executor result + GateEngine + registry bundle (P5 integrate)")

    # Viewer note: md/json ready for L0 viewers / GUI evidence panels (see GUI_DESIGN)
    print("  (viewer-friendly outputs for GUI + PRs/docs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
