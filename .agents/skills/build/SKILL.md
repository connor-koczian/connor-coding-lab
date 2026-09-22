---
name: build
description: Runs the learner-facing build workflow for one bounded feature, from specification through validation and diff review. Use when Connor types /build or asks Antigravity to implement a chosen feature.
---

# /build

Use the build-feature protocol.

Required sequence:

`goal -> files -> concept -> acceptance checks -> bounded change -> run/test -> diff -> explanation -> decision`

Do not silently broaden scope.

Do not commit until the save point is understandable and the relevant validation has been reported.
