# AGENTS.md for lab0-engine

## Overview
lab0 is a headless, programmable design and simulation engine spanning three domains: Mechanical, Electronics, and Biomedical. Designed for AI agents to parametrically generate designs, run free in-silico validations, and rapidly iterate before dispatching to physical fabrication or wet labs.

## Development

### Setup
```bash
uv sync
```

### Run
```bash
uv run python -m src
```

### Test
```bash
uv run pytest
```

### Lint
```bash
uv run ruff check .
```

### Type Check
```bash
uv run mypy .
```

## Deployment
Designed to run as a local or cloud-based simulation engine. Uses cadquery, trimesh, PySpice, ngspice, RDKit, and COBRApy for multi-domain simulation.
