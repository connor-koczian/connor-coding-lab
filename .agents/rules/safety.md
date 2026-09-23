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


## AI, connectors and internet boundaries

Do not send secrets, private family data or unnecessary personal information to external models, connectors, websites or services.

Before using an external service, downloaded script, extension or package, establish what it does, what data it receives and what permissions/network access it needs.

Local development servers are not authority to expose a service publicly. Do not create tunnels, port forwarding, public shares or firewall changes without Geza's explicit authority.

## Credential incident response

If a real credential reaches tracked files or output:

1. stop using it;
2. tell Geza;
3. revoke/rotate it at the source;
4. only then consider Git-history cleanup.

Deleting the visible file does not make an exposed credential safe.
