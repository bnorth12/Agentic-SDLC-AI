"""Structured logging utilities for the application."""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Any

from rich.console import Console
from rich.logging import RichHandler

from src.config import get_settings

# Rich console for pretty output
console = Console()


def setup_logging() -> logging.Logger:
    """Configure application logging with rich formatting."""
    settings = get_settings()

    # Create logs directory if it doesn't exist
    log_dir = Path("data/logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.log_level)

    # Remove existing handlers
    root_logger.handlers.clear()

    # Console handler with rich formatting
    console_handler = RichHandler(
        console=console,
        rich_tracebacks=True,
        tracebacks_show_locals=True,
        markup=True,
    )
    console_handler.setLevel(settings.log_level)
    console_formatter = logging.Formatter(
        "%(message)s",
        datefmt="[%X]",
    )
    console_handler.setFormatter(console_formatter)

    # File handler with detailed formatting
    file_handler = logging.FileHandler(
        log_dir / "agentic_sdlc.log",
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(file_formatter)

    # Add handlers
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Suppress noisy third-party loggers
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("ollama").setLevel(logging.INFO)

    return root_logger


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance for a specific module."""
    return logging.getLogger(name)


class AgentLogger:
    """Structured logger for agent activities."""

    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self.logger = get_logger(f"agent.{agent_name}")

    def log_start(self, task: str) -> None:
        """Log the start of an agent task."""
        self.logger.info(
            f"[bold cyan]{self.agent_name}[/] starting: {task}",
            extra={"markup": True},
        )

    def log_complete(self, task: str, result: Any = None) -> None:
        """Log the completion of an agent task."""
        msg = f"[bold green]{self.agent_name}[/] completed: {task}"
        if result:
            msg += f" | Result: {result}"
        self.logger.info(msg, extra={"markup": True})

    def log_error(self, task: str, error: Exception) -> None:
        """Log an agent error."""
        self.logger.error(
            f"[bold red]{self.agent_name}[/] error in {task}: {error}",
            exc_info=True,
            extra={"markup": True},
        )

    def log_decision(self, decision: str, rationale: str) -> None:
        """Log an agent decision."""
        self.logger.info(
            f"[bold yellow]{self.agent_name}[/] DECISION: {decision}\n"
            f"  Rationale: {rationale}",
            extra={"markup": True},
        )

    def log_escalation(self, issue: str, to: str) -> None:
        """Log an escalation to another agent or human."""
        self.logger.warning(
            f"[bold magenta]{self.agent_name}[/] ESCALATING to {to}: {issue}",
            extra={"markup": True},
        )


def log_state_update(field: str, old_value: Any, new_value: Any) -> None:
    """Log a shared state update."""
    logger = get_logger("state")
    logger.debug(f"State update: {field} changed from {old_value} to {new_value}")


def log_board_activity(board_name: str, activity: str) -> None:
    """Log review board activity."""
    logger = get_logger(f"board.{board_name}")
    logger.info(f"[bold blue]{board_name}[/]: {activity}", extra={"markup": True})
