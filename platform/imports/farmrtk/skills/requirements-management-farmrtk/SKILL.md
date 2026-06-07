---
name: requirements-management-farmrtk
description: >
  FarmRTK requirements workflow — REQ ID lint, allocation matrix edits in
  01-System-Requirements.md and segment 01-Requirements. No DOORS/Jama. Use for
  new REQ, requirements management, or allocation matrix update.
metadata:
  short-description: "REQ authoring and lint"
---

# requirements-management-farmrtk

**Agent:** Requirements Manager  
**Parent:** [01-System-Requirements.md](../../../Docs/System-Level/01-System-Requirements.md)

## Steps

1. Lint REQ IDs: `powershell -File Tools/ci/requirements_lint.ps1`
2. Add new SYS-REQ row in `Docs/System-Level/01-System-Requirements.md` **before** referencing in backlog/code.
3. Allocate to segment in `Docs/<Segment>/01-Requirements.md`.
4. Run `traceability-audit-farmrtk` on same PR.
5. Tag backlog items with `REQ:` prefix.

## Enforce

`$env:FARMRTK_ENFORCE_CHECKS = "1"; powershell -File Tools/ci/requirements_lint.ps1 -Enforce`