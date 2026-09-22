---
name: debug-with-connor
description: Debugs a reproducible problem with Connor using evidence, hypotheses and the smallest reliable fix. Use for errors, crashes, wrong behaviour, rendering problems or environment failures.
---

# Debug With Connor

Use this sequence:

`reproduce -> observe -> hypothesise -> isolate -> smallest reliable fix -> rerun -> verify`

1. Reproduce the problem or obtain the exact evidence.
2. Classify the failure: syntax, runtime, logic, state, input, rendering, environment or unknown.
3. State the strongest current hypothesis and why.
4. Isolate the smallest relevant area.
5. Change only what the evidence supports.
6. Rerun the failing path.
7. Check for regressions where relevant.
8. Explain the lesson Connor should retain.

Do not respond to a local bug by rewriting the whole feature unless evidence justifies it.
