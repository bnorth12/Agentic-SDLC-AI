---
name: orchestrate-farmrtk
description: >
  FarmRTK wave orchestration — read BACKLOG + SYS-DOC-10, map open items to
  agents and project/bundled skills, emit wave plan. Program Manager and Chief
  Engineer use before sprint scope. Use for orchestrate wave, delegate backlog,
  agent routing, or /orchestrate-farmrtk.
metadata:
  short-description: "Backlog to agent/skill wave plan"
---

# orchestrate-farmrtk

**Agents:** Program Manager (primary), Chief Engineer (technical routing)  
**Parent:** [AGENTS-AND-SKILLS.md](../../../AGENTS-AND-SKILLS.md) · [11-Agent-Readiness.md](../../../Docs/System-Level/11-Agent-Readiness.md)

FarmRTK has **no separate LangGraph runtime** — this skill is the executable orchestration procedure: plan → delegate → HITL → EIRC → metrics.

## When to invoke

- Start of wave or sprint (HITL G0)
- User: "what should we work on next", "orchestrate wave", "route backlog"
- After SYS-DOC-10 epic updates

## Steps

1. Generate wave plan:

```powershell
powershell -File Tools/orchestrate/wave_plan.ps1
```

2. Read report under `.farmrtk/orchestrate/wave-plan-*.md`.
3. **G0 charter:** `powershell -File Tools/orchestrate/g0_wave_select.ps1` → `Docs/System-Level/waves/G0-wave-selection-*.md`.
4. **Program Manager:** confirm in-scope rows with user (do not auto-start ASK-01 if deferred).
5. For each in-scope row, invoke the listed **project skill** first; use bundled `design` / `implement` / `review` for deep loops.
6. Bench sessions: **Integration Engineer** + `integration-bench-farmrtk` before TC execution.
7. Before merge: `independent-review-farmrtk` merge mode.
8. Wave end: `program-metrics-farmrtk` + bump SYS-DOC-10.

## Delegation rules

See [references/DELEGATION_MATRIX.md](references/DELEGATION_MATRIX.md) and `Tools/orchestrate/delegation_map.json`.

## Escalation

- Cross-segment conflict → Chief Engineer
- Scope creep → Program Manager + user HITL G0
- REQ orphan → Traceability Manager + `requirements-management-farmrtk`