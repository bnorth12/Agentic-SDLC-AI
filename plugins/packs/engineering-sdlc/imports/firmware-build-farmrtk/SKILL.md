---
name: firmware-build-farmrtk
description: >
  FarmRTK PlatformIO compile check for Base-CYD and Rover-CYD via Tools/dev/pio.ps1.
  Firmware Engineer. Use for firmware build check, PIO compile verify, or pre-bench
  flash prep.
metadata:
  short-description: "PlatformIO Base/Rover build check"
---

# firmware-build-farmrtk

**Agent:** Firmware Engineer  
**Parent:** [Software/BACKLOG.md](../../../Software/BACKLOG.md) · [Tools/README.md](../../../Tools/README.md)

## When to invoke

- After shared lib or `platformio.ini` changes
- ASK-03 bench prep (before `pio run -t upload`)
- Pre-merge firmware segment edits

## Build check

```powershell
powershell -File Tools/ci/firmware_build_check.ps1
```

Single target:

```powershell
powershell -File Tools/ci/firmware_build_check.ps1 -Target base
powershell -File Tools/ci/firmware_build_check.ps1 -Target rover
```

Flash (bench HITL — user confirms USB port):

```powershell
powershell -File Tools/dev/pio.ps1 run -t upload -d Segments/Base-Station/Software/Base-CYD
```

## Procedure

1. Run `firmware_build_check.ps1` — both targets must pass before merge.
2. Use bundled `implement` + `check-work` for feature work; this skill is compile gate only.
3. Deps: `Tools/dev/install_firmware_deps.ps1` if TFT_eSPI / lib paths break.
4. Bench sessions: hand off to Integration Engineer + `integration-bench-farmrtk`.

## Escalation

- Compile regression in shared lib → Software Architect review
- Upload / serial issues on bench → Integration Engineer