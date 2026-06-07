---
name: ide-repo-audit
description: >
  IDE platform repo organization audit — README coverage, BACKLOG index, folder
  hygiene, and traceability scan for generalized agents/skills and packs.
  Use for repo audit, structure hygiene check, or before major XGEN tranche closeout.
  Generalizes repo-audit-farmrtk.
metadata:
  short-description: "Repo README, backlog, and IDE structure audit"
  agent: repo-organization-manager
  gates: [G1_traceability, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-repo-audit

**Agent:** Repo Organization Manager (generalized)  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) (L4/L7 + Cross XGEN/XDOC) · [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](../../../docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md)

## Purpose
Audit the IDE platform repo for organization hygiene, README coverage, BACKLOG index presence, and traceability of generalized content (agents/skills in packs, structure changes). Ensures the filesystem demonstrates L0-L8 decomposition and supports self-hosting as a clean workspace example. Pairs with ide-process-audit and ide-traceability-audit for full governance sweep.

## When to Invoke
- End of XGEN tranche or structural wave (e.g., after FarmRTK or MATM generalization batch).
- Before promoting pack content or closing G5 baseline.
- Quarterly QA or before major doc archive / legacy quarantine.
- User: "run repo audit", "check IDE structure hygiene", "/ide-repo-audit".
- As part of ide-structural-refactoring Phase 0/5 or Planning Agent wave closeout.

## Inputs
- Active workspace manifest (repos, packs, maturity).
- `platform/gates/registry.yaml` and current generalized content in `plugins/packs/ide-platform/`.
- Root README, BACKLOG.md (or equivalent in docs/project-plan/), and layer work package index.
- Recent invocation records and traceability matrix.

## Procedure

### 1. Run Core Audit (generalized)
```powershell
# Example (replace with generalized script or executor call once L2 tools mature)
pwsh -File tools/ci/ide_repo_audit.ps1 -Scope "ide-platform + generalized-agents-skills"
```

### 2. Fix Missing Top-Level Documentation
- Ensure README.md, CONTRIBUTING.md, and key charter docs (FRAMEWORK_DECOMPOSITION, IDE_REFACTOR_PLAN §5, the traceability matrix) are present and current at root or docs/charter/.
- Update BACKLOG index or layer work package index if new generalized items (e.g., new ide-* from FarmRTK) are added.

### 3. Traceability & Hierarchy Scan (using new tools)
- Invoke `validate_hierarchy_metadata` (from ide_core tools) on recent generalized SKILL.md and .agent.md in ide-platform.
- Cross-check that new content references the traceability matrix and IDE_REFACTOR_PLAN §5.
- Pair with `ide-source-to-evidence-traceability` for full chain audit on structure changes.

### 4. Post-Remediation Metrics
- Run `ide-kpi-drift-analyst` or program-metrics equivalent after fixes.
- Log findings to evidence/ or update the matrix with new XGEN rows.

## Outputs
- Audit report with severity-ranked findings (RH-01 style for IDE structure).
- Updated BACKLOG / layer index segments.
- Evidence bundle suitable for G1/G4/G5 (links to matrix rows).

## Escalation
- Persistent hygiene debt in generalized content → Refactoring Agent + update to matrix.
- Missing hierarchy on new ide-* artifacts → ide-hierarchy-taxonomy-steward.

## Generalization & IDE-Specific Notes
- Stripped all -farmrtk product assumptions (Tools/, SYS-DOC-*, CAD/firmware paths).
- Replaced with manifest-driven equivalents (workspace manifests, ide-platform pack, gate registry, L0-L8 references).
- Added explicit support for IDE surfaces: auditing generalized .agent.md/SKILL.md as first-class pack content, self-hosting workspace cleanliness, and traceability matrix maintenance.
- PowerShell + GitHub native by default (gh for evidence attachment on XGEN PRs).
- Now participates in the platform's own governance (used during Tranche 2 and WAVE-02).

## Related Platform Artifacts
- Gates: G1, G4, G5.
- Tools: ide_core (validate_hierarchy_metadata, read/write_ide_artifact).
- Used by: ide-structural-refactoring (Phase 0/5), ide-process-audit, Planning Agent wave closeout.
- Updates the IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md (Cross XGEN / XDOC rows).
