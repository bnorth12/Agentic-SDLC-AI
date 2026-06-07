<#
.SYNOPSIS
  PS discovery helper for packs, skills, and declared tools (P3 conclusion).

.DESCRIPTION
  First-class PS surface to discover via the L4 PluginLoader (manifest-driven).
  Lists packs, their skills (from entry.skills_dir), and declared_tools (from SKILL frontmatter).
  Dual with Python loader.discover() / discover_skills().
  For PS-MVP terminal, future GUI command palette / explorer, and scripts.

  Complements Run-RobustPwsh / Invoke-IdeTool.

.EXAMPLE
  pwsh -File src/platform/tools/Discover-IdePack.ps1 -Pack ide-platform

  # List all + tools
  & "$PSScriptRoot/Discover-IdePack.ps1"
#>
[CmdletBinding()]
param(
    [string]$Pack,
    [string]$PythonExe = 'python'
)

$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Resolve-Path (Join-Path $here '..\..\..\..')).Path

$pyCode = @'
import sys, json
sys.path.insert(0, r"'" + $repoRoot + r'"')
from src.platform.plugins.loader import PluginLoader
loader = PluginLoader()
packs = [{"id": p.id, "name": p.name, "path": str(p.path)} for p in loader.discover()]
skills = loader.discover_skills()
if sys.argv[1]:
    pfilter = sys.argv[1]
    packs = [p for p in packs if p["id"] == pfilter]
    skills = [s for s in skills if s["pack_id"] == pfilter]
res = {
    "packs": packs,
    "skills": [{"id": s["id"], "pack": s["pack_id"], "tools": s["declared_tools"], "path": s["path"]} for s in skills]
}
print(json.dumps(res, indent=2))
'@
$tmpPy = Join-Path $env:TEMP "discover_ide_pack_$(Get-Random).py"
Set-Content -Path $tmpPy -Value $pyCode -Encoding UTF8

try {
    & $PythonExe $tmpPy $Pack
    if ($LASTEXITCODE -ne 0) { throw "discovery failed (exit $LASTEXITCODE)" }
} finally {
    Remove-Item $tmpPy -ErrorAction SilentlyContinue | Out-Null
}
