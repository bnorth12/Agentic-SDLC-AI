# Sync Markdown params block into a single-part .scad file.
# Layout: Hardware/cad-parts/<PartId>/<PartId>.md + <PartId>.scad
# Enforces CUSTOMIZER_LAYOUT.md: PARAMS BEGIN must be line 1 (moves header below END).
param(
    [Parameter(Mandatory = $true)]
    [string]$PartFile,
    [string]$ScadFile = ""
)

$ErrorActionPreference = "Stop"
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..\..\..")
$partPath = Resolve-Path $PartFile
$partDir = Split-Path $partPath -Parent
$content = Get-Content -Raw -Path $partPath

$partId = "Unknown"
if ($content -match '(?ms)^---\s*\r?\n(.*?)\r?\n---') {
    $fm = $Matches[1]
    if ($fm -match 'part_id:\s*(\S+)') { $partId = $Matches[1] }
}

if ($content -notmatch '(?ms)```params\s*\r?\n(.*?)```') {
    Write-Error "No ```params block in $PartFile"
}
$block = $Matches[1]

$paramLines = New-Object System.Collections.Generic.List[string]
$null = $paramLines.Add("// AUTO-SYNCED from $partPath")
$null = $paramLines.Add("// part_id: $partId - edit $partId.md then re-run parse_cad_params.ps1")
$null = $paramLines.Add("")

foreach ($raw in ($block -split "`r?`n")) {
    $line = $raw.Trim()
    if ($line -eq "" -or $line.StartsWith("//")) { continue }

    if ($line -match '^#\s*group\s+(.+)$') {
        $null = $paramLines.Add("/* [$($Matches[1].Trim())] */")
        continue
    }

    if ($line -match '^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+)$') {
        $key = $Matches[1]
        $rest = $Matches[2]
        if ($rest -match '^(.+?)\s*//\s*(.+)$') {
            $val = $Matches[1].TrimEnd(';').Trim()
            $comment = $Matches[2].Trim()
            $null = $paramLines.Add("${key} = ${val}; // ${comment}")
        } else {
            $val = $rest.TrimEnd(';').Trim()
            $null = $paramLines.Add("${key} = ${val};")
        }
    }
}

$begin = "// [FarmRTK PARAMS BEGIN]"
$end = "// [FarmRTK PARAMS END]"
$paramsBlock = ($paramLines -join "`n")

if (-not $ScadFile) {
    $ScadFile = Join-Path $partDir ($partId + ".scad")
}
$scadPath = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($ScadFile)

$templateScad = Join-Path $PSScriptRoot "..\templates\part.scad"
if (-not (Test-Path $scadPath)) {
    if (-not (Test-Path $templateScad)) {
        Write-Error "SCAD not found ($scadPath) and no template at $templateScad"
    }
    $stub = Get-Content -Raw -Path $templateScad
    $stub = $stub -replace '@part_id@', $partId
    $stub = $stub -replace '@param_source@', $partPath
    $stub = $stub -replace '@mechanical_id@', 'M-XX'
    $stub = $stub -replace '@req@', 'SYS-REQ-006'
    $newBlock = "$begin`n$paramsBlock`n$end"
    if ($stub -match '(?s)// \[FarmRTK PARAMS BEGIN\].*?// \[FarmRTK PARAMS END\]') {
        $stub = $stub -replace '(?s)// \[FarmRTK PARAMS BEGIN\].*?// \[FarmRTK PARAMS END\]', $newBlock
    } else {
        $stub = "$stub`n$newBlock`n"
    }
    New-Item -ItemType Directory -Force -Path (Split-Path $scadPath -Parent) | Out-Null
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($scadPath, $stub, $utf8NoBom)
    Write-Host "Created $scadPath from template ($($paramLines.Count) param lines)"
    exit 0
}

$scadContent = Get-Content -Raw -Path $scadPath
$newBlock = "$begin`n$paramsBlock`n$end"
if ($scadContent -match '(?s)// \[FarmRTK PARAMS BEGIN\].*?// \[FarmRTK PARAMS END\]') {
    $scadContent = $scadContent -replace '(?s)// \[FarmRTK PARAMS BEGIN\].*?// \[FarmRTK PARAMS END\]', $newBlock
} else {
    Write-Error "Missing $begin / $end markers in $scadPath - add markers or scaffold with init_cad_part.ps1"
}

# OpenSCAD Customizer (2021.01): parameters must be first lines in file
if ($scadContent -match '(?s)^(.*?)// \[FarmRTK PARAMS BEGIN\].*?// \[FarmRTK PARAMS END\]([\s\S]*)$') {
    $headerBefore = $Matches[1].TrimEnd()
    $bodyAfter = $Matches[2].TrimStart()
    if ($headerBefore) {
        $scadContent = "$newBlock`n`n$headerBefore`n`n$bodyAfter"
    }
}

$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($scadPath, $scadContent, $utf8NoBom)
Write-Host "Synced params into $scadPath ($($paramLines.Count) lines)"