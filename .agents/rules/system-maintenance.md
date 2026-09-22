# System Maintenance Rule

Separate workspace engineering from machine administration.

## Workspace work

Normal project work may edit files inside authorised coding repositories and run ordinary non-admin development commands.

## System-level work

The following require the approved maintenance path and appropriate parent/admin authority:

- `sudo`;
- system package installation;
- account or group changes;
- security configuration;
- firewall/network-service exposure;
- SSH key changes;
- system services;
- disk/partition operations;
- BIOS/storage changes;
- destructive operating-system work.

When a coding task needs a system-level prerequisite, explain exactly what is needed and why, then stop at the authority boundary.

Do not give Antigravity unrestricted root authority.

The separate `gk-home-lab` project remains the physical-machine lifecycle authority.
