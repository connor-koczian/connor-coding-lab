# Dell Setup Checklist — Parent/Admin

Target machine:

- Dell Latitude E5550
- Intel Core i5-5300U
- 16 GB RAM
- Crucial MX500 2 TB SATA SSD
- Ubuntu Desktop 26.04.1 LTS amd64

Connor uses a normal non-admin account. Ordinary coding must not require `sudo`.

For the next-session restart point and exact sequence, read
`docs/admin/NEXT-DELL-BUILD.md` first.

## Before replacing the existing OS

Boot the Ubuntu installer in its live/try mode and verify the actual machine:

- native display resolution;
- Wi-Fi;
- Ethernet;
- sound;
- webcam;
- keyboard;
- touchpad;
- sleep/resume;
- HDMI;
- Bluetooth if it will be used.

Confirm separately that any required existing user data has been backed up.

The Snake game currently requests a 1400×950 window, so the real panel resolution must be checked before declaring game compatibility.

## Parent/admin provisioning

Use the supported Ubuntu installation path for system-level software such as:

- Git;
- VS Code;
- any system libraries Pygame actually requires on this machine.

Install/configure `uv` for Connor's user environment rather than using raw `pip` as the project workflow.

Do not create project virtual environments manually. `uv sync` should recreate them from repository configuration.

## Connor workspace

Create the final topology:

```text
/home/connor/Projects/Connor/
|-- connor-coding-lab/
`-- projects/
    |-- python-basics/
    `-- snake-game/
```

Clone all three repositories independently. Do not use Git submodules and do not copy old `.venv` directories.

After Phase 12, use the Connor-owned repository URLs. Do not leave the Dell dependent on Geza's WebshopCompany credentials.

Open:

`/home/connor/Projects/Connor/connor-coding-lab/Connor-Coding-Lab.code-workspace`

Do not depend on custom shell aliases for the learning missions.

## Python version policy

Python Basics and Snake now declare Python 3.12 as the repository baseline.

Use `uv` to install/manage Python 3.12 and recreate each project's environment
from its committed lock file. Do not copy old `.venv` directories from the
ThinkPad or edit version declarations locally on the Dell.

## Validation

Run the exact fresh-clone checks in:

`docs/admin/ACCEPTANCE-CHECKLIST.md`

The Dell is not ready merely because Ubuntu and VS Code start successfully.


## Final workstation authority

Use [DELL-WORKSTATION-V2.md](DELL-WORKSTATION-V2.md) for the final VS Code, Antigravity, account, Git, Python and user-settings baseline.
