# Safety Rule

Safety boundaries override convenience.

## Secrets and privacy

Never expose, request unnecessarily, print or commit:

- passwords;
- API keys;
- access tokens;
- SSH/private keys;
- secret `.env` values;
- private family information;
- credentials or account identifiers not required for the task.

If a secret appears in output, stop using it and tell Geza what needs rotating or removing.

## Permissions

Do not teach permission bypasses.

Connor's normal coding environment is non-admin.

Ordinary coding must not require `sudo`.

Do not weaken security controls merely to make a task easier.

## External code and dependencies

Treat install scripts, packages, extensions and downloaded code as dependencies that need a clear purpose and proportionate review.

Do not run opaque destructive commands.

## Dell boundary

Repository work does not authorise physical Dell lifecycle changes.

Until Geza explicitly confirms Father's ASUS migration is accepted and the Dell is released for Connor, do not wipe, repartition, erase, install Ubuntu, change BIOS/storage settings or otherwise mutate the Dell.
