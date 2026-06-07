---
name: ide-artifact-lineage
description: >
  Generalized skill for auditing artifact provenance, lineage continuity, and retention hygiene across generated outputs for the agentic IDE platform.
  Primary for Artifact Lineage Auditor. Generalizes artifact-lineage-auditor (MATM) and related assets. Ensures lineage for generalized skills/agents, structure changes, and self-hosted evidence during the prioritized procedures and repo refactor.
metadata:
  short-description: "Artifact lineage audit for IDE generalized assets, structure changes, and evidence"
  agent: ide-artifact-lineage-auditor
  gates: [G1_traceability, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-artifact-lineage

**Agents:** Artifact Lineage Auditor (primary), Source-to-Evidence Traceability Auditor, Verification Coverage Planner, Governance Policy Compiler, Refactoring Agent  
**Parent:** [ide-artifact-lineage-auditor.agent.md](../../../agents/ide-platform/ide-artifact-lineage-auditor.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · Structural Refactor Execution Plan

## Purpose
Maintain trustworthy artifact lineage from source evidence to generated outputs for the IDE (generalized agents/skills in ide-platform, structure change records, evidence bundles, editor/viewer outputs, pack manifests). This supports compliance, the structure refactor, and self-hosting by ensuring no broken chains or orphaned artifacts.

## When to Invoke
- During or after XGEN batches and structure execution phases (e.g., content moves, legacy quarantine, doc archive).
- When auditing evidence from self-hosted procedures (baseline, disposition, execution plan, compliance audits).
- At G1, G4, G5 for lineage integrity.
- User: "audit lineage for the structure execution plan", "check generalized artifacts", "/ide-artifact-lineage".

## Inputs
- independent_reviews/, exports, release evidence, archive artifacts.
- Generalized artifacts in ide-platform (SKILL.md/.agent.md, manifests).
- Structure change records (from execution plan).
- Baseline, disposition, and previous audit outputs.

## Procedure

### 1. Verify Provenance and Lineage Chain Completeness
- For each generated artifact (e.g., generalized skills, structure moves, evidence), verify source provenance (e.g., from original imports or requirements) and full lineage chain to output.
- Check deterministic naming (e.g., ide- prefixed in ide-platform, dated evidence, archive in docs/archive/).

### 2. Check Naming, Versioning, and Retention Consistency
- Confirm artifact naming and versioning follow IDE conventions (e.g., ide- prefix for generalized, clear versioning in manifests).
- Validate retention policy compliance (e.g., active in ide-platform, archived in docs/archive/, legacy in legacy/).

### 3. Detect Orphaned, Duplicate, or Untraceable Artifacts
- Scan for orphaned (no source trace), duplicate, or broken chain artifacts (e.g., old farmrtk/matm files left after moves, unlinked evidence).
- Especially during structure changes: ensure no artifacts left in wrong places (e.g., scattered legacy).

### 4. Emit Cleanup and Remediation
- Produce lineage status summary, archive hygiene and retention corrections.
- Recommendations tied to the execution plan (e.g., "move orphaned generalized docs to ide-platform or archive per Phase 3").
- Support self-hosting: ensure the platform's own artifacts (like this plan) have clean lineage.

### 5. PowerShell / GitHub Native Emphasis
```powershell
# Example (future runner or ACP)
pwsh -File tools/traceability/artifact-lineage.ps1 -Scope "Structure-Refactor XGEN-Batch" -Baseline docs/ide-structure-requirements-baseline.md -Output evidence/artifact-lineage-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Artifact lineage issues in IDE structure" --label traceability,compliance,ide-platform --body-file evidence/artifact-lineage-*.md
```

### 6. Support Iteration and Self-Hosting
- Re-audit after changes (e.g., post-Phase moves).
- The skill is self-referential: audit lineage of the generalized skills and the structure work itself.
- Feed into other skills for updates (e.g., update verification coverage if lineage gaps found).

## Outputs
- Artifact lineage status summary.
- Archive hygiene and retention corrections.
- Gap list for orphaned/broken chains.
- Evidence for G1, G4, G5.

## Guardrails
- Preserve traceability from source to generated output.
- Prefer deterministic naming and inventory.
- Local-first.

## Generalization & IDE-Specific Notes
- Removed product-specific (e.g., FarmRTK exports, MATM independent_reviews paths).
- Added focus on IDE: lineage for generalized agents/skills in ide-platform, structure changes (moves, quarantine, archive), generated evidence from procedures, self-hosting (lineage of the platform's own development artifacts).
- Strong support for the structure refactor (ensuring clean lineage post-moves) and functional decomp.

## Related Platform Artifacts
- Gates: G1, G4, G5.
- Agents: Artifact Lineage Auditor (primary) + Traceability, Verification, Compliance agents, Refactoring Agent.
- Used with the execution plan and other early skills. This skill is self-referential and will audit lineage for the changes that generalize the copied agents and make the repo IDE-native.