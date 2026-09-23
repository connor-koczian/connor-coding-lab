# Recovery and Rebuild Notes — Parent/Admin

The repository and Git history are the source of truth. A copied virtual environment is not.

## If the laptop is replaced or rebuilt

1. install/configure Git, VS Code and `uv`;
2. create `~/Projects/Connor/projects`;
3. clone Mission Control to `~/Projects/Connor/connor-coding-lab`;
4. clone Python Basics and Snake Game independently under `~/Projects/Connor/projects/`;
5. run `uv sync --locked` inside each Python project;
6. open the canonical multi-root workspace;
7. run the fresh-clone acceptance checklist.

Do not restore old `.venv` directories.

## What Git can recover

Committed files and branches pushed to GitHub can be restored from GitHub.

Uncommitted local changes cannot be recovered from GitHub merely because the repository was cloned previously.

Teach Connor to use meaningful commits and push completed save points.

## If a project environment is broken

From that project directory, inspect:

    git status
    uv run python --version

If the repository files are clean, recreate the environment through the project's normal `uv sync` workflow rather than manually modifying site-packages.

Do not use raw `pip` as a repair shortcut.

## If the repository itself looks wrong

Stop before deleting anything.

Record:

    pwd
    git status
    git branch --show-current
    git log --oneline --decorate -10

Then compare with the current GitHub state.

Do not use `git reset --hard`, `git clean -fd` or force-push as a first-line recovery action.
