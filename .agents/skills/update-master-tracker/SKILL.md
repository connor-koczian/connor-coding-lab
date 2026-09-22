---
name: update-master-tracker
description: Updates Connor's canonical learner-state tracker from evidence after meaningful work. Use after a meaningful learner session when progress/CONNOR-MASTER-TRACKER.md exists and the session provides evidence about learning or capability.
---

# Update Master Tracker

Canonical file: `progress/CONNOR-MASTER-TRACKER.md`.

## Authority

The tracker is the single current learner-state authority.

Do not create a second progress file, private shadow state, or competing capability summary.

## Evidence classes

Use:

- DIRECT DEMONSTRATION;
- EXPLANATION;
- DECISION / SPECIFICATION;
- VERIFICATION;
- REPOSITORY ARTEFACT;
- AI OUTPUT;
- UNVERIFIED.

Repository artefacts and AI output can provide context, but they do not automatically prove learner competence.

## Update protocol

1. Read the current tracker before making learner-state claims.
2. Identify exactly what Connor personally demonstrated in the current meaningful session.
3. Separate Connor actions from Antigravity actions.
4. Identify only the tracker sections materially affected.
5. Apply the smallest evidence-supported update.
6. Add one concise session-log entry when the session produced meaningful learner evidence.
7. Preserve uncertainty and record what remains unverified.
8. Inspect the tracker diff before treating the update as complete.

If the session produced no learner evidence, it is valid to leave the tracker unchanged.

## Promotion rules

- Do not upgrade a capability because code works, tests pass, or Antigravity completed the task.
- Do not mark a historical mission complete merely because its file exists.
- `CAN EXPLAIN` requires Connor's explanation.
- `CAN USE` requires correct learner use.
- `CAN DIRECT AI` requires a bounded Connor specification with useful requirements, constraints or acceptance checks.
- `CAN VERIFY AI` requires Connor-led inspection or validation of AI work.
- `INDEPENDENT` requires repeated evidence across relevant situations.
- Keep `CAN DIRECT AI` distinct from `CAN VERIFY AI`.
- Do not promote unrelated capabilities in the same edit.

## Required update note

For any promotion, be able to answer:

1. What did Connor personally demonstrate?
2. What evidence supports the new state?
3. Was the relevant behaviour performed by Connor, by AI, or jointly?
4. What remains unverified?

If those questions cannot be answered, keep the existing state.
