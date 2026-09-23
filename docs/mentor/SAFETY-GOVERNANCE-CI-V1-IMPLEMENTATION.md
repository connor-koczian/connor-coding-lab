# Safety, Governance and CI V1 — Phase 7 Implementation Record

**Phase:** 7 — Safety, governance and CI  
**Branch:** `governance/safety-ci-v1`  
**Base:** Phase 6 merged `main` at `9f62b7fea276f98a463ddd23bd3e3281b7fad0fb`

## Purpose

Add small independent engineering controls that Connor can understand.

This phase is not a security theatre exercise. Each control should answer a concrete question:

- did the repository accidentally track an obviously sensitive file?
- do the shell scripts parse?
- is the basic learner environment coherent?
- do the current Python Basics lint/tests pass?
- can the Snake dependency environment import Pygame?
- is `main` protected from casual direct/destructive changes?

## CI design

Workflow: `.github/workflows/ci.yml`

Triggers:

- pull requests;
- pushes to `main`.

Permissions:

- `contents: read` only.

The workflow uses pinned action revisions and uv 0.12.17, then:

1. installs Python 3.12 through uv;
2. runs `scripts/check-repo-policy.sh`;
3. syntax-checks learner shell scripts;
4. runs the read-only lab doctor;
5. runs Python Basics `uv sync --locked`, Ruff and pytest;
6. runs Snake `uv sync --locked` and imports Pygame.

It intentionally does not launch interactive GUI/browser programs.

## Repository policy

`scripts/check-repo-policy.sh`:

- rejects tracked secret/private-key style paths;
- scans tracked content for private-key headers without printing the secret body;
- verifies core governance files are regular files, not symlinks;
- verifies key learner control scripts retain executable Git mode.

It is a guardrail, not a complete secret scanner.

## Human-readable security boundary

`SECURITY.md` documents:

- secrets and credential response;
- dependency/download review;
- network/public-exposure boundary;
- AI/connector data-sharing boundary;
- administrator boundary;
- what CI proves and does not prove.

## Main protection

No repository ruleset existed at Phase 7 start.

The current connector lacks administration access for classic branch protection and returned 403 for that endpoint.

The exact post-merge target is therefore recorded in `docs/governance/MAIN-BRANCH-PROTECTION.md`.

Phase 7 is not fully complete until:

1. PR CI is green;
2. Phase 7 is merged;
3. CI is green on merged `main`;
4. Geza enables the documented `main` ruleset in GitHub;
5. the ruleset is re-fetched and verified.

## Acceptance requirements

Before candidate merge:

- policy script passes on the ThinkPad;
- CI workflow runs on PR and succeeds;
- inspect CI job steps/logs rather than assuming a green badge means the intended commands ran;
- learner tracker remains unchanged;
- no historical project migration occurs;
- no Dell lifecycle work occurs.

After merge:

- merged-main CI succeeds;
- configure and verify the documented `main` ruleset.
