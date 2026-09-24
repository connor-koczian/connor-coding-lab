# Phase 13 — Dell deployment acceptance

Status: COMPLETE

Accepted: 24 September 2026

## Authority and scope

Phase 13 began only after the Dell was explicitly released for Connor by the separate `gk-home-lab` machine-lifecycle authority.

This record closes the Connor Coding Lab developer-environment deployment. It does not replace `gk-home-lab` authority for hardware lifecycle, firmware, operating-system rebuilds, remote-access infrastructure or destructive machine work.

## Accepted workstation

- Dell Latitude E5550
- Ubuntu Desktop 26.04.1 LTS amd64
- Connor operates as a normal non-admin user
- ordinary programming does not require routine `sudo`

## Repository topology

Canonical local topology:

- `/home/connor/Projects/Connor/connor-coding-lab`
- `/home/connor/Projects/Connor/projects/python-basics`
- `/home/connor/Projects/Connor/projects/snake-game`

These are three independent Git repositories.

Accepted repository heads before this close-out change:

- Mission Control: `f7b3ca117259cbc9abde6657235c564419c5e76b`
- Python Basics: `55778063bc1fc6e547bedf7eea95664274e78b61`
- Snake Game: `7af14048e972ab079eb52ce875995d8707b3314e`

All three working trees were clean on `main`.

## Toolchain acceptance

Verified on the Dell:

- Git 2.53.0
- uv 0.12.18
- uv-managed CPython 3.12.14
- VS Code 1.139.0
- Pygame 2.6.1
- curated VS Code Python/Ruff/Antigravity extensions

VS Code opens the intended three-root workspace and does not automatically activate a project virtual environment in a neutral terminal.

## Git and GitHub acceptance

Connor's Git identity is configured with his name and GitHub noreply address.

GitHub SSH authentication successfully identifies the workstation as `connor-koczian`.

The repositories use Connor-owned GitHub remotes.

Connor remains outside the `sudo` group.

## Automated validation

Accepted successfully:

- `./scripts/show-my-computer.sh`
- `./scripts/check-repo-policy.sh`
- `./scripts/lab projects`
- `./scripts/lab doctor`
- `./scripts/lab status`
- Python Basics `uv sync --locked`
- Python Basics Ruff validation
- Python Basics pytest
- Python Basics interactive execution
- Snake `uv sync --locked`
- Snake Python compilation/import validation

The post-reboot `./scripts/lab doctor` also passed.

## Interactive validation

Accepted interactively on the physical Dell display:

- Classic Snake
- Campaign Snake
- Browser Snake
- Neon City preview
- Snake OVERDRIVE
- Lab menu
- three-root VS Code workspace
- three independent Source Control repositories
- neutral terminal behaviour
- Antigravity `/start`

Antigravity discovered Mission Control, the canonical learner tracker, the independent project repositories and the next evidence-based learner mission.

## Reboot-to-learning acceptance

After a complete reboot Connor logged directly into his own desktop account and successfully recovered the learning environment without first entering the Geza desktop account.

Verified after reboot:

- Connor user context
- correct Mission Control working directory
- no active project `VIRTUAL_ENV`
- `lab doctor` PASS
- `lab status` clean for all three repositories
- Git identity persisted
- GitHub SSH authentication persisted
- Antigravity remained usable
- `/start` recovered the learner state correctly

## Parent-account exception

Connor's GitHub/Git/SSH identity remains Connor-owned.

A deliberate parent-authorised exception exists for Antigravity: the Antigravity provider session uses Geza's Google/Gemini Pro account under parental supervision. No Geza GitHub SSH identity is used for Connor's repositories.

## Command interface

The canonical repository interface remains:

`./scripts/lab ...`

`make` and `just` are not Phase 13 dependencies. A future `Justfile` may be considered as a separate learner-experience enhancement, but it was not introduced during acceptance.

## Result

Phase 13 Dell deployment and reboot-to-learning acceptance: PASS.

Connor Coding Lab V2 is accepted for normal learner use on the Dell.
