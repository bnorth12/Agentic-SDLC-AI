# Merge tier scope

**Script:** `Tools/ci/check_independent_review.sh merge`

## Diff scope

`origin/main...HEAD` (all commits on branch).

## Checks (changed files only)

| Check | Enforce when `FARMRTK_ENFORCE_MERGE_CHECKS=1` |
|-------|-----------------------------------------------|
| Unknown `REQ:` ID in touched paths | FAIL |
| Broken relative markdown links | WARN |
| `cad-parts/*.md` frontmatter (`part_id`, `req`, `mechanical_id`) | WARN |
| `.scad` PARAMS BEGIN line 1 | FAIL |

## Invocation

```bash
FARMRTK_ENFORCE_MERGE_CHECKS=1 bash Tools/ci/check_independent_review.sh merge
```

Pre-push hook runs merge mode **without** enforce by default (advisory).