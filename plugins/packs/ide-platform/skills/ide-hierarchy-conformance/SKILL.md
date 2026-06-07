---
name: ide-hierarchy-conformance
description: >
  Generalized skill for auditing hierarchy conformance and producing enforceable governance findings for the agentic IDE platform.
  Primary for Hierarchy Conformance Auditor. Generalizes hierarchy-conformance-auditor (MATM) and related assets. Enforces functional decomposition and hierarchy metadata for requirements, generalized agents, and structure changes.
metadata:
  short-description: "Hierarchy conformance audit for IDE functional decomp, generalized assets, and structure"
  agent: ide-hierarchy-conformance-auditor
  gates: [G1_traceability, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-hierarchy-conformance

**Agents:** Hierarchy Conformance Auditor (primary), Requirements Baseline Steward, Architecture/Design Traceability Auditor, Source-to-Evidence Traceability Auditor, Independent Review Orchestrator, Refactoring Agent  
**Parent:** [ide-hierarchy-conformance-auditor.agent.md](../../../agents/ide-platform/ide-hierarchy-conformance-auditor.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · Structural Refactor Execution Plan

## Purpose
Enforce structural hierarchy completeness (parent capability, child function, decomposition level, allocated component/module, verification method) in requirements, architecture, generalized skills/agents, and repo structure changes for the IDE. Publish auditable metrics and escalate missing fields as governance findings. Supports functional decomp of L0-L8 and the structure refactor.

## When to Invoke
- During requirements baseline, arch/design audits, and structure execution for functional decomp.
- Before/after generalization to validate hierarchy in new IDE-native versions.
- When reviewing repo structure or layer decomp.
- At G1, G4, G5.
- User: "audit hierarchy for the structure execution plan", "check decomp in generalized agents", "/ide-hierarchy-conformance".

## Inputs
- Sprint/work ID or scope (e.g., "Structure-Refactor").
- Requirements, architecture docs, generalized agents/skills in ide-platform, structure execution plan, hierarchy artifacts (from baseline/disposition).
- Independent review outputs.

## Procedure

### 1. Run Hierarchy Verification
- For the scope (e.g., structure changes, XGEN batch), analyze artifacts for required hierarchy fields.
- Use scripts or manual check on the execution plan, generalized SKILL.md/.agent.md, manifests, baseline/disposition docs.
- Example (adapt for IDE):
  - Validate hierarchy in requirements for IDE structure.
  - Check generalized agents have decomp for L4 packs, L0 editors, etc.
  - Confirm structure moves allocate to correct components (ide-platform, legacy, archive).

### 2. Compute Conformance Metrics
- Calculate: hierarchy coverage ratio, decomposition level counts (L0/L1/L2 for layers), phase/component counts, parent capability fan-out, missing hierarchy field rows.
- Especially for functional decomp: ensure L0-L8 and cross-cuts (structure) are properly decomposed and allocated.

### 3. Escalate Findings
- By severity: major if coverage below threshold (e.g., for foundational structure or generalized process agents), minor for isolated omissions, informational for optimization.
- Escalate missing fields as governance findings (not notes).
- Tie to the execution plan: e.g., "add hierarchy to structure moves for L4/L7".

### 4. Publish Outputs
- Reports under evidence/ or independent_reviews/ (e.g., hierarchy_conformance_structure.md).
- Metrics and prioritized remediation for the Refactoring Agent and other skills.
- Feed into independent review and verification.

### 5. PowerShell / GitHub Native Emphasis
```powershell
# Example (adapt and implement)
pwsh -File tools/hierarchy/conformance.ps1 -Scope "Structure-Refactor" -Baseline docs/ide-structure-requirements-baseline.md -Output evidence/hierarchy-conformance-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Hierarchy conformance gaps in IDE structure" --label compliance,hierarchy,ide-platform --body-file evidence/hierarchy-conformance-*.md
```

### 6. Support Iteration and Self-Hosting
- Re-audit after changes (e.g., post-moves or new generalizations).
- The skill is self-referential: audit hierarchy in the generalized skills and the structure work.
- Use to enforce decomp in the IDE's own architecture during the refactor.

## Outputs
- independent_reviews or evidence reports with metrics.
- Hierarchy coverage, decomp counts, missing fields.
- Escalated findings and remediation for governance.
- Evidence for G1, G4, G5.

## Guardrails
- Local-only evidence.
- Do not downgrade missing hierarchy to non-governance.
- Support functional decomp for the IDE model.

## Generalization & IDE-Specific Notes
- Removed product-specific (e.g., sprint-specific scripts, FarmRTK/MATM paths).
- Added explicit focus on IDE: hierarchy for L0-L8 decomp, agents/skills artifacts, pack allocation (ide-platform), repo structure as decomp subject, self-hosting (hierarchy in the platform's own development).
- Strong support for the structure refactor and generalization (ensuring decomp in new versions and layout).

## Related Platform Artifacts
- Gates: G1, G4, G5.
- Agents: Hierarchy Conformance Auditor (primary) + other early governance agents, Refactoring Agent.
- Used with the execution plan and traceability/verification skills. This skill is self-referential and will enforce decomp for the changes that generalize the copied agents and make the repo IDE-native.