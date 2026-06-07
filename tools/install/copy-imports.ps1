# One-time import copy from FarmRTK + MATM (platform reboot scaffold)
$Root = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$fr = "C:\Users\brian\OneDrive\Documents\GitHubRepos\FarmRTK\.grok\skills"
$matm = "C:\Users\brian\OneDrive\Documents\GitHubRepos\Multi Agent Threat Modeler"

$platformSkills = @(
    "orchestrate-farmrtk", "independent-review-farmrtk", "check-work-commit-farmrtk",
    "traceability-audit-farmrtk", "program-metrics-farmrtk", "requirements-management-farmrtk",
    "test-authoring-farmrtk", "configuration-baseline-farmrtk", "icd-maintenance-farmrtk",
    "decision-record-farmrtk", "repo-audit-farmrtk", "validation-plan-farmrtk",
    "risk-register-farmrtk", "process-audit-farmrtk", "technical-writer-farmrtk",
    "data-storage-farmrtk", "bom-procurement-farmrtk"
)
$domainSkills = @(
    "OpenSCAD-Parametric-FarmRTK", "firmware-build-farmrtk", "integration-bench-farmrtk",
    "electronics-wiring-farmrtk", "rf-antenna-farmrtk"
)

$dstPlatform = Join-Path $Root "platform\imports\farmrtk\skills"
$dstEng = Join-Path $Root "plugins\packs\engineering-sdlc\imports"
New-Item -ItemType Directory -Force -Path $dstPlatform, $dstEng | Out-Null

foreach ($s in $platformSkills) {
    Copy-Item -Recurse -Force (Join-Path $fr $s) (Join-Path $dstPlatform $s)
}
foreach ($s in $domainSkills) {
    Copy-Item -Recurse -Force (Join-Path $fr $s) (Join-Path $dstEng $s)
}

$dstMatmSkills = Join-Path $Root "platform\imports\matm\skills"
$dstMatmAgents = Join-Path $Root "platform\imports\matm\agents"
New-Item -ItemType Directory -Force -Path $dstMatmSkills, $dstMatmAgents | Out-Null
Copy-Item -Recurse -Force (Join-Path $matm ".github\skills\*") $dstMatmSkills
Copy-Item -Recurse -Force (Join-Path $matm ".github\agents\*") $dstMatmAgents

Write-Host "Import copy complete."