---
name: ide-independent-review-orchestrator
description: >
  Generalized skill for orchestrating full-scope independent local reviews of the agentic IDE platform.
  Primary for Independent Review Orchestrator. Generalizes independent-review-orchestrator (MATM),
  independent-review-farmrtk, and related review assets. Used early for compliance and to independently
  audit Requirements, Arch/Design, and Verification work (including self-hosted structure refactors and generalization).
metadata:
  short-description: "Full-scope independent review orchestration for IDE layers, generalized assets, and structure"
  agent: independent-review-orchestrator
  gates: [G1_traceability, G4_independent_review]
  maturity: M0+
---

# ide-independent-review-orchestrator

**Agents:** Independent Review Orchestrator (primary), Requirements Baseline Steward, Architecture/Design Disposition Planner, Source-to-Evidence Traceability Auditor, Verification Coverage Planner, Governance Policy Compiler, Refactoring Agent, Planning Agent  
**Parent:** [independent-review-orchestrator.agent.md](../../../agents/ide-platform/independent-review-orchestrator.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md)

## Purpose
Orchestrate complete, independent, local-only reviews of the IDE platform's development. Delegate to specialized skills to validate requirements quality, architecture/design alignment, traceability chains, verification coverage, compliance with plans/policies, artifact hygiene, and the health of self-hosted work (e.g., repo structure changes and generalization of copied agents). Produce objective reports that feed G4 gates and continuous improvement.

This is the core "EIRC" capability made IDE-native: we use it to independently review the very work that builds the IDE.

## When to Invoke
- Before/after major structural refactors or XGEN batches.
- At wave closeout or before G4 independent review gates.
- When assessing readiness of new generalized agents/skills or IDE surfaces.
- Periodically for compliance or after significant redlines/iteration.
- User: "run independent review on the structure execution plan", "ide-platform compliance review", "/ide-independent-review".

## Inputs
- Current requirements baselines and hierarchy.
- Architecture/design dispositions and workpacks.
- Implementation artifacts (generalized SKILL.md/.agent.md, manifests, code/structure changes).
- Verification plans and coverage reports.
- Gate registry, policies, and prior review reports.
- Traceability matrix and root hierarchy artifacts.

## Procedure

### 1. Scope and Delegate
- Define review scope (e.g., "IDE structure refactor + recent XGEN tranche" or "full platform process capabilities").
- Delegate to specialized skills:
  - Requirements baseline quality and planning readiness.
  - Architecture/design traceability, conceptual vs. as-built, and functional decomp consistency.
  - Source-to-evidence chain validation.
  - Verification coverage and missing-evidence prioritization.
  - Compliance with policies, gate modes, and layered model (via governance-policy-compiler).
  - Artifact lineage, repo hygiene, and self-hosting readiness.
- Require explicit hierarchy-field validation for all findings.

### 2. Gather Evidence Locally
- Use only local files, docs, manifests, and artifacts (no external services by default).
- Collect objective evidence with file references and snippets.

### 3. Classify and Score
- Classify findings: critical, major, minor, informational.
- Treat missing required hierarchy fields as governance findings.
- Produce overall health/score and trend indicators (where prior reviews exist).

### 4. Generate Report and Backlog
- Emit a local-only report (e.g., under independent_reviews/ or evidence/).
- Include summary, classified findings with context, and prioritized remediation backlog.
- Recommendations should be directly actionable by Planning Agent (wave impact), Refactoring Agent (execution), or the specialized review agents.

### 5. PowerShell / GitHub Native Emphasis
```powershell
# Example (future runner)
pwsh -File tools/review/ide-independent-review.ps1 -Scope "Structure-Refactor XGEN-Batch-1" -Output independent_reviews/ide-platform-review-$(Get-Date -Format yyyyMMdd).md

# Optionally create a local tracking issue (or GitHub if configured for the wave)
gh issue create --title "Independent review findings: IDE structure" --label review,compliance,ide-platform --body-file independent_reviews/ide-platform-review-*.md
```

### 6. Support Iteration and Self-Hosting
- Re-run after remediation or when new architecture/designs emerge.
- The review skill itself must have traceable chains and can be reviewed by future instances.

## Outputs
- Full-scope independent review report (score + classified findings + evidence refs).
- Prioritized remediation backlog.
- Updated views for traceability, compliance, and verification.
- Local evidence suitable for G1, G4, and continuous improvement.

## Guardrails
- Reviews are independent and do not modify reviewed artifacts.
- Local-first by default.
- Explicit references and hierarchy only.

## Generalization & IDE-Specific Notes
- Removed product-specific review contexts.
- Strong focus on reviewing the IDE's own model: agents/skills as editable artifacts, editors/viewers, pack content (ide-platform as self-governance), L0-L8 decomposition, repo structure as architecture subject, hybrid orchestration, self-hosting.
- Explicitly supports reviewing the generalization of copied agents and the structural refactors that make the IDE possible.
- Designed to be used on its own outputs and the platform's governance artifacts.

## Related Platform Artifacts
- Gates: G1, G4.
- Agents: Independent Review Orchestrator (primary) + all specialized review agents (Requirements, Arch/Design, Traceability, Verification, Compliance).
- Used in conjunction with ide-governance-policy-compiler and the full set of early governance skills. This skill is self-referential and will be used to independently review the very procedures and structure work that generalize the imported agents.