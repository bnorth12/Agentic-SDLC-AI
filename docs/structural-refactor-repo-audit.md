# Repo Audit of the Structural Refactor Execution Plan

**Produced by:** Repo Audit (using `ide-repo-audit` skill)  
**Date:** 2026-06  
**Parent:** [structural-refactor-execution-plan.md](./structural-refactor-execution-plan.md)  
**Gates:** G1, G4, G5.

**Hierarchy:** Parent = Cross-layer Repo Structure; Child = Repo organization and hygiene for the refactored IDE layout; Decomposition level = 2; Allocated = ide-platform (content), legacy (quarantine), docs/archive (historical), platform (config only); Verification = this audit + re-audit post-execution.

## Scope
Audit repo organization for the IDE platform during the structure refactor: README coverage, BACKLOG/index (adapt to plans and structure), traceability scan, folder hygiene in the new layout (ide-platform, legacy, archive, living docs).

## Audit Steps (adapted for IDE)
1. Run audit — checked for missing top-level READMEs or indexes in the new structure (e.g., ide-platform has good coverage for generalized, docs living has the plans and artifacts, legacy and archive will need indexes).
2. Update root index or BACKLOG segment if needed (the structural-refactor-execution-plan.md and WAVE_01 serve as the "BACKLOG" for the structure work; update to include the new generalized audits).
3. Run metrics or coverage after remediation (the execution plan has high "coverage" for the prioritized generalized; add the new audits to the plan).
4. Pair with process-audit for full sweep (done in parallel, the process audit confirmed coherence).

## Findings
- **Coverage:** Good for active areas (ide-platform has the generalized agents/skills with docs, the execution plan and WAVE cover the work). Living docs (charter, project-plan) have the self-hosted artifacts.
- **Hygiene:** The plan proposes fixes for missing in the new layout (e.g., add README to ide-platform if needed, index in archive and legacy).
- **Traceability Scan:** The generalized have good trace from imports to ide-platform (via the audits); the structure plan has links to baselines and dispositions.
- **Remediation:** 
  - Add top-level README or index in ide-platform for the generalized content.
  - Update the execution plan and WAVE_01 to reference the new audits (process, repo, traceability).
  - For legacy and archive: ensure they have hygiene (e.g., README explaining the quarantine and archive).
  - Run the audit again after Phase 1-3 to confirm the new layout has full coverage and no orphans.

## Outputs
- This audit report.
- Recommendations: Update the execution plan to include the new audits in Phase 5; add hygiene fixes to the plan.
- Evidence for G1, G4, G5.

## PowerShell Example (adapted)
```powershell
# Adapted for IDE
pwsh -File tools/ci/ide-repo-audit.ps1 -Scope "Structure-Refactor"

# To enforce
$env:IDE_ENFORCE_CHECKS = "1"
pwsh -File tools/ci/ide-repo-audit.ps1
```

## Generalization Note
This audit uses the generalized ide-repo-audit, demonstrating self-hosting. The copied repo-audit-farmrtk is now IDE-native and used to audit the refactor using the generalized agents.

**Status:** Audit complete. The execution plan's proposed layout has good coverage potential; add the recommended updates to the plan for full hygiene in the new structure.

This is part of burning through the procedures using the prioritized generalized agents. The structural refactor execution plan is now audited with process and repo audits. Ready for Phase 1, with updates to the plan.