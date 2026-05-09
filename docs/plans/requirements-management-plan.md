# Requirements Management Plan

**Document ID**: RMP-PLAN-001  
**Policy Reference**: RMP-001 (Requirements Management Policy)  
**Date**: 2026-05-08  
**Status**: Baseline

---

## 1. Purpose

This plan defines how requirements are authored, managed, traced, and verified for the **Agentic-SDLC-AI** project. It applies to two distinct but related requirement domains:

| Domain | Description |
|--------|-------------|
| **Product Requirements** | What the Agentic-SDLC-AI tool itself must do — the agents, workflows, governance gates, HITL behavior, observability, and CLI capabilities delivered by this repo |
| **Tool-Enforced Requirements** | Requirements that the running Agentic-SDLC-AI system will impose, enforce, and trace when managing *other* projects with the tool |

Both domains follow identical authoring, numbering, and verification standards defined in this plan.

---

## 2. Requirements Authoring Standard

### 2.1 Mandatory Format

Every requirement **SHALL** be written using the following format:

> **[Subject noun] SHALL [verb phrase describing the required behavior or property].**

The subject noun names the entity being constrained (the system, agent, module, component, or process). Using "SHALL" is mandatory for binding requirements. "SHOULD" indicates a recommendation. "MAY" indicates permission.

**Correct examples:**
- `The Requirements Agent SHALL assign a unique identifier to every elicited requirement.`
- `The supervisor graph SHALL block any phase transition where gate readiness status is NOT_READY.`
- `The HITL gateway SHALL present the human reviewer with the full evidence package before requesting approval.`

**Incorrect (do not use):**
- `Requirements need a unique ID.` — missing noun-SHALL-verb form
- `The system should validate inputs.` — SHOULD is not binding; use SHALL for mandates
- `Ensure requirements are traceable.` — imperative form, not noun-SHALL-verb

### 2.2 Unique Requirement Identifier

Every requirement SHALL have a unique ID using the following scheme:

```
[PREFIX]-[NNNN]
```

| Prefix | Domain |
|--------|--------|
| `SYS` | System-level product requirements (Agentic-SDLC-AI) |
| `AGT` | Agent behavior requirements |
| `GOV` | Governance and gate requirements |
| `HITL` | Human-in-the-loop requirements |
| `INFRA` | Infrastructure and deployment requirements |
| `SEC` | Security requirements |
| `PERF` | Performance requirements |
| `INT` | Interface requirements |
| `DATA` | Data management requirements |
| `TEST` | Test and verification requirements |

Examples: `SYS-0001`, `AGT-0042`, `GOV-0010`, `HITL-0003`

NNNN is zero-padded to four digits and is never reused, even after a requirement is deleted (deleted requirements are marked RETIRED).

### 2.3 Required Requirement Attributes

Every requirement record SHALL contain all of the following attributes:

| Attribute | Description |
|-----------|-------------|
| **ID** | Unique identifier per §2.2 |
| **Short Name** | A brief (3-7 word) descriptive label used in RTMs, work items, and references. Not a sentence — a name. Example: `Supervisor Gate Blocking` |
| **Level** | Hierarchy level per §2.5: `L0-Stakeholder`, `L1-System`, `L2-Subsystem`, `L3-Implementation` |
| **Requirement Text** | The full noun-SHALL-verb statement per §2.1 |
| **Rationale** | Explains *why* the requirement exists — the problem it solves, the risk it mitigates, or the stakeholder need it addresses. Minimum 1-2 sentences. |
| **Verification Method(s)** | One or more of: `Test`, `Analysis`, `Demonstration`, `Inspection`. See §2.4. |
| **Verification Statement** | Explains *how* the requirement will be verified — what specific test, review, or analysis will confirm compliance. References the specific test file, script, or review checklist where applicable. |
| **Status** | `DRAFT` → `APPROVED` → `IMPLEMENTED` → `VERIFIED` → `RETIRED` |
| **Priority** | `P1-Critical`, `P2-High`, `P3-Medium`, `P4-Low` |
| **Source** | Document, stakeholder, or policy that originated the requirement |
| **Trace: Parent** | ID of parent/derived-from requirement (or `ORIGIN` if L0 top-level). See §2.5. |
| **Trace: Children** | IDs of requirements derived from this one, at the next lower level. `NONE` if a leaf requirement. |
| **Trace: Work Item** | Sprint work item ID(s) that implement this requirement (L2/L3 only; L0/L1 are implemented through their children) |
| **Trace: Test** | Test case ID(s) or file path(s) that verify this requirement |

### 2.4 Hierarchy and Decomposition

Requirements SHALL be organized in a **four-level hierarchy**. Each level represents a progressively lower level of abstraction, with each lower-level requirement derived from and traceable to a parent at the level above.

```
L0 — Stakeholder / Mission Needs
  └── L1 — System Requirements
        └── L2 — Subsystem / Component Requirements
              └── L3 — Implementation Requirements
```

| Level | Label | Description | Who Owns | Work Items Assigned |
|-------|-------|-------------|----------|--------------------|
| **L0** | Stakeholder / Mission | High-level capabilities and outcomes that stakeholders need the system to provide. Written from the stakeholder perspective. Validated by stakeholders. | Program Manager | No — decompose to L1 |
| **L1** | System | What the system as a whole must do or be to satisfy the L0 needs. The primary engineering baseline. | Chief Engineer | No — decompose to L2 |
| **L2** | Subsystem / Component | What a specific subsystem, agent, module, or component must do to satisfy its parent L1 requirement. | Requirements Agent / Lead | Yes — sprint-level |
| **L3** | Implementation | Precise implementation constraints — algorithms, data formats, API contracts, performance thresholds — that narrow how an L2 requirement is satisfied. | Developer / Agent | Yes — task-level |

**Decomposition Rules:**

1. Every L1 requirement SHALL derive from at least one L0 requirement. An L1 requirement with no L0 parent is an **orphan** and must be escalated for stakeholder review.
2. Every L2 requirement SHALL derive from at least one L1 requirement. An L2 requirement with no L1 parent signals a scope gap and must be resolved before Gate 2.
3. Every L3 requirement SHALL derive from at least one L2 requirement.
4. L0 and L1 requirements are verified **by showing that their children are all verified** (rollup verification). They do not independently require separate test cases.
5. An L1 requirement that has no L2 children at Gate 2 is a **decomposition gap** and blocks gate readiness.
6. Requirements SHALL NOT skip levels (e.g., an L0 requirement may not be the direct parent of an L3 requirement).
7. When an L2 or L3 requirement is added after baseline, its parent chain SHALL be updated to reflect the new child in `Trace: Children`.

**Derivation Statement:** When recording a derived requirement, the Rationale SHALL explicitly state: *"Derived from [parent ID] to address [specific aspect or constraint]."*

---

### 2.5 Verification Methods

| Method | When to Use |
|--------|-------------|
| **Test** | A repeatable automated or manual test can produce a pass/fail result. Preferred for all functional requirements. |
| **Analysis** | Requirements verified by reviewing code, design documents, algorithms, or models (e.g., proving a coverage constraint by static analysis). |
| **Demonstration** | A live walkthrough or manual exercise demonstrates the behavior (e.g., showing HITL pause and resume in a running system). |
| **Inspection** | A human review of the artifact confirms the requirement (e.g., confirming a config file contains the required field). |

A requirement MAY specify more than one method.

> **Note on L0/L1 verification:** High-level requirements are verified by rollup — when all child requirements at the level below are VERIFIED, the parent is considered VERIFIED. The Verification Statement for L0/L1 requirements SHALL describe this rollup: *"Verified when children [list IDs] are all in VERIFIED status."*

---

## 3. Requirements Record Template

Use this template when recording any new requirement:

```markdown
### [ID] — [Short Name]

| Field | Value |
|-------|-------|
| **ID** | [e.g., SYS-0001] |
| **Short Name** | [3-7 word label] |
| **Level** | [L0-Stakeholder / L1-System / L2-Subsystem / L3-Implementation] |
| **Status** | DRAFT |
| **Priority** | [P1-Critical / P2-High / P3-Medium / P4-Low] |
| **Source** | [Policy ID, stakeholder, or originating document] |
| **Trace: Parent** | [Parent requirement ID or ORIGIN if L0] |
| **Trace: Children** | [Child requirement IDs, or NONE if leaf] |
| **Trace: Work Item** | [Sprint item ID — fill when sprint planned; L0/L1 leave blank] |
| **Trace: Test** | [Test file/case ID — fill when implemented; L0/L1 use rollup] |

**Requirement Text**  
[Subject noun] SHALL [verb phrase].

**Rationale**  
[Why this requirement exists. Derived requirements SHALL state: "Derived from [parent ID] to address [specific aspect]."]

**Verification Method(s)**  
[Test | Analysis | Demonstration | Inspection]

**Verification Statement**  
[How this requirement will be confirmed. L0/L1: "Verified when children [IDs] are all VERIFIED." L2/L3: specific test, review, or analysis referencing artifacts.]
```

---

## 4. Requirement Lifecycle

```
DRAFT → APPROVED → IMPLEMENTED → VERIFIED → (RETIRED)
```

| State | Entry Condition | Responsible |
|-------|----------------|-------------|
| DRAFT | Requirement text written, attributes populated | Requirements Agent / Developer |
| APPROVED | Chief Engineer or Program Manager has reviewed and approved | Chief Engineer |
| IMPLEMENTED | Work item linked and code merged | Developer |
| VERIFIED | Verification statement executed and passed | V&V Agent / Developer |
| RETIRED | Requirement superseded or removed; never re-used | Chief Engineer |

---

## 5. Traceability Rules

**Hierarchy rules:**
1. Every L1 requirement SHALL trace to at least one L0 parent. Orphan L1 requirements block Gate 2.
2. Every L2 requirement SHALL trace to at least one L1 parent. Orphan L2 requirements block Gate 2.
3. Every L3 requirement SHALL trace to at least one L2 parent.
4. Every L0 and L1 requirement SHALL declare its children (`Trace: Children`) once decomposition is complete. An L1 with no L2 children at Gate 2 is a decomposition gap and blocks gate readiness.
5. Verification of L0 and L1 requirements is satisfied by rollup when all declared children reach VERIFIED status.

**Implementation rules:**
6. Every `[IMPL]` sprint work item SHALL trace to at least one APPROVED L2 or L3 requirement.
7. Every APPROVED L2/L3 requirement SHALL trace to at least one work item before sprint close.
8. Every APPROVED L2/L3 requirement in `IMPLEMENTED` status SHALL trace to at least one test case.
9. Missing trace links block Gate 2, Gate 4, and Gate 5 readiness.
10. The Requirements Traceability Matrix (RTM) SHALL be updated before each governance gate review and SHALL represent the full four-level hierarchy.

---

## 6. Requirements Baseline and Change Control

- Requirements are **baselined** at Gate 2 (Requirements Review).
- Post-baseline changes require a **Change Request** with rationale, impact on architecture/tests, and Chief Engineer approval.
- The baseline version is tagged in the repo as `req-baseline-<gate>-<date>`.

---

## 7. Application to This Repo

This plan applies immediately to the development of the Agentic-SDLC-AI product. A seed set of product requirements is maintained in:

> `docs/requirements/PRODUCT_REQUIREMENTS.md`

That file is the authoritative requirements register for this project and SHALL be updated as work is planned and completed. Every sprint work item in `docs/project-plan/SPRINT_1_DETAILS.md` (and subsequent sprints) SHALL reference at least one requirement ID from that register.

---

## 8. Application When Using the Tool

When the completed Agentic-SDLC-AI tool is used to manage an external project, the **Requirements Development Agent** SHALL:

1. Elicit L0 stakeholder needs first, then decompose to L1 system requirements, then guide decomposition to L2 and L3 as elaboration proceeds.
2. Enforce the four-level hierarchy defined in §2.4 — flagging orphan requirements (missing parent links) and decomposition gaps (L1 with no L2 children) as gate blockers.
3. Write all requirements in noun-SHALL-verb format per §2.1.
4. Assign IDs using the prefix scheme in §2.2 (with domain prefixes adapted to the target project).
5. Populate all mandatory attributes in §2.3 — including `Level`, `Trace: Parent`, and `Trace: Children` — for every requirement.
6. Store the full requirement hierarchy in the shared `AgentState` and persist it to the PostgreSQL checkpoint store.
7. Detect and report orphan requirements (no parent), childless non-leaf requirements (no children at expected decomposition level), and missing derivation rationale.
8. Generate a draft RTM that represents all four levels, linking L2/L3 requirements to architecture elements and proposed work items.
9. Emit a Gate 2 governance output package containing the requirements baseline (all levels), decomposition completeness check, and RTM.

These behaviors SHALL be implemented as agent logic in `src/agents/requirements_agent.py` and enforced by the supervisor gate hook.
