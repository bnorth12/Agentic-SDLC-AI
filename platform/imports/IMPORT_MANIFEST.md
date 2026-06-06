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