---
name: ide-data-storage
description: >
  Audit and maintain data storage schemas, paths, and verification artifacts for
  the IDE platform (evidence bundles, matrix data, generalized skill outputs from
  batches, invocation records, baselines). Generalizes data-storage-farmrtk.
  Use for storage audit, schema change during self-hosting (after batch 2), or
  "field verification" equivalent for the platform's own data.
metadata:
  short-description: "Data storage / evidence schema audit for IDE platform"
  agent: data-manager
  gates: [G1_traceability, G4_independent_review]
  maturity: M0+
---

# ide-data-storage

**Agent:** Data Manager (generalized)  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) (Cross XGEN / XSELF) · [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](../../../docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md)

## Purpose
Audit storage layout and schemas for IDE platform data: evidence bundles from generalized skills (including this FarmRTK batch), traceability matrix content, invocation records, baselines, tool outputs (ide_core). Ensures consistency when new tools or the executor produce data, and supports self-hosting by keeping the platform's "data" clean and verifiable.

## When to Invoke
- Before or after changes that affect data output (e.g., new evidence from executor runs on batch skills, matrix extensions after batch 2, new generalized outputs).
- During WAVE-02 or after using new tools to generate artifacts for this batch.
- For schema changes in evidence formats or matrix structure.
- User: "audit IDE evidence storage after batch 2", "verify matrix data paths after tools addition".
- As part of self-hosted audits or G1 closure for the batch.

## Inputs
- Current evidence/ directory structure, matrix file, recent audit reports and invocation records (including batch 2).
- Generalized skill outputs (e.g., from ide-program-metrics, ide-decision-record for this batch).
- Tool implementations that write data (executor, ide_core write functions).

## Procedure

### 1. Run Storage Audit (generalized)
```powershell
pwsh -File tools/ci/ide_data_storage_audit.ps1 -Scope "evidence + matrix + generalized-outputs + batch-2"
```

### 2. Align Schemas and Paths
- Ensure evidence bundles, matrix data, and reports follow consistent layout (e.g., date-stamped, linked to matrix rows for batch items).
- On schema change (e.g., new tool output fields from ide_core): update relevant docs (matrix, §5), tool code if needed, and run verification.
- Coordinate with generalized skills that produce data (e.g., update their "Outputs" sections to reference storage conventions for batch 2).

### 3. Verify and Trace
- Run validate_hierarchy_metadata or traceability checks on affected data artifacts.
- Update the matrix if storage changes impact Cross rows for this batch.
- Notify relevant agents (e.g., via ide-kpi-drift-analyst if quality affected).

### 4. Enforce (optional)
- Use enforcement flag for critical self-hosting data integrity after batch.

## Outputs
- Audit report with schema/path findings and fixes for batch 2 data.
- Updated storage conventions in matrix or plans.
- Evidence for G1/G4.

## Escalation
- Schema conflicts affecting traceability (e.g., new tool outputs from batch not linked in matrix) → Refactoring Agent + matrix update.
- Data integrity issues in self-hosted evidence from batch → update audit process or tools.

## Generalization & IDE-Specific Notes
- Stripped FarmRTK-specific (SD card, rover logging, CSV headers for positions/points, firmware sd_paths.h).
- Focused on IDE platform data: evidence bundles from generalized skills/executor (batch 2 outputs), matrix as central data structure, invocation records, baselines, tool outputs from ide_core.
- Explicit support for data produced by the new L2 executor and ide_core tools during this batch execution.
- PowerShell + gh for data schema PRs during generalization.
- Maintains the traceability matrix as the authoritative "schema" for architecture data.

## Related Platform Artifacts
- Gates: G1, G4.
- Tools: ide_core (read/write_ide_artifact for data artifacts), the matrix itself.
- Used by: ide-structural-refactoring, self-hosted audit reports, WAVE-02 charter.
- Updates IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md (Cross XGEN / data-related rows).
