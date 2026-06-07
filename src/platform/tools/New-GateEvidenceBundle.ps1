<#
.SYNOPSIS
  PS wrapper for Gate Evidence Bundler (P5 slice 2).

.DESCRIPTION
  Exposes the Python gate_evidence_bundler (src/platform/tools/gate_evidence_bundler.py) to PowerShell
  for PS-MVP terminal and future custom GUI integrated terminal (supports PS integration).

  Takes sources (JSON array of exec/gh results) and produces bundle (dict/md/json) for G1/G3/G4.
  Dual with Python 'bundle_gate_evidence' in registry.

  Complements Invoke-GhEvidence.ps1, Discover-IdePack.ps1, Run-RobustPwsh.ps1.

.EXAMPLE
  $sources = '[{"type":"skill_execution","id":"ide-foo","result":{"status":"success","evidence":[{"step_type":"pwsh","status":"success"}]}}]'
  pwsh -File src/platform/tools/New-GateEvidenceBundle.ps1 -GateId G4_independent_review -SourcesJson $sources -Format md
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$GateId,

    [Parameter(Mandatory = $true)]
    [string]$SourcesJson,

    [string]$Format = "json",  # json | md
    [string]$PythonExe = "python"
)

$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Resolve-Path (Join-Path $here "..\..\..\..")).Path

$pyCode = @'
import sys, json
sys.path.insert(0, r"'" + $repoRoot + r'"')
from src.platform.tools.gate_evidence_bundler import create_gate_evidence_bundle, bundle_to_markdown, bundle_to_json
gate_id = sys.argv[1]
sources = json.loads(sys.argv[2])
bundle = create_gate_evidence_bundle(gate_id, sources)
if sys.argv[3] == "md":
    print(bundle_to_markdown(bundle))
else:
    print(bundle_to_json(bundle))
'@
$tmpPy = Join-Path $env:TEMP "new_gate_evidence_bundle_$(Get-Random).py"
Set-Content -Path $tmpPy -Value $pyCode -Encoding UTF8

try {
    & $PythonExe $tmpPy $GateId $SourcesJson $Format
    if ($LASTEXITCODE -ne 0) { throw "gate evidence bundle failed (exit $LASTEXITCODE)" }
} finally {
    Remove-Item $tmpPy -ErrorAction SilentlyContinue | Out-Null
}
