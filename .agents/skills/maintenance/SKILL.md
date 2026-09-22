---
name: maintenance
description: Runs the learner-facing safe maintenance workflow and stops at administrator or physical-machine boundaries. Use when Connor types /maintenance or needs help with tools, updates, permissions or environment setup.
---

# /maintenance

Use the safe-maintenance protocol.

First classify the request.

Normal coding should remain non-admin.

If the task needs `sudo`, system-wide package installation, account changes, security changes, disks, BIOS or Dell lifecycle actions, explain the need and stop unless Geza has explicitly authorised that exact system action.
