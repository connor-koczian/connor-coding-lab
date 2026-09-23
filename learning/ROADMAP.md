# 🧭 Connor Coding Lab — Learning Roadmap

This is a **multi-track engineering roadmap**, not a school-style sequence of lessons.

Connor can move quickly in one track and slowly in another. Progress is based on demonstrated understanding and useful project needs, not age, time spent, or how much code an AI agent generated.

## The operating loop

```text
UNDERSTAND
-> SPECIFY
-> PLAN
-> BUILD
-> RUN
-> BREAK
-> DEBUG
-> IMPROVE
-> TEST
-> REVIEW
-> COMMIT
-> EXPLAIN
```

Antigravity may do substantial implementation. Connor must increasingly be able to make decisions, explain the important ideas, run the work, inspect evidence and decide whether it is acceptable.

## Progression bands

These are capability bands, not grades.

| Band | Main question |
| --- | --- |
| **Orientation** | Can Connor find the work, run it and describe what happened? |
| **Guided Builder** | Can Connor make or direct a small bounded change with help? |
| **Verifier** | Can Connor prove whether a change works instead of trusting the agent? |
| **Project Builder** | Can Connor combine several concepts to improve a real project? |
| **Engineer** | Can Connor plan, review, debug and ship coherent changes with increasingly little help? |

A track may be at a different band from another track.

## Curriculum tracks

| Track | Starter mission | What grows later |
| --- | --- | --- |
| 🖥️ Linux & terminal | [Navigate Mission Control](../missions/linux/001-navigate-mission-control.md) | paths, processes, permissions, networking, maintenance |
| 🤖 AI-native development | [Give AI a testable job](../missions/ai-native-development/001-testable-request.md) | context, planning, tools, agents, orchestration |
| 🐍 Python | [Predict, change, explain](../missions/python/001-predict-change-explain.md) | control flow, functions, data, files, modules, objects |
| 🐛 Debugging | [Reproduce before fixing](../missions/debugging/001-reproduce-before-fix.md) | isolation, state, environment, rendering, regression |
| 🌿 Git & GitHub | [Inspect a save point](../missions/git-github/001-inspect-a-save-point.md) | branches, merge, remotes, PRs, review |
| 🧪 Testing | [Read the evidence](../missions/testing/001-read-a-test-result.md) | test design, failure cases, regression, CI |
| 🎮 Game development | [Design one Snake change](../missions/game-development/001-design-a-snake-change.md) | state, collision, UI, levels, architecture |
| 🌐 Web development | [Change a browser preview](../missions/web/001-change-a-browser-preview.md) | HTML, CSS, JavaScript, browser debugging |
| 🏗️ Software engineering | [Plan before building](../missions/engineering/001-plan-before-build.md) | requirements, architecture, APIs, dependencies, review |

The [first evidence cycle](../missions/foundations/001-first-evidence-cycle.md) combines several tracks and is a useful starting point when Connor's current live capability is still uncertain.

## Track guides

- [AI collaboration engineering](AI-AND-PROMPTING.md)
- [Python](PYTHON.md)
- [Linux and terminal](LINUX.md)
- [Git and GitHub](GIT-AND-GITHUB.md)
- [Debugging](DEBUGGING.md)
- [Testing](TESTING.md)
- [Game development](GAME-DEVELOPMENT.md)
- [Web development](WEB-DEVELOPMENT.md)
- [Software engineering](SOFTWARE-ENGINEERING.md)

## How a mission is selected

Antigravity should not simply choose the next file alphabetically.

Use:

1. the canonical learner state in `progress/CONNOR-MASTER-TRACKER.md`;
2. Connor's current project or interest;
3. a capability that needs live evidence or useful stretch;
4. the smallest mission that produces a visible result;
5. one optional harder challenge.

If a mission assumes a capability that Connor has not demonstrated, either teach the prerequisite inside the mission or choose a smaller mission.

## Evidence and advancement

Mission completion and capability promotion are different things.

A mission can be finished while a capability remains **GUIDED** or **INTRODUCED**.

Promote only from evidence such as:

- Connor accurately explains what happened;
- Connor predicts behaviour before running it;
- Connor makes a meaningful design decision;
- Connor gives a bounded AI specification;
- Connor independently checks the result;
- Connor diagnoses a failure from evidence;
- Connor understands the Git save point.

The agent doing the work is never sufficient evidence by itself.

## Practice versus missions versus projects

- **Practice** isolates one skill and is cheap to break.
- **Missions** combine learning with a bounded visible outcome.
- **Projects** continue over time and eventually deserve their own repository.

The curriculum should increasingly be driven by Connor's real project ideas rather than a fixed list of artificial exercises.
