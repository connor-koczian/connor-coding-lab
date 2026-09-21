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

Create:

    /home/connor/Projects

Clone the repository as one repository:

    cd /home/connor/Projects
    git clone https://github.com/WebshopCompany/connor-coding-lab.git
    cd connor-coding-lab

After the final GitHub handover, update this document to the Connor-owned repository URL before the Dell is considered final.

Open `/home/connor/Projects/connor-coding-lab` as the VS Code workspace root.

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
