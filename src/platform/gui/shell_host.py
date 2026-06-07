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
from tkinter import ttk, scrolledtext
import subprocess
import threading
import queue

# Platform backend (P3 loader, P2 executor, P5 bundler, etc.) for wiring in batches
from ..plugins.loader import PluginLoader
from ..orchestration.executor import ProceduralSkillExecutor, run_procedural_skill
from ..tools.gate_evidence_bundler import create_gate_evidence_bundle, bundle_to_markdown


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

        # Status bar (L5 / governance)
        status_var = tk.StringVar(value=f"Workspace: {self.config.workspace_root} | Backend: CUSTOM (tkinter) | Terminal: {self.config.terminal_shell} | Tools: P1-P5 ready")
        status_bar = ttk.Label(root, textvariable=status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Terminal pane (integrated PS)
        term_frame = ttk.LabelFrame(root, text="Integrated PowerShell Terminal (L2 Execution Surface)")
        term_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

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
        explorer_frame.pack(side=tk.LEFT, fill=tk.Y, padx=8, pady=8)

        loader = PluginLoader()
        packs = loader.discover()
        skills = loader.discover_skills()

        tree = ttk.Treeview(explorer_frame, height=14, show="tree")
        tree.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)

        # Populate tree (tiny: limit for MVP, real packs + their skills)
        pack_map = {}
        for p in packs[:4]:  # small MVP
            pid = tree.insert("", "end", text=f"📦 {p.id}", open=True)
            pack_map[p.id] = pid
            for s in [s for s in skills if s["pack_id"] == p.id][:3]:
                tree.insert(pid, "end", text=f"  📄 {s['id']}")

        def invoke_from_tree() -> None:
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