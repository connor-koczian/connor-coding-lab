# Connor Coding Lab V2 — Repository Transition Map

This document explains the structural transition from the current repository to the approved V2 architecture.

The canonical programme authority remains:

[`CONNOR-CODING-LAB-V2-MASTER-IMPLEMENTATION-PLAN.md`](CONNOR-CODING-LAB-V2-MASTER-IMPLEMENTATION-PLAN.md)

## Phase 1 principle

**Add the new control plane before removing the old one.**

The existing repository remains runnable while Mission Control V2 is introduced.

## Current-to-target mapping

| Current area | V2 direction | Phase 1 action |
| --- | --- | --- |
| Root `README.md` | Repository overview | Update to point at Mission Control |
| `00-CONNOR-HQ/` | Superseded by root entry + `missions/` + `learning/` | Preserve; add compatibility pointer |
| `python-basics/` | Independent project repo eventually | Preserve unchanged |
| `snake-game/` | Independent project repo eventually | Preserve unchanged |
| `demos/` | `showcase/` eventually | Preserve implementations; create showcase boundary |
| `experiments/` | Mostly `practice/` concept | Preserve current area; establish new practice boundary |
| `web-playground/` | Future web practice/projects | Preserve |
| `docs/admin/` | Admin documentation | Preserve; final V2 Dell reconciliation is later |
| `scripts/` | Learner/admin control tooling | Preserve; V2 launcher work is later |
| `.vscode/` | V2 cockpit configuration | Preserve in Phase 1; dedicated UX phase later |
| `GEMINI.md` | V2 Antigravity control system | Preserve in Phase 1; replace/expand only in Phase 2 |
| `AI-CODING-RULES.md` | Core AI governance | Preserve in Phase 1; reconcile in Phase 2 |

## Newly established Phase 1 areas

- root `START-HERE.md`;
- `missions/`;
- `learning/`;
- `practice/`;
- `progress/`;
- `showcase/`;
- `docs/mentor/`.

These establish information architecture. They do not pretend later-phase functionality already exists.

## Hard preservation rules

During Phase 1:

- do not move or rewrite imported `python-basics` history;
- do not move or rewrite imported `snake-game` history;
- do not create Connor's real `neon-city` project;
- do not implement the Antigravity V2 agent system;
- do not implement the master tracker;
- do not alter physical Dell state;
- do not transfer repositories to Connor's GitHub account.

## Known transition debt

Some current documentation predates the approved V2 architecture. Examples include Dell paths and wording written before the final Mission Control + independent-project-repository model was approved.

Those documents remain evidence of the earlier preparation state and will be reconciled in their dedicated phases rather than opportunistically rewritten during Phase 1.

## Exit condition

Phase 1 is complete when:

1. Connor has one clear root entry point.
2. The V2 control-plane areas exist and explain their purpose honestly.
3. Old navigation remains usable during transition.
4. Historical projects remain unchanged.
5. No later-phase capability is falsely presented as implemented.
6. The Phase 1 diff is reviewed and accepted.
