# Connor Coding Lab

Connor's long-term programming, game-development and Git learning repository.

The goal is progressive independence: understand → build → run → break → debug → improve → test → commit → explain.

## Start here

Connor should open:

- `00-CONNOR-HQ/00-START-HERE-CONNOR.md`
- `00-CONNOR-HQ/LEARNING-PATH.md`
- `00-CONNOR-HQ/GIT-PLAYBOOK.md`

Repository-wide AI guidance lives in:

- `AI-CODING-RULES.md`
- `GEMINI.md`

Parent/admin material lives under `docs/admin/`.

## Repository layout

### `00-CONNOR-HQ/`

Connor-facing missions, learning progression, Git guidance and achievements.

### `python-basics/`

Small Python programs for syntax, control flow, functions, debugging, Ruff and the first simple tests.

### `snake-game/`

Connor's first substantial historical game project. Its imported Git history and save points are intentionally preserved.

The current Pygame game, Classic Snake and historical browser Snake remain here so they can be compared rather than rewritten into a new architecture.

### `experiments/`

Small disposable investigations. Experiments may fail; important ideas should graduate into a real project deliberately.

### `web-playground/`

New HTML, CSS and JavaScript learning work. Historical browser Snake remains under `snake-game/web/`.

### `neon-city/`

Reserved for the next flagship project. It should be introduced in a separate reviewed change rather than generated all at once.

## Python environments

Each Python project owns its own `pyproject.toml` and `uv.lock`.

There is intentionally no root Python workspace yet. That keeps project boundaries visible while Connor is learning.

The imported projects currently declare Python 3.10. Python 3.12 is the intended future baseline, but changing interpreter requirements and lock files is a separate migration that must be run and validated before integration.

Do not copy old `.venv` directories between computers. Recreate environments with `uv sync`.

## Git workflow

Treat `main` as stable.

Before work:

    cd ~/Projects/connor-coding-lab
    git status

For a bounded mission or feature:

    git switch main
    git pull --ff-only
    git switch -c mission/short-name

Inspect changes:

    git status
    git diff

Stage only the intended files:

    git add path/to/file
    git diff --cached

Then commit a useful save point.

## Safety

Ordinary development must not require `sudo`.

Never commit passwords, tokens, API keys, SSH private keys or secret `.env` values.

## Repository ownership

During preparation this repository is hosted under `WebshopCompany`.

The intended long-term home is `connor-koczian/connor-coding-lab`. Any handover must preserve the imported Python Basics and Snake histories.

The repository must not be described as Dell-ready until the fresh-clone acceptance checks in `docs/admin/ACCEPTANCE-CHECKLIST.md` have actually passed.
