# Main Branch Protection Target

This file records the intended GitHub protection state for `main`.

It is deliberately simple. The purpose is to protect Connor's learning history and require independent validation without creating enterprise bureaucracy.

## Target ruleset

Create one **active branch ruleset** targeting the default branch / `main`.

Enable:

- require a pull request before merging;
- require the Phase 7 CI status check once it has successfully run on `main`;
- block force pushes;
- block branch deletion.

Do not enable merely for appearance:

- signed-commit requirements;
- linear-history requirements (the repository currently uses normal merge commits);
- multiple mandatory approvals;
- deployment requirements;
- administrator-only workflows Connor cannot understand.

If GitHub presents an approval-count field, use **0 required approvals** for the current learner repository posture. The PR itself remains the reviewable change boundary.

## Required CI check

After Phase 7 merges and the workflow has completed successfully on `main`, select the check produced by:

- workflow: **CI**
- job: **validate**

Use the exact check name GitHub exposes in the ruleset UI rather than guessing it.

## Why protection is post-merge

The required CI workflow must exist on `main` and have produced a check before GitHub can reliably offer it as a required status check.

Therefore Phase 7 uses this sequence:

1. build/review the CI candidate;
2. observe a successful PR CI run;
3. merge Phase 7;
4. observe successful CI on the merged `main`;
5. Geza enables the ruleset in GitHub Settings;
6. verify the ruleset through current GitHub authority;
7. record the exact protection state.

## Connector limitation

The current GitHub integration can inspect repository rulesets but does not have administration permission to configure classic branch protection. Protection must not be claimed until the repository setting is actually observed.

## Connor ownership

Phase 12 transferred publication authority to Connor-owned repositories. Protection must be checked against the Connor repositories rather than assumed to have carried over from `WebshopCompany`.


## Observed active state — 2026-09-23

The target above is now implemented and verified from CURRENT GitHub authority.

Observed repository ruleset:

- name: **Main branch protection**
- ID: `23868188`
- enforcement: **active**
- target condition: `~DEFAULT_BRANCH`, currently `main`
- bypass list: empty
- current user can bypass: never
- deletion rule: enabled
- non-fast-forward / force-push rule: enabled
- pull-request rule: enabled
- required approvals: 0
- allowed merge methods: merge, squash, rebase
- required-status-check rule: enabled
- required check: `validate`
- required-check integration ID: `15368` (GitHub Actions)
- strict required-status-check policy / "up to date before merge": disabled

Merged-main CI run `35835236186` completed successfully on `main` commit `63c1c14a99eb5568e7c88a0b6f079abe78bf7804` before the required check was selected.

This section records the pre-transfer Phase 7 protection state on the preparation repository.

## Post-handover state — 2026-09-23

Canonical repository: `connor-koczian/connor-coding-lab`.

The Phase 12 handover configured protected `main` with PR-based integration and required `validate` CI. CURRENT GitHub branch metadata independently confirms that `main` is protected and that `validate` is required with enforcement for everyone.

Publication CI run `35851754414` completed successfully on Connor-owned `main` commit `5d0b48be60831b2e87f730878fb9f2f59a8c86bf`.

The current ChatGPT GitHub integration can read the public branch summary but receives `403 Resource not accessible by integration` from the detailed branch-protection endpoint. Therefore detailed fields such as approval count, administrator enforcement, force-push/deletion switches and strict/up-to-date policy must be re-checked from Connor's repository settings if they are changed or need fresh independent verification.
