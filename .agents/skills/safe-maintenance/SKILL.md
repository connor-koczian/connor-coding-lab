---
name: safe-maintenance
description: Classifies a maintenance request and handles workspace-safe actions while stopping at system-administration and Dell lifecycle boundaries. Use for updates, installations, permissions or environment problems.
---

# Safe Maintenance

1. Classify the request as workspace/project maintenance, user-level tooling, system administration or physical machine lifecycle.
2. For workspace-safe work, explain and proceed within repository authority.
3. If `sudo`, system packages, accounts, security configuration, services, disks, BIOS or machine-wide settings are required, explain the prerequisite and why, then stop at the admin boundary unless Geza has explicitly authorised the exact action.
4. Never bypass permissions.
5. Never expose secrets.
6. The Dell lifecycle remains under `gk-home-lab`, not this repository.
