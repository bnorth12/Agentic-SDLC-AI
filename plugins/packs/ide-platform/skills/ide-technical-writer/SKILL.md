---
name: ide-technical-writer
description: >
  Generalized skill for producing crisp, living technical documentation, decision records, and
  IDE-focused content (charter, plans, agent/skill definitions, invocation records) for the agentic IDE platform.
  Generalizes technical-writer-farmrtk with full IDE surface, self-hosting, and L0-L8 awareness.
  Primary for Technical Writer role in platform process packs.
metadata:
  short-description: "Living docs, ADRs, generalized agent/skill content, and IDE-focused technical writing"
  agent: technical-writer (or composed in ide-platform)
  gates: [G1_traceability, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-technical-writer

**Agents:** Technical Writer (composed), Refactoring Agent (primary consumer for generalization and structural docs), Planning Agent  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · `agents/platform/invocations/remaining-xgen-refactoring-session.md` · Reusability Evaluation Report

## Purpose
Produce and maintain crisp, living technical documentation that describes the agentic IDE (not historical SDLC bloat). This includes generalized agent and skill definitions, invocation records, layered plans, decision records (ADRs), quick-start guides for adding editors/viewers/skills/agents/packs, and self-hosting examples. The skill is used heavily by the Refactoring Agent during generalization and structural work to ensure new IDE-native artifacts have high-quality, consistent, IDE-surface-aware documentation.

## When to Invoke
- When generalizing new agents or skills (remaining XGEN tranche) — produce the rich .agent.md and SKILL.md content.
- During structural execution (content moves, legacy quarantine, doc archive) — update plans, manifests, and living docs.
- When producing invocation records, tranche plans, or evidence bundles.
- For ADRs on major choices (legacy handling, where generalized skills live, editor/viewer contracts).
- At G4 independent review prep and G5 baseline handoff (clear, traceable documentation).
- User: "write the generalized definition for the new hierarchy steward", "produce ADR for remaining XGEN registration", "refresh living docs after ide-platform updates".
- As a supporting step in ide-structural-refactoring (especially Phases 1, 3, 4) and self-hosting.

## Inputs
- Source material (raw imports for generalization, existing generalized artifacts, plans, invocation records, architecture decisions).
- Target audience and surface (future IDE editors for .agent.md/SKILL.md, evidence viewers, pack manifests, GitHub PRs).
- Current layer model, gate registry, and manifest state.
- Prior living docs that must be kept concise and IDE-focused.

## Procedure

### 1. Audience & Surface Analysis
- Determine the primary surfaces the content will live on (editable .agent.md or SKILL.md in ide-platform, layer index, invocation record, ADR, plan section, evidence bundle).
- Identify required IDE-specific elements: hierarchy metadata, L0-L8 or Cross references, generalization notes, PowerShell + gh examples, Parent links, gate mappings, self-hosting notes.

### 2. Content Generation / Update (IDE-Native)
- Produce rich frontmatter + structured sections (Purpose, When to Invoke, Inputs, Procedure with PS/gh, Outputs, Generalization & IDE-Specific Notes, Related Platform Artifacts).
- Ensure all content supports agents/skills as first-class editable artifacts, pack delivery, hybrid orchestration, and self-hosting.
- For generalized items: explicitly document the source import, changes made, and how the item participates in the IDE model.

### 3. Evidence & Traceability
- Include explicit links back to source (import path or prior artifact), architecture (layer or WP), and verification (this tranche's audits).
- Add compaction / rollup notes when archiving historical content.

### 4. PowerShell / GitHub Native
```powershell
# Example (to be turned into reusable fragment)
pwsh -File tools/docs/write-ide-generalized.ps1 -Source "platform/imports/matm/agents/xxx.agent.md" -Target "plugins/packs/ide-platform/agents/ide-xxx.agent.md" -Template "ide-agent" -Output evidence/ide-xxx-doc-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Generalized technical content for ide-xxx" --label docs,xgen,ide-platform --body-file evidence/ide-xxx-doc-*.md
```

### 5. Review & Self-Hosting Close
- Run hierarchy steward + traceability auditor on the new/updated content.
- Update this skill with lessons (self-referential).
- Hand evidence to the Refactoring Agent for Phase 4/5.

## Outputs
- High-quality, IDE-aware .agent.md, SKILL.md, plans, invocation records, ADRs, and living docs.
- Updated quick-start / "how to add" guidance for the IDE surfaces.
- Evidence bundles with clear traceability.

## Generalization & IDE-Specific Notes
- Original FarmRTK technical-writer (quick-start templates, product-specific paths) generalized to focus exclusively on the agentic IDE: generalized agents/skills as editable artifacts, L0-L8 decomposition, self-hosting of the reboot, PowerShell + GitHub native by default, pack manifests as the delivery mechanism.
- Removed all hardware/firmware/CAD-specific content (those belong in domain packs such as engineering-sdlc).
- Designed to be the primary writer for the remaining XGEN tranche and ongoing structural IDE integration work.

## Related Platform Artifacts
- Gates: G1, G4, G5.
- Primary consumer: Refactoring Agent (ide-structural-refactoring).
- Works alongside ide-process-audit, ide-repo-audit, and the meta drivers.
- Future home: ide-platform pack (or core technical writing capability surfaced in the IDE).