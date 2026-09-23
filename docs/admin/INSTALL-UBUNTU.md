# Dell Ubuntu Installation Runbook

Target: Dell Latitude E5550 prepared for Connor Coding Lab.

## 0. Before erasing Windows

Do not erase the SSD until Geza has independently verified the required family
files are backed up and readable from another system.

The hardware baseline is recorded in `DELL-HARDWARE.md`.

## 1. Boot the Ubuntu 26.04.1 LTS live USB

Choose **Try Ubuntu** first.

Before installation, verify:

- display runs at 1920 × 1080;
- keyboard and touchpad work;
- Intel AC 7265 Wi-Fi connects;
- Ethernet receives a connection when plugged in;
- audio output works;
- webcam is detected;
- Bluetooth can be enabled;
- suspend and resume returns to a usable desktop.

If an essential device fails in the live environment, investigate before
erasing Windows.

## 2. Install Ubuntu

Once backups and live hardware checks pass, install Ubuntu to the whole Crucial
MX500 SSD.

Recommended account layout:

- create a Geza-controlled administrator account during installation;
- create `connor` afterwards as a normal user;
- do not add `connor` to the `sudo` group for ordinary development.

Example after first boot:

```bash
sudo adduser connor
```

Do not add Connor to sudo unless Geza later changes that policy deliberately.

## 3. System provisioning

Transfer or clone the complete repository, then from its root run:

```bash
sudo ./scripts/admin/provision-ubuntu.sh
```

The admin script installs only machine-level prerequisites and Visual Studio
Code. It does not install Python packages globally.

## 4. Connor user setup

Log into the graphical desktop as Connor.

The intended workspace topology is:

```text
/home/connor/Projects/Connor/
|-- connor-coding-lab/
`-- projects/
    |-- python-basics/
    `-- snake-game/
```

Run, without sudo:

```bash
cd ~/Projects/Connor/connor-coding-lab
./scripts/setup-connor-user.sh
```

Then inspect and validate:

```bash
./scripts/show-my-computer.sh
./scripts/check-environment.sh
```

## 5. Repository source of truth

During preparation, the canonical remote is:

`WebshopCompany/connor-coding-lab`

The long-term intended home is:

`connor-koczian/connor-coding-lab`

Clone or transfer all three independent repositories so their Git histories remain intact.
Do not recreate them by copying working directories without their `.git` histories.

## 6. Final acceptance

Open the canonical multi-root workspace in VS Code:

```bash
code ~/Projects/Connor/connor-coding-lab/Connor-Coding-Lab.code-workspace
```

Complete `docs/admin/ACCEPTANCE-CHECKLIST.md`.

The Dell is ready only after the installed machine passes the applicable
hardware, Git, Python, Pygame, browser and VS Code checks.


## 7. Workstation/account configuration

Apply [DELL-WORKSTATION-V2.md](DELL-WORKSTATION-V2.md) after repository ownership handover and before final acceptance.

This includes Antigravity, VS Code user settings, Git identity/authentication and the explicit requirement that Connor's normal account remain non-admin.
