# Connor Coding Lab — Fresh-Clone Acceptance

This checklist is evidence for repository readiness. Do not mark an item complete unless it was actually run or inspected.

## 1. Git and repository

From a fresh clone:

    cd ~/Projects/connor-coding-lab
    git status
    git log --oneline --all --decorate -20

Confirm:

- the working tree is clean;
- `main` is the expected branch;
- imported Python Basics and Snake history is visible;
- no generated `.venv`, cache or secret file has been committed.

For a pre-merge PR test, switch explicitly to the candidate branch before running the remaining checks.

## 2. Python Basics

    cd ~/Projects/connor-coding-lab/python-basics
    uv sync
    uv run python src/python_basics/hello.py
    uv run python-basics
    uv run ruff check .
    uv run pytest

Record the Python version used by `uv`:

    uv run python --version

## 3. Pygame Snake

    cd ~/Projects/connor-coding-lab/snake-game
    uv sync
    uv run python --version
    uv run python src/snake_game/classic_snake.py
    uv run python src/snake_game/__init__.py

For both games confirm:

- a window opens;
- input works;
- the game can be exited normally;
- the window is usable on the actual display.

Do not claim the 1400×950 current game is Dell-compatible until this has been checked on the actual panel.

## 4. Browser Snake

From `snake-game/`:

    uv run python -m http.server 8000 --directory web

Open `http://127.0.0.1:8000/` in the browser.

Confirm:

- the page loads;
- keyboard controls work;
- restarting works;
- the browser console has no obvious runtime errors.

Stop the local server with Ctrl+C.

## 5. VS Code

Open the repository root in VS Code.

Confirm:

- the integrated terminal starts at the repository root;
- Python and Ruff extension recommendations are sensible;
- no project depends on a hidden machine-specific path;
- Connor can run the documented commands without admin privileges.

## 6. Neon City

Do not mark this complete until a reviewed `neon-city/` starter exists.

Acceptance will require its documented setup, run, lint and test commands to work from a fresh clone.

## 7. Security and cleanliness

Confirm:

- no password, token, API key, private key or secret `.env` file is tracked;
- no ordinary development command requires `sudo`;
- generated environments and caches remain untracked.

The GitHub current-tree review is not a complete historical secret scan. Before final transfer, run an appropriate local history-aware secret scan if tooling is available.

## Definition of Done

The repository is Dell-ready only when every applicable section above has passed on a clean test clone and remaining exceptions are explicitly recorded.
