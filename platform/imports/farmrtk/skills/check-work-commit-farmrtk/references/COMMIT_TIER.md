# Commit-tier scope

| Check | Severity at M1 |
|-------|----------------|
| Orphan REQ/TC in **staged** files | warn |
| Broken relative links in changed `.md` | warn |
| `cad-parts/` MD missing frontmatter | warn |
| `.scad` PARAMS not line 1 | warn |
| Maturity note for empty matrices elsewhere | info |

Reports: `.farmrtk/reviews/commit-<timestamp>.md` (gitignored)