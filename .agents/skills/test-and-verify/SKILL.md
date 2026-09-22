---
name: test-and-verify
description: Designs and executes proportionate verification for a change, distinguishing automated evidence from runtime, interactive and hardware checks. Use before claiming a feature or fix works.
---

# Test And Verify

1. Convert the requirement into observable acceptance checks.
2. Choose the cheapest reliable evidence first.
3. Run applicable checks using the repository's verified toolchain.
4. Record each result as static, automated, runtime, interactive/GUI, hardware or unverified.
5. Test the changed behaviour and important unchanged behaviour.
6. Do not count "the program starts" as proof of correct behaviour.
7. If a check cannot be performed, say exactly what remains unverified and who or what must verify it.
