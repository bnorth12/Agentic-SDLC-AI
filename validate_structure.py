"""Quick validation that project structure is complete (no imports needed)."""

import os
from pathlib import Path


def check_file(path: str) -> bool:
    """Check if a file exists."""
    exists = Path(path).exists()
    symbol = "✅" if exists else "❌"
    print(f"  {symbol} {path}")
    return exists


def main():
    print("🔍 Validating Agentic SDLC AI Structure\n")

    all_good = True

    print("📁 Core Modules:")
    files = [
        "src/__init__.py",
        "src/config/settings.py",
        "src/config/prompts.py",
        "src/agents/base_agent.py",
        "src/agents/program_manager.py",
        "src/agents/requirements_agent.py",
        "src/state/schema.py",
        "src/state/persistence.py",
        "src/graphs/supervisor.py",
        "src/boards/base_board.py",
        "src/boards/architecture_review.py",
        "src/tools/file_operations.py",
        "src/utils/logging.py",
        "src/utils/hitl.py",
        "src/cli/main.py",
    ]
    for f in files:
        all_good &= check_file(f)

    print("\n📝 Examples:")
    examples = [
        "examples/01_basic_requirement.py",
        "examples/02_review_board.py",
        "examples/03_hitl_workflow.py",
    ]
    for f in examples:
        all_good &= check_file(f)

    print("\n🔧 Scripts:")
    scripts = [
        "scripts/setup_db.py",
        "scripts/pull_models.py",
        "scripts/health_check.py",
    ]
    for f in scripts:
        all_good &= check_file(f)

    print("\n📚 Documentation:")
    docs = [
        "README.md",
        "docs/development-guide.md",
        "docs/testing-strategy.md",
        "docs/ARCHITECTURE_DECISIONS.md",
        "IMPLEMENTATION_SUMMARY.md",
    ]
    for f in docs:
        all_good &= check_file(f)

    print("\n⚙️ Configuration:")
    config = [
        "pyproject.toml",
        ".env.example",
        "Makefile",
        ".pre-commit-config.yaml",
    ]
    for f in config:
        all_good &= check_file(f)

    print("\n🧪 Tests:")
    tests = [
        "tests/conftest.py",
        "tests/test_starter_modules.py",
        "tests/unit/test_base_agent.py",
        "tests/fixtures/__init__.py",
    ]
    for f in tests:
        all_good &= check_file(f)

    print("\n" + "="*60)
    if all_good:
        print("✅ ALL FILES PRESENT - Structure is complete!")
        print("\nNext steps:")
        print("1. Install dependencies: pip install -e \".[dev]\"")
        print("2. Start Docker: docker compose -f docker/docker-compose.yml up -d")
        print("3. Setup database: python scripts/setup_db.py")
        print("4. Run example: python examples/01_basic_requirement.py")
    else:
        print("❌ SOME FILES MISSING - Check above for details")

    print("="*60)


if __name__ == "__main__":
    main()
