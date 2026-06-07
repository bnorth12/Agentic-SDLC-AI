---
name: check-work-commit-farmrtk
description: >
  FarmRTK commit-tier independent review (EIRC). Light pre-commit scan:
  orphan REQ/TC, broken links in changed docs, cad-part frontmatter, SCAD
  PARAMS line 1. Informational and non-blocking at M0-M1 unless
  FARMRTK_ENFORCE_CHECKS=1. Use before git commit or via pre-commit hook.
metadata:
  short-description: "EIRC commit-tier check (informational)"
---

# check-work-commit-farmrtk

**Agent:** Independent Review Committee (EIRC)  
**Tier:** Commit — **non-blocking** at M0–M1 (default)  
**Parent:** [AGENTS-AND-SKILLS.md](../../../AGENTS-AND-SKILLS.md) · [EIRC-MILESTONE-CHECKLIST.md](../../../Docs/System-Level/EIRC-MILESTONE-CHECKLIST.md)

## When to invoke

- Before `git commit` (via `Tools/hooks/pre-commit` or explicit run)
- After agent edits docs, cad-parts, or firmware
- User: "commit check", "EIRC commit review"

## Steps

1. Ensure changes are **staged** if simulating pre-commit.
2. Run from repo root:

```powershell
powershell -File Tools/ci/check_independent_review.ps1 -Mode commit
```

Or Git Bash:

```bash
bash Tools/ci/check_independent_review.sh commit
```

3. Read report under `.farmrtk/reviews/commit-*.md`.
4. **Do not block** commit at M0–M1 unless user sets `FARMRTK_ENFORCE_CHECKS=1`.
5. Log warnings for trend (KPI-3 RE-06).

## Scope

See [references/COMMIT_TIER.md](references/COMMIT_TIER.md).

## Escalation

Merge-blocking issues → defer to merge-tier (`check_repo.sh --merge`) or Chief Engineer.