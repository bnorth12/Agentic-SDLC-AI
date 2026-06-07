"""GitHub Evidence Tool (P4 slice 1+).

Reliable gh CLI wrapper for evidence attachment (issues, PRs, comments, files).
- Auth check first.
- Basic commands: create issue/PR note, attach file as comment or release asset, etc.
- Evidence schema: dict with {type, target (issue# or pr#), title, body, files, labels, ...}
- Returns structured result like ExecutionEvidence (status, stdout, etc.).
- Dual: Python (for executor/tools/registry) + PS wrappers.
- Traceable to TOOL-001, L2/L4, §5, matrix.

Future: more schema, sandboxed gh (limited scopes), integration with gates/evidence bundles.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any

import yaml  # for schema if needed later


def _run_gh(args: list[str], cwd: str | None = None, timeout: int = 60) -> dict[str, Any]:
    """Internal: run gh with list args, return structured result."""
    try:
        # Pre-check auth for reliability
        auth_result = subprocess.run(
            ["gh", "auth", "status"],
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=10,
        )
        if auth_result.returncode != 0:
            return {
                "status": "error",
                "stdout": auth_result.stdout,
                "stderr": "gh auth failed: " + auth_result.stderr,
                "returncode": auth_result.returncode,
                "command": "gh auth status",
            }

        result = subprocess.run(
            ["gh"] + args,
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=timeout,
        )
        return {
            "status": "success" if result.returncode == 0 else "error",
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
            "command": "gh " + " ".join(args),
        }
    except FileNotFoundError:
        return {
            "status": "error",
            "stderr": "gh CLI not found in PATH. Install from https://cli.github.com/",
            "returncode": -1,
            "command": "gh " + " ".join(args),
        }
    except subprocess.TimeoutExpired:
        return {
            "status": "timeout",
            "stderr": f"gh command timed out after {timeout}s",
            "returncode": -1,
            "command": "gh " + " ".join(args),
        }
    except Exception as e:
        return {
            "status": "error",
            "stderr": str(e),
            "returncode": -1,
            "command": "gh " + " ".join(args),
        }


def gh_evidence(action: str, target: str | None = None, title: str | None = None, body: str | None = None, body_file: str | None = None, labels: list[str] | None = None, files: list[str] | None = None, cwd: str | None = None, **kwargs) -> dict[str, Any]:
    """P4: GitHub Evidence Tool entrypoint.

    action: 'create-issue', 'create-pr-note', 'attach', 'comment'
    target: e.g. 'owner/repo#123' or just '#123' (assumes current repo)
    title, body, body_file, labels, files: for evidence attachment.
    Returns dict with status, stdout/stderr, etc. (compatible with ExecutionEvidence).

    Examples (via registry or direct):
    - gh_evidence('create-issue', title='Evidence: foo', body='...', labels=['evidence'])
    - gh_evidence('attach', target='#42', files=['evidence/foo.md'])
    """
    args = []
    if action == "create-issue":
        args = ["issue", "create"]
        if title:
            args += ["--title", title]
        if body:
            args += ["--body", body]
        if body_file:
            args += ["--body-file", body_file]
        if labels:
            args += ["--label", ",".join(labels)]
    elif action in ("create-pr-note", "comment"):
        if not target:
            return {"status": "error", "stderr": "target (e.g. #123) required for comment"}
        args = ["issue", "comment", target]
        if body:
            args += ["--body", body]
        if body_file:
            args += ["--body-file", body_file]
    elif action == "attach":
        if not target:
            return {"status": "error", "stderr": "target required for attach"}
        # Use comment for attach evidence; for real files use gh release or pr edit if needed.
        # For simplicity: comment with file mention + attach if release.
        args = ["issue", "comment", target]
        body_content = body or ""
        if files:
            for f in files:
                body_content += f"\n\nEvidence attached: {f}"
            # Note: gh doesn't auto-attach binary in comment easily; use --body-file or external.
            # For evidence, often body_file with markdown links or use `gh pr review` etc.
        if body_content:
            args += ["--body", body_content.strip()]
    else:
        # Fallback: raw gh subcommand support for flexibility (e.g. action="pr", args=["create", ...] but via kwargs)
        args = [action] + (kwargs.get("gh_args", []) if isinstance(kwargs.get("gh_args"), list) else [])

    # Add files handling for attach if possible (e.g. for releases)
    if files and action == "attach":
        # Extend for release upload as example evidence bundle
        # For now, log in body; real attach may use gh release upload in future slice.
        pass

    return _run_gh(args, cwd=cwd)


# For registry exposure
GH_EVIDENCE_TOOL = gh_evidence

# Simple evidence schema helper (for docs/tests)
def evidence_schema_example() -> dict:
    return {
        "type": "gh-evidence",
        "target": "owner/repo#123",
        "title": "Evidence bundle for X",
        "body": "See attached...",
        "files": ["evidence/trace.md"],
        "labels": ["evidence", "g1"],
    }
