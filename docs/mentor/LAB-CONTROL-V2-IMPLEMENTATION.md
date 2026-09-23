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


## Behavioural acceptance — 2026-09-23

ThinkPad rehearsal was completed against candidate head `084f9220b3a1fcf5255343b81dfd9d5adcf1e07a`.

### User-observed rehearsal

Geza reported completing the prescribed Phase 6 acceptance block, including:

- Bash syntax check for `scripts/lab`, `scripts/run-lab.sh` and `scripts/check-environment.sh`;
- `lab help`;
- `lab status`;
- `lab projects`;
- `lab doctor`;
- inspection-only `lab git status` / `lab git diff`;
- Python Basics launched through `lab run python-basics` with controlled input;
- compatibility launcher menu;
- compatibility environment-check shim.

The captured output directly confirms:

- the compatibility menu displayed the current run options and exited with **See you next mission.**;
- `scripts/check-environment.sh` explicitly forwarded to `./scripts/lab doctor`;
- the compatibility check stated that the V2 doctor is read-only and does not silently sync or repair projects;
- `lab doctor` ran as normal user `connor`;
- Git 2.34.1, uv 0.12.17 and VS Code 1.138.0 were present;
- Mission Control Git metadata, `START-HERE.md`, V2 mission catalogue, learner tracker, Python Basics metadata and Snake metadata were present;
- Python 3.12 was available through uv;
- the working tree was clean;
- there was no active project virtual environment;
- final doctor result: **DOCTOR: PASS**;
- doctor explicitly separated environment readiness from project runtime/test evidence.

### Final state

- Tracker SHA-256: `e88992f52185369bb26ef8de1f81d7a4d8160ed0d18b68f72d58860282997f9f`
- Working tree: clean
- Final candidate HEAD: `084f9220b3a1fcf5255343b81dfd9d5adcf1e07a`

### Acceptance classification

- Script syntax / command-surface rehearsal: **PASS (user-reported execution)**
- Read-only doctor behaviour: **PASS**
- Compatibility menu: **PASS**
- Compatibility environment-check shim: **PASS**
- Normal-user / neutral-shell boundary: **PASS**
- Tracker non-mutation: **PASS**
- Final repository cleanliness: **PASS**
- No Dell lifecycle work: **PASS**

Phase 6 is behaviourally accepted. PR #16 may proceed through final exact-state review and normal merge if current GitHub authority remains unchanged.
