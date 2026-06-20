# kadavul-gpt

> First of many small LLMs build on indigenous topics. Also helpful to learn.

## Development Roadmap

- Part 1
    - Environment Setup & Data Curation
- Part 2
    - Tokenizer & PyTorch Data Loader
- Part 3
    - Coding the Tiny Transformer Architecture
- Part 4    
    - Model Training & Text Generation Loop

## Project tracking on JIRA

- [JRMJAVV](https://jrmjavv.atlassian.net?continue=https%3A%2F%2Fjrmjavv.atlassian.net%2Fwelcome%2Fsoftware&atlOrigin=eyJpIjoiYjVmZDYxNzg3MzcxNGY1OTgxMzkxOWIxMmRiMDU0NWEiLCJwIjoiaiJ9)

---

## UV setup - 🚀 The Fast-Track `uv` Project Checklist

Here is your fast-track **`uv` Project Cheatsheet**. Save this as a quick reference guide before kicking off any new application.

---

### Phase 1: Initialize the Project

Navigate to your empty project folder (or let `uv` create it for you) and pick your target Python version.

```bash
# Initialize inside an existing directory
uv init

# OR: Create and initialize a new directory all at once
uv init my-new-app && cd my-new-app

```

### Phase 2: Lock Your Python Version

Ensure everyone (and your future self) runs the exact same Python runtime. `uv` will automatically download this binary on the fly if your system doesn't have it.

```bash
# Pin the project to a specific Python version (creates a .python-version file)
uv python pin 3.12

```

### Phase 3: Add Dependencies (The Venv creates itself here)

You do **not** need to manually run `uv venv`. The very first time you add a package, `uv` instantly provisions the `.venv` and updates your `pyproject.toml` and `uv.lock`.

```bash
# Production dependencies
uv add fastapi uvicorn

# Development dependencies (testing, linting, formatting)
uv add --dev pytest ruff

```

### Phase 4: Run Your Code (No Activation Needed)

Skip `source .venv/bin/activate`. Use `uv run` to safely execute scripts or binaries inside your isolated workspace context.

```bash
# Run a specific script
uv run main.py

# Run a module or test suite
uv run pytest

# Boot up a local server
uv run uvicorn main:app --reload

```

---

## 🛠️ The Essential `uv` Cheat Sheet (Quick Reference)

### Dependency Management

* **Remove a package:** `uv remove requests`
* **Sync environment from lockfile:** `uv sync` *(Use this when pulling down someone else's repo)*
* **Inspect dependency tree:** `uv tree`
* **Upgrade a single package:** `uv lock --upgrade-package fastapi`

### Global Tools (The `pipx` Replacement)

Run CLI utilities globally without cluttering your project workspace or system environment.

* **Run a tool temporarily (ephemeral):** `uvx ruff format .`
* **Install a tool permanently to your system:** `uv tool install black`

### Legacy/Drop-in Mode

If you are forced to work on an older codebase with a loose virtual environment and a `requirements.txt` file:

* **Create environment:** `uv venv`
* **Traditional install:** `uv pip install -r requirements.txt`
* **Export lockfile to raw text:** `uv export --format requirements-txt > requirements.txt`