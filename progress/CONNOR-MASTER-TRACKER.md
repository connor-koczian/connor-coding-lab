# 📈 Connor Master Tracker

**Canonical learner-state file:** `progress/CONNOR-MASTER-TRACKER.md`  
**Established:** 2026-09-22  
**Last evidence update:** 2026-09-22 — Phase 3 initialisation  
**Update owner:** Antigravity after meaningful learner sessions  
**Baseline confidence:** Conservative — seeded from repository evidence only

> This file records **Connor's demonstrated capability**, not how much code exists and not what an AI agent can do.

## Evidence rules

A repository artefact can show that a topic or project exists. It does **not** automatically prove that Connor understands, can use, can direct, or can verify it.

Use these evidence classes when updating the tracker:

- **DIRECT DEMONSTRATION** — Connor performs the task or produces the result.
- **EXPLANATION** — Connor explains the concept or behaviour accurately in his own words.
- **DECISION / SPECIFICATION** — Connor makes a meaningful design choice or gives a bounded requirement.
- **VERIFICATION** — Connor checks AI or program behaviour using appropriate evidence.
- **REPOSITORY ARTEFACT** — source/history shows exposure or prior work but not current competence by itself.
- **AI OUTPUT** — useful project evidence, but **not learner-capability evidence** unless Connor directs, explains or verifies it.
- **UNVERIFIED** — claim exists but there is not enough evidence to promote capability.

### Capability states

| State | Meaning |
| --- | --- |
| **NOT STARTED** | No reliable learner evidence yet. This does not necessarily mean Connor has never seen the topic. |
| **INTRODUCED** | There is evidence that Connor has encountered the concept or used it in a learning context. |
| **GUIDED** | Connor can perform the task with prompts, examples or active help. |
| **CAN EXPLAIN** | Connor can accurately explain the important idea in his own words. |
| **CAN USE** | Connor can apply the skill correctly with limited help. |
| **CAN DIRECT AI** | Connor can specify a bounded AI task with useful requirements/constraints. |
| **CAN VERIFY AI** | Connor can independently inspect and validate AI-produced work using suitable evidence. |
| **INDEPENDENT** | Connor repeatedly performs the capability correctly across relevant situations without routine guidance. |

`CAN DIRECT AI` and `CAN VERIFY AI` are separate capabilities. Do not treat one as proof of the other.

---

## Current Position

Connor has historical Python and Snake learning artefacts in independent project repositories, while Mission Control holds the **canonical evidence model**.

No capability is seeded above **INTRODUCED** from historical repository evidence alone.

The next meaningful learner session should establish live evidence rather than trying to reconstruct competence from old files or AI-generated project history.

## Current Objectives

1. Establish a reliable live baseline from Connor's own explanations, choices, execution and verification.
2. Use one bounded visible mission at a time.
3. Teach the development loop:
   `Understand -> Specify -> Plan -> Build -> Run -> Break -> Debug -> Improve -> Test -> Review -> Commit -> Explain`.
4. Update this tracker only when a session provides material learner evidence.
5. Keep AI execution separate from Connor-demonstrated capability.

## Skills Dashboard

| Track | Capability | State | Evidence / reason |
| --- | --- | --- | --- |
| AI-native development | Understands that AI can assist implementation while Connor remains the decision-maker | **INTRODUCED** | Historical `WebshopCompany/snake-game` README explicitly describes Connor as designer and Antigravity as builder. This proves project-role exposure, not independent AI direction. |
| Programming | Python input/output and string interpolation | **INTRODUCED** | Historical learning artefact `WebshopCompany/python-basics:src/python_basics/hello.py` uses `input()`, `print()` and an f-string. Current understanding is not yet live-verified. |
| Debugging | Evidence-led debugging loop | **NOT STARTED** | Governance teaches the loop; no canonical learner demonstration is recorded yet. |
| Git / GitHub | Inspecting status/diff and creating save points | **NOT STARTED** | Historical mission material exists, but mission completion is not proven by the repository. |
| Linux / Terminal | Navigation with `pwd`, `ls`, `cd` | **NOT STARTED** | Historical mission material exists, but no canonical live demonstration is recorded yet. |
| Testing | Running and interpreting automated tests | **NOT STARTED** | A pytest exists in the independent Python Basics repository; its existence is not proof Connor can use or explain testing. |
| Software Design | Breaking a change into goal/files/concept/acceptance checks | **NOT STARTED** | Mentor system supports this; Connor's own demonstration is not yet recorded. |
| Game Development | Game/product design decisions | **INTRODUCED** | Historical Snake README attributes design direction to Connor and implementation to Antigravity. |
| Web Development | HTML/CSS/JavaScript development | **NOT STARTED** | AI-built showcases do not count as Connor capability. |
| System Maintenance | Distinguishing project work from admin/system changes | **NOT STARTED** | Safety rules exist; no learner demonstration recorded yet. |

## AI-Native Development

**Current state:** INTRODUCED

Evidence:

- historical Snake material separates Connor's design role from Antigravity's implementation role;
- this supports exposure to AI-assisted development;
- it does **not** justify `CAN DIRECT AI` or `CAN VERIFY AI`.

Next evidence needed:

- Connor states a bounded goal;
- Connor names at least one constraint or thing that must not change;
- Connor states how success should be checked;
- Connor reviews the result rather than accepting it automatically.

## Programming Concepts

**Current state:** INTRODUCED

Repository evidence currently shows:

- Python input with `input()`;
- output with `print()`;
- an f-string using the user's answer.

Live evidence still needed before promotion:

- Connor explains what the variable stores;
- Connor predicts an output;
- Connor makes or directs a small change and explains the result.

## Debugging

**Current state:** NOT STARTED

Target method:

`reproduce -> observe -> hypothesise -> isolate -> smallest reliable fix -> rerun -> verify`

No canonical learner debugging evidence is recorded yet.

## Git / GitHub

**Current state:** NOT STARTED

Target progression:

`status -> diff -> specific-file add -> commit -> log -> branches -> merge -> pull/push -> PR -> review`

Historical mission instructions are present, but they do not prove mission completion.

## Linux / Terminal

**Current state:** NOT STARTED

Initial target capabilities:

- know the current directory;
- list files/directories;
- move into and out of project directories;
- distinguish a user-space coding command from an administrator/system command.

No canonical live learner evidence is recorded yet.

## Testing

**Current state:** NOT STARTED

A small pytest is present in the independent Python Basics repository at `tests/test_main.py`.

That proves the project contains an automated test. It does not prove Connor understands what the test checks or can use it.

## Software Design

**Current state:** NOT STARTED

Initial target:

- goal;
- relevant files;
- important concept;
- acceptance checks;
- smallest coherent change.

No canonical learner demonstration is recorded yet.

## Game Development

**Current state:** INTRODUCED

Historical evidence:

- the independent `WebshopCompany/snake-game` repository preserves the substantial historical project;
- its README attributes design/game-direction to Connor and implementation to Antigravity.

This supports exposure to game design/product decisions, not independent programming capability.

Next evidence needed:

- Connor identifies a game-loop or state concept in the code;
- Connor chooses a mechanic change;
- Connor predicts or verifies its gameplay effect.

## Web Development

**Current state:** NOT STARTED

AI-built browser showcases are reference material only and are not learner evidence.

## System Maintenance

**Current state:** NOT STARTED

Normal coding should remain non-admin.

A later learner demonstration can establish whether Connor understands why `sudo`, system packages, accounts, security settings, disks or BIOS changes cross an authority boundary.

## Active Projects

| Project | Current role | Evidence status |
| --- | --- | --- |
| `WebshopCompany/python-basics` | Independent historical small Python learning project | Original Connor history preserved; learner capability remains evidence-based |
| `WebshopCompany/snake-game` | Independent historical game project / preserved save points | Original Connor history preserved; README separates Connor design from Antigravity implementation |
| Neon City | Future Connor-owned project | Not created yet |
| AI-built demos | Showcase/reference only | Must not be treated as Connor capability |

## Current Tasks

1. Run the first tracker-backed learner session with `/start`.
2. Choose one bounded mission.
3. Collect learner evidence through explanation, decisions, execution or verification.
4. End with `/finish`.
5. Inspect the tracker diff and confirm that only evidence-supported sections changed.

## Completed Missions

No mission is marked canonically complete at Phase 3 initialisation.

Historical mission files exist under `00-CONNOR-HQ/`, but file existence alone does not prove Connor completed their acceptance checks.

## Achievements

- **Historical game-design involvement — evidence class: REPOSITORY ARTEFACT.** Snake project documentation attributes design/game-direction to Connor while identifying Antigravity as the implementation agent.
- **Historical Python learning artefact — evidence class: REPOSITORY ARTEFACT.** The Python Basics project contains a small interactive input/output program.

These are context, not automatic capability promotions.

## Bugs Connor Has Solved

No canonically evidenced learner-debugging result is recorded yet.

## Things Connor Can Do Without Help

No capability is currently promoted to **CAN USE** or **INDEPENDENT** from source-supported evidence alone.

This section should grow only after direct learner evidence.

## Things Connor Can Direct Antigravity To Do

No capability is currently promoted to **CAN DIRECT AI**.

Historical project design involvement is recorded as INTRODUCED exposure only until a live bounded specification is demonstrated.

## Areas Needing More Practice

Current baseline priorities:

- establish actual terminal/navigation ability;
- establish current Python understanding;
- establish `git status` / `git diff` understanding;
- practise one evidence-led debugging problem;
- practise defining acceptance checks before an AI change;
- practise validating AI output instead of trusting it.

## Session Log

### 2026-09-22 — Phase 3 tracker initialisation

- **Type:** control-plane initialisation, not a learner session.
- **Evidence source:** current repository authority after Phase 2 merge.
- Created the canonical learner-state structure.
- Seeded only conservative source-supported exposure.
- Did not mark historical missions complete.
- Did not promote skills because AI-generated projects or tests exist.
- No learner capability promotion occurred in this entry.

## Next Recommended Challenges

1. **Workspace orientation:** Connor demonstrates `pwd`, `ls`, `cd` and explains `git status`.
2. **Python prediction/change:** run the small Python program, predict output, change one behaviour and explain the result.
3. **AI specification:** Connor asks Antigravity for one bounded change using goal + constraint + acceptance check.
4. **Verification:** Connor inspects the diff and runs the relevant program/test before accepting the change.

---

## Update rule

After a meaningful learner session, Antigravity should update only the sections supported by new evidence.

Every capability promotion must answer:

1. **What did Connor personally demonstrate?**
2. **What evidence supports the new state?**
3. **Was the behaviour performed by Connor, by AI, or jointly?**
4. **What remains unverified?**

If those questions cannot be answered, keep the existing state.
