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

    [string]$PythonExe = 'python'
)

$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Resolve-Path (Join-Path $here '..\..\..\..')).Path   # src/platform/tools -> repo root

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
