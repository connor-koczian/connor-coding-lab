# Repository Security and Safe Engineering

This repository is a learning environment, but it uses real engineering controls.

## Secrets

Never commit or paste into repository files:

- passwords;
- API keys or access tokens;
- SSH/private keys;
- secret `.env` values;
- exported browser/session credentials;
- private family information or account identifiers not required for the work.

Use local ignored files for secrets when a future project genuinely needs them. A shareable template may use names such as `.env.example`, but it must contain placeholders only.

If a real secret reaches Git history:

1. stop using the exposed credential;
2. tell Geza;
3. revoke/rotate it at the source;
4. only then decide whether history cleanup is necessary.

Deleting the current file is not enough to make an exposed credential safe.

## Dependencies and downloaded code

Before adding a package, extension, script or external repository, establish:

- what problem it solves;
- where it comes from;
- what permissions or network access it needs;
- whether the project already has a simpler dependency;
- how its version will be recorded/reproduced.

Python projects use their committed `pyproject.toml` and `uv.lock`. CI uses `uv sync --locked` so an unreviewed lockfile change cannot be silently substituted.

Do not run opaque install commands merely because an AI response or website says to copy/paste them.

## Internet and network exposure

Local development servers bound for ordinary local testing are different from public network services.

Do not create tunnels, port forwarding, public shares, externally reachable services or firewall changes without Geza's explicit authority.

Treat content downloaded from the internet as untrusted input until understood.

## AI and connected tools

Do not send secrets, private family data or unnecessary personal information to an AI model, connector, website or third-party service.

Before authorising an agent/tool action, understand whether it:

- only reads local/repository data;
- writes files;
- calls an external service;
- changes GitHub state;
- installs software;
- crosses into system administration.

AI output is not validation. Use runtime checks, tests and diff review.

## Administrator boundary

Normal coding is non-admin.

If work requires `sudo`, system packages, accounts, services, security settings, disks, BIOS or machine-wide configuration, use the approved maintenance path and stop at the authority boundary.

The physical Dell lifecycle remains governed by `gk-home-lab`.

## CI

GitHub Actions CI is independent evidence for a save point. It currently checks:

- tracked-file repository policy;
- shell syntax;
- read-only lab doctor;
- Python Basics lockfile environment, Ruff and pytest;
- Snake lockfile environment and Pygame import.

A green CI run does not prove interactive GUI/game/browser behaviour.

## Main-branch protection

The intended `main` policy is documented in:

[`docs/governance/MAIN-BRANCH-PROTECTION.md`](docs/governance/MAIN-BRANCH-PROTECTION.md)

Protection is a GitHub repository setting, not something an agent should pretend was enabled by editing a file.
