"""Centralized configuration management using Pydantic Settings."""

from __future__ import annotations

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    app_env: Literal["development", "production", "test"] = Field(
        default="development",
        description="Application environment",
    )
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO",
        description="Logging level",
    )

    # Model Provider
    ollama_base_url: str = Field(
        default="http://localhost:11434",
        description="Ollama API base URL",
    )
    ollama_model: str = Field(
        default="llama3.1:8b-instruct-q4_K_M",
        description="Default Ollama model for agents",
    )

    # Role-specific models (can override default)
    model_program_manager: str | None = None
    model_chief_engineer: str | None = None
    model_requirements: str | None = None
    model_architecture: str | None = None
    model_safety: str | None = None
    model_development: str | None = None
    model_verification: str | None = None
    model_low_complexity: str | None = None
    model_medium_complexity: str | None = None
    model_high_complexity: str | None = None
    enable_adaptive_model_routing: bool = Field(
        default=True,
        description="Enable adaptive model routing based on execution telemetry",
    )
    adaptive_latency_threshold_seconds: float = Field(
        default=2.5,
        description="Latency threshold used for adaptive model routing",
        ge=0.1,
    )
    adaptive_error_threshold: int = Field(
        default=2,
        description="Consecutive error threshold before model fallback",
        ge=1,
    )

    # Persistence
    postgres_url: str = Field(
        default="postgresql://agentic:agentic@localhost:5432/agentic_sdlc",
        description="PostgreSQL connection string",
    )
    checkpoint_table: str = Field(
        default="langgraph_checkpoints",
        description="Table name for LangGraph checkpoints",
    )
    vector_table: str = Field(
        default="agent_embeddings",
        description="Table name for vector embeddings",
    )

    # Human-in-the-Loop
    enable_hitl: bool = Field(
        default=True,
        description="Enable human approval gates",
    )
    hitl_timeout_seconds: int = Field(
        default=300,
        description="Timeout for human approval (0 = no timeout)",
    )
    auto_approve_low_risk: bool = Field(
        default=False,
        description="Automatically approve low-risk decisions",
    )

    # Performance
    default_timeout_seconds: int = Field(
        default=120,
        description="Default timeout for agent operations",
    )
    max_iterations: int = Field(
        default=25,
        description="Maximum graph iterations before stopping",
    )
    temperature: float = Field(
        default=0.7,
        description="Default model temperature",
        ge=0.0,
        le=2.0,
    )

    # Memory & Context
    enable_vector_memory: bool = Field(
        default=True,
        description="Enable vector-based long-term memory",
    )
    max_context_messages: int = Field(
        default=20,
        description="Maximum messages to keep in context",
    )
    summarization_threshold: int = Field(
        default=10,
        description="Number of messages before summarization",
    )

    # Development
    enable_tracing: bool = Field(
        default=False,
        description="Enable LangSmith tracing",
    )
    langsmith_api_key: str | None = None
    langsmith_project: str = Field(
        default="agentic-sdlc-ai",
        description="LangSmith project name",
    )

    # Observability backend stub
    enable_observability_backend: bool = Field(
        default=False,
        description="Enable structured logging backend integration stub",
    )
    observability_backend_url: str | None = Field(
        default=None,
        description="Optional backend endpoint for observability log forwarding",
    )
    observability_backend_token: str | None = Field(
        default=None,
        description="Optional bearer token for backend log forwarding",
    )

    def get_model_for_role(self, role: str, complexity: str | None = None) -> str:
        """Get the preferred model for an agent role and optional complexity."""
        return self.get_model_candidates_for_role(role, complexity)[0]

    def get_model_candidates_for_role(
        self, role: str, complexity: str | None = None
    ) -> list[str]:
        """Return ordered model candidates for a role and optional complexity tier."""
        candidates: list[str] = []
        role_fields = self._role_model_field_candidates(role)

        for field_name in role_fields:
            model_name = getattr(self, field_name, None)
            if model_name and model_name not in candidates:
                candidates.append(model_name)

        complexity_map = {
            "low": self.model_low_complexity,
            "medium": self.model_medium_complexity,
            "high": self.model_high_complexity,
        }
        complexity_key = (complexity or "").strip().lower()
        complexity_model = complexity_map.get(complexity_key)
        if complexity_model and complexity_model not in candidates:
            candidates.append(complexity_model)

        if self.ollama_model not in candidates:
            candidates.append(self.ollama_model)

        return candidates

    @staticmethod
    def _role_model_field_candidates(role: str) -> list[str]:
        """Return candidate settings fields for a role name."""
        normalized = role.strip().lower().replace("-", "_").replace(" ", "_")
        candidates = [f"model_{normalized}"]

        aliases = {
            "requirements_agent": "model_requirements",
            "architecture_agent": "model_architecture",
            "cyber_architect": "model_architecture",
            "chief_safety_officer": "model_safety",
            "software_development_agent": "model_development",
            "configuration_management_agent": "model_development",
            "integration_manager": "model_development",
            "verification_validation_agent": "model_verification",
            "qa_manager": "model_verification",
        }

        mapped = aliases.get(normalized)
        if mapped and mapped not in candidates:
            candidates.append(mapped)

        if normalized.endswith("_agent"):
            trimmed = normalized[: -len("_agent")]
            if trimmed:
                trimmed_field = f"model_{trimmed}"
                if trimmed_field not in candidates:
                    candidates.append(trimmed_field)

        return candidates


@lru_cache
def get_settings() -> Settings:
    """Get cached application settings."""
    return Settings()
