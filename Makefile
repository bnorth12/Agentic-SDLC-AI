# Makefile for Agentic SDLC AI

.PHONY: help setup install test lint format clean run-example health check-db pull-models

help:
    @echo "Agentic SDLC AI - Development Commands"
    @echo ""
    @echo "Setup:"
    @echo "  make setup        - Complete first-time setup"
    @echo "  make install      - Install Python dependencies"
    @echo "  make pull-models  - Download Ollama models"
    @echo ""
    @echo "Development:"
    @echo "  make test         - Run tests"
    @echo "  make lint         - Run linters"
    @echo "  make format       - Format code"
    @echo "  make health       - Check system health"
    @echo ""
    @echo "Running:"
    @echo "  make run-example  - Run basic example"
    @echo "  make docker-up    - Start Docker services"
    @echo "  make docker-down  - Stop Docker services"

setup: docker-up install check-db pull-models health
    @echo "✅ Setup complete!"

install:
    @echo "📦 Installing dependencies..."
    pip install -e ".[dev]"

docker-up:
    @echo "🐳 Starting Docker services..."
    docker compose -f docker/docker-compose.yml up -d

docker-down:
    @echo "🛑 Stopping Docker services..."
    docker compose -f docker/docker-compose.yml down

check-db:
    @echo "🗄️  Initializing database..."
    python scripts/setup_db.py

pull-models:
    @echo "🤖 Pulling Ollama models..."
    python scripts/pull_models.py

health:
    @echo "🏥 Running health check..."
    python scripts/health_check.py

test:
    @echo "🧪 Running tests..."
    pytest

test-cov:
    @echo "🧪 Running tests with coverage..."
    pytest --cov=src --cov-report=html --cov-report=term

lint:
    @echo "🔍 Running linters..."
    ruff check src tests examples scripts
    mypy src

format:
    @echo "✨ Formatting code..."
    ruff check --fix src tests examples scripts
    ruff format src tests examples scripts

run-example:
    @echo "🚀 Running basic example..."
    python examples/01_basic_requirement.py

run-cli:
    @echo "🚀 Running CLI..."
    python -m src.cli.main --help

clean:
    @echo "🧹 Cleaning up..."
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
    rm -rf htmlcov/ .coverage

.DEFAULT_GOAL := help
