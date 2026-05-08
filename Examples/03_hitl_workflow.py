"""Example 03: Human-in-the-loop workflow.

This example demonstrates:
1. HITL approval request
2. Human feedback collection
3. Decision modification based on feedback
"""

from rich.console import Console

from src.utils.hitl import (
    ApprovalDecision,
    RiskLevel,
    collect_human_input,
    request_human_approval,
    request_simple_confirmation,
)
from src.utils.logging import setup_logging

console = Console()


def main() -> None:
    """Demonstrate human-in-the-loop interactions."""
    setup_logging()

    console.print("\n[bold cyan]═══ Example 03: Human-in-the-Loop ═══[/]\n")

    # Example 1: Simple confirmation
    console.print("[bold]Example 1: Simple Confirmation[/]")
    if request_simple_confirmation("Proceed with requirements development?"):
        console.print("[green]✓ User confirmed[/]")
    else:
        console.print("[yellow]User declined[/]")

    console.print()

    # Example 2: Approval request
    console.print("[bold]Example 2: Approval Request[/]\n")

    response = request_human_approval(
        decision_type="Architecture Baseline",
        risk_level=RiskLevel.MEDIUM,
        requesting_agent="architecture_agent",
        context="Architecture has been developed for the distributed task system. "
        "It includes 4 major components with well-defined interfaces.",
        recommendation="Approve architecture and proceed to detailed design",
        rationale="All requirements are traced, interfaces are documented, "
        "and the design follows established patterns. Risk is manageable.",
    )

    console.print(f"\n[bold]Decision:[/] {response.decision.value}")
    if response.feedback:
        console.print(f"[bold]Feedback:[/] {response.feedback}")
    if response.modifications:
        console.print(f"[bold]Modifications:[/] {response.modifications}")

    console.print()

    # Example 3: Collect detailed input
    console.print("[bold]Example 3: Collect Detailed Input[/]\n")

    user_input = collect_human_input(
        "Describe any additional requirements or constraints:", required=False
    )

    if user_input:
        console.print(f"\n[green]✓ Received input:[/] {user_input}")
    else:
        console.print("\n[yellow]No input provided[/]")

    console.print("\n[bold green]✅ Example complete![/]\n")


if __name__ == "__main__":
    main()
