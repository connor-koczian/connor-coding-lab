# Dell Setup Checklist — Parent/Admin

Target machine: Dell Latitude E5550, Intel Core i5-5300U, 16 GB RAM, Crucial MX500 2 TB SSD.

Target OS: Ubuntu Desktop 26.04.1 LTS amd64.

## Before wiping Windows

Boot the Ubuntu USB in Try Ubuntu mode and verify:

- display
- Wi-Fi
- Ethernet
- Bluetooth
- sound
- webcam
- keyboard and touchpad
- sleep/resume
- HDMI

Also independently verify that the previous Windows user's required data has been migrated.

## After Ubuntu installation

Parent/admin tasks:

- apply OS updates;
- install Git;
- install VS Code from Microsoft's supported Linux distribution method;
- install any required system libraries for Pygame;
- install `uv`;
- configure a normal non-admin `connor` account.

Connor should not routinely use `sudo`.

## Repository

Final intended clone:

```bash
cd ~/Projects
git clone <Connor's final repository URL> connor-coding-lab
cd connor-coding-lab
```

Do not copy `.venv` directories from the old machine.

Recreate Python environments from `pyproject.toml` and `uv.lock`.

## Validation

From the repository root verify Git:

```bash
git status
git log --oneline --decorate -10
```

For each Python project:

```bash
uv sync
```

Then validate the existing projects with their documented commands.

The migration is not complete until Snake and Python Basics work and the original Git history is visible.
