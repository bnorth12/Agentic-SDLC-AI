"""Procedural Skill Executor for the Agentic IDE platform (L2).

Parses SKILL.md (frontmatter + procedure steps), executes supported steps
(PowerShell via pwsh, Python fragments, or tool calls), and returns
structured evidence.

This is the initial minimal implementation per E1.1 / WAVE_01 plan.
Wires to OrchestrationRouter for PROCEDURAL mode.

Supports basic evidence capture for G1/G3/G4.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field

# Priority 1: Tool registry + declaration parser (L2/L4)
from ..tools.registry import get_registry, parse_declared_tools, parse_required_scopes  # type: ignore[attr-defined]


class SkillFrontmatter(BaseModel):
    name: str
    description: str | None = None
    agent: str | None = None
    gates: list[str] = Field(default_factory=list)
    maturity: str | None = None
    # Priority 1 tool registry integration (declaration model for permissions/scoping)
    tools: list[str] = Field(default_factory=list)
    required_scopes: list[str] = Field(default_factory=list)


class ExecutionEvidence(BaseModel):
    skill_id: str
    step_index: int
    step_type: str
    command_or_code: str
    stdout: str = ""
    stderr: str = ""
    returncode: int | None = None
    status: str = "success"  # success | error | skipped


class SkillExecutionResult(BaseModel):
    skill_id: str
    status: str  # success | partial | error
    evidence: list[ExecutionEvidence] = Field(default_factory=list)
    outputs: dict[str, Any] = Field(default_factory=dict)
    error: str | None = None


def parse_skill_md(skill_path: str | Path) -> tuple[SkillFrontmatter, str]:
    """Parse SKILL.md into frontmatter and body (simple YAML + markdown)."""
    path = Path(skill_path)
    if not path.exists():
        raise FileNotFoundError(f"SKILL.md not found: {path}")

    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        # Fallback: no frontmatter, treat whole as body with minimal frontmatter
        front = SkillFrontmatter(name=path.stem)
        body = content
    else:
        parts = content.split("---", 2)
        if len(parts) < 3:
            front = SkillFrontmatter(name=path.stem)
            body = content
        else:
            fm_text = parts[1].strip()
            body = parts[2].strip()
            fm_dict = yaml.safe_load(fm_text) or {}
            front = SkillFrontmatter(**fm_dict)

    return front, body


def _execute_powershell(command: str, cwd: str | None = None, timeout: int = 120, max_output: int = 8192) -> ExecutionEvidence:
    """Execute a PowerShell step using pwsh (Windows primary).

    P2 smallest slice (robust): added explicit TimeoutExpired handling + output truncation
    (prevents huge evidence blobs). Defaults preserve exact prior behavior.
    Future slices: env scoping, sandbox profile, duration, full tool registration.
    """
    try:
        result = subprocess.run(
            ["pwsh", "-NoProfile", "-Command", command],
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=timeout,
        )
        stdout = result.stdout or ""
        stderr = result.stderr or ""
        if len(stdout) > max_output:
            stdout = stdout[:max_output] + "\n... [truncated for evidence size]"
        if len(stderr) > max_output:
            stderr = stderr[:max_output] + "\n... [truncated for evidence size]"
        return ExecutionEvidence(
            skill_id="",
            step_index=0,
            step_type="pwsh",
            command_or_code=command,
            stdout=stdout,
            stderr=stderr,
            returncode=result.returncode,
            status="success" if result.returncode == 0 else "error",
        )
    except subprocess.TimeoutExpired:
        return ExecutionEvidence(
            skill_id="",
            step_index=0,
            step_type="pwsh",
            command_or_code=command,
            stderr=f"Timeout after {timeout}s",
            returncode=-1,
            status="timeout",
        )
    except Exception as e:
        return ExecutionEvidence(
            skill_id="",
            step_index=0,
            step_type="pwsh",
            command_or_code=command,
            stderr=str(e),
            returncode=-1,
            status="error",
        )


def run_robust_powershell(command: str, cwd: str | None = None, timeout: int = 120, max_output: int = 8192) -> ExecutionEvidence:
    """P2 smallest viable slice: public robust PowerShell execution surface.

    Thin wrapper over the hardened _execute_powershell.
    - Output truncation to keep evidence manageable
    - Explicit timeout status
    - Ready for env scoping / sandbox in next micro-slice

    Dual surface: Python (called from executor steps, agents, or via ToolRegistry)
    + PowerShell (via Invoke-IdeTool.ps1 or future GUI terminal integration).

    Traceable to L2-001 / TOOL rows in IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md
    and IDE_REFACTOR_PLAN §5 (L2 orchestration + tooling).
    """
    return _execute_powershell(command, cwd=cwd, timeout=timeout, max_output=max_output)


def _execute_python_fragment(code: str, cwd: str | None = None) -> ExecutionEvidence:
    """Execute a Python code fragment (captures print output)."""
    try:
        # Very basic: exec in isolated globals, capture stdout
        import io
        import contextlib

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exec_globals: dict[str, Any] = {"__name__": "__main__"}
            exec(code, exec_globals)

        stdout = output.getvalue()
        return ExecutionEvidence(
            skill_id="",
            step_index=0,
            step_type="python",
            command_or_code=code[:200] + ("..." if len(code) > 200 else ""),
            stdout=stdout,
            status="success",
        )
    except Exception as e:
        return ExecutionEvidence(
            skill_id="",
            step_index=0,
            step_type="python",
            command_or_code=code[:200] + ("..." if len(code) > 200 else ""),
            stderr=str(e),
            returncode=1,
            status="error",
        )


class ProceduralSkillExecutor:
    """Minimal procedural executor.

    Usage:
        executor = ProceduralSkillExecutor()
        result = executor.execute("plugins/packs/ide-platform/skills/ide-hierarchy-taxonomy-steward/SKILL.md")
    """

    def __init__(self, workspace_root: str | Path = "."):
        self.workspace_root = Path(workspace_root).resolve()

    def execute(self, skill_path: str | Path, payload: dict[str, Any] | None = None) -> SkillExecutionResult:
        """Execute a SKILL.md procedurally and return evidence."""
        skill_path = Path(skill_path)
        if not skill_path.is_absolute():
            skill_path = self.workspace_root / skill_path

        front, body = parse_skill_md(skill_path)
        skill_id = front.name

        evidence_list: list[ExecutionEvidence] = []
        outputs: dict[str, Any] = {"frontmatter": front.model_dump()}

        # Priority 1 tool registry integration: capture declarations from frontmatter for permission/scoping model
        # (SKILL authors declare in frontmatter; executor records for evidence/G1; registry will enforce in later batches)
        declared = parse_declared_tools(front) or getattr(front, "tools", []) or []
        req_scopes = parse_required_scopes(front) or getattr(front, "required_scopes", []) or []
        outputs["declared_tools"] = declared
        outputs["required_scopes"] = req_scopes
        if declared:
            outputs["tool_registry_available"] = True

        # Very simple step parser: look for ```pwsh or ```python blocks in Procedure section
        # This is a minimal first cut; real version would parse the full "Procedure" markdown list.
        import re

        # Find code blocks
        code_blocks = re.findall(r"```(pwsh|powershell|python)\n(.*?)```", body, re.DOTALL | re.IGNORECASE)

        for idx, (lang, code) in enumerate(code_blocks):
            code = code.strip()
            if not code:
                continue

            if lang.lower() in ("pwsh", "powershell"):
                ev = _execute_powershell(code, cwd=str(self.workspace_root))
            elif lang.lower() == "python":
                ev = _execute_python_fragment(code, cwd=str(self.workspace_root))
            else:
                ev = ExecutionEvidence(
                    skill_id=skill_id,
                    step_index=idx,
                    step_type=lang,
                    command_or_code=code[:100],
                    stderr="Unsupported language in this minimal executor",
                    status="skipped",
                )

            ev.skill_id = skill_id
            ev.step_index = idx
            evidence_list.append(ev)

            if ev.status == "error":
                break  # Stop on first error for minimal impl

        # Priority 1: lightweight "tool:" step support (inline in Procedure or comments)
        # Skills can write: tool: validate_hierarchy_metadata   (or in lists)
        # This produces step_type="tool" evidence and attempts registry invoke (no-arg or safe defaults for core tools).
        import re as _re_tool  # local to block
        tool_refs = _re_tool.findall(r"tool:\s*([a-zA-Z0-9_.-]+)", body, _re_tool.IGNORECASE)
        reg = None
        for t_idx, t_name in enumerate(dict.fromkeys(tool_refs)):  # dedup order
            if t_name not in (outputs.get("declared_tools") or []):
                # still allow for now (declaration is advisory in batch 1); future strict
                pass
            try:
                if reg is None:
                    reg = get_registry()
                # For batch 1 core tools we support a couple no/low-arg calls for smoke
                call_kwargs: dict[str, Any] = {}
                if t_name in ("validate_hierarchy_metadata", "read_ide_artifact"):
                    # point at a known good artifact in the pack for self-test
                    call_kwargs = {"artifact": "plugins/packs/ide-platform/skills/ide-hierarchy-taxonomy-steward/SKILL.md"}
                tool_result = reg.invoke(t_name, **call_kwargs) if reg else None
                tool_ev = ExecutionEvidence(
                    skill_id=skill_id,
                    step_index=len(evidence_list) + t_idx,
                    step_type="tool",
                    command_or_code=f"tool: {t_name}",
                    stdout=str(tool_result)[:1500] if tool_result is not None else "",
                    status="success",
                )
                evidence_list.append(tool_ev)
            except Exception as ex:
                err_ev = ExecutionEvidence(
                    skill_id=skill_id,
                    step_index=len(evidence_list) + t_idx,
                    step_type="tool",
                    command_or_code=f"tool: {t_name}",
                    stderr=str(ex)[:500],
                    returncode=1,
                    status="error",
                )
                evidence_list.append(err_ev)
                if any(e.status == "error" for e in evidence_list):
                    break

        overall_status = "success"
        if any(e.status == "error" for e in evidence_list):
            overall_status = "error"
        elif not evidence_list:
            overall_status = "partial"  # No executable steps found

        return SkillExecutionResult(
            skill_id=skill_id,
            status=overall_status,
            evidence=evidence_list,
            outputs=outputs,
            error=None if overall_status != "error" else "One or more steps failed",
        )


# Convenience for router
def run_procedural_skill(skill_id: str, payload: dict[str, Any] | None = None, workspace_root: str = ".") -> dict[str, Any]:
    """Entry point used by router for PROCEDURAL mode."""
    # Map skill_id to file path (simple convention for now)
    # In real version this would use L4 pack loader + manifest
    candidate_paths = [
        f"plugins/packs/ide-platform/skills/{skill_id}/SKILL.md",
        f"platform/skills/{skill_id}/SKILL.md",
    ]

    executor = ProceduralSkillExecutor(workspace_root=workspace_root)
    for p in candidate_paths:
        try:
            result = executor.execute(p, payload)
            return result.model_dump()
        except FileNotFoundError:
            continue

    return {
        "skill_id": skill_id,
        "status": "error",
        "error": f"SKILL.md not found for {skill_id} in known locations",
    }
