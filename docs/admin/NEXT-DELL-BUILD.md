# Next Session — Dell Build Handover

This is the restart point for the next Connor Coding Lab setup session.

Do not reconstruct the Dell plan from chat history. Start here, then use the linked
runbooks and the current `main` branch.

## Current preparation state

Repository source of truth during preparation:

`WebshopCompany/connor-coding-lab`

Treat current GitHub `main` as canonical. Do not assume a SHA copied into this
document is still current; re-fetch `main` at the start of the Dell session.

The preparation phase has already established:

- imported Python Basics history is preserved;
- imported Snake history is preserved;
- Python Basics and Snake now target Python 3.12;
- `uv` is the Python environment/dependency workflow;
- Ruff and pytest are configured where currently used;
- Dell provisioning/user-setup/environment-check scripts exist;
- the ThinkPad rehearsal proved the core Python 3.12 / uv / Ruff / pytest / Pygame workflow;
- Connor's intended workspace is `/home/connor/Projects/connor-coding-lab`;
- Connor should use a normal non-admin account;
- Geza should retain a separate administrator account;
- the AI demos are demonstrations only and are not Connor's historical work;
- Connor's future real `neon-city/` project has intentionally not been created.

## Stop/go gate before touching the Dell

Do not erase Windows until ALL of these are true:

1. Father's required files are backed up.
2. The backup has been opened/read from another machine.
3. The Dell is physically available.
4. Ubuntu 26.04.1 LTS installation media is ready.
5. The Ubuntu live environment has been tested on the Dell.
6. The current BIOS/SATA storage mode has been inspected.

Windows previously reported the Crucial MX500 through a RAID storage path. Do
not casually change RAID/AHCI while the existing Windows installation still
matters. Inspect the BIOS and decide the storage-mode action deliberately on the
wipe/install day.

## Exact Dell sequence

### 1. Re-fetch repository authority

Before installation work, inspect current GitHub `main` and the current versions
of:

- `docs/admin/DELL-HARDWARE.md`
- `docs/admin/INSTALL-UBUNTU.md`
- `docs/admin/DELL-SETUP-CHECKLIST.md`
- `docs/admin/ACCEPTANCE-CHECKLIST.md`
- `scripts/admin/provision-ubuntu.sh`
- `scripts/setup-connor-user.sh`
- `scripts/check-environment.sh`

Do not use an old ThinkPad copy as authority.

### 2. Boot the Ubuntu live USB — do not install yet

Choose **Try Ubuntu**.

Test on the physical Dell:

- 1920×1080 display and sensible scaling;
- keyboard;
- touchpad;
- Intel AC 7265 Wi-Fi;
- Intel I218-LM Ethernet;
- speakers;
- headphone output if practical;
- microphone;
- webcam;
- Bluetooth;
- USB ports;
- HDMI if practical;
- suspend/resume;
- charging and battery reporting.

If an essential device fails, investigate before wiping Windows.

### 3. Install Ubuntu

Target:

- Ubuntu Desktop 26.04.1 LTS amd64;
- whole Crucial MX500 2 TB SSD, once the wipe gate has passed;
- UEFI installation.

Create a Geza-controlled administrator account during installation.

After first boot create Connor as a normal user, for example:

```bash
sudo adduser connor
```

Do not add Connor to the `sudo` group for ordinary development.

### 4. Put the complete repository on the Dell

Use the complete Git repository, not copied individual project folders.

Target path:

```text
/home/connor/Projects/connor-coding-lab
```

During preparation the canonical remote is:

```text
WebshopCompany/connor-coding-lab
```

The intended long-term repository is:

```text
connor-koczian/connor-coding-lab
```

Only perform that handover deliberately and preserve the imported history.

### 5. Geza/admin provisioning

From the repository root, as an administrator:

```bash
sudo ./scripts/admin/provision-ubuntu.sh
```

This installs the machine-level prerequisites and Microsoft's VS Code package.

It does not install project Python packages globally.

### 6. Connor user setup

Log into the graphical desktop as Connor.

From the repository root, without sudo:

```bash
./scripts/setup-connor-user.sh
```

This installs/configures the user-level `uv` workflow, Python 3.12 and the
beginner VS Code extensions.

### 7. Automated environment acceptance

Still as Connor:

```bash
./scripts/show-my-computer.sh
./scripts/check-environment.sh
```

The environment check must pass.

### 8. Interactive acceptance

Run:

```bash
./scripts/run-lab.sh
```

Test at minimum:

- Python Basics;
- Classic Snake;
- Campaign Snake;
- original browser Snake;
- AI Neon City technology preview;
- AI Snake: OVERDRIVE showcase.

For Pygame/browser work, verify actual keyboard input, display fit, audio where
applicable, clean exit, and acceptable performance.

The AI demos are optional demonstrations. A demo bug does not rewrite or replace
Connor's historical Snake work, but any demo presented to Connor should be
tested honestly rather than assumed working.

### 9. Complete the acceptance checklist

Use:

`docs/admin/ACCEPTANCE-CHECKLIST.md`

The Dell is ready only when the applicable hardware and software checks have
actually passed on the Dell.

## What the repository automates

The repository automates/configures:

- Git and common command-line prerequisites;
- Microsoft's VS Code package;
- `uv`;
- Python 3.12;
- VS Code Python and Ruff extensions;
- per-project dependency environments;
- Python Basics lint/tests;
- Pygame dependency/import checks;
- Connor's launcher and machine/environment inspection helpers.

## What the repository deliberately does not automate

It does not:

- back up Father's files;
- wipe Windows;
- partition/install Ubuntu unattended;
- change BIOS RAID/AHCI settings;
- create the administrator account;
- add Connor to sudo;
- configure private GitHub credentials;
- transfer repository ownership;
- guess hardware workarounds;
- declare hardware good without physical testing.

Those remain deliberate admin decisions.

## Final principle

Do not build Connor's real `neon-city/` before he chooses its direction.

The next programming session with Connor should begin from his historical work,
the learning missions and the demos, then let Connor choose the next save point.
