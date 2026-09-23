# Connor Coding Lab — Multi-Repository Fresh-Clone Acceptance

This checklist is evidence for repository readiness. Do not mark an item complete unless it was actually run or inspected.

## 1. Target topology

Use a clean rehearsal location:

```text
~/Projects/Connor/
|
|-- connor-coding-lab/
|
`-- projects/
    |-- python-basics/
    `-- snake-game/
```

Clone each repository independently. Do not use Git submodules and do not copy old `.venv` directories.

Expected preparation repositories:

- `WebshopCompany/connor-coding-lab`
- `WebshopCompany/python-basics`
- `WebshopCompany/snake-game`

## 2. Git independence

From each repository, run:

```bash
git status
git branch --show-current
git log -5 --oneline --decorate
git remote -v
```

Confirm:

- all three working trees are clean;
- each repository has its own `.git` directory;
- each repository points at the expected remote;
- Python Basics contains Connor's original three-commit lineage;
- Snake contains Connor's original ten-commit lineage;
- changing Git state in one repository does not change the others.

## 3. Mission Control

From `~/Projects/Connor/connor-coding-lab`:

```bash
./scripts/check-repo-policy.sh
./scripts/lab projects
./scripts/lab doctor
./scripts/lab status
```

Confirm:

- doctor finds both independent project repositories;
- no hidden clone/install/sync/repair occurs;
- the canonical learner tracker remains in Mission Control;
- `python-basics/` and `snake-game/` are not embedded Git project copies inside Mission Control.

## 4. Python Basics

From `~/Projects/Connor/projects/python-basics`:

```bash
uv sync --locked
uv run python --version
uv run ruff check .
uv run pytest
printf 'Minecraft\n' | uv run python src/python_basics/hello.py
```

Record the Python version and test result.

## 5. Pygame Snake

From `~/Projects/Connor/projects/snake-game`:

```bash
uv sync --locked
uv run python --version
uv run python -m compileall -q src
```

Then run both graphical variants separately:

```bash
uv run python src/snake_game/classic_snake.py
uv run python src/snake_game/__init__.py
```

For both games confirm:

- a window opens;
- keyboard input works;
- gameplay visibly updates;
- the game can be exited normally;
- the window is usable on the actual display.

Do not claim the 1400×950 current game is Dell-compatible until checked on the actual Dell panel.

## 6. Browser Snake

From `~/Projects/Connor/projects/snake-game`:

```bash
uv run python -m http.server 8000 --directory web
```

Open `http://127.0.0.1:8000/`.

Confirm page load, controls, restart behaviour and no obvious browser-console runtime error. Stop the server with Ctrl+C.

## 7. VS Code / Antigravity cockpit

Open:

`~/Projects/Connor/connor-coding-lab/Connor-Coding-Lab.code-workspace`

Confirm Explorer shows exactly these three roots:

- Mission Control;
- Python Basics;
- Snake Game.

Confirm:

- each Source Control repository is independent;
- the integrated Mission Control terminal starts neutral;
- Python/Snake tasks execute from their named project roots;
- `/start` discovers current Mission Control skills and reads the canonical tracker;
- Antigravity can inspect the independent project roots before proposing current commands.

## 8. CI and safety

Confirm the latest `main` CI is green in all three repositories.

Confirm:

- no password, token, API key, private key or secret `.env` file is tracked;
- no ordinary development command requires `sudo`;
- generated environments and caches remain untracked.

A current-tree check is not a complete historical secret scan.

## 9. Browser showcases

From Mission Control, use:

```bash
./scripts/lab menu
```

Validate the AI-built browser demonstrations separately from Connor's historical project evidence.

## Definition of Done

The multi-repository environment is accepted only when all applicable checks above pass from a clean target-layout rehearsal and remaining exceptions are explicitly recorded.
