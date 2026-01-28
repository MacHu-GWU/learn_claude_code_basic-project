# CLAUDE.md

## Role

- @./claude/teaching.md

## Overview

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Quick Reference

For app spec, see [app-spec](app-spec.md)

## Prerequisites

- Python 3.12
- `uv` package manager (installed via `mise`)
- Virtual environment

## Key Commands

All commands use `mise` task runner (defined in `mise.toml`). The `.venv` contains a Python interpreter, so scripts can be run as `.venv/bin/python`.

**Environment Setup:**

- `mise run venv-create` - Create virtual environment
- `mise run inst` - Install all dependencies (runtime + dev + test + doc)

## Dependency Management

- `pyproject.toml` defines all dependencies with version constraints
- `uv` handles dependency resolution and lockfile (`uv.lock`)
- Virtual environment in `.venv/` managed via `mise`

## Python Version & Environment

- **Python Version**: 3.12 (specified in `pyproject.toml` and `mise.toml`)
- **Virtual Environment**: `.venv/` directory (created by `mise run venv-create`)
- **Python Executable**: `.venv/bin/python`
- **Package Manager**: `uv` (latest version via `mise`)
