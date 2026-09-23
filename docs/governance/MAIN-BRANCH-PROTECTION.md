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

If GitHub presents an approval-count field, use **0 required approvals** during the current preparation phase. The PR itself remains the reviewable change boundary.

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

## Future ownership

When repositories are eventually transferred to Connor, re-check ruleset ownership/bypass behaviour. Do not assume organisation settings transfer unchanged.
