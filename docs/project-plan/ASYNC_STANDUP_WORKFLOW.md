# Async Standup Default Workflow

Document ID: ASYNC-STANDUP-001  
Date: 2026-05-18  
Status: Active Default

---

## Purpose

Define the default no-meeting execution rhythm for sprint delivery. This workflow replaces synchronous standups with lightweight asynchronous updates captured in sprint standup board files.

---

## Default Operating Rule

Effective immediately, sprint execution SHALL use async standup tracking by default unless explicitly overridden.

Each active sprint SHALL maintain:
1. A sprint execution details file (scope, stories, dependencies, estimates, day plan).
2. A sprint async standup board (daily deltas, blockers, next actions, evidence links).

---

## Update Cadence

During implementation sessions (including vibe coding), update the async standup board:
1. At start of session.
2. After each meaningful work burst.
3. When story status changes (Not Started, In Progress, In Review, Done, Blocked).
4. At session close with next action and blocker state.

---

## Required Entry Format

Each update entry SHALL include:
1. Timestamp
2. Story ID(s)
3. What changed
4. Evidence/artifacts touched
5. Blockers/risks
6. Next action

Suggested structure:

- Timestamp: 2026-06-21 09:30
- Stories: SKILL-4001
- Update: Added initial contract model and validators.
- Evidence: src/skills/contracts.py, tests/unit/test_skill_contract_schema.py
- Blockers: None
- Next: Add version parser tests and open PR.

---

## Story Status Model

Use only these statuses for consistency:
1. NOT STARTED
2. IN PROGRESS
3. IN REVIEW
4. BLOCKED
5. DONE

---

## Traceability Expectations

When a story reaches DONE:
1. Update sprint details document status.
2. Update requirement Trace: Work Item fields for linked requirement IDs.
3. Record verification artifact links in standup board.

---

## Minimal Governance Checks Per Session

1. Any new blocker captured.
2. Any risk trend change captured.
3. Next action identified for each IN PROGRESS story.
4. No story marked DONE without evidence artifact path.

---

## File Naming Standard

For each sprint N:
1. Execution details: docs/project-plan/SPRINT_N_DETAILS.md (or equivalent sprint-specific detail file)
2. Async board: docs/project-plan/SPRINT_N_ASYNC_STANDUP_BOARD.md

For skill-focused sprints, allowed naming variant:
- docs/project-plan/SPRINT_N_SKILLS_DETAILS.md
- docs/project-plan/SPRINT_N_SKILLS_ASYNC_STANDUP_BOARD.md
