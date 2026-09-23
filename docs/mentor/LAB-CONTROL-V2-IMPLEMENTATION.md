# Lab Control V2 — Phase 6 Implementation Record

**Phase:** 6 — Lab control tooling  
**Branch:** `tooling/lab-control-v2`  
**Base:** Phase 5 merged `main` at `9c3fa2ceefa1cf203d0bf9ab547b17b1478ca003`

## Purpose

Phase 6 creates one learner-facing control entry point:

`./scripts/lab`

It is a navigation and execution aid, not a replacement for understanding the terminal, Git or `uv`.

## Command surface

- `lab help` — show commands and rules;
- `lab start` — show current state and open the Mission Control start page when a graphical VS Code surface is available;
- `lab status` — show repository/branch/HEAD/Git state and canonical learning paths;
- `lab projects` — show current project locations and run targets;
- `lab run <target>` — run a known project/showcase target;
- `lab doctor` — read-only environment checks;
- `lab git <action>` — inspection-only Git helpers;
- `lab computer` — show current machine information;
- `lab maintenance` — explain the maintenance/admin boundary;
- `lab menu` — compatibility interactive launcher.

## Transparency rule

Before a delegated run/Git command, `lab` prints:

- the working directory;
- the exact shell command.

The wrapper must not make ordinary engineering concepts invisible.

## Mutation boundary

`lab doctor` does not:

- run `uv sync`;
- install packages;
- update dependencies;
- fetch/pull/push;
- stage/commit;
- repair files;
- use `sudo`.

Runtime commands still use the declared real project workflows, such as `uv run ...`. Those commands are printed before execution.

The old `scripts/check-environment.sh` becomes a compatibility shim to the read-only doctor. The old `scripts/run-lab.sh` becomes a compatibility shim to `lab menu`.

## Git boundary

`lab git` is deliberately inspection-only:

- status;
- diff;
- staged diff;
- recent log;
- current branch.

Staging, commits, pull/push and history changes remain explicit Git learning/engineering actions.

## System boundary

`lab maintenance` performs no administrator action.

It points Connor toward `/maintenance` and stops at `sudo`, system-package, account, service, security, disk, BIOS and physical-machine boundaries.

The Dell lifecycle remains outside this repository's authority.

## Behavioural acceptance required before merge

On the rehearsal ThinkPad:

1. check out the exact Phase 6 candidate;
2. run `bash -n scripts/lab scripts/run-lab.sh scripts/check-environment.sh`;
3. run `./scripts/lab help`;
4. run `./scripts/lab status`;
5. run `./scripts/lab projects`;
6. run `./scripts/lab doctor` and verify it performs no sync/install/repair;
7. run `./scripts/lab git status` and `./scripts/lab git diff`;
8. run Python Basics through `./scripts/lab run python-basics` with controlled input and verify the printed underlying command;
9. exercise the compatibility launcher without starting a long-running project (quit from the menu);
10. verify `scripts/check-environment.sh` forwards to the read-only doctor;
11. inspect final Git state and confirm no learner tracker mutation.

Optional GUI/game/browser runs may add evidence but are not required if their unchanged underlying commands were already validated in earlier phases.

Static inspection alone is not sufficient acceptance.
