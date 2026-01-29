# Project Overview

> One-sentence description of what this mini project does.

## Development Environment

### Python Version & Runtime

- **Python Version**: 3.12 (specified in `pyproject.toml` and `mise.toml`)
- **Virtual Environment**: `.venv/` directory (created by `mise run venv-create`)
- **Python Executable**: `.venv/bin/python`
- **Package Manager**: `uv` (latest version via `mise`)

### Dependency Management

- `pyproject.toml` defines all dependencies with version constraints
- `uv` handles dependency resolution and lockfile (`uv.lock`)
- Virtual environment in `.venv/` managed via `mise`

## Key Commands

All commands use `mise` task runner (defined in `mise.toml`). Run `mise tasks` to see all available commands.

### Environment Setup

- `mise run venv-create` - Create virtual environment
- `mise run inst` - Install all dependencies (runtime + dev + test + doc)
