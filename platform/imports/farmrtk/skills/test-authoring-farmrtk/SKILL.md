---
name: test-authoring-farmrtk
description: >
  Scaffold and maintain FarmRTK TC-xxx test cases and artifact dirs. System
  Test and Software Test engineers. Use for new test case, TC scaffold, or CT/TC
  authoring.
metadata:
  short-description: "TC-xxx test case scaffold"
---

# test-authoring-farmrtk

**Agents:** System Test Engineer, Software Test Engineer  
**Parent:** [Tests/Verification/01-Verification-Plan.md](../../../Tests/Verification/01-Verification-Plan.md)

## Scaffold

```powershell
powershell -File Tools/ci/scaffold_tc.ps1 -TcId TC-013 -ParentReq SYS-REQ-005 -Method Test
```

## Steps

1. Scaffold TC + `Tests/Verification/artifacts/TC-nnn/`.
2. Link parent REQ and segment REQs in traceability table.
3. Add row to [Tests/BACKLOG.md](../../../Tests/BACKLOG.md) and verification plan.
4. Execute on bench; log in `execution-log.md` (see TC-002 template).
5. Run `validation-plan-farmrtk` audit.