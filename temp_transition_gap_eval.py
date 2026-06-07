#!/usr/bin/env python
"""Self-hosted evaluation of gaps for PS-to-IDE transition and overall IDE application.
Uses L2 skills + P1 tools as required by the project rules.
Focus: document what basic functionality exists today (acceptable for transition even with stubs/TODOs),
identify gaps in traceability (matrix), governance enforcement, documentation for move from PS-primary to IDE-primary dev.
"""
import sys
from pathlib import Path
ROOT = Path(".").resolve()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.platform.orchestration.executor import run_procedural_skill
from src.platform.tools.registry import get_registry

print("=" * 70)
print("PS-to-IDE TRANSITION + OVERALL IDE APPLICATION GAP EVALUATION")
print("Using skills (ide-verification-coverage, ide-source-to-evidence-traceability,")
print("ide-governance-policy-compiler, ide-hierarchy-taxonomy-steward) + P1 registry tools.")
print("Goal: Ensure skills/tools represented; catalog basic functionality for self-host transition;")
print("document gaps so transition is well-documented/tested when ready.")
print("=" * 70)

reg = get_registry()
print("\n## P1 Tools Available (for dual PS/GUI and transition work)")
print("  " + ", ".join(reg.list_tools()))

print("\n## Running Governance/Trace/Verification Skills for Gap Analysis")
skills = [
    "ide-verification-coverage",
    "ide-source-to-evidence-traceability",
    "ide-governance-policy-compiler",
    "ide-hierarchy-taxonomy-steward",
]
for sk in skills:
    try:
        r = run_procedural_skill(sk, workspace_root=".")
        outs = r.get("outputs", {})
        print(f"\n{sk}:")
        print(f"  status: {r.get('status')}")
        print(f"  declared_tools: {outs.get('declared_tools')}")
        print(f"  required_scopes: {outs.get('required_scopes')}")
        print(f"  tool_registry_available: {outs.get('tool_registry_available')}")
    except Exception as e:
        print(f"\n{sk}: error during execution - {str(e)[:120]} (partial run still provides frontmatter/declared)")

print("\n## Ground Truth Basic Functionality (CUSTOM GUI + PS Dual - Acceptable for Transition)")
print("From code inspection + self-host demo:")
print("  - Launch: .\\.venv\\Scripts\\python.exe -m src.platform.gui.launch_ide (Win11, stdlib tkinter, no extra deps)")
print("  - Menu (primary controls): File Open/Close Folder (L4 reload), GitHub (P4 gh_evidence), Grok/Build (ACP launch + L2 handoff + Open PS with context), Help (full UI Legend for all stubs)")
print("  - Dockables: ttk.PanedWindow (explorer | center: editor + viewers + PS terminal as first-class tool)")
print("  - Explorer (L4): Tree from PluginLoader, packs/skills, select loads real SKILL.md, Invoke runs L2 + P5 bundle")
print("  - Command Palette (Ctrl+P): lists skills + actions, dispatches real L2 invokes")
print("  - Editor: real SKILL load (stub for full structure-aware edit/save)")
print("  - Viewers: P5 bundle display (stub for rich markdown/mermaid/etc.)")
print("  - ACP Panel: full JSON protocol (system context for opened workspace + user messages), preflight gov before send/handoff, real L2 handoff button, stub fallback when no grok CLI")
print("  - Governance Preflight (wired in GUI + PS Invoke-IdeTool): runs ide-gov-*, ide-check-work-*, hierarchy before user actions/exposure; produces P5 evidence; surfaces in viewers/status (evidence today, strict block future)")
print("  - PS Dual: All P1-P5 have PS wrappers; 'Open PowerShell with IDE Context' menu; robust pwsh in terminal pane")
print("  - Self-host demo: Open this repo -> L4 shows ide-* -> invoke generalized skill via L2 -> P5 bundle visible")
print("  - Status/Gates: Shows active gates, P1-P5 ready, self-host note")
print("Stubs/TODOs explicitly called out in UI Legend and code (acceptable for basic functionality):")
print("  - Editor: stub (real load + invoke; full structure-aware future)")
print("  - Viewers: partial (P5 bundles work; rich viewers R2+)")
print("  - ACP: stub mode when no CLI; 'stub vs procedural' menu item; preflight is evidence+visibility (not hard block yet)")
print("  - Future: Tauri/Dear PyGui evolution, full multi-agent, rich editors")

print("\n## Identified Gaps for Overall IDE Application (to be documented in matrix/invocation/GUI_DESIGN)")
gaps = [
    "PS-to-IDE Transition Plan: No dedicated artifact/section cataloging migration steps, testing criteria, or 'when basic functionality is sufficient'. Current is parallel PS-primary + GUI MVP.",
    "Matrix Ground Truth Drift (recurring): Recent GOV wiring + HMI preflights + dual enforcement are in X GOV-WIRING-001 and expanded L0-001, but verification columns and child rows for 'interface enforcement as transition enabler' and 'basic functionality baseline' are still narrative-heavy rather than fully decomposed.",
    "Governance Enforcement Maturity: Preflights always run and produce evidence (good for 'never before testing'), but still 'future strict enforcement' / 'HITL in future' / evidence-only today. Not yet hard-blocking on G0.1/G_pre for all paths.",
    "L2 Executor Gaps for IDE Dev: Does not yet auto-run declared governance gates from SKILL frontmatter before user-invoked procedures. Manual preflight in interfaces only.",
    "Stub Documentation for Transition: Good in UI Legend + GUI_DESIGN 2.6, but no single 'IDE Basic Functionality Catalog for Self-Host Transition' that lists exactly what a developer can rely on today (menu/dockables/L2 invokes/gov preflight/ACP/PS context) vs. what is stub (editor full edit, rich viewers, hard gov blocks).",
    "Testing for Transition: phase1_batch1_smoke covers core, but no dedicated 'transition smoke' or 'IDE self-host regression' that exercises the full path a dev would use when moving work into the IDE.",
    "Skills/Tools Representation in Transition: GOV skills are called in preflights (good), but no explicit 'for all future IDE dev work, the following skills must be used first' note wired into manifests, launch_ide, or a transition checklist.",
]
for g in gaps:
    print(f"  - {g}")

print("\n## Recommendations for Transition Readiness (basic functionality OK with stubs)")
print("  1. Document explicit 'Basic Functionality Baseline' in GUI_DESIGN + matrix (what works for self-host dev today).")
print("  2. Expand matrix with child rows under Cross/L0/L3 for 'PS-IDE Transition' and 'Interface Governance as Enabler'.")
print("  3. Add transition notes + checklist to invocation record and launch_ide.py docstring.")
print("  4. Keep using skills in preflights and for self-audits of the transition docs themselves.")
print("  5. When ready: flip primary dev surface in docs/manifests, with PS remaining fully supported.")

print("\n=== EVALUATION COMPLETE ===")
print("Next: document gaps in matrix + invocation + GUI_DESIGN; ensure skills/tools actively represented.")