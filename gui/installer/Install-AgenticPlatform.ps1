# Agentic SDLC AI — platform bootstrap (scaffold)
param(
    [ValidateSet("minimal", "full")]
    [string]$Profile = "minimal"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
Write-Host "Agentic-SDLC-AI platform installer (scaffold)"
Write-Host "Root: $Root"
Write-Host "Profile: $Profile"
Write-Host ""
Write-Host "Prerequisites (manual until R6):"
Write-Host "  1. Zed Personal — https://zed.dev/download"
Write-Host "  2. Grok Build CLI — authenticated"
Write-Host "  3. Python 3.11+ — for platform CLI"
Write-Host ""
Write-Host "Zed settings snippet: gui/shell/zed-agent-servers.json"
Write-Host "Workspace template: workspace/templates/example-farmrtk.workspace.yaml"
if ($Profile -eq "full") {
    Write-Host "Installing Python package editable..."
    Push-Location $Root
    pip install -e ".[dev]" 2>$null
    Pop-Location
}
Write-Host "Done (scaffold). See docs/charter/REBOOT_CHARTER.md"