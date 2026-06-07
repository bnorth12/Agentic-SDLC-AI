---
name: ide-bom-procurement
description: >
  Audit and maintain "procurement" backlog vs "inventory" of generalized content
  for the IDE platform. Track pending generalization items (like BOM lines) vs
  open XGEN/PROC items in the matrix or layer index. Use for procurement-style
  audit of remaining FarmRTK/MATM, alternates review, or wave planning.
  Generalizes bom-procurement-farmrtk.
metadata:
  short-description: "Generalized content inventory vs XGEN backlog audit"
  agent: procurement-coordinator
  gates: [G1_traceability, G4_independent_review]
  maturity: M0+
---

# ide-bom-procurement

**Agent:** Procurement Coordinator (generalized)  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) (Cross XGEN) · [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](../../../docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md)

## Purpose
Reconcile the "inventory" of already-generalized IDE platform content (Tranche 1/2/3 agents/skills, tools, executor) against open "procurement" items in the XGEN backlog (matrix rows, layer index, WAVE charter). Track pending items (like connectors/CYD variants) and escalate alternates or blocks. Ensures complete coverage for self-hosting and G5.

## When to Invoke
- Before or after a FarmRTK/MATM batch (e.g., after batch 3).
- Monthly "procurement review" with Planning Agent.
- After matrix or layer index updates (new pending rows).
- User: "audit generalized inventory vs XGEN backlog", "sync matrix with remaining FarmRTK".
- As part of ide-portfolio-planning or before G0 wave.

## Inputs
- The traceability matrix (as the "BOM"), layer work package index (backlog), recent generalized content in ide-platform.
- WAVE_02 or current charter for pending scope.
- Status of tools/executor adoption.

## Procedure

### 1. Run Audit (generalized)
```powershell
pwsh -File tools/ci/ide_bom_procurement_audit.ps1 -Scope "ide-platform + matrix + batch-3"
```

### 2. Reconcile Pending Items
- For each "pending" row in the matrix (un-generalized FarmRTK or tooling), ensure a matching open XGEN item in the layer index or charter.
- When "ordered" (i.e., generalized and added to matrix), close the backlog item and update inventory (matrix).

### 3. Document Variants and Escalate
- Document "CYD vs Hosyond" style choices (e.g., different approaches to generalizing a skill, or tool vs direct code) in notes.
- Escalate lead-time blocks (e.g., complex remaining items) or conflicts to Planning Agent / Chief Engineer.
- When "shipped" (validated via audit), update matrix status and notify for baseline.

### 4. Close with Traceability
- Link to ide-decision-record for variant choices.
- Feed into program metrics.

## Outputs
- Updated matrix and layer index with reconciled inventory/backlog.
- Evidence for G1/G4 (coverage report).

## Escalation
- Persistent pending items blocking wave scope → Planning Agent + G0 update.
- Inventory ↔ matrix conflict (e.g., generalized item not in matrix) → Refactoring Agent + update.

## Generalization & IDE-Specific Notes
- Stripped FarmRTK-specific (hardware BOM, connectors, CYD variants, mechanical orders).
- Reframed as generalized content "inventory" vs XGEN "procurement" backlog (matrix rows as BOM lines, layer index as backlog).
- Explicit support for tracking the new tools, executor, and batch 3 items.
- PowerShell + gh for backlog sync PRs during generalization.
- Directly maintains the IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md as the central "BOM".

## Related Platform Artifacts
- Gates: G1, G4.
- Tools: ide_core, the matrix (as BOM).
- Used by: ide-program-metrics, ide-portfolio-planning (WAVE_02 charter), ide-structural-refactoring closeout.
- Updates IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md (Cross XGEN rows for remaining items).
