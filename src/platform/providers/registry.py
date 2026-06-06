"""Provider registry — Grok Build, Grok API, GitHub, OpenAI, Ollama."""

from __future__ import annotations

from enum import Enum


class ProviderId(str, Enum):
    GROK_BUILD = "grok-build"
    GROK_API = "grok-api"
    GITHUB = "github"
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    OLLAMA = "ollama"


class ProviderRegistry:
    DEFAULT_ORDER = [
        ProviderId.GROK_BUILD,
        ProviderId.GROK_API,
        ProviderId.OPENAI,
        ProviderId.OLLAMA,
    ]

    def list_providers(self) -> list[str]:
        return [p.value for p in ProviderId]

    def resolve(self, primary: str | None, fallback: list[str] | None = None) -> list[str]:
        chain = [primary] if primary else []
        chain.extend(fallback or [])
        return [p for p in chain if p]