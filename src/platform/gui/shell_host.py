"""Portable IDE shell host — Zed ACP first; custom host later."""

from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, Field


class ShellBackend(str, Enum):
    ZED_ACP = "zed-acp"
    CUSTOM_TAURI = "custom-tauri"
    HEADLESS = "headless"


class ShellConfig(BaseModel):
    backend: ShellBackend = ShellBackend.ZED_ACP
    terminal_shell: str = "powershell"
    agent_command: list[str] = Field(default_factory=lambda: ["grok", "agent", "stdio"])
    workspace_root: str = "."


class ShellHost:
    """Scaffold — R4 implements launch, viewer docking, settings persistence."""

    def __init__(self, config: ShellConfig) -> None:
        self.config = config

    def status(self) -> dict[str, str]:
        return {
            "backend": self.config.backend.value,
            "terminal": self.config.terminal_shell,
            "state": "scaffold",
        }