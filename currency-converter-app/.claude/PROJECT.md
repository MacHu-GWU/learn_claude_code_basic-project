# Project Overview

A simple streamlit app for converting currencies based on predefined exchange rates.

## Development Setup

**Core Configuration Files:**
- `mise.toml` - Project tasks and tool versions (Claude Code, Python 3.12, uv)
- `pyproject.toml` - Dependencies and project metadata
- `.venv/` - Virtual environment directory
- `.venv/bin/python` - Python executable (always use for running Python)

**Package Manager:** `uv` (via mise)

## Available Tasks

Run `mise tasks` to see all available commands. Current tasks:

- `mise run venv-create` - ✨ Create Python virtual environment (.venv)
- `mise run venv-remove` - 💥 Remove Python virtual environment folder (.venv)
- `mise run inst` - 💾 Install Python dependencies (dev, test, doc, etc.) via uv
- `mise run app` - 🚀 Run Streamlit app locally
