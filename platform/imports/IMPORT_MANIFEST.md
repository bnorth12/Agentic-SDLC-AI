# Import Manifest — FarmRTK + MATM scaffold copy

**Date:** 2026-06-06  
**Purpose:** Staged imports for generalization per [REFACTOR_TODO.md](../../docs/charter/REFACTOR_TODO.md)

Do not edit imports in place for product work — copy → generalize → move to `plugins/packs/` or `platform/skills/`.

---

## FarmRTK platform skills (17)

Copied to `platform/imports/farmrtk/skills/`:

- orchestrate-farmrtk
- independent-review-farmrtk
- check-work-commit-farmrtk
- traceability-audit-farmrtk
- program-metrics-farmrtk
- requirements-management-farmrtk
- test-authoring-farmrtk
- configuration-baseline-farmrtk
- icd-maintenance-farmrtk
- decision-record-farmrtk
- repo-audit-farmrtk
- validation-plan-farmrtk
- risk-register-farmrtk
- process-audit-farmrtk
- technical-writer-farmrtk
- data-storage-farmrtk
- bom-procurement-farmrtk

**Source:** `FarmRTK/.grok/skills/` @ FarmRTK main (2026-06-06)

## FarmRTK domain skills (5)

Copied to `plugins/packs/engineering-sdlc/imports/`:

- OpenSCAD-Parametric-FarmRTK
- firmware-build-farmrtk
- integration-bench-farmrtk
- electronics-wiring-farmrtk
- rf-antenna-farmrtk

## MATM governance

Copied to `platform/imports/matm/skills/` (26 skills) and `platform/imports/matm/agents/` (24 agents).

**Source:** `Multi Agent Threat Modeler/.github/skills|agents/` @ MATM main (2026-06-06)

---

## Re-copy command

```powershell
powershell -File tools/install/copy-imports.ps1
```

## Post-import generalization (R1+; complete for platform skills)

New generalized platform skills/agents created under `plugins/packs/ide-platform/` (following "move to `plugins/packs/` or `platform/skills/`"; coordinated via ide_core tools + Refactoring Agent):

- Meta: `ide-portfolio-planning` (Planning Agent; from orchestrate-farmrtk + multi-sprint-portfolio-planner + ...), `ide-structural-refactoring` (Refactoring Agent; from repo-governance-autoflow-orchestrator + architecture-design-* + ...).
- FarmRTK platform (all 17 generalized in batches; now in ide-platform/skills/ as ide-*; see matrix for full traceability/hierarchy):
  - Batch 1: ide-repo-audit, ide-process-audit, ide-program-metrics, ide-check-work-commit.
  - Batch 2 (in order): ide-decision-record, ide-icd-maintenance, ide-risk-register, ide-configuration-baseline, ide-data-storage.
  - Batch 3: ide-test-authoring, ide-independent-review, ide-bom-procurement.
  - Priority/earlier: ide-technical-writer, ide-validation-plan, ide-kpi-drift-analyst, ide-requirements-baseline, ide-traceability-audit, ide-source-to-evidence-traceability, ide-hierarchy-taxonomy-steward, ide-hierarchy-conformance, ide-requirements-implementation-auditor, ide-governance-policy-compiler, ide-process-audit, ide-repo-audit, ide-independent-review-orchestrator, ide-multi-sprint-portfolio-planner, ide-sprint-*, ide-traceability-*, ide-verification-*, ide-remediation-*, ide-artifact-lineage, ide-architecture-*, etc.
- MATM: 24 agents + 26 skills generalized/synthesized into ide-platform (Tranche 1/2; e.g., ide-hierarchy-*, ide-requirements-*, ide-governance-*, ide-independent-review-*, ide-kpi-*, etc.; see PLATFORM_AGENTS.md and matrix).
- Supporting: Full coordination in ide-platform/agents/ (e.g., ide-*.agent.md for key ones like ide-kpi-drift-analyst, ide-repo-governance-autoflow-orchestrator) and skills/.

A starter pack manifest was added at `plugins/packs/ide-platform/plugin.manifest.yaml` (now fully lists all; references platform/skills during transition but content moved to pack for L4/L7).

All original imported `*-farmrtk` and MATM-specific names, paths, and assumptions generalized per IDE_REFACTOR_PLAN.md (L0-L8 + Cross), matrix, and invocation record. ide-portfolio-planning + ide-structural-refactoring + ide_core tools (L2/L4) are primary vehicles for ongoing generalization, self-hosting, and coordination (e.g., with L2 executor, L3 gates, PowerShell-MVP, custom GUI). Domain FarmRTK stay in engineering-sdlc/imports/. See REFACTOR_TODO.md, LAYER_WORK_PACKAGE_INDEX.md for status.