---
name: validation-plan-farmrtk
description: >
  Audit FarmRTK verification plan TC links vs Test-Cases files. V&V Lead M-G3.
  Use for validation plan audit, V&V coverage check, or TC plan sync.
metadata:
  short-description: "Verification plan TC audit"
---

# validation-plan-farmrtk

**Agent:** V&V Lead  
**Parent:** [01-Verification-Plan.md](../../../Tests/Verification/01-Verification-Plan.md)

## Steps

1. `powershell -File Tools/ci/validation_plan_audit.ps1`
2. Scaffold missing TCs with `test-authoring-farmrtk`.
3. Coordinate System Test + Software Test execution calendar.
4. Distinguish verification (TC pass) vs validation (G4 user sign-off).