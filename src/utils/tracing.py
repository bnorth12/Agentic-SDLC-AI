"""Observability and tracing utilities for debugging and monitoring."""

from __future__ import annotations

import functools
import time
from typing import Any, Callable

from src.config import get_settings
from src.utils.logging import get_logger

logger = get_logger(__name__)


def setup_tracing() -> None:
    """Configure LangSmith tracing if enabled."""
    settings = get_settings()

    if settings.enable_tracing and settings.langsmith_api_key:
        import os

        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_API_KEY"] = settings.langsmith_api_key
        os.environ["LANGCHAIN_PROJECT"] = settings.langsmith_project
        logger.info(f"LangSmith tracing enabled for project: {settings.langsmith_project}")
    else:
        logger.debug("Tracing disabled")


def trace_agent_execution(func: Callable) -> Callable:
    """Decorator to trace agent execution time and results."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        agent_name = kwargs.get("agent_name", func.__name__)
        start_time = time.time()

        logger.debug(f"Starting {agent_name}")

        try:
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
            logger.debug(f"Completed {agent_name} in {elapsed:.2f}s")
            return result
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"Failed {agent_name} after {elapsed:.2f}s: {e}")
            raise

    return wrapper


def log_llm_call(
    model: str,
    prompt_length: int,
    response_length: int,
    duration: float,
) -> None:
    """Log LLM API call metrics."""
    logger.debug(
        f"LLM call | Model: {model} | "
        f"Prompt: {prompt_length} chars | "
        f"Response: {response_length} chars | "
        f"Duration: {duration:.2f}s"
    )
