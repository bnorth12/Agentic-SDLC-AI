"""Example 01: Basic requirement workflow.

This example demonstrates:
1. Submitting a simple objective
2. Requirements agent developing requirements
3. Board review process
4. Human approval gates (simplified)
"""

from rich.console import Console

from src.graphs.supervisor import build_supervisor_graph
from src.state.schema import AgentState
from src.utils.logging import setup_logging

console = Console()


def main() -> None:
    """Run a basic requirements workflow."""
    # Setup
    setup_logging()

    console.print("\n[bold cyan]═══ Example 01: Basic Requirement Workflow ═══[/]\n")

    # Define objective
    objective = (
        "Build a web application for tracking personal fitness goals "
        "with daily logging, progress charts, and goal reminders"
    )

    console.print(f"[bold]Objective:[/] {objective}\n")

    # Build graph
    console.print("[yellow]Building supervisor graph...[/]")
    graph = build_supervisor_graph()

    # Create initial state
    initial_state = AgentState(objective=objective)

    # Run workflow
    console.print("[yellow]Starting workflow execution...[/]\n")

    config = {"recursion_limit": 15}
    result = graph.invoke(initial_state, config=config)

    # Display results
    console.print("\n[bold green]═══ Results ═══[/]\n")

    console.print(f"[bold]Final Phase:[/] {result['phase']}")
    console.print(f"[bold]Messages:[/]")
    for msg in result.get("messages", []):
        console.print(f"  {msg}")

    console.print(f"\n[bold]Requirements Developed:[/]")
    for req_id, req in result.get("requirements", {}).items():
        console.print(f"\n  [cyan]{req_id}:[/] {req.text}")
        console.print(f"    Category: {req.category}")
        console.print(f"    Priority: {req.priority}")
        console.print(f"    Verification: {req.verification_method}")

    if result.get("board_results"):
        console.print(f"\n[bold]Board Decisions:[/]")
        for board_name, decision in result["board_results"].items():
            console.print(f"\n  [yellow]{board_name}:[/]")
            console.print(f"    Decision: {decision.decision}")
            console.print(f"    Votes: {decision.votes}")

    console.print("\n[bold green]✅ Example complete![/]\n")


if __name__ == "__main__":
    main()
