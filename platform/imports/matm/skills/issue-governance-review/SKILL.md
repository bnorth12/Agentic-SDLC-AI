---
name: issue-governance-review
description: "Audit sprint issue tracker quality for requirement linkage and GitHub issue reference consistency using local repository evidence."
---
# Issue Governance Review Skill

## Purpose
Validate local sprint governance documentation quality and GitHub-link consistency from local artifacts.

## Checks
1. Every parsed sprint issue row has an issue ID.
2. Every active/proposed/in-review row should include requirement IDs.
3. Every row should include a GitHub issue reference token or URL.
4. Status values should be explicit and auditable.

## Data Sources
- planning/issues/Sprint_*_Issue_Tracker.md
- planning/issues/issue_*.md

## Execution
Use the main independent review script and read issue-focused sections in the report.
