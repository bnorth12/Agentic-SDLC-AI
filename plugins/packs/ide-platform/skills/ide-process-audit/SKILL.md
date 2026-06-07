---
name: ide-process-audit
description: >
  Audit IDE platform agent/skill registry coherence, pack manifests, delegation,
  and readiness. Quality Assurance for the generalized platform process capabilities.
  Generalizes process-audit-farmrtk. Use for process audit, registry check, or
  before G5 baseline after XGEN waves.
metadata:
  short-description: "Agent/skill/pack registry and process audit for IDE platform"
  agent: quality-assurance-engineer
  gates: [G1_traceability, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-process-audit

**Agent:** Quality Assurance Engineer (generalized)  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) (L4 + Cross XGEN) · [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](../../../docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md)

## Purpose
Audit coherence of the IDE platform's generalized agents, skills, and packs (ide-platform content vs manifests vs layer work package index). Checks registry currency, skill/pack pairing, orchestration artifacts, and process compliance for self-hosting and generalization waves. Distinct from EIRC design review — focuses on executable process hygiene.

## When to Invoke
- End of XGEN tranche or after adding generalized content (FarmRTK/MATM batches).
- Before promoting pack readiness or closing G5.
- Quarterly QA with Repo Organization Manager.
- User: "audit ide-platform registry", "check generalized skill burn-down".
- As supporting step in ide-structural-refactoring Phase 0/5 and Planning Agent closeout.

## Inputs
- `plugins/packs/ide-platform/plugin.manifest.yaml` and skills/agents/ directories.
- `platform/gates/registry.yaml`, LAYER_WORK_PACKAGE_INDEX.md, and recent invocation records.
- Current generalized SKILL.md / .agent.md files.

## Procedure

### 1. Run Core Registry Audit (generalized)
```powershell
# Generalized from original process_audit.ps1
pwsh -File tools/ci/ide_process_audit.ps1 -Scope "ide-platform + Tranche-2 + FarmRTK-batch"
```

### 2. Cross-Check Manifest vs On-Disk
- Compare ide-platform manifest entries against actual SKILL.md and .agent.md in the pack.
- Verify that new generalized items (e.g., ide-repo-audit, ide-process-audit) appear in the traceability matrix and have correct Parent links to IDE_REFACTOR_PLAN §5.

### 3. Delegation & Orchestration Verification
- Check that routing for new skills (via L2 executor) matches layer assignments in the matrix.
- Confirm each new ide-* has documented execution path (procedural via executor or ACP).

### 4. Log & Remediate
- Open items in the layer index or BACKLOG for gaps.
- Pair with `ide-repo-audit` and `ide-traceability-audit` for full sweep.
- Re-run `ide-kpi-drift-analyst` after fixes.

## Outputs
- Process audit report with findings on registry drift or missing pairings.
- Updated manifests or matrix rows if needed.
- Evidence for G1/G4/G5.

## Escalation
- Generalized skill without executable support (executor/tool) → Refactoring Agent + L2 tooling work.
- Registry gaps in ide-platform → update plugin.manifest.yaml and re-audit.

## Generalization & IDE-Specific Notes
- Removed FarmRTK-specific paths (Tools/, SYS-DOC-*, delegation_map.json assumptions).
- Made fully manifest/pack/gate-driven.
- Added explicit checks for IDE model: agents/skills as first-class editable pack content, L0-L8 decomposition in the matrix, self-hosting cleanliness.
- PowerShell + gh examples for evidence on generalization PRs.
- Now core to the platform's own QA during WAVE-02 and future XGEN.

## Related Platform Artifacts
- Gates: G1, G4, G5.
- Tools: ide_core (validate_hierarchy_metadata, read_ide_artifact).
- Complements: ide-repo-audit, ide-kpi-drift-analyst, ide-structural-refactoring.
- Updates IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md Cross rows.
