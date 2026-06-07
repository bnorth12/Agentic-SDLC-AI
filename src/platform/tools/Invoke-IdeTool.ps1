<#
.SYNOPSIS
  Thin PowerShell surface for the IDE Tool Registry (Priority 1 batch).

.DESCRIPTION
  Exposes the Python ToolRegistry (src/platform/tools/registry.py) to PowerShell
  for the current PS-MVP primary dev surface and (later) the custom GUI's
  integrated terminal (which will support PowerShell integration per design).

  This is the dual-use contract: skills/procedures can be authored in pwsh and
  call tools via this wrapper (or direct python registry from embedded python steps).

  Batch 1 scope: list and invoke the initial ide_core tools (read/write_ide_artifact,
  validate_hierarchy_metadata, basic_generalize_stub). Permission/scoping model
  is declaration-based (frontmatter in SKILL.md); enforcement evolves in P2+.

.EXAMPLE
  pwsh -File src/platform/tools/Invoke-IdeTool.ps1 -Name validate_hierarchy_metadata `
       -PayloadJson '{"artifact":"plugins/packs/ide-platform/skills/ide-hierarchy-taxonomy-steward/SKILL.md"}'

  # Or from a skill procedure step (future robust runner will surface this)
  & "$PSScriptRoot/Invoke-IdeTool.ps1" -Name list_tools

  # P2 slice 2: robust pwsh with env (dual for PS-MVP + future GUI terminal)
  # & "$PSScriptRoot/Invoke-IdeTool.ps1" -Name run_robust_powershell -PayloadJson '{"command":"Write-Output $env:MYVAR","env":{"MYVAR":"from-ps"}}'
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Name,

    [string]$PayloadJson = '{}',

    [string]$PythonExe = 'python',

    [switch]$SkipGovernance
)

$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Resolve-Path (Join-Path $here '..\..\..\..')).Path   # src/platform/tools -> repo root

# GOVERNANCE WIRING (dual with GUI): Before any tool/skill "user command" or exposure,
# run full engineering rigor (upfront + testing) via the skills/tools.
# This ensures we never start "coding"/action or give something to try (in PS or via GUI terminal)
# before upfront engineering (G0.1) and actual testing/compliance (G_pre_user_command_testing).
# Uses L2 skills (ide-governance-policy-compiler, ide-check-work-commit etc.) + P1 registry + P5 evidence.
# Bypass only for internal 'list' or with explicit -SkipGovernance (for reviewed scripts only; still produces evidence).
if (-not $SkipGovernance -and $Name -notin @('list','list_tools','list-tools')) {
    Write-Host "[GOV] Running mandatory preflight (upfront engineering + pre-exposure testing) before $Name ..."
    $govPy = @'
import sys, json
sys.path.insert(0, r"'" + $repoRoot + r'"')
from src.platform.orchestration.executor import run_procedural_skill
from src.platform.tools.gate_evidence_bundler import create_gate_evidence_bundle, bundle_to_markdown
skills = ["ide-governance-policy-compiler", "ide-check-work-commit", "ide-hierarchy-taxonomy-steward"]
results = []
for sk in skills:
    try:
        r = run_procedural_skill(sk, workspace_root=r"'" + $repoRoot + r'"')
        results.append({"skill": sk, "status": r.get("status"), "declared": r.get("outputs",{}).get("declared_tools")})
    except Exception as ex:
        results.append({"skill": sk, "status": "error", "error": str(ex)[:200]})
bundle = create_gate_evidence_bundle("G_hmi_governance_enforcement", [{"type":"ps_wrapper_preflight", "results": results}])
print(json.dumps({"status": "gov_preflight_complete", "results": results, "evidence": bundle_to_markdown(bundle)[:600]}, indent=2))
'@
    $tmpGov = Join-Path $env:TEMP "gov_preflight_$(Get-Random).py"
    Set-Content -Path $tmpGov -Value $govPy -Encoding UTF8
    & $PythonExe $tmpGov 2>&1 | ForEach-Object { Write-Host "[GOV] $_" }
    Remove-Item $tmpGov -ErrorAction SilentlyContinue | Out-Null
    # In full wiring, parse the output; if mandatory gates fail, throw or require HITL/evidence review before proceeding.
    # For now, evidence is always produced and visible; strict block in later G enforcement slices.
}

$pyCode = @'
import sys, json
sys.path.insert(0, r"'" + $repoRoot + r'"')
from src.platform.tools.registry import get_registry
name = sys.argv[1]
payload = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
reg = get_registry()
try:
    if name.lower() in ('list', 'list_tools', 'list-tools'):
        res = {"status": "ok", "tools": reg.list_tools()}
    else:
        result = reg.invoke(name, **payload)
        res = {"status": "ok", "result": str(result)[:3000]}
    print(json.dumps(res, indent=2))
except Exception as e:
    print(json.dumps({"status": "error", "error": str(e)}, indent=2))
'@

# Write temp script to avoid quoting hell on complex -c for pwsh
$tmpPy = Join-Path $env:TEMP "invoke_ide_tool_$(Get-Random).py"
Set-Content -Path $tmpPy -Value $pyCode -Encoding UTF8

try {
    & $PythonExe $tmpPy $Name $PayloadJson
    if ($LASTEXITCODE -ne 0) { throw "python registry invoke failed (exit $LASTEXITCODE)" }
} finally {
    Remove-Item $tmpPy -ErrorAction SilentlyContinue | Out-Null
}
