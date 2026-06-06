---
name: independent-review-farmrtk
description: >
  FarmRTK EIRC unified review — commit, merge, and milestone gate modes.
  Extends check-work-commit-farmrtk. Merge enforce optional via
  FARMRTK_ENFORCE_MERGE_CHECKS. Milestone mode runs M-G0..G5 checklist
  scans. Use for EIRC review, milestone gate, or merge enforce check.
metadata:
  short-description: "EIRC commit/merge/milestone review"
---

# independent-review-farmrtk

**Agent:** Independent Review Committee (EIRC)  
**Parent:** [AGENTS-AND-SKILLS.md](../../../AGENTS-AND-SKILLS.md) · [EIRC-MILESTONE-CHECKLIST.md](../../../Docs/System-Level/EIRC-MILESTONE-CHECKLIST.md)

Orchestrates all EIRC tiers. Commit-tier remains **non-blocking** at M0–M1 unless `FARMRTK_ENFORCE_CHECKS=1`.

## Modes

| Mode | When | Blocking |
|------|------|----------|
| `commit` | pre-commit, agent before commit | No (M0–M1) |
| `merge` | pre-push, CI, PR to `main` | Optional (`FARMRTK_ENFORCE_MERGE_CHECKS=1`) |
| `milestone` | Wave end, M-G0..G5 gate | Human sign-off; script is advisory |

## Steps

### Commit tier

```powershell
powershell -File Tools/ci/check_independent_review.ps1 -Mode commit
```

### Merge tier

```powershell
powershell -File Tools/ci/check_independent_review.ps1 -Mode merge
```

Enforce:

```powershell
$env:FARMRTK_ENFORCE_MERGE_CHECKS = "1"
powershell -File Tools/ci/check_independent_review.ps1 -Mode merge
```

### Milestone tier

```powershell
powershell -File Tools/ci/check_independent_review.ps1 -Mode milestone -Gate M-G1
```

Gates: `M-G0`, `M-G1`, `M-G2`, `M-G3`, `M-G4`, `M-G5` — see [references/MILESTONE_TIER.md](references/MILESTONE_TIER.md).

## Outputs

Reports under `.farmrtk/reviews/{commit,merge,milestone}-*.md` (gitignored).

## Escalation

- FAIL at merge enforce → Chief Engineer or user waive
- Milestone FAIL → Program Manager reschedules gate; do not advance maturity phase

## Related skills

- `check-work-commit-farmrtk` — commit-only alias (subset of this skill)
- `traceability-audit-farmrtk` — full-repo REQ scan (milestone M-G1 supplement)
- `review` — bundled Grok deep review on large diffs