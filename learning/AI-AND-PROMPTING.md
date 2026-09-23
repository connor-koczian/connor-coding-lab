# 🤖 AI Collaboration Engineering

Prompting is only one part of working well with a coding agent.

The real skill is turning an idea into a **bounded, testable engineering task**, then checking the result.

## Progression

### 1. State the job

A useful request answers:

- What do I want?
- Why?
- What must not change?
- How will we know it worked?

### 2. Add engineering context

Progressively add relevant files, examples, constraints, acceptance checks, known risks and uncertainty.

### 3. Ask for a plan

For meaningful changes, ask the agent to identify affected files, important concepts, implementation steps, checks and likely failure modes.

Connor should challenge a plan that changes too much or assumes facts not checked in the repository.

### 4. Direct, do not merely request

Connor should increasingly choose feature behaviour, game mechanics, visual direction, trade-offs, scope and what gets built next.

### 5. Verify the agent

A strong AI workflow ends with evidence:

```text
specification -> implementation -> run -> test -> diff -> explanation -> decision
```

"AI says it works" is not verification.

## Later topics

After the core loop is understood:

- persistent instructions and context engineering;
- reusable skills;
- tool permissions;
- MCP and external tools;
- specialised agents;
- model choice;
- multi-agent or orchestrated workflows.

## Starter mission

[Give AI a testable job](../missions/ai-native-development/001-testable-request.md)
