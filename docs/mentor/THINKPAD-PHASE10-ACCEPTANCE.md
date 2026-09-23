# ThinkPad Rehearsal — Phase 10 Acceptance Record

**Phase:** 10 — ThinkPad rehearsal  
**Date:** 2026-09-23  
**Result:** PASS  
**Mission Control baseline:** `2b3916b046350e02a94cad100a69376582fd5147`

## Purpose

Prove the accepted V2 architecture works from fresh final-`main` clones in the target multi-repository layout before Dell handover design and repository ownership transfer.

## Fresh-clone topology

```text
/home/connor/Projects/Connor/
|-- connor-coding-lab/
`-- projects/
    |-- python-basics/
    `-- snake-game/
```

Fresh clone identities:

- Mission Control: `2b3916b046350e02a94cad100a69376582fd5147`
- Python Basics: `55778063bc1fc6e547bedf7eea95664274e78b61`
- Snake Game: `7af14048e972ab079eb52ce875995d8707b3314e`

All three repositories were on `main`, tracking `origin/main`, with clean working trees.

## Environment evidence

Full `./scripts/lab doctor` passed, including:

- normal non-admin user;
- Git and uv available;
- VS Code available;
- Mission Control repository present;
- canonical tracker present;
- multi-root workspace present;
- Python 3.12 available through uv;
- independent Python Basics and Snake repositories present;
- all three working trees clean;
- no active project virtual environment in the neutral Mission Control shell.

## Runtime evidence

Python Basics:

- launched through `./scripts/lab run python-basics`;
- uv selected CPython 3.12.14;
- Ruff: PASS;
- pytest: `1 passed`.

Snake Game:

- uv selected CPython 3.12.14;
- static compilation: PASS;
- Classic Snake: interactively exercised successfully;
- Campaign Snake: interactively exercised successfully.

Browser/showcase/menu:

- Original Browser Snake: exercised successfully;
- Neon City preview: exercised successfully;
- Snake: OVERDRIVE: exercised successfully;
- Show My Computer: exercised successfully;
- Lab Doctor: exercised successfully;
- all menu items were reported operational.

## Antigravity session evidence

`/start`:

- read the canonical Mission Control tracker;
- found Mission Control on clean `main`;
- discovered the independent `python-basics` and `snake-game` repositories under `../projects/`;
- selected Mission FND-01 — First Evidence Cycle;
- produced current commands using the independent Python Basics path.

`/finish`:

- inspected repository state;
- recognised that the rehearsal had not supplied Connor learner actions;
- did not promote Connor capability states;
- left the learner tracker unchanged;
- correctly reported the evidence still required for a genuine learner session.

This validates the tracker mutation decision path: the mentor can update when evidence exists and can deliberately leave the tracker unchanged when evidence does not justify mutation.

## Git workflow evidence

A bounded local rehearsal branch, `rehearsal/phase10-git-flow`, was used to exercise:

- branch creation;
- `git status`;
- exact-file `git diff`;
- specific-file `git add`;
- `git diff --cached`.

The temporary marker was not intended for permanent history. The real Phase 10 closeout branch/PR provides the PR, CI and protected-merge evidence.

## Offline evidence

Local Mission Control navigation, missions, tracker, project READMEs and lab commands were exercised without requiring live GitHub/web access. Core learning/navigation material remains usable offline.

## Learner-state integrity

The Phase 10 rehearsal was performed by Geza as a system acceptance exercise.

It is not evidence of Connor capability and must not promote learner-state capability levels.

## Result

Phase 10 is accepted.

The next programme phase is Phase 11 — Dell handover / final workstation configuration design. Physical Dell lifecycle remains outside this repository's authority until separately released by `gk-home-lab`.
