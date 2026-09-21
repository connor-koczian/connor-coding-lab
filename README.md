# Connor Coding Lab

Connor's long-term programming, game-development and Git learning workspace.

This repository is designed to grow with Connor from beginner projects into progressively more structured software and games. The goal is not to let AI build everything for him; the goal is for Connor to understand, change, test and save what he builds.

## Start here

Connor: open `00-CONNOR-HQ/00-START-HERE-CONNOR.md`.

Then use:

- `LEARNING-PATH.md` — what to learn next
- `GIT-PLAYBOOK.md` — how to save and manage work
- `AI-CODING-RULES.md` — how to use Antigravity as a useful pair programmer
- `00-CONNOR-HQ/` — missions and challenges

## Current projects

### python-basics

Small Python experiments. This is where syntax, variables, input/output, conditions, loops and functions should be learned before they disappear inside larger games.

### snake-game

Connor's first substantial game project. Its history is intentionally preserved, including the Classic Snake save point and later Fruit Kingdom / Championship versions.

### experiments

Small throwaway investigations. It is fine for these to fail.

### web-playground

HTML, CSS and JavaScript experiments.

## Next game track: Neon City

`00-CONNOR-HQ/MISSION-06-START-NEON-CITY.md` introduces an original top-down open-world game project.

The inspiration is the *kind* of systems found in games Connor enjoys — exploration, missions, vehicles, upgrades, maps and arena challenges — without copying GTA, Fortnite, their assets, characters or worlds.

## Developer workflow

Before changing code:

```bash
git status
git pull --ff-only
```

For a new piece of work:

```bash
git switch -c mission/short-name
```

Inspect changes:

```bash
git status
git diff
```

Save a checkpoint:

```bash
git add <files>
git commit -m "Explain what changed"
```

Python projects use `uv`. Do not use raw `pip` as the normal project workflow.

## Safety

Connor works as a normal non-admin Linux user.

Ordinary coding must not require `sudo`. If system software needs installing, ask Apa/Geza.

Never commit passwords, tokens, API keys, private keys or secret `.env` files.

## Repository ownership

During preparation this repository may be hosted temporarily under `WebshopCompany`. The intended long-term home is Connor's own GitHub account.

Existing history must be preserved during that handover.
