# IDE Structure Requirements Baseline

**Produced by:** Requirements Baseline Steward (using generalized `ide-requirements-baseline` skill)  
**Date:** 2026-06 (initial baseline for Wave 01 / R1 structural work)  
**Context:** Self-hosted governance exercise on the Agentic-SDLC-AI platform repo itself.  
**Inputs:** Current repo tree, layered IDE_REFACTOR_PLAN.md (L0-L8), REUSABILITY_EVALUATION_REPORT.md, AGENTIC_IDE_PROJECT_PLAN.md, WAVE_01_R1_FOUNDATIONS_DETAILED_PLAN.md, FRAMEWORK_DECOMPOSITION.md, existing platform/ + plugins/packs/ + agents/platform/ skeleton, legacy src/ and docs bloat.  
**Gates exercised:** G0 (intake for this baseline task), G1 (traceability).  
**Hierarchy Metadata Applied:** Parent = L5 Workspace + Cross-layer Repo Structure; Child = IDE-aligned filesystem for agents/skills as artifacts, pack content, platform config vs. content separation; Decomposition level = 2; Allocated = platform/ + plugins/packs/ide-platform/ + agents/ + docs/ (living vs archive); Verification method = compliance audit by ide-governance-policy-compiler + architecture disposition by ide-architecture-design-disposition.

---

## 1. Purpose of this Baseline
Establish clear, verifiable requirements for the **filesystem and content organization** of the Agentic IDE platform repo so that it can serve as:
- A clean, self-hosting workspace example.
- A natural home for developing and editing agents (.agent.md), skills (SKILL.md), packs, manifests, gate evidence, and functional decompositions of the L0-L8 layers.
- Something that the future IDE surfaces (agent editor, skill editor, structure viewer, compliance dashboard) can open and work with directly without fighting historical noise.

This baseline precedes any major structural refactor (XLEG / XDOC / XPACK work in Wave 01) and any further generalization of imported agents/skills.

## 2. Quality Findings (from ide-requirements-baseline procedure)

**High Severity (must address before structural work proceeds):**
- REQ-STRUCT-001: The repo must separate **platform configuration** (manifests, gates, schemas, temporary imports) from **content** (agents, skills, pack-delivered process capabilities). Current state mixes them (platform/skills/ next to platform/imports/ and platform/manifest.yaml). This violates the "packs deliver capabilities" model (L4/L7) and makes self-hosting confusing.
- REQ-STRUCT-002: All first-class IDE artifacts (agents, skills, manifests, evidence bundles) must live in locations that are discoverable and editable as a normal workspace (under plugins/packs/<id>/ or a clearly designated content area). Scattered locations (agents/platform/, platform/skills/, docs/project-plan/ mixed with old sprint boards) break the "agents and skills as editable artifacts" vision (L0/L4).
- REQ-STRUCT-003: Legacy and historical material must be quarantined so it does not pollute the living IDE development surface. Current state has src/ monolith, massive docs/governance/ + old project-plan/ boards, root-level PHASE_0_*/IMPLEMENTATION_SUMMARY_*/NEXT_STEPS_*, etc. This is a compliance and onboarding risk.

**Medium Severity:**
- REQ-STRUCT-004: The repo structure should itself demonstrate functional decomposition of the L0-L8 layers and cross-cuts (e.g., clear homes for L0 GUI/viewer experiments, L2 orchestration adapters, L3 gate extensions, L4 plugin host content, L7 ide-platform process pack).
- REQ-STRUCT-005: Packaging, discovery, and bootstrap (pyproject.toml, Makefile, ide-platform manifest, future skill/agent loaders) must align with the structure so that "opening this repo as a workspace" immediately surfaces the platform's own agents, skills, and packs.
- REQ-STRUCT-006: Traceability from structure decisions back to IDE requirements (editors for agents/skills, viewers for evidence, self-hosting, PowerShell + GitHub native) must be explicit and maintained.

**Low / Notes:**
- Some legacy scripts and the old src/ agents/boards may have reusable patterns (hitl, governance_validation, state ideas) that should be extracted under L1/L2/L3 or L4 tools rather than discarded.
- Old docs have institutional value but belong in archive for the living development surface.

## 3. Traceability & Architecture Linkage
- Linked to L5 (Workspace) + Cross (Repo Structure as first-class architecture subject).
- Supports L0 (editors/viewers for .agent.md / SKILL.md / manifests / evidence).
- Supports L4 (plugin host loading from packs, not scattered platform/ locations).
- Supports L7 (ide-platform as the natural home for platform process agents/skills).
- Enables self-hosting: the same requirements/architecture/compliance/verification we will deliver to users must govern our own repo and development.
- Hierarchy: Parent = "Agentic IDE Platform as Self-Hosting Workspace"; Child functions include "Clean separation of config vs content", "Agents/skills as first-class editable artifacts", "Living vs archive docs", "Alignment to L0-L8 decomposition".

## 4. Intake Verdict for Structural Work
**Conditional** (ready to proceed with limited exploration + mandatory follow-up disposition).

**Required closure criteria before large-scale moves (to be verified by ide-governance-policy-compiler and ide-architecture-design-disposition):**
- Produce an explicit Architecture/Design Disposition for the proposed structure (see next step).
- Define minimal success criteria for the restructured repo (e.g., "can open as workspace and immediately see/edit the platform's own agents and skills", "no low-reusability legacy mixed into active development tree").
- Run a compliance audit of the proposed changes against current gate registry and policies.
- Update this baseline with any new requirements discovered during the disposition.

## 5. Recommended Next (Self-Hosted) Steps
1. Use the Architecture/Design Disposition Planner (`ide-architecture-design-disposition`) on the concrete question: "What filesystem layout best supports the IDE model (agents/skills as artifacts, packs as delivery, L0-L8 separation, self-hosting) while minimizing future thrash?"
2. Use Governance Policy Compiler to check the current state and proposed changes for policy violations (strict for platform core structure).
3. Execute the approved structural changes under the Refactoring Agent, producing evidence for G1/G4.
4. Re-baseline requirements after the changes (iteration is expected and planned).

This exercise demonstrates the value of having Requirements + Arch/Design + Compliance capabilities early: we are using them to govern the platform's own structural work instead of ad-hoc changes.

---

**Evidence for G1/G4:** This document + links to the source plans and reusability report. Hierarchy metadata applied throughout.

**Verification method:** Compliance audit (ide-governance-policy-compiler) + architecture disposition (ide-architecture-design-disposition) + re-audit after structural changes.

**Owner:** Requirements Baseline Steward (this baseline) → handoff to Architecture/Design Disposition Planner and Refactoring Agent for execution.

**Status:** Baseline complete. Ready for disposition step. (Hardware benchmarks deferred per direction; process first, redline and adapt as we execute.)