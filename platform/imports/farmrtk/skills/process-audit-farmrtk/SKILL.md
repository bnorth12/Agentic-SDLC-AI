---
name: process-audit-farmrtk
description: >
  Audit FarmRTK agent/skill registry coherence — SYS-DOC-10 vs on-disk skills,
  delegation map, and readiness index. Quality Assurance Engineer. Use for
  process audit, agent registry check, or skill burn-down verification.
metadata:
  short-description: "Agent/skill registry audit"
---

# process-audit-farmrtk

**Agent:** Quality Assurance Engineer  
**Parent:** [AGENTS-AND-SKILLS.md](../../../AGENTS-AND-SKILLS.md) · [10-Agent-Skill-Development-Backlog.md](../../../Docs/System-Level/10-Agent-Skill-Development-Backlog.md)

Distinct from EIRC design review — this skill checks **process compliance**: registry currency, skill/script pairing, orchestration artifacts.

## When to invoke

- End of agent/skill burn-down wave
- Before promoting Partial → Ready in SYS-DOC-11
- Quarterly QA pass with Repo Organization Manager

## Audit

```powershell
powershell -File Tools/ci/process_audit.ps1
```

Pair with `repo-audit-farmrtk` and `traceability-audit-farmrtk` for full governance sweep.

## Procedure

1. Run `process_audit.ps1` — fix WARN on missing registry files or skill count drift.
2. Cross-check SYS-DOC-10 **Active** rows against `.grok/skills/*/SKILL.md` on disk.
3. Verify `Tools/orchestrate/delegation_map.json` tag rules match backlog prefixes (`PROC:`, `INT:`, etc.).
4. Confirm each new project skill has a `Tools/ci/*.ps1` or documented script path in SYS-DOC-10.
5. Log findings; open `DOC:` or Repo Org backlog items for registry gaps.

## Escalation

- Skill without script → Repo Organization Manager + `create-skill`
- Orchestration routing gap → Program Manager + `orchestrate-farmrtk`