# Connor Coding Lab

Connor's AI-native programming, game-development and software-engineering environment.

This repository is **Mission Control**: the place that tells Connor where he is, what he is learning, what to do next, how to run it, how to verify it, and what harder challenge is available.

## Start here

Connor should open:

- [`START-HERE.md`](START-HERE.md)

The previous `00-CONNOR-HQ/` material remains preserved as historical material, but it is no longer the long-term navigation model.

## Current V2 status

The approved architecture and phased implementation programme live at:

- [`docs/governance/CONNOR-CODING-LAB-V2-MASTER-IMPLEMENTATION-PLAN.md`](docs/governance/CONNOR-CODING-LAB-V2-MASTER-IMPLEMENTATION-PLAN.md)

The V2 design was implemented through bounded phases. Current GitHub state and the phase tracker in the master plan determine what is accepted; target architecture text alone is not implementation evidence.

## What exists today

### Historical learning projects

- `connor-koczian/python-basics` — Connor's independent Python learning project.
- `connor-koczian/snake-game` — Connor's independent historical Snake project and preserved save points.

The project repositories are separate Git histories. Mission Control links them together through the multi-root workspace; there are no Git submodules.

### Current AI-built showcases

- `demos/neon-city-preview/`
- `demos/snake-overdrive/`

These are reference/showcase material. They are not evidence that Connor designed or built those systems himself.

### Neon City

Connor's real `neon-city` project **does not exist yet**.

The existing Neon City preview is an AI-built technology demonstration. Connor's eventual Neon City project will be created deliberately when he is ready to make the design decisions himself.

## Open the learner cockpit

The accepted learner workspace is:

`Connor-Coding-Lab.code-workspace`

Open that file in VS Code from the target `~/Projects/Connor/` topology for the Mission Control + independent Python Basics + independent Snake Game cockpit.

The workspace is designed to provide:

- rendered Markdown navigation;
- Antigravity skills;
- Git/source-control access;
- an integrated Mission Control terminal;
- visible run/test tasks.

The Phase 6 control command is:

```bash
./scripts/lab help
```

Useful examples:

```bash
./scripts/lab status
./scripts/lab projects
./scripts/lab doctor
./scripts/lab run python-basics
./scripts/lab git status
```

The wrapper prints real delegated commands before execution and deliberately keeps Git mutation, installation and administrator work explicit.

`./scripts/run-lab.sh` remains as a compatibility launcher for the interactive menu.

## Target repository model

The long-term model is:

```text
~/Projects/Connor/
|
|-- connor-coding-lab/          # Mission Control / learning control plane
|
`-- projects/
    |-- python-basics/
    |-- snake-game/
    |-- neon-city/
    `-- future-projects/
```

Small practice stays in Mission Control. Serious continuing projects eventually become independent Git repositories.

Do not introduce Git submodules for this initial design.

## AI mentor

Antigravity is intended to be Connor's primary day-to-day teacher, mentor, coding agent, debugger, tester and reviewer.

The accepted Phase 2 mentor system defines:

- root `GEMINI.md` for project bootstrap context;
- `.agents/rules/` for persistent governance;
- `.agents/skills/` for focused mentor protocols and learner slash commands.

Phase 2 was behaviourally validated on the rehearsal ThinkPad and merged into `main` at `32c8b62a80d3c1f2a62cd680bbd7e3abe8e019c1`.

Phase 3 established and behaviourally validated the canonical learner tracker at `progress/CONNOR-MASTER-TRACKER.md`, then merged into `main` at `f5866c7e29195ed1a4dee4e5d0ecff87f4b98a64`.

Phases 4–12 are accepted. Phase 12 completed the GitHub ownership/publication handover to Connor. Phase 13 is the separately authorised Dell deployment and must not begin until the Dell is explicitly released.

## Python

Repository baseline: Python 3.12.

Each current Python project owns its own `pyproject.toml` and `uv.lock`.

Use `uv` rather than raw `pip` as the normal project workflow.

Do not copy `.venv` directories between machines.

## Git

Treat `main` as stable.

For bounded work:

```bash
git status
git switch main
git pull --ff-only
git switch -c <bounded-branch-name>
```

Inspect changes before committing:

```bash
git status
git diff
git add path/to/file
git diff --cached
```

Connor should understand these concepts; once he does, Antigravity may increasingly perform the mechanical Git operations while Connor reviews what will happen and what was recorded.

## Administration

Parent/admin material lives under `docs/admin/`.

Governance and the V2 implementation authority live under `docs/governance/`.

Mentor-system documentation is being established under `docs/mentor/`.

## Safety

Ordinary coding must not require `sudo`.

Never commit passwords, tokens, API keys, SSH private keys, secret `.env` values, or private family information.

## Dell boundary

The Dell remains outside repository implementation authority until Geza explicitly confirms Father's ASUS migration is accepted and the Dell is released for Connor.

Do not treat repository progress as authority to wipe, repartition, install Ubuntu, or alter BIOS/storage settings.

## Repository ownership

The canonical public Connor-owned repositories are:

- `connor-koczian/connor-coding-lab` — Mission Control;
- `connor-koczian/python-basics` — Python Basics;
- `connor-koczian/snake-game` — Snake Game.

The corresponding `WebshopCompany` repositories are private preparation/archive copies, not current learner authority.


## Repository safety and CI

See [SECURITY.md](SECURITY.md) for the practical rules around secrets, dependencies, external services, AI/connectors and administrator boundaries.

Phase 7 established a small GitHub Actions CI workflow and protected `main` with a required PR and `validate` check. CI provides independent checks without claiming interactive GUI/game behaviour.
