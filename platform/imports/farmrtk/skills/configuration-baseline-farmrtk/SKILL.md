---
name: configuration-baseline-farmrtk
description: >
  Generate FarmRTK configuration baseline manifest (git SHA, BOM, mechanical
  FILE_REV). Configuration Manager at M-G5 release. Use for baseline manifest,
  field kit snapshot, or release tag.
metadata:
  short-description: "CM baseline manifest"
---

# configuration-baseline-farmrtk

**Agent:** Configuration Manager  
**Parent:** [AGENTS-AND-SKILLS.md](../../../AGENTS-AND-SKILLS.md) G5 release gate

## Steps

1. Generate manifest:

```powershell
powershell -File Tools/ci/baseline_manifest.ps1 -Tag v0.1.0-mvp
```

2. Review `Docs/System-Level/baselines/<name>.md`.
3. Git tag + record skill versions under `.grok/skills/`.
4. EIRC milestone M-G5 with `independent-review-farmrtk`.