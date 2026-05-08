"""Pull required Ollama models."""

import subprocess
import sys

from rich.console import Console

from src.config import get_settings

console = Console()


def pull_model(model_name: str) -> bool:
    """
    Pull an Ollama model.

    Args:
        model_name: Name of the model to pull

    Returns:
        True if successful
    """
    console.print(f"\n[yellow]Pulling model: {model_name}[/]")

    try:
        result = subprocess.run(
            ["ollama", "pull", model_name],
            capture_output=True,
            text=True,
            check=True,
        )

        console.print(f"[green]✓ Successfully pulled {model_name}[/]")
        return True

    except subprocess.CalledProcessError as e:
        console.print(f"[red]✗ Failed to pull {model_name}[/]")
        console.print(f"Error: {e.stderr}")
        return False
    except FileNotFoundError:
        console.print(
            "[red]✗ Ollama not found. Please install Ollama first.[/]"
        )
        return False


def main() -> None:
    """Pull all required models."""
    console.print("[bold cyan]Agentic SDLC - Model Setup[/]\n")

    settings = get_settings()

    models_to_pull = [settings.ollama_model]

    # Add role-specific models if different
    role_models = [
        settings.model_program_manager,
        settings.model_chief_engineer,
        settings.model_requirements,
        settings.model_architecture,
    ]

    for model in role_models:
        if model and model not in models_to_pull:
            models_to_pull.append(model)

    console.print(f"[bold]Models to pull:[/]")
    for model in models_to_pull:
        console.print(f"  • {model}")

    success_count = 0
    for model in models_to_pull:
        if pull_model(model):
            success_count += 1

    console.print(f"\n[bold]Results:[/]")
    console.print(f"  Successfully pulled: {success_count}/{len(models_to_pull)}")

    if success_count == len(models_to_pull):
        console.print("\n[bold green]✅ All models ready![/]")
        sys.exit(0)
    else:
        console.print("\n[bold yellow]⚠️  Some models failed to pull[/]")
        sys.exit(1)


if __name__ == "__main__":
    main()
