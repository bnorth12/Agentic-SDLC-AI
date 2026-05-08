"""Example 02: Architecture review board workflow.

This example demonstrates:
1. Requirements to architecture transition
2. Architecture agent developing design
3. Architecture Review Board evaluation
4. Board voting and decision making
"""

from rich.console import Console

from src.agents import ArchitectureAgent, RequirementsAgent
from src.boards import ArchitectureReviewBoard
from src.state.schema import AgentState, Phase, Requirement
from src.utils.logging import setup_logging

console = Console()


def main() -> None:
    """Run an architecture review board workflow."""
    setup_logging()

    console.print("\n[bold cyan]═══ Example 02: Architecture Review Board ═══[/]\n")

    # Create a state with existing requirements
    state = AgentState(
        objective="Build a distributed task scheduling system",
        phase=Phase.ARCHITECTURE,
        requirements={
            "REQ-001": Requirement(
                id="REQ-001",
                text="System shall support distributed task execution across multiple nodes",
                category="functional",
                priority="critical",
                verification_method="test",
                created_by="requirements_agent",
            ),
            "REQ-002": Requirement(
                id="REQ-002",
                text="System shall provide fault tolerance with automatic failover",
                category="non-functional",
                priority="high",
                verification_method="test",
                created_by="requirements_agent",
            ),
            "REQ-003": Requirement(
                id="REQ-003",
                text="System shall scale to handle 10,000 concurrent tasks",
                category="non-functional",
                priority="high",
                verification_method="analysis",
                created_by="requirements_agent",
            ),
        },
    )

    console.print("[bold]Objective:[/] Build a distributed task scheduling system")
    console.print(f"[bold]Requirements:[/] {len(state.requirements)} defined\n")

    # Run architecture agent
    console.print("[yellow]Running Architecture Agent...[/]")
    arch_agent = ArchitectureAgent()
    updates = arch_agent(state)

    # Update state
    for key, value in updates.items():
        setattr(state, key, value)

    console.print("[green]✓ Architecture developed[/]\n")

    # Display architecture
    if state.architecture:
        console.print("[bold]Architecture Overview:[/]")
        console.print(f"  {state.architecture.get('overview')}")
        console.print(f"\n[bold]Components:[/]")
        for comp in state.architecture.get("components", []):
            console.print(f"  • {comp['name']}: {comp['responsibility']}")

    # Convene Architecture Review Board
    console.print("\n[yellow]Convening Architecture Review Board...[/]\n")

    board = ArchitectureReviewBoard()
    decision = board.evaluate(state, state.architecture)

    # Display board decision
    console.print("[bold green]═══ Board Decision ═══[/]\n")
    console.print(f"[bold]Decision:[/] {decision.decision.upper()}")
    console.print(f"\n[bold]Votes:[/]")
    for member, vote in decision.votes.items():
        console.print(f"  • {member}: {vote}")

    console.print(f"\n[bold]Rationale:[/]")
    console.print(decision.rationale)

    if decision.conditions:
        console.print(f"\n[bold yellow]Conditions:[/]")
        for condition in decision.conditions:
            console.print(f"  • {condition}")

    console.print("\n[bold green]✅ Example complete![/]\n")


if __name__ == "__main__":
    main()
