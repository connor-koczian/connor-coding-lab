# Connor's Dell Latitude E5550 — Hardware Baseline

This file records the hardware measured **before** the machine is wiped and rebuilt for Connor.

It is an administration/evidence document. Connor's simpler explanation is in
`00-CONNOR-HQ/MY-COMPUTER.md`.

## Machine

| Item | Observed value |
| --- | --- |
| Manufacturer | Dell Inc. |
| Model | Latitude E5550 |
| Firmware mode | UEFI |
| BIOS | A24, 19 June 2020 |
| Secure Boot | Enabled |
| TPM | Not present |
| Current pre-rebuild OS | Windows 10 Pro, 64-bit |

## Processor

- Intel Core i5-5300U @ 2.30 GHz
- 2 physical CPU cores
- 4 logical processors

## Memory

- 16 GB total
- 2 × 8 GB Samsung modules
- 1600 MT/s configured speed

## Storage

- Crucial MX500 2 TB SATA SSD
- Windows reported the drive as healthy
- GPT partition table

## Graphics and display

- Intel HD Graphics 5500
- observed internal display mode: 1920 × 1080
- Windows-reported graphics driver: 20.19.15.5063

The existing Pygame Snake requests a 1400 × 950 window. The 1920 × 1080 panel
has enough raw pixels for that window, but final acceptance must still check
window decorations and desktop scaling under Ubuntu.

## Networking

- Intel Dual Band Wireless-AC 7265 Wi-Fi
- Intel Ethernet Connection (3) I218-LM
- Intel Wireless Bluetooth
- Dell Wireless 5809e Gobi 4G LTE hardware is enumerated by Windows, although
  most WWAN interfaces were reported as not present/disconnected

Ubuntu acceptance must verify Wi-Fi, Ethernet and Bluetooth from the live USB
before the disk is erased.

## Audio

- Realtek Audio

## Battery

Windows battery report:

- battery: DELL WYJC253, manufactured by SMP
- chemistry: lithium-ion
- design capacity: 53,666 mWh
- full-charge capacity: 42,266 mWh
- estimated retained capacity: about 78.8%

That is usable for an older machine. Replace the battery only if real Ubuntu
runtime or battery behaviour proves inadequate.

## Target software baseline

- Ubuntu Desktop 26.04.1 LTS amd64
- normal daily user: `connor`
- separate administrator account controlled by Geza
- workspace: `/home/connor/Projects/connor-coding-lab`
- Git
- Visual Studio Code
- `uv`
- Python 3.12 for new work after the dedicated 3.12 migration is accepted
- Ruff and pytest where the individual project declares them

## Final hardware acceptance

Before this laptop is declared ready, verify on the installed Ubuntu system:

- 1920 × 1080 display and sensible scaling;
- keyboard and touchpad;
- Wi-Fi;
- Ethernet;
- Bluetooth;
- speakers and headphone output;
- webcam and microphone;
- sleep and resume;
- charging and battery reporting;
- USB ports;
- HDMI output if available for testing;
- both Pygame Snake versions;
- browser games in a hardware-accelerated browser.

Do not call the Dell ready solely because installation completed.
