---
name: ide-configuration-baseline
description: >
  Generate and maintain configuration baselines for the IDE platform (git SHA,
  generalized content inventory from batches, tool/executor versions, matrix revision,
  pack manifests). Generalizes configuration-baseline-farmrtk. Use for baseline
  manifest at wave closeout (e.g., after this FarmRTK batch), release tag, or
  self-hosting snapshot.
metadata:
  short-description: "CM baseline manifest for IDE platform state after XGEN batches"
  agent: configuration-manager
  gates: [G1_traceability, G5_baseline]
  maturity: M0+
---

# ide-configuration-baseline

**Agent:** Configuration Manager (generalized)  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) (Cross XGEN / XSELF / G5) · [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](../../../docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md)

## Purpose
Capture a point-in-time baseline of the IDE platform state after generalization work: inventory of generalized agents/skills (including this FarmRTK batch 2), tool/executor versions (ide_core, L2 executor), matrix and plan revisions, pack manifests. Enables reproducible self-hosting, traceability for G5 baselines, and tracking progress across batches.

## When to Invoke
- End of XGEN tranche or WAVE (e.g., after completing this FarmRTK batch 2 or full FarmRTK).
- Before G5 baseline or major release of the platform.
- After significant changes to generalized content, tools, or the matrix.
- User: "generate IDE platform baseline after batch 2", "snapshot for WAVE-02".
- As part of ide-structural-refactoring Phase 4/5 or Planning Agent closeout.

## Inputs
- Current git SHA, list of generalized items in ide-platform (from matrix or manifest, including batch 2).
- Tool versions (ide_core.py, executor.py), matrix revision, plan references (§5).
- Gate registry state.

## Procedure

### 1. Generate Baseline Manifest (generalized)
```powershell
pwsh -File tools/ci/ide_baseline_manifest.ps1 -Tag v0.2-ide-farmrtk-batch2 -Scope "XGEN + matrix + tools + batch-2"
```

### 2. Review and Record
- Review the generated manifest (e.g., docs/baselines/ide-platform-<tag>.md).
- Record versions of generalized SKILL.md/.agent.md from this batch and new tools (executor, ide_core).
- Git tag the state.
- Link to EIRC / independent review if at milestone.

### 3. Update Traceability
- Add baseline reference to the matrix (Cross XGEN / G5 rows).
- Ensure all new generalized items from batch 2 are captured with their matrix rows.

### 4. Closeout
- Pair with `ide-independent-review-orchestrator` or EIRC for milestone if applicable.

## Outputs
- Baseline manifest with full inventory (including this batch) and versions.
- Updated matrix and plans with baseline links.
- Evidence for G1/G5.

## Escalation
- Missing generalized content from batch 2 in baseline → Refactoring Agent + matrix update.
- Version drift in tools/executor → L2 tooling work.

## Generalization & IDE-Specific Notes
- Stripped FarmRTK-specific (BOM, mechanical FILE_REV, firmware tags, .grok/skills paths).
- Focused on IDE platform: generalized content count (MATM + this FarmRTK batch), L2/L4 components (executor + ide_core tools), matrix/plan revisions, self-hosting state after batch execution.
- Explicit support for baselining after using the new tools for this batch.
- PowerShell + gh for baseline PRs and tags.
- Directly supports G5 and the traceability matrix as the inventory source.

## Related Platform Artifacts
- Gates: G1, G5.
- Tools: ide_core (for inventory), the matrix (as living inventory).
- Used by: ide-structural-refactoring Phase 4, Planning Agent (WAVE closeout), independent review.
- Updates IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md (G5 / Cross rows).
