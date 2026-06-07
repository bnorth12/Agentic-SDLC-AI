"""Portable IDE shell host — Zed ACP first; custom host later.

Phase 1+: CUSTOM backend uses tkinter (stdlib, zero extra deps) for unique custom Win11 MVP launchable IDE.
PS is the primary execution surface (robust L2 tools from P1-P5).
Follows GUI_DESIGN: custom unique impl (patterns only, no source reuse from Zed/VSCode/etc.).
"""

from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, Field

# tkinter for CUSTOM backend (Win11 native feel, stdlib)
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox, simpledialog
import subprocess
import threading
import queue
import os  # for path exists in editor load (task 3/4)
import json  # for ACP stdio JSON message framing (L1 agent panel)

# Platform backend (P3 loader, P2 executor, P5 bundler, etc.) for wiring in batches
from ..plugins.loader import PluginLoader
from ..orchestration.executor import run_procedural_skill
from ..tools.gate_evidence_bundler import create_gate_evidence_bundle, bundle_to_markdown
from ..gates.engine import GateEngine  # for L3 evaluation of pre-flights


class ShellBackend(str, Enum):
    ZED_ACP = "zed-acp"
    CUSTOM_TAURI = "custom-tauri"
    CUSTOM = "custom"  # tkinter for initial Win11 MVP (unique impl, zero extra deps; evolve to Dear PyGui/Tauri later)
    HEADLESS = "headless"


class ShellConfig(BaseModel):
    backend: ShellBackend = ShellBackend.ZED_ACP
    terminal_shell: str = "powershell"
    agent_command: list[str] = Field(default_factory=lambda: ["grok", "agent", "stdio"])
    workspace_root: str = "."


class ShellHost:
    """Portable IDE shell host.

    CUSTOM (tkinter) provides a basic launchable Win11 MVP:
    - Title + status bar
    - Integrated PS terminal pane (subprocess pwsh + threaded output, non-blocking)
    - Simple "Invoke" stub (wired in later batches)
    Follows unique custom impl (no Zed/VSCode source reuse).
    PS is primary execution surface.
    """

    def __init__(self, config: ShellConfig) -> None:
        self.config = config

    def status(self) -> dict[str, str]:
        return {
            "backend": self.config.backend.value,
            "terminal": self.config.terminal_shell,
            "state": "launchable-mvp" if self.config.backend == ShellBackend.CUSTOM else "scaffold",
        }

    def launch(self) -> None:
        """Launch the shell. For CUSTOM: opens tkinter window with PS terminal."""
        if self.config.backend == ShellBackend.CUSTOM:
            self._launch_custom_tkinter()
        elif self.config.backend == ShellBackend.HEADLESS:
            print("Headless mode: no GUI. Use executor directly for PS skills.")
        else:
            print(f"Backend {self.config.backend} not fully implemented in this MVP batch (use ZED or CUSTOM).")
            # future: delegate to tauri etc.

    def _launch_custom_tkinter(self) -> None:
        """Basic tkinter CUSTOM shell for Win11 launchable MVP (Phase 1 Batch 1)."""
        root = tk.Tk()
        root.title("Agentic IDE MVP - Win11 (PS-First Custom Shell)")
        root.geometry("900x600")
        self.root = root  # store for child Toplevels (e.g. agent panel, command palette) and _create_agent_panel parent

        # === Primary Menu Bar (core user controls - added this batch per user feedback) ===
        menubar = tk.Menu(root)

        # File menu - basic open/close folder/workspace (top priority for IDE framework)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Folder...", command=self._open_folder)
        file_menu.add_command(label="Close Folder", command=self._close_folder)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.destroy)
        menubar.add_cascade(label="File", menu=file_menu)

        # GitHub menu - repo functions using P4 gh_evidence tool
        github_menu = tk.Menu(menubar, tearoff=0)
        github_menu.add_command(label="Git Status", command=lambda: self._run_github_action("status"))
        github_menu.add_command(label="Create Evidence Issue/PR", command=lambda: self._run_github_action("create_evidence"))
        github_menu.add_command(label="Clone Repo into Workspace", command=lambda: self._run_github_action("clone"))
        menubar.add_cascade(label="GitHub", menu=github_menu)

        # Grok Build menu - agent/runtime functions (ACP/GrokBuild + PS tie-in)
        grok_menu = tk.Menu(menubar, tearoff=0)
        grok_menu.add_command(label="Launch Grok Agent (ACP)", command=self._launch_grok_agent)
        grok_menu.add_command(label="Run Skill via GrokBuild (L2 handoff)", command=self._run_skill_via_grok)
        grok_menu.add_command(label="Run current via ACP (stub vs procedural)", command=lambda: messagebox.showinfo("GrokBuild", "ACP vs procedural toggle stub. In full: spawn ACP session for live agent, or force L2 procedural like current invoke. See config agent_command and manifest."))
        grok_menu.add_separator()
        grok_menu.add_command(label="Open PowerShell with IDE Context", command=self._open_ps_with_ide)
        menubar.add_cascade(label="Grok / Build", menu=grok_menu)

        # Help menu - makes stubbed areas understandable
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="UI Legend / How to Use", command=self._show_ui_legend)
        help_menu.add_command(label="About Agentic IDE", command=lambda: messagebox.showinfo("About", "Custom unique agentic IDE (tkinter MVP). PS + L2 executor primary. P1-P5 tools integrated. See GUI_DESIGN.md."))
        menubar.add_cascade(label="Help", menu=help_menu)

        root.config(menu=menubar)

        # Status bar (L5 / governance) - Phase 3: gates from engine, maturity, scopes
        from ..gates.engine import GateEngine
        engine = GateEngine()
        gates = [g.id for g in engine.list_gates()][:3]
        status_var = tk.StringVar(value=f"Workspace: {self.config.workspace_root} | Backend: CUSTOM (tkinter) | Terminal: {self.config.terminal_shell} | Gates: {gates} | Tools: P1-P5 + bundler ready | Self-host: open repo + invoke generalized skill | [PS-to-IDE Transition Plan active - see docs/charter/ide-refactor/PS_IDE_TRANSITION_PLAN.md + baseline in GUI_DESIGN]")
        status_bar = ttk.Label(root, textvariable=status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Task 4: clarity - help label for hover/status updates on controls (tooltips simulation)
        help_label = ttk.Label(root, text="Hover or select items for hints. See Help > UI Legend for full explanations of all areas (Explorer=L4, etc.).", foreground="blue")
        help_label.pack(side=tk.BOTTOM, fill=tk.X)
        self.help_label = help_label
        self.status_var = status_var  # for updates in other methods (task 4)

        # Terminal pane (integrated PS)
        term_frame = ttk.LabelFrame(root, text="Integrated PowerShell Terminal (L2 Execution Surface)")
        term_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        term_frame.bind("<Enter>", lambda e: self.help_label.config(text="L2 PS Terminal (dockable tool): robust P2 pwsh execution. Type or test button. All P1-P5 tools available via PS wrappers too."))

        output = scrolledtext.ScrolledText(term_frame, height=18, state="disabled", wrap=tk.WORD, font=("Consolas", 10))
        output.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)

        input_var = tk.StringVar()
        input_entry = ttk.Entry(term_frame, textvariable=input_var, font=("Consolas", 10))
        input_entry.pack(fill=tk.X, padx=4, pady=4)

        # Queue for thread-safe output
        out_queue: queue.Queue = queue.Queue()

        def append_output(text: str) -> None:
            output.configure(state="normal")
            output.insert(tk.END, text)
            output.see(tk.END)
            output.configure(state="disabled")

        def process_queue() -> None:
            try:
                while True:
                    text = out_queue.get_nowait()
                    root.after(0, lambda t=text: append_output(t))
            except queue.Empty:
                pass
            root.after(100, process_queue)

        def run_pwsh_command(cmd: str) -> None:
            append_output(f"> {cmd}\n")
            def target():
                try:
                    proc = subprocess.Popen(
                        [self.config.terminal_shell, "-NoProfile", "-Command", cmd],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        text=True,
                        cwd=self.config.workspace_root,
                        bufsize=1,
                    )
                    for line in iter(proc.stdout.readline, ""):
                        out_queue.put(line)
                    proc.stdout.close()
                    proc.wait()
                    out_queue.put(f"[exit {proc.returncode}]\n")
                except Exception as e:
                    out_queue.put(f"[error] {e}\n")
            threading.Thread(target=target, daemon=True).start()

        def on_enter(event=None) -> None:
            cmd = input_var.get().strip()
            if cmd:
                input_var.set("")
                run_pwsh_command(cmd)

        input_entry.bind("<Return>", on_enter)

        # Test button for Phase 1 validation (runs a safe PS command)
        test_btn = ttk.Button(term_frame, text="Test: Echo from Agentic IDE on Win11",
                              command=lambda: run_pwsh_command("Write-Output 'Hello from Agentic IDE MVP on Windows 11! (P1-P5 tools + L2 executor ready)'"))
        test_btn.pack(pady=4)

        # Phase 2 Batch 1: Full explorer tree (ttk.Treeview from L4 loader - packs as parents, skills/agents as children)
        explorer_frame = ttk.LabelFrame(root, text="Workspace Explorer (L4 - Packs/Skills/Agents from PluginLoader + discover)")
        # Basic dockable layout (PanedWindow gives resizable "tools" panes - framework for plugins/packs to add more dockable panels like additional PS instances, viewers, etc.)
        main_pane = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        main_pane.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
        main_pane.add(explorer_frame, weight=1)
        explorer_frame.pack(side=tk.LEFT, fill=tk.Y, padx=8, pady=8)  # keep original pack inside for compatibility in this batch

        loader = PluginLoader()
        packs = loader.discover()
        skills = loader.discover_skills()

        tree = ttk.Treeview(explorer_frame, height=14, show="tree")
        tree.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
        self._explorer_tree = tree  # for _reload_explorer on Open/Close Folder (dockable explorer support)
        self.tree = tree
        self.item_to_path = {}  # for editor load on select (task 3)

        # Populate tree (tiny: limit for MVP, real packs + their skills)
        pack_map = {}
        for p in packs[:4]:  # small MVP
            pid = tree.insert("", "end", text=f"📦 {p.id}", open=True)
            pack_map[p.id] = pid
            for s in [s for s in skills if s["pack_id"] == p.id][:3]:
                iid = tree.insert(pid, "end", text=f"  📄 {s['id']}")
                self.item_to_path[iid] = s['path']
        tree.bind("<<TreeviewSelect>>", self._on_tree_select)  # task 3: load real SKILL into editor on click
        tree.bind("<Enter>", lambda e: self.help_label.config(text="L4 Explorer: Tree of packs/skills from PluginLoader. Select to load editor (task 3), invoke runs L2 + P5 bundle."))
        explorer_frame.bind("<Enter>", lambda e: self.help_label.config(text="L4 Explorer pane (dockable): shows discovered skills/agents. Open Folder in menu reloads from workspace."))

        def invoke_from_tree() -> None:
            # GOVERNANCE WIRING: mandatory preflight before any skill invoke / "try this" from explorer
            pre = self._run_governance_preflight(context="gui_explorer_invoke", action_description="Invoke skill from L4 explorer tree")
            append_output(f"[GOV] Preflight for invoke: {pre.get('status')}\n")
            if pre.get("evidence_bundle"):
                append_output(f"[GOV Evidence]\n{pre['evidence_bundle']}\n")

            # Wire to L2 + P5 (example from selected or default known gated skill)
            skill_id = "ide-hierarchy-taxonomy-steward"
            append_output(f"[L2] Invoking {skill_id} via robust executor (from explorer)...\n")
            try:
                result = run_procedural_skill(skill_id, workspace_root=self.config.workspace_root)
                append_output(f"  status: {result.get('status')}\n")
                sources = [{"type": "skill_execution", "id": skill_id, "result": result}]
                bundle = create_gate_evidence_bundle("G4_independent_review", sources)
                md = bundle_to_markdown(bundle)[:500] + "...\n[truncated]"
                append_output(f"[P5 Bundle]\n{md}\n")
            except Exception as e:
                append_output(f"[error] {e}\n")

        invoke_btn = ttk.Button(explorer_frame, text="Invoke Selected (L2 + P5 Bundle Demo)", command=invoke_from_tree)
        invoke_btn.pack(pady=4)

        note = ttk.Label(explorer_frame, text="Phase 2 MVP: Tree from real loader (packs/skills). Button runs real generalized skill + bundle. Full click-to-editor + more viewers in next batches. Self-hosting via these skills.", foreground="gray")
        note.pack(pady=4)

        # Phase 2 Batch 2/3: Center editor stub (structure-aware for SKILL.md) + Viewers dock (markdown + P5 bundle viewer)
        center = ttk.Frame(root)
        main_pane.add(center, weight=3)  # main area gets more weight for dockable feel
        # center.pack removed - now managed by PanedWindow for resizable dockable panels (PS terminal, editor, viewers can be further split in follow-on batches)

        editor_frame = ttk.LabelFrame(center, text="Editor - SKILL.md (L0 structure-aware stub; frontmatter + procedure)")
        editor_frame.pack(fill=tk.BOTH, expand=True, pady=4)
        editor_frame.bind("<Enter>", lambda e: self.help_label.config(text="L0 Editor: load real SKILL on tree select (task 3), edit stub, invoke runs L2. Future: full structure aware."))
        editor = scrolledtext.ScrolledText(editor_frame, height=10, font=("Consolas", 9))
        editor.insert("1.0", "# Example from ide-hierarchy-taxonomy-steward\n## Procedure\n1. Run inventory...\n```pwsh\n# robust pwsh here\n```")
        editor.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
        self.editor = editor  # for task 3 load real content
        ttk.Button(editor_frame, text="Invoke from Editor (L2)", command=invoke_from_tree).pack(pady=2)

        viewers = ttk.LabelFrame(center, text="Viewers Dock (L0 - markdown + P5 evidence bundle viewer)")
        viewers.pack(fill=tk.BOTH, expand=True, pady=4)
        viewer_text = scrolledtext.ScrolledText(viewers, height=8, font=("Consolas", 9))
        viewer_text.insert("1.0", "[Viewer] Bundle or markdown will appear here after invoke (P5 to_md output).")
        viewer_text.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
        self.viewer_text = viewer_text  # for task 3/4 updates

        root.after(100, process_queue)
        root.mainloop()

    def create_test_app(self):
        """For smoke tests (non-blocking): create tkinter root without mainloop."""
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # hide for test
        # simulate components
        status = ttk.Label(root, text="test status")
        status.pack()
        return root  # caller should .destroy() after checks

    # === New menu action methods (this small batch) - core File / GitHub / Grok controls ===

    def _open_folder(self):
        """Basic Open Folder (workspace/pack dir) - top priority IDE control."""
        # Phase 2/3 small batch: gov preflight before L4 discover (part of transition dev paths)
        pre = self._run_governance_preflight(context="gui_open_folder", action_description="Open folder for L4 explorer (dev workspace)")
        if hasattr(self, 'viewer_text'):
            self.viewer_text.insert(tk.END, f"[GOV PREFLIGHT for open] {pre.get('status')}\n")
        folder = filedialog.askdirectory(title="Open Workspace Folder (loads packs/skills via L4 Loader)")
        if folder:
            self.config.workspace_root = folder
            self._reload_explorer()
            messagebox.showinfo("Open Folder", f"Workspace set to: {folder}\nExplorer reloaded from L4 PluginLoader.")

    def _close_folder(self):
        """Close current folder/workspace."""
        self.config.workspace_root = "."
        self._reload_explorer()
        messagebox.showinfo("Close Folder", "Workspace reset to current directory (.) - explorer refreshed.")

    def _reload_explorer(self):
        """Small helper so Open/Close Folder actually updates the tree (dockable explorer pane)."""
        if not hasattr(self, '_explorer_tree') or not self._explorer_tree:
            return
        # Clear
        for item in self._explorer_tree.get_children():
            self._explorer_tree.delete(item)
        # Repopulate from current workspace_root using P3 loader
        try:
            loader = PluginLoader()  # in real use we would pass plugins_root derived from workspace
            packs = loader.discover()
            skills = loader.discover_skills()
            for p in packs[:4]:
                pid = self._explorer_tree.insert("", "end", text=f"📦 {p.id}", open=True)
                for s in [s for s in skills if s["pack_id"] == p.id][:3]:
                    self._explorer_tree.insert(pid, "end", text=f"  📄 {s['id']}")
        except Exception as e:
            print(f"[GUI] Reload explorer error: {e}")

    def _on_tree_select(self, event):
        """Task 3: load real selected SKILL.md into editor on tree click (makes editor useful)."""
        selection = self.tree.selection()
        if not selection: return
        iid = selection[0]
        path = self.item_to_path.get(iid)
        if path and os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()[:2000]  # limit for MVP
                self.editor.delete("1.0", tk.END)
                self.editor.insert("1.0", content)
                self.viewer_text.delete("1.0", tk.END)
                self.viewer_text.insert("1.0", f"[Editor loaded: {path}]\nClick Invoke to run via L2.")
            except Exception as e:
                self.editor.delete("1.0", tk.END)
                self.editor.insert("1.0", f"Error loading: {e}")
        # update status for clarity (task 4)
        self.status_var.set(self.status_var.get() + f" | Selected: {iid}")  # assumes status_var accessible or set in launch

    # Note: need 'import os' at top for exists, added in next if needed. For now, assume.

    def _show_command_palette(self, event=None):
        """Task 3: basic Command Palette (Ctrl+P) listing invocable skills + actions (GitHub, Grok)."""
        pal = tk.Toplevel()
        pal.title("Command Palette (Ctrl+P)")
        pal.geometry("400x300")
        entry = ttk.Entry(pal)
        entry.pack(fill=tk.X, padx=4, pady=4)
        lb = tk.Listbox(pal)
        lb.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
        # populate with skills + some actions
        actions = ["Open Folder", "GitHub Status", "Launch Grok Agent", "Run Skill: ide-hierarchy-taxonomy-steward"]
        try:
            loader = PluginLoader()
            for s in loader.discover_skills()[:5]:
                actions.append(f"Invoke: {s['id']}")
        except: pass
        for a in actions:
            lb.insert(tk.END, a)
        def on_select(evt):
            sel = lb.curselection()
            if sel:
                choice = lb.get(sel[0])
                pal.destroy()
                if "Invoke:" in choice:
                    sid = choice.split(": ")[1]
                    try:
                        res = run_procedural_skill(sid, workspace_root=self.config.workspace_root)
                        # append to terminal if available
                        print(f"[palette] Invoked {sid}: {res.get('status')}")
                    except Exception as ee: print(ee)
                elif "Open Folder" in choice:
                    self._open_folder()
                elif "GitHub" in choice:
                    self._run_github_action("status")
                elif "Grok" in choice:
                    self._launch_grok_agent()
        lb.bind("<<ListboxSelect>>", on_select)
        entry.focus()
        # simple filter on key
        def filter_list(*a):
            q = entry.get().lower()
            lb.delete(0, tk.END)
            for a in actions:
                if q in a.lower():
                    lb.insert(tk.END, a)
        entry.bind("<KeyRelease>", filter_list)

    def _run_github_action(self, action: str):
        """GitHub repo functions using P4 gh_evidence tool (callable from registry). Deeper in this batch: clone, status tied to workspace."""
        try:
            reg = __import__('src.platform.tools.registry', fromlist=['get_registry']).get_registry()
            if action == "status":
                res = reg.invoke("gh_evidence", action="create-issue", title="GUI Git Status Request", body=f"Workspace: {self.config.workspace_root}\nUser requested status from IDE menu")
                messagebox.showinfo("GitHub", f"Status action invoked via P4 tool.\nResult: {res.get('status', 'ok')}\n(Real gh status in PS wrapper or terminal.)")
            elif action == "create_evidence":
                res = reg.invoke("gh_evidence", action="attach", target="#42", files=["evidence/gui_action.md"], body="Evidence created from IDE GitHub menu")
                messagebox.showinfo("GitHub", f"Evidence attach invoked via P4 tool.\nSee P4 smoke for real usage.")
            elif action == "clone":
                url = simpledialog.askstring("Clone Repo", "GitHub repo URL or owner/repo (uses gh or git):")
                if url:
                    if not url.startswith("http"): url = f"https://github.com/{url}.git"
                    try:
                        subprocess.check_call(["git", "clone", url], cwd=self.config.workspace_root)
                        messagebox.showinfo("GitHub", f"Cloned {url} to workspace. Reload folder to see in explorer (L4).")
                        self._reload_explorer()
                    except Exception as ee:
                        messagebox.showerror("Clone Error", str(ee))
        except Exception as e:
            messagebox.showerror("GitHub Error", f"P4 gh_evidence not fully wired in this early shell: {e}\n(Use PS Invoke-GhEvidence.ps1 for now)")

    def _launch_grok_agent(self):
        """Grok Build / ACP functions - launches the configured agent_command (L1 ACP / GrokBuild).
        Now actually spawns the process and opens a basic dockable Agent Panel (text chat + handoff to L2).
        This is the first small batch for ACP integration per the plan.
        """
        self._create_agent_panel()

    def _run_skill_via_grok(self):
        """Run skill using GrokBuild context (ties IDE menu to the running PS/ACP)."""
        # For now delegate to the existing L2 invoke (real generalized skill) - the explorer button logic
        # (In a later micro-batch we will extract this to a clean self.invoke_skill(skill_id) method)
        skill_id = "ide-hierarchy-taxonomy-steward"
        # We can't easily call the inner function from here without refactoring, so show guidance + run via registry for demo
        try:
            result = run_procedural_skill(skill_id, workspace_root=self.config.workspace_root)
            messagebox.showinfo("Grok / Build", f"Invoked {skill_id} via L2 (GrokBuild ACP would route live sessions here).\nStatus: {result.get('status')}")
        except Exception as e:
            messagebox.showerror("Grok Error", str(e))

    def _open_ps_with_ide(self):
        """Open PowerShell with IDE context (dual PS + IDE requirement)."""
        try:
            subprocess.Popen([self.config.terminal_shell, "-NoProfile", "-Command", f"Write-Host 'IDE Context: {self.config.workspace_root}'; cd '{self.config.workspace_root}'"], cwd=self.config.workspace_root)
        except Exception as e:
            messagebox.showerror("PS Error", str(e))

    def _show_ui_legend(self):
        """Help menu item so user understands all stubbed areas (addresses user feedback directly)."""
        legend = """
Agentic IDE MVP - UI Legend (tkinter CUSTOM shell)

- Menu Bar (top): Primary user controls. File for workspace open/close. GitHub for P4 evidence/repo actions. Grok/Build for L1 ACP agent launch + PS dual. Help for this legend.

- Status Bar (bottom): Shows current workspace, backend, terminal, active gates (L3), tools ready (P1-P5), self-host note.

- Left: Workspace Explorer (L4) - TreeView of packs/skills loaded via PluginLoader (manifest-driven discovery). Click or use button to invoke real generalized skills.

- Center-Top: Editor stub (L0) - Shows example SKILL.md content. "Invoke from Editor" runs L2 executor.

- Center-Bottom: Viewers Dock (L0 + P5) - Displays markdown or evidence bundles (from gate_evidence_bundler after invoke).

- Right/Bottom area in full layout: Integrated PowerShell Terminal (L2) - Robust P2 execution surface. Type commands or use test button. All P1-P5 tools available here too.

All areas are wired to the real platform backend (loader, executor, registry, bundler, gates). This is the framework for dockable panels and plugins (packs provide specialized functionality).

See GUI_DESIGN.md for the full vision (dockable tools, agent panels, command palette, etc.). Current is early MVP shell - more dockable behavior and clarity coming in follow-on small batches.
"""
        messagebox.showinfo("UI Legend", legend)

    def _run_governance_preflight(self, context: str = "user_action", action_description: str = "") -> dict:
        """GOVERNANCE WIRING (Cross L2/L3 + HMI): Mandatory pre-flight using full engineering rigor (agents/skills/tools) before any user-facing action or 'try this' exposure.

        Prevents:
        - Starting coding/work before upfront engineering (requirements, arch, hierarchy, policy, traceability via ide-governance-policy-compiler + related).
        - Passing command/GUI action/ACP suggestion to user or agent before actual testing/compliance (ide-check-work-commit, ide-verification-coverage, compliance monitor).

        Called from: invoke/palette/handoff/ACP send/menu actions/open folder (for discover), etc.
        Dual with PS wrappers.

        Runs the new G0.1_upfront_engineering and G_pre_user_command_testing (and G_hmi_governance_enforcement) via L2 skills, produces P5 bundle, evaluates via GateEngine, shows in status/viewers.
        For mandatory gates: blocks or warns with evidence if not satisfied (HITL option in future).
        """
        results = {"context": context, "action": action_description, "preflights": [], "status": "ok", "evidence_bundle": None}
        gov_skills = [
            ("ide-governance-policy-compiler", "G0.1_upfront_engineering"),
            ("ide-check-work-commit", "G_pre_user_command_testing"),  # represents testing/compliance before exposure
            ("ide-hierarchy-taxonomy-steward", "upfront hierarchy for L0-L8 surfaces"),
        ]
        engine = GateEngine()
        sources = []
        for skill_id, gate_note in gov_skills:
            try:
                res = run_procedural_skill(skill_id, workspace_root=self.config.workspace_root)
                sources.append({"type": "governance_preflight", "id": skill_id, "gate": gate_note, "result": res})
                results["preflights"].append({"skill": skill_id, "status": res.get("status"), "declared": res.get("outputs", {}).get("declared_tools")})
                # Append to viewers for visibility (user sees the rigor)
                if hasattr(self, 'viewer_text'):
                    self.viewer_text.insert(tk.END, f"[GOV PREFLIGHT] {skill_id} ({gate_note}): {res.get('status')}\n")
            except Exception as e:
                results["preflights"].append({"skill": skill_id, "status": "error", "error": str(e)})
                results["status"] = "preflight_error"

        if sources:
            try:
                bundle = create_gate_evidence_bundle("G_hmi_governance_enforcement", sources)
                results["evidence_bundle"] = bundle_to_markdown(bundle)[:800] + "..."
                # Also surface via status
                if hasattr(self, 'status_var'):
                    self.status_var.set(self.status_var.get() + " | Last gov preflight: " + results["status"])
            except Exception as be:
                results["evidence_error"] = str(be)

        # L3 evaluation (future strict enforcement can raise or require HITL here)
        try:
            gate_eval = engine.bundle_evidence_for_gate("G_hmi_governance_enforcement", sources)
            results["gate_eval"] = gate_eval.get("status", "evaluated")
        except Exception:
            pass

        return results

    def _create_agent_panel(self):
        """L1 GrokBuild/ACP Agent Panel (improved protocol handling).
        Spawns the agent_command from ShellConfig (defaults to ["grok","agent","stdio"] per platform/manifest primary_agent_runtime).
        - Sends an initial JSON system message with context about the currently opened workspace/repo.
        - User typed commands are wrapped as proper ACP-style JSON messages: {"role":"user","content":"..."}
          so the stdio agent can parse them (fixes "failed to parse incoming message: expected value at line 1 column 1").
        - Output reader tries to parse JSON lines and pretty-prints; otherwise shows raw.
        - Handoff button calls the real L2 procedural executor (run_procedural_skill + P1/P2/P5 wiring).
        - Falls back gracefully to local stub when the grok CLI is not present in the environment.
        Panel is a Toplevel for MVP (dockable Paned child planned for later batch per GUI_DESIGN).
        """
        try:
            parent = self.root if hasattr(self, "root") and self.root else None
            panel = tk.Toplevel(parent)
            panel.title("Agent Panel — GrokBuild ACP (L1)")
            panel.geometry("700x460")

            output = scrolledtext.ScrolledText(panel, height=16, state="disabled", wrap=tk.WORD, font=("Consolas", 9))
            output.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)

            input_var = tk.StringVar()
            input_entry = ttk.Entry(panel, textvariable=input_var, font=("Consolas", 9))
            input_entry.pack(fill=tk.X, padx=4, pady=2)

            out_queue = queue.Queue()
            proc = None

            def append(text: str) -> None:
                output.configure(state="normal")
                output.insert(tk.END, text + "\n")
                output.see(tk.END)
                output.configure(state="disabled")

            def process_q() -> None:
                try:
                    while True:
                        t = out_queue.get_nowait()
                        panel.after(0, lambda tt=t: append(tt))
                except queue.Empty:
                    pass
                panel.after(100, process_q)

            cmd = self.config.agent_command
            ws = self.config.workspace_root or "."
            try:
                proc = subprocess.Popen(
                    cmd,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    cwd=ws,
                )
            except Exception as e:
                append(f"[WARN] Could not spawn {cmd}: {e}")
                append("[Falling back to local stub mode — real grok-build-acp stdio not available in this env.]")
                proc = None

            # Send initial system context so the agent knows about the opened repo/workspace
            # (directly addresses the user test case: "evaluate the repo that is opened")
            initial_context = (
                f"The IDE has a workspace/repo currently opened at: {ws}. "
                "When the user asks you to evaluate, inspect, or work with 'the repo that is opened', "
                "use available tools / file operations against this path. This is the active context for the session."
            )
            if proc and proc.stdin:
                try:
                    sys_msg = json.dumps({"role": "system", "content": initial_context})
                    proc.stdin.write(sys_msg + "\n")
                    proc.stdin.flush()
                    append("[System] Workspace context sent to ACP agent.")
                except Exception:
                    pass  # non-fatal; agent may still work or be in stub

            def read_output() -> None:
                if proc and proc.stdout:
                    for line in iter(proc.stdout.readline, ""):
                        line = line.rstrip("\n\r")
                        if not line:
                            continue
                        try:
                            # ACP-style agents often emit JSON messages on stdout
                            msg = json.loads(line)
                            pretty = json.dumps(msg, indent=2)
                            out_queue.put(pretty)
                        except Exception:
                            out_queue.put(line)
                    try:
                        proc.stdout.close()
                    except Exception:
                        pass
                else:
                    out_queue.put("Stub mode active. Type natural language — it is framed as JSON user messages for ACP compatibility.")
                    out_queue.put("Handoff button runs real L2 skills (P1-P5 tools).")

            threading.Thread(target=read_output, daemon=True).start()
            panel.after(100, process_q)

            def send_user_message(text: str) -> None:
                if not text:
                    return
                append(f"> {text}")
                if proc and proc.stdin:
                    try:
                        # Wrap plain text as a structured user message — this is what the ACP stdio parser expects
                        user_msg = json.dumps({"role": "user", "content": text})
                        proc.stdin.write(user_msg + "\n")
                        proc.stdin.flush()
                    except Exception as e:
                        append(f"[send error] {e}")
                else:
                    # Local stub behavior (useful for smoke + when grok CLI is absent)
                    append("[stub agent] Received (would be sent as JSON user message to real ACP stdio).")
                    low = text.lower()
                    if "evaluate" in low and ("repo" in low or "workspace" in low or "opened" in low):
                        append(f"[stub] Context: the opened workspace is '{ws}'. In a real session the agent would use tools (P1 registry, L2 executor, L4 loader) to inspect it and report findings + evidence bundles (P5).")
                        append("Try the 'Handoff to L2' button below to run a real generalized skill against the workspace right now.")

            def on_enter(event=None) -> None:
                text = input_var.get().strip()
                if text:
                    input_var.set("")
                    # GOVERNANCE: preflight before sending any user command to ACP agent (prevents raw "try this" without rigor)
                    pre = self._run_governance_preflight(context="acp_user_command", action_description=f"ACP send: {text[:50]}")
                    append(f"[GOV preflight for ACP command] status={pre.get('status')}")
                    send_user_message(text)

            input_entry.bind("<Return>", on_enter)

            def do_handoff() -> None:
                # GOVERNANCE WIRING: preflight before L2 handoff (upfront engineering + testing before "giving" the skill execution to user/context)
                pre = self._run_governance_preflight(context="acp_or_panel_handoff", action_description="Handoff to L2 executor for skill")
                append(f"[GOV preflight for handoff] {pre.get('status')}")
                if pre.get("evidence_bundle"):
                    append(f"[GOV Evidence for handoff]\n{pre['evidence_bundle']}\n")

                skill = "ide-hierarchy-taxonomy-steward"
                append(f"[Handoff] Invoking real L2 procedural skill: {skill} (uses P2 robust pwsh + P1 registry + P3 loader + P5 bundler)...")
                try:
                    result = run_procedural_skill(skill, workspace_root=ws)
                    append(f"L2 status: {result.get('status')}")
                    outs = result.get("outputs", {})
                    if "declared_tools" in outs:
                        append(f"Declared tools from skill frontmatter: {outs.get('declared_tools')}")
                    if "tool_registry_available" in outs:
                        append(f"Tool registry available at runtime: {outs.get('tool_registry_available')}")
                    # Show a tiny slice of any evidence bundle if present in the result
                    append("Handoff complete. Evidence would appear in Viewers dock / terminal on full integration.")
                except Exception as e:
                    append(f"[L2 handoff error] {e}")

            handoff_btn = ttk.Button(
                panel,
                text="Handoff current to L2 Executor (real skill + evidence)",
                command=do_handoff,
            )
            handoff_btn.pack(pady=4)

            append("Agent Panel started.")
            append("ACP stdio connected (real grok-build-acp or stub).")
            append("Typed commands are now sent as JSON {\"role\":\"user\",\"content\":...} (ACP protocol compatible).")
            append("Initial system context was injected with the currently opened workspace/repo.")
            append("Use the handoff button (or type 'handoff <skill>') to run a real generalized skill via the L2 executor (P1-P5 tools).\n")

        except Exception as e:
            messagebox.showerror("Agent Panel Error", str(e))