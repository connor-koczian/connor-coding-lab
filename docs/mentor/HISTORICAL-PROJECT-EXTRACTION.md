# Historical Project Extraction — Phase 8

**Date:** 2026-09-23  
**Mission Control authority:** protected `main` at `9b8ea81ebb49bd2a53d88f2f02bd82ff66014206`

## Purpose

Phase 8 preserves Connor's original Python Basics and Snake histories while establishing each project as an independent Git repository.

The migration deliberately avoided copying directories into fresh repositories with synthetic history.

## Python Basics

Independent repository:

`WebshopCompany/python-basics`

Original Connor lineage:

- `555f124b554cd12a76e47e043a714adaa39a2963` — Start Python basics
- `6f8e29f90e5364a16a075a18b6072abc1f6b4845` — Add hello script and test tools
- `97c51706c44b521f3473c8936f4931850c11ef69` — Ask about favourite video games

Those three commit identities remain unchanged.

Two bounded post-import commits were then added:

- `e6274bed3503119a4e411d56a147cf6dbe9679a6` — Add Python learning README and first test
- `82f11181755839cac40c50419e972f534c0cf634` — Move Python project to 3.12 baseline

Final repository state:

- commit count: **5**
- head: `82f11181755839cac40c50419e972f534c0cf634`
- tree: `91f57117b5cafc2c88c3e86e3dd9bc6d49658706`

The final tree exactly matches the Python subtree in Mission Control at the extraction authority commit.

Validation performed in an isolated staging clone:

- uv-managed Python 3.12.14;
- `uv sync --locked`;
- `uv run ruff check .` — PASS;
- `uv run pytest` — **1 passed**;
- controlled `hello.py` runtime input — PASS;
- final working tree clean.

## Snake Game

Independent repository:

`WebshopCompany/snake-game`

The original ten-commit Connor history from `e93fd9d8130436f134184128627bff2a01746285` through `a31761a0ea3503c71db8eea6d3279ef0bc8ab8ab` remains unchanged.

One bounded post-import commit was added:

- `7d6fa8b0c1b13d1bad14028be3556b4d6035449b` — Move Python project to 3.12 baseline

Final repository state:

- commit count: **11**
- head: `7d6fa8b0c1b13d1bad14028be3556b4d6035449b`
- tree: `43330b81e8afab839ead624f5e0f0f12e1453c5e`

The final tree exactly matches the Snake subtree in Mission Control at the extraction authority commit.

Validation performed in an isolated staging clone:

- uv-managed Python 3.12.14;
- `uv sync --locked`;
- Pygame 2.6.1 import — PASS;
- `python -m compileall -q src` — PASS;
- final working tree clean.

Interactive graphical Snake behaviour was intentionally not claimed by this extraction transaction. That belongs to the subsequent multi-repository ThinkPad rehearsal.

## Independent GitHub verification

After each push, CURRENT GitHub authority was re-fetched independently.

Verified:

- exact extracted head SHA;
- exact final tree SHA;
- exact commit count;
- original Connor commit identities and parent chain;
- private repository state.

Mission Control `main` did not move during the extraction.

## Phase boundary

Phase 8 establishes safe independent repositories.

It does **not** yet remove the embedded project copies from Mission Control.

Phase 9 must first rewire:

- the VS Code multi-root workspace;
- `.vscode/tasks.json`;
- `scripts/lab`;
- Mission Control CI;
- learner missions/navigation;
- acceptance/admin documentation;
- historical references where current-path semantics matter.

Only after the replacement multi-repository topology is validated may the live embedded copies be removed from Mission Control.
