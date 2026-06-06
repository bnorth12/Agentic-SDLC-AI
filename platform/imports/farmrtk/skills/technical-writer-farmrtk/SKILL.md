---
name: technical-writer-farmrtk
description: >
  Scaffold and maintain FarmRTK operator docs — field quick-start, CONTRIBUTING
  cross-links, bench runbook pointers. Technical Writer. Use for field quick-start,
  contributor doc scaffold, or operator procedure draft.
metadata:
  short-description: "Field quick-start and doc scaffold"
---

# technical-writer-farmrtk

**Agent:** Technical Writer  
**Parent:** [CONTRIBUTING.md](../../../Docs/CONTRIBUTING.md) · [BACKLOG.md](../../../BACKLOG.md) (`DOC:` items)

## When to invoke

- P2 `DOC:` Field operator quick-start guide
- New bench runbook or TC artifact needs operator-facing summary
- CONTRIBUTING onboarding path updates (Typora, PlatformIO CLI)

## Scaffold field quick-start

```powershell
powershell -File Tools/ci/scaffold_field_quickstart.ps1
```

Use `-Force` to regenerate [Field-Quick-Start.md](../../../Docs/Field-Quick-Start.md).

## Procedure

1. Scaffold or edit field quick-start — link bench-runbook, DATA-STORAGE, EL-DOC-PWR-001.
2. Keep one-page operator focus; defer IDE setup docs until un-deferred in BACKLOG.
3. Cross-check links with `traceability-audit-farmrtk` after bulk doc edits.
4. Pair with Integration Engineer for bench steps; EIRC commit-tier before merge.

## Escalation

- UI/operator workflow conflict → UI segment + Chief Engineer
- Missing EL or power doc → Electronics Engineer + `electronics-wiring-farmrtk`