"""System health check script."""

import subprocess
import sys
from urllib.parse import urlparse

import psycopg
import requests
from rich.console import Console
from rich.table import Table

from src.config import get_settings

console = Console()


def check_ollama() -> bool:
    """Check if Ollama is accessible."""
    settings = get_settings()

    try:
        response = requests.get(
            f"{settings.ollama_base_url}/api/tags",
            timeout=5,
        )
        if response.status_code == 200:
            models = response.json().get("models", [])
            return True
        return False
    except Exception:
        return False


def check_postgres() -> bool:
    """Check if PostgreSQL is accessible."""
    settings = get_settings()

    try:
        conn = psycopg.connect(settings.postgres_url)
        conn.close()
        return True
    except Exception:
        return False


def check_docker() -> bool:
    """Check if Docker containers are running."""
    try:
        result = subprocess.run(
            ["docker", "ps"],
            capture_output=True,
            text=True,
            check=True,
        )
        return "ollama" in result.stdout and "postgres" in result.stdout
    except Exception:
        return False


def main() -> None:
    """Run health checks."""
    console.print("[bold cyan]Agentic SDLC - System Health Check[/]\n")

    # Create results table
    table = Table(title="System Status")
    table.add_column("Component", style="cyan")
    table.add_column("Status", style="bold")
    table.add_column("Details")

    all_healthy = True

    # Check Docker
    docker_ok = check_docker()
    table.add_row(
        "Docker Containers",
        "[green]✓ Running[/]" if docker_ok else "[red]✗ Not Running[/]",
        "ollama, postgres" if docker_ok else "Run: docker compose up -d",
    )
    all_healthy = all_healthy and docker_ok

    # Check Ollama
    ollama_ok = check_ollama()
    settings = get_settings()
    table.add_row(
        "Ollama API",
        "[green]✓ Accessible[/]" if ollama_ok else "[red]✗ Not Accessible[/]",
        settings.ollama_base_url,
    )
    all_healthy = all_healthy and ollama_ok

    # Check PostgreSQL
    postgres_ok = check_postgres()
    parsed = urlparse(settings.postgres_url)
    db_info = f"{parsed.hostname}:{parsed.port}/{parsed.path.lstrip('/')}"
    table.add_row(
        "PostgreSQL",
        "[green]✓ Connected[/]" if postgres_ok else "[red]✗ Connection Failed[/]",
        db_info,
    )
    all_healthy = all_healthy and postgres_ok

    # Check Python dependencies
    try:
        import langgraph
        import langchain
        import pydantic

        deps_ok = True
        deps_info = "All installed"
    except ImportError:
        deps_ok = False
        deps_info = "Run: pip install -e ."

    table.add_row(
        "Python Dependencies",
        "[green]✓ Installed[/]" if deps_ok else "[red]✗ Missing[/]",
        deps_info,
    )
    all_healthy = all_healthy and deps_ok

    console.print(table)

    # Print summary
    if all_healthy:
        console.print("\n[bold green]✅ All systems operational![/]")
        console.print("\n[dim]You're ready to run examples:[/]")
        console.print("  python examples/01_basic_requirement.py")
        sys.exit(0)
    else:
        console.print("\n[bold yellow]⚠️  Some systems are not ready[/]")
        console.print("\n[dim]Setup steps:[/]")
        if not docker_ok:
            console.print("  1. docker compose up -d")
        if not deps_ok:
            console.print("  2. pip install -e .")
        if not postgres_ok:
            console.print("  3. python scripts/setup_db.py")
        console.print("  4. python scripts/pull_models.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
