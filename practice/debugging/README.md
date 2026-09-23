# Debugging Practice

Use small controlled failures.

Suggested drills:

1. Syntax error: locate the parser complaint.
2. Runtime error: read the traceback from bottom to top.
3. Logic error: program runs but gives the wrong answer.
4. State bug: value changes at the wrong time.
5. Environment bug: code is fine but the command/tooling is wrong.

Always record:

`expected -> actual -> evidence -> hypothesis -> test -> fix -> rerun`
