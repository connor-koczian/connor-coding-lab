# 🐛 Mission DBG-01 — Reproduce Before Fixing

**Track:** Debugging

## Where am I?

A deliberately bounded bug in practice or a naturally occurring current project bug.

## What am I learning?

Why reliable reproduction comes before editing code.

## What do I do next?

1. Record the expected behaviour.
2. Run the exact steps that show the failure.
3. Record the actual evidence: output, traceback, wrong state or visual behaviour.
4. Connor proposes at least one hypothesis.
5. Change or inspect the smallest thing that can test that hypothesis.
6. Apply the smallest reliable fix.
7. Rerun the original reproduction.
8. Run any relevant regression check.

## How do I run it?

Use a practice bug when no natural project bug is available. Do not introduce destructive or environment-wide failures for teaching.

## How do I know it worked?

The original failure is reproducible before the fix and no longer reproduces afterwards; Connor can explain the evidence chain.

## Connor decides

Connor chooses which hypothesis to test first when more than one is plausible.

## Tracker evidence

Do **not** promote capability merely because Antigravity completed the work.

Potential evidence from this mission:

- EXPLANATION: expected versus actual behaviour.
- DECISION: hypothesis selection.
- VERIFICATION: reruns original reproduction and regression check.

## Harder challenge

Explain whether the bug was syntax, runtime, logic, state, input, rendering or environment related.
