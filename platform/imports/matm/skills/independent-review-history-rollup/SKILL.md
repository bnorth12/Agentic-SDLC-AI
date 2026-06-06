---
name: independent-review-history-rollup
description: "Roll up stale independent review outputs from latest into history and keep the latest set canonical."
---
# Independent Review History Rollup Skill

## Purpose

Archive superseded independent review artifacts from `independent_reviews/latest/` into `independent_reviews/history/reports/` so the active workspace only retains the canonical review outputs.

## Inputs

- Independent review outputs under `independent_reviews/latest/`
- Archived batches under `independent_reviews/history/reports/by_context/`
- History compaction manifests and summaries

## Procedure

- Identify stale or superseded latest review artifacts.
- Move them into the appropriate history batch for the active run context.
- Compact older auto-compaction batches while preserving the configured retention window.
- Confirm the latest folder remains focused on the canonical review pair and embedded appendices.

## Outputs

- Latest-output cleanup summary.
- History batch archive path(s).
- Updated compaction summary for the active run context.
