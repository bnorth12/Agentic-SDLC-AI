"""Main CLI application."""

from __future__ import annotations

import sys

import typer
from rich.console import Console

from src.config import get_settings
from src.graphs.supervisor import build_supervisor_graph, get_kpi_tracker
from src.state.schema import AgentState
from src.utils.logging import setup_logging
from src.utils.tracing import setup_tracing

app = typer.Typer(
    name="agentic-sdlc",
    help="Agentic SDLC AI Organization - Multi-agent systems engineering",
)
console = Console()


@app.command()
def run(
    objective: str = typer.Argument(..., help="Project objective or requirement"),
    max_iterations: int = typer.Option(
        25, "--max-iter", "-m", help="Maximum graph iterations"
    ),
    enable_hitl: bool = typer.Option(True, "--hitl/--no-hitl", help="Enable HITL gates"),
) -> None:
    """Run the agentic SDLC system with a given objective."""

    # Setup logging and tracing
    setup_logging()
    setup_tracing()

    console.print("[bold green]🚀 Agentic SDLC AI Starting...[/]")
    console.print(f"[cyan]Objective:[/] {objective}\n")

    # Build the supervisor graph
    graph = build_supervisor_graph()

    # Create initial state
    initial_state = AgentState(objective=objective)

    # Run the graph
    try:
        config = {"recursion_limit": max_iterations}

        console.print("[yellow]⚙️  Executing workflow...[/]\n")

        result = graph.invoke(initial_state, config=config)

        console.print("\n[bold green]✅ Execution Complete[/]\n")

        # Display results
        console.print("[bold]Requirements Developed:[/]")
        for req_id, req in result.get("requirements", {}).items():
            console.print(f"  • {req_id}: {req.text}")

        console.print(f"\n[bold]Final Phase:[/] {result.get('phase')}")

        if result.get("board_results"):
            console.print("\n[bold]Board Decisions:[/]")
            for board, decision in result["board_results"].items():
                console.print(f"  • {board}: {decision.decision}")

    except Exception as e:
        console.print(f"[bold red]❌ Error:[/] {e}")
        sys.exit(1)


@app.command()
def init_db() -> None:
    """Initialize the PostgreSQL database for checkpointing."""
    from src.state.persistence import get_persistence_manager

    setup_logging()

    console.print("[yellow]Initializing database...[/]")

    try:
        manager = get_persistence_manager()
        manager.setup_database()
        console.print("[bold green]✅ Database initialized successfully[/]")
    except Exception as e:
        console.print(f"[bold red]❌ Error:[/] {e}")
        sys.exit(1)


@app.command()
def config() -> None:
    """Display current configuration."""
    setup_logging()
    settings = get_settings()

    console.print("[bold]Current Configuration:[/]\n")
    console.print(f"Environment: {settings.app_env}")
    console.print(f"Log Level: {settings.log_level}")
    console.print(f"Ollama URL: {settings.ollama_base_url}")
    console.print(f"Default Model: {settings.ollama_model}")
    console.print(f"HITL Enabled: {settings.enable_hitl}")
    console.print(f"Tracing Enabled: {settings.enable_tracing}")


@app.command()
def version() -> None:
    """Display version information."""
    console.print("[bold]Agentic SDLC AI[/]")
    console.print("Version: 0.1.0")
    console.print("Status: Active development beyond the original Phase 0 baseline")


@app.command()
def status() -> None:
    """Display runtime status, checkpoint sessions, and KPI summary."""
    setup_logging()
    settings = get_settings()

    from src.state.persistence import get_persistence_manager

    manager = get_persistence_manager()
    tracker = get_kpi_tracker()

    console.print("[bold]Runtime Status:[/]")
    console.print(f"Environment: {settings.app_env}")
    console.print(f"HITL Enabled: {settings.enable_hitl}")
    console.print(f"Tracing Enabled: {settings.enable_tracing}")

    sessions = manager.list_checkpoint_sessions()
    console.print(f"Checkpoint Sessions: {len(sessions)}")
    if sessions:
        for session_id in sessions:
            console.print(f"  • {session_id}")

    report = tracker.get_metrics_report()
    summary = report.get("summary", {})
    console.print("\n[bold]Governance KPI Summary:[/]")
    console.print(f"Gate Pass Rate: {summary.get('gate_pass_rate', '0.0%')}")
    console.print(
        f"First Attempt Success: {summary.get('first_attempt_success_rate', '0.0%')}"
    )
    console.print(
        f"Gates Attempted: {summary.get('gates_attempted', 0)}"
    )


@app.command()
def dashboard() -> None:
    """Launch the observability dashboard."""
    setup_logging()

    try:
        from src.observability import run_dashboard

        console.print("[cyan]Launching observability dashboard...[/]")
        console.print("[dim]Dashboard available at: http://localhost:8501[/]\n")
        run_dashboard()
    except ImportError:
        console.print(
            "[bold red]❌ Dashboard dependencies not installed[/]\n"
            "[yellow]Install with:[/] pip install -e '.[ui]'"
        )
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]❌ Error launching dashboard:[/] {e}")
        sys.exit(1)


if __name__ == "__main__":
    app()
