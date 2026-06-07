---
name: ide-source-to-evidence-traceability
description: >
  Generalized skill for auditing full source-to-evidence traceability chains for IDE platform requirements and work items.
  Primary for Source-to-Evidence Traceability Auditor. Generalizes source-to-evidence-traceability-auditor (MATM),
  traceability-audit-farmrtk, and related assets. Critical for ensuring Requirements, Arch/Design, and Verification
  chains are complete during generalization, structural refactors, and self-hosting.
metadata:
  short-description: "Full source-to-evidence traceability audit for IDE layers, surfaces, structure, and generalized assets"
  agent: source-to-evidence-traceability-auditor
  gates: [G1_traceability, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-source-to-evidence-traceability

**Agents:** Source-to-Evidence Traceability Auditor (primary), Requirements Baseline Steward, Architecture/Design Disposition Planner, Verification Coverage Planner, Refactoring Agent  
**Parent:** [source-to-evidence-traceability-auditor.agent.md](../../../agents/ide-platform/source-to-evidence-traceability-auditor.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md)

## Purpose
Validate that every requirement and governed work item for the agentic IDE has a complete, explicit, auditable source-to-evidence traceability chain (source → architecture/design → implementation → verification). This skill is essential early so that generalization of imported agents/skills, repo structure improvements, functional decomposition, and new IDE surfaces (editors for agents/skills, viewers, etc.) are traceable from the start.

## When to Invoke
- After requirements baselining and architecture/design disposition.
- Before/after generalization batches (XGEN) to confirm the new IDE-native versions have full chains.
- When planning or auditing structural/repo changes or layer functional decomp.
- At G1 traceability checkpoints, G4 reviews, and before G5 baselines.
- User: "audit traceability for the IDE structure changes", "check chains for generalized skills", "/ide-traceability-audit".

## Inputs
- Requirements baselines with hierarchy metadata.
- Architecture/design workpacks and dispositions.
- Implementation artifacts (generalized SKILL.md/.agent.md files, pack manifests, code changes, docs).
- Verification plans, artifacts, and coverage reports.
- Current traceability matrix and root hierarchy artifacts.

## Procedure

### 1. Build Inventory and Chains
- Inventory the scope (e.g., all requirements for IDE structure, a batch of generalized agents/skills, or specific work packages).
- For each item, capture explicit references for all four legs:
  - Source (e.g., this baseline or original imported SKILL.md/.agent.md).
  - Architecture/Design (e.g., disposition records, layered architecture docs, hierarchy metadata).
  - Implementation (e.g., files in ide-platform pack, manifests, code, structure changes).
  - Verification (e.g., tests, evidence bundles, coverage reports, compliance audits).

### 2. Validate Hierarchy at Each Leg
- Confirm parent capability, child function, decomposition level, allocated component/module, and verification method are present and consistent.
- Do not infer — require explicit fields or references.

### 3. Classify and Report
- Classify each chain: complete (all legs + hierarchy), partial, or missing-link (critical gap).
- Group findings by severity, layer (L0-L8 or Cross), and type (e.g., generalized skill, structural move).
- Produce readable summaries with requirement/work item text and evidence snippets.

### 4. Identify Systemic Issues and Remediation
- Highlight patterns (e.g., many generalized items missing verification legs, or structure changes breaking source provenance).
- Produce prioritized remediation backlog (e.g., "add verification evidence for ide-requirements-baseline in the structure execution plan").
- Recommend updates to traceability matrix, gate entries (G1/G3/G4/G5), or architecture artifacts.

### 5. PowerShell / GitHub Native Emphasis
```powershell
# Example (future runner or ACP)
pwsh -File tools/traceability/audit.ps1 -Scope "IDE-Structure XGEN-Batch-1" -Baseline docs/ide-structure-requirements-baseline.md -Disposition docs/ide-structure-architecture-disposition.md -Output evidence/traceability-audit-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Traceability gaps in IDE structure refactor" --label traceability,compliance,ide-platform --body-file evidence/traceability-audit-*.md
```

### 6. Support Iteration and Self-Hosting
- Re-run as new architecture/designs or requirements emerge.
- Use on the platform's own artifacts (e.g., this skill itself must have traceable chains from its generalized source).

## Outputs
- Chain completeness summary and ratios.
- Missing-link breakdown with clear evidence context.
- Hierarchy field coverage report.
- Prioritized remediation backlog.
- Evidence suitable for gates and independent review.

## Guardrails
- Explicit references only — no inference.
- Local-first and file-referenced.
- Compatible with independent review reporting.

## Generalization & IDE-Specific Notes
- Removed product-specific elements (e.g., FarmRTK/MATM-specific docs paths).
- Added coverage for IDE model: traceability of agent/skill editors and viewers, pack content, layer decomposition, self-hosting (the platform traces its own development), and structural changes.
- Designed to audit the very work that generalizes the imported assets and improves the repo structure.

## Related Platform Artifacts
- Gates: G1, G4, G5.
- Agents: Source-to-Evidence Traceability Auditor (primary), Requirements, Arch/Design, Verification, and Compliance agents.
- Used in parallel with ide-requirements-baseline, ide-architecture-design-disposition, and ide-verification-coverage. This skill is self-referential and will be used to verify chains for its own generalization and the structure work it governs.