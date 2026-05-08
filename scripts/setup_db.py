"""Database setup script."""

import sys

from rich.console import Console

from src.config import get_settings
from src.state.persistence import get_persistence_manager
from src.utils.logging import setup_logging

console = Console()


def main() -> None:
    """Initialize the database schema."""
    setup_logging()

    console.print("[bold cyan]Agentic SDLC - Database Setup[/]\n")

    settings = get_settings()
    console.print(f"Database URL: {settings.postgres_url}")

    try:
        console.print("\n[yellow]Creating database schema...[/]")

        manager = get_persistence_manager()
        manager.setup_database()

        console.print("[bold green]✅ Database initialized successfully![/]\n")

        console.print("[dim]You can now run the examples or CLI commands.[/]")

    except Exception as e:
        console.print(f"\n[bold red]❌ Error initializing database:[/]\n{e}\n")
        console.print("[dim]Make sure PostgreSQL is running (docker compose up -d)[/]")
        sys.exit(1)


if __name__ == "__main__":
    main()
