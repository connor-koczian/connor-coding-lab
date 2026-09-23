# Multi-Repository Workspace V1 — Phase 9 Implementation Record

**Phase:** 9 — Multi-repository workspace integration  
**Branch:** `integration/multi-repo-workspace-v1`  
**Base:** Phase 8 close-out `main` at `2d851ef93b2d60100f3d1b7f010e24fb6040411b`

## Purpose

Replace the transitional monorepo project copies with the independent Python Basics and Snake repositories while keeping one coherent Connor-facing cockpit.

## Target topology

```text
~/Projects/Connor/
|
|-- connor-coding-lab/
|
`-- projects/
    |-- python-basics/
    `-- snake-game/
```

The repositories are siblings in one workspace. They are **not** Git submodules.

## Project authority

- Mission Control: `WebshopCompany/connor-coding-lab`
- Python Basics: `WebshopCompany/python-basics`
- Snake Game: `WebshopCompany/snake-game`

Phase 8 preserved the original Connor histories before this integration change.

## Cockpit

`Connor-Coding-Lab.code-workspace` now uses:

- `.` — Mission Control;
- `../projects/python-basics` — Python Basics;
- `../projects/snake-game` — Snake Game.

Python/Snake VS Code tasks use named workspace roots instead of paths inside Mission Control.

## Lab control

`scripts/lab` derives the default projects directory from the Mission Control parent:

`../projects`

An explicit `CONNOR_PROJECTS_ROOT` environment override exists for controlled testing, not as a required learner configuration.

Full `lab doctor` checks:

- Mission Control;
- Python Basics independent repository;
- Snake Game independent repository;
- Python 3.12 through uv;
- neutral shell;
- working-tree state.

`lab doctor --mission-control-only` exists so GitHub CI can validate Mission Control without requiring credentials to clone private sibling repositories.

The doctor remains read-only.

## CI ownership

Mission Control CI validates only Mission Control concerns.

Python Basics CI independently validates:

- Python 3.12;
- locked uv environment;
- Ruff;
- pytest.

Snake CI independently validates:

- Python 3.12;
- locked uv environment;
- Python compilation;
- Pygame import.

This keeps evidence with the repository that owns the code.

## Legacy cleanup safety

The previous cleanup script could classify separate Python/Snake directories as old monorepo leftovers.

That behaviour is now retired with a hard failure message. Independent project repositories must not be archived or purged as "legacy" folders.

## Learner state

Current repository/path references may change during this migration.

Capability states must **not** change merely because the repository architecture changed.

## Embedded-copy removal

The duplicate `python-basics/` and `snake-game/` trees may be deleted from Mission Control in this candidate because:

1. independent repositories exist;
2. original histories were verified;
3. extraction tree identities matched;
4. each project now has its own CI;
5. workspace/tasks/lab/current missions point to the independent project locations.

The old content remains permanently recoverable in Mission Control Git history and the frozen pre-V2 backup branch.

## Behavioural acceptance required

Use a clean target-layout ThinkPad rehearsal.

Acceptance must prove:

1. three independent clean Git repositories;
2. correct remotes;
3. exact three-root VS Code Explorer;
4. neutral Mission Control terminal;
5. full `lab doctor` PASS;
6. `lab status` shows all three repositories independently;
7. Python Basics run + Ruff + pytest;
8. Classic and Campaign Snake open and accept input;
9. browser Snake loads and accepts input;
10. Git status in one project is independent from Mission Control and the other project;
11. Antigravity `/start` reads Mission Control tracker and can inspect current independent project roots without inventing monorepo paths;
12. learner tracker capability states remain unchanged unless Connor personally supplies new evidence.

Static CI alone is not enough to merge Phase 9.
