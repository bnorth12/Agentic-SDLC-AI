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

    def get_model_for_role(self, role: str) -> str:
        """Get the appropriate model for a specific agent role."""
        role_model = getattr(self, f"model_{role.lower()}", None)
        return role_model or self.ollama_model


@lru_cache
def get_settings() -> Settings:
    """Get cached application settings."""
    return Settings()
