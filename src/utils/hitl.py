"""Human-in-the-loop utilities for approval gates and feedback."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from src.config import get_settings
from src.utils.logging import get_logger

console = Console()
logger = get_logger(__name__)


class ApprovalDecision(str, Enum):
    """Human approval decision options."""

    APPROVE = "approve"
    APPROVE_WITH_CHANGES = "approve_with_changes"
    REJECT = "reject"
    DEFER = "defer"


class RiskLevel(str, Enum):
    """Risk level classification."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ApprovalRequest(BaseModel):
    """Request for human approval."""

    decision_type: str = Field(description="Type of decision requiring approval")
    risk_level: RiskLevel = Field(description="Risk level of the decision")
    requesting_agent: str = Field(description="Agent requesting approval")
    context: str = Field(description="Context and background information")
    recommendation: str = Field(description="Agent's recommendation")
    rationale: str = Field(description="Reasoning behind the recommendation")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ApprovalResponse(BaseModel):
    """Human response to an approval request."""

    decision: ApprovalDecision
    feedback: str | None = None
    modifications: dict[str, Any] | None = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)


def display_approval_request(request: ApprovalRequest) -> None:
    """Display approval request in a formatted panel."""
    risk_colors = {
        RiskLevel.LOW: "green",
        RiskLevel.MEDIUM: "yellow",
        RiskLevel.HIGH: "orange",
        RiskLevel.CRITICAL: "red",
    }

    content = f"""
[bold]Decision Type:[/] {request.decision_type}
[bold]Risk Level:[/] [{risk_colors[request.risk_level]}]{request.risk_level.value.upper()}[/]
[bold]Requesting Agent:[/] {request.requesting_agent}

[bold cyan]Context:[/]
{request.context}

[bold green]Recommendation:[/]
{request.recommendation}

[bold yellow]Rationale:[/]
{request.rationale}
"""

    console.print(
        Panel(
            content.strip(),
            title="🔔 Human Approval Required",
            border_style=risk_colors[request.risk_level],
        )
    )


def request_human_approval(
    decision_type: str,
    risk_level: RiskLevel,
    requesting_agent: str,
    context: str,
    recommendation: str,
    rationale: str,
    timeout: int | None = None,
) -> ApprovalResponse:
    """
    Request human approval for a decision.

    Args:
        decision_type: Type of decision (e.g., "Architecture Approval", "Requirement Baseline")
        risk_level: Risk level classification
        requesting_agent: Name of the agent requesting approval
        context: Background information and current state
        recommendation: Recommended action
        rationale: Reasoning for the recommendation
        timeout: Timeout in seconds (None = no timeout)

    Returns:
        ApprovalResponse with human decision and feedback
    """
    settings = get_settings()

    # Check if HITL is disabled
    if not settings.enable_hitl:
        logger.info("HITL disabled, auto-approving request")
        return ApprovalResponse(
            decision=ApprovalDecision.APPROVE,
            feedback="Auto-approved (HITL disabled)",
        )

    # Auto-approve low-risk decisions if configured
    if settings.auto_approve_low_risk and risk_level == RiskLevel.LOW:
        logger.info("Auto-approving low-risk decision")
        return ApprovalResponse(
            decision=ApprovalDecision.APPROVE,
            feedback="Auto-approved (low risk)",
        )

    # Create approval request
    request = ApprovalRequest(
        decision_type=decision_type,
        risk_level=risk_level,
        requesting_agent=requesting_agent,
        context=context,
        recommendation=recommendation,
        rationale=rationale,
    )

    # Display request
    display_approval_request(request)

    # Get human input
    console.print("\n[bold]Available Actions:[/]")
    console.print("  [green]approve[/] - Accept recommendation as-is")
    console.print("  [cyan]approve_with_changes[/] - Approve with modifications")
    console.print("  [red]reject[/] - Reject and provide alternative guidance")
    console.print("  [yellow]defer[/] - Request more information\n")

    decision_str = Prompt.ask(
        "Your decision",
        choices=["approve", "approve_with_changes", "reject", "defer"],
        default="defer",
    )

    decision = ApprovalDecision(decision_str)

    # Get feedback if not simple approval
    feedback = None
    if decision != ApprovalDecision.APPROVE:
        console.print("\n[bold]Please provide feedback or guidance:[/]")
        feedback = Prompt.ask("Feedback")

    # Get modifications if approving with changes
    modifications = None
    if decision == ApprovalDecision.APPROVE_WITH_CHANGES:
        console.print(
            "\n[dim]Enter modifications as key=value pairs (press Enter when done)[/]"
        )
        modifications = {}
        while True:
            mod = Prompt.ask("Modification (or press Enter to finish)", default="")
            if not mod:
                break
            if "=" in mod:
                key, value = mod.split("=", 1)
                modifications[key.strip()] = value.strip()

    response = ApprovalResponse(
        decision=decision,
        feedback=feedback,
        modifications=modifications,
    )

    # Log the decision
    logger.info(
        f"Human decision: {decision.value}"
        + (f" - {feedback}" if feedback else "")
    )

    return response


def request_simple_confirmation(message: str, default: bool = True) -> bool:
    """Request a simple yes/no confirmation from the user."""
    settings = get_settings()

    if not settings.enable_hitl:
        return default

    console.print(f"\n[bold yellow]❓ {message}[/]")
    response = Prompt.ask(
        "Continue?",
        choices=["y", "n"],
        default="y" if default else "n",
    )

    return response.lower() == "y"


def collect_human_input(prompt_text: str, required: bool = True) -> str:
    """Collect free-form input from the user."""
    console.print(f"\n[bold cyan]📝 {prompt_text}[/]")

    while True:
        response = Prompt.ask("Input")
        if response or not required:
            return response
        console.print("[red]Input is required. Please try again.[/]")
