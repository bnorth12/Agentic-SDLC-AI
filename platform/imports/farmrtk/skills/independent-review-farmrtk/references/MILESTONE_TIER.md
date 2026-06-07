# Milestone tier scope

**Script:** `Tools/ci/check_independent_review.sh milestone <gate>`

Human convenes EIRC at gates M-G0..M-G5 per [EIRC-MILESTONE-CHECKLIST.md](../../../../Docs/System-Level/EIRC-MILESTONE-CHECKLIST.md).

## Automated scans (advisory)

| Gate | Automated focus |
|------|-----------------|
| **M-G0** | Root BACKLOG P0 items have `REQ:` or `TC:` tags |
| **M-G1** | Orphan REQ count in `Docs/`; segment 01-Requirements exist |
| **M-G2** | SYS-DOC-02 + SYS-DOC-04 present; risk register linked |
| **M-G3** | TC-002/TC-011 specs exist; CT P0 specs in Tests/ |
| **M-G4** | TC artifact dirs populated (execution logs) |
| **M-G5** | `dashboard_rev` current; BOM + mechanical FILE_REV noted |

## Supplement

Run full traceability before M-G1:

```powershell
powershell -File Tools/ci/traceability_audit.ps1
```

## Pass criteria

Script **info/warn only** — PM + user HITL approve gate in checklist markdown.