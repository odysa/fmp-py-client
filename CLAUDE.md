# CLAUDE.md

This file provides guidance for Claude Code when working with this repository.

## Project Overview

`fmp-py-client` is an async Python client for the Financial Modeling Prep (FMP) API, built with httpx. It provides typed responses using TypedDict for all API endpoints.

## Commands

### Development Setup
```bash
uv sync --group dev  # Install dependencies
```

### Linting & Formatting
```bash
uv run ruff check              # Run linter
uv run ruff check --fix        # Auto-fix lint issues
uv run ruff format             # Format code
uv run ruff format --check     # Check formatting without changes
```

### Type Checking
```bash
uv run ty check                # Run ty type checker (from Astral)
```

### Testing
```bash
uv run pytest tests/                                    # Run all tests
uv run pytest tests/ --cov=fmp_py_client               # Run with coverage
uv run pytest tests/ --cov=fmp_py_client --cov-fail-under=80  # Require 80% coverage
```

## Code Style

- Use `ruff` for linting and formatting (configured in pyproject.toml)
- Use `ty` for type checking
- All API methods should have typed return values using TypedDict models from `src/fmp_py_client/models/`
- Async-first design - all API methods are async

## Architecture

- `src/fmp_py_client/_client.py` - Main client class composing all mixins
- `src/fmp_py_client/_base.py` - Base HTTP client with request handling
- `src/fmp_py_client/api/` - API endpoint mixins organized by domain
- `src/fmp_py_client/models/` - TypedDict response models organized by domain
- `src/fmp_py_client/_exceptions.py` - Custom exception classes
- `src/fmp_py_client/_types.py` - Enums (Period, Timeframe)

## CI Requirements

Before committing, ensure:
1. `uv run ruff check` passes
2. `uv run ruff format --check` passes
3. `uv run ty check` passes
4. `uv run pytest tests/` passes with 80%+ coverage
