<#
.SYNOPSIS
  Dedicated PowerShell wrapper for the robust pwsh execution tool (P2 conclusion).

.DESCRIPTION
  Provides a first-class PS surface for running PowerShell steps with the platform's
  robust features (truncation, explicit timeouts, env scoping, basic sandbox notes).
  Intended for SKILL.md procedures, direct use in PS-MVP, and future custom GUI
  integrated terminal (which supports PS integration).

  This complements Invoke-IdeTool.ps1 (general registry) with a specialized robust-pwsh
  entrypoint. Dual with the Python run_robust_powershell (exposed in ToolRegistry).

  Sandbox notes: -NoProfile enforced in backend; env is caller-controlled (safe merge);
  only use with reviewed commands; full policy-restricted sandbox in future slices.

.EXAMPLE
  pwsh -File src/platform/tools/Run-RobustPwsh.ps1 -Command "Write-Output 'P2 real step'" -EnvJson '{"P2_VAR":"value"}'

  # From within a skill procedure (future runner will surface robust by default)
  & "$PSScriptRoot/Run-RobustPwsh.ps1" -Command "Get-Location" -Timeout 30 -MaxOutput 4096
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Command,

    [string]$Cwd = ".",

    [int]$Timeout = 120,

    [int]$MaxOutput = 8192,

    [string]$EnvJson = '{}',

    [string]$PythonExe = 'python'
)

$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Resolve-Path (Join-Path $here '..\..\..\..')).Path

$pyCode = @'
import sys, json, os
sys.path.insert(0, r"'" + $repoRoot + r'"')
from src.platform.orchestration.executor import run_robust_powershell
cmd = sys.argv[1]
cwd = sys.argv[2]
timeout = int(sys.argv[3])
max_out = int(sys.argv[4])
env = json.loads(sys.argv[5]) if len(sys.argv) > 5 else None
try:
    ev = run_robust_powershell(cmd, cwd=cwd, timeout=timeout, max_output=max_out, env=env)
    res = {
        "status": ev.status,
        "stdout": ev.stdout,
        "stderr": ev.stderr,
        "returncode": ev.returncode,
        "truncated": "truncated" in (ev.stdout or "") or "truncated" in (ev.stderr or "")
    }
    print(json.dumps(res, indent=2))
except Exception as e:
    print(json.dumps({"status": "error", "error": str(e)}, indent=2))
'@

$tmpPy = Join-Path $env:TEMP "run_robust_pwsh_$(Get-Random).py"
Set-Content -Path $tmpPy -Value $pyCode -Encoding UTF8

try {
    & $PythonExe $tmpPy $Command $Cwd $Timeout $MaxOutput $EnvJson
    if ($LASTEXITCODE -ne 0) { throw "robust pwsh failed (exit $LASTEXITCODE)" }
} finally {
    Remove-Item $tmpPy -ErrorAction SilentlyContinue | Out-Null
}
