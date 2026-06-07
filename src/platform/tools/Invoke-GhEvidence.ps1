<#
.SYNOPSIS
  PS wrapper for gh CLI / GitHub Evidence Tool (P4 slice 2).

.DESCRIPTION
  Exposes the Python gh_evidence tool (src/platform/tools/gh_evidence.py) to PowerShell
  for current PS-MVP and future custom GUI integrated terminal (PS integration supported).

  Supports evidence actions: create-issue, attach (comment + file refs), comment.
  Evidence schema: action, target (#123), title, body/body_file, labels, files.
  Reliable (auth precheck in backend).

  Dual with Python gh_evidence / registry 'gh_evidence'.
  Complements Discover-IdePack.ps1, Run-RobustPwsh.ps1, Invoke-IdeTool.ps1.

.EXAMPLE
  pwsh -File src/platform/tools/Invoke-GhEvidence.ps1 -Action create-issue `
       -Title "P4 evidence test" -Body "See attached trace." -Labels "evidence,g1" `
       -Files "evidence/trace.md"

  # Attach to existing
  & "$PSScriptRoot/Invoke-GhEvidence.ps1" -Action attach -Target "#42" -Files "evidence/bundle.zip"
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Action,

    [string]$Target,

    [string]$Title,

    [string]$Body,

    [string]$BodyFile,

    [string]$Labels,  # comma sep

    [string]$Files,   # comma sep or json?

    [string]$PythonExe = 'python'
)

$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Resolve-Path (Join-Path $here '..\..\..\..')).Path

$pyCode = @'
import sys, json
sys.path.insert(0, r"'" + $repoRoot + r'"')
from src.platform.tools.gh_evidence import gh_evidence
action = sys.argv[1]
target = sys.argv[2] if len(sys.argv) > 2 else None
title = sys.argv[3] if len(sys.argv) > 3 else None
body = sys.argv[4] if len(sys.argv) > 4 else None
body_file = sys.argv[5] if len(sys.argv) > 5 else None
labels = sys.argv[6].split(",") if len(sys.argv) > 6 and sys.argv[6] else None
files = sys.argv[7].split(",") if len(sys.argv) > 7 and sys.argv[7] else None
try:
    res = gh_evidence(action, target=target, title=title, body=body, body_file=body_file, labels=labels, files=files)
    print(json.dumps(res, indent=2))
except Exception as e:
    print(json.dumps({"status": "error", "error": str(e)}, indent=2))
'@
$tmpPy = Join-Path $env:TEMP "invoke_gh_evidence_$(Get-Random).py"
Set-Content -Path $tmpPy -Value $pyCode -Encoding UTF8

try {
    & $PythonExe $tmpPy $Action $Target $Title $Body $BodyFile $Labels $Files
    if ($LASTEXITCODE -ne 0) { throw "gh evidence invoke failed (exit $LASTEXITCODE)" }
} finally {
    Remove-Item $tmpPy -ErrorAction SilentlyContinue | Out-Null
}
