# Master Tracker V1 — Phase 3 Implementation Record

**Phase:** 3 — Master tracker  
**Branch:** `learning/master-tracker-v1`  
**Implementation date:** 2026-09-22  
**Canonical learner-state file:** `progress/CONNOR-MASTER-TRACKER.md`

## Purpose

Phase 3 turns learner progress from an informal idea into one canonical, evidence-controlled state file.

The tracker is not a reward board and not a count of AI-generated output. Its purpose is to let Connor return after a gap and let Antigravity answer, from evidence:

- where Connor is;
- what he has actually demonstrated;
- what he is learning now;
- what remains unverified;
- what the next useful challenge is.

## Canonical state rule

There is exactly one current learner-state file:

`progress/CONNOR-MASTER-TRACKER.md`

Do not create competing progress summaries elsewhere.

Other documents may link to the tracker but must not maintain a second capability state.

## Seed policy

The initial tracker is intentionally conservative.

Repository artefacts can establish project/context facts and limited exposure, but they do not automatically establish competence.

Examples:

- a test file proves a test exists, not that Connor understands testing;
- an AI-built game proves software exists, not that Connor can program it;
- a mission file proves the mission exists, not that Connor completed it;
- historical documentation that explicitly attributes a design role to Connor may justify INTRODUCED exposure, but not CAN DIRECT AI or CAN VERIFY AI.

No capability is seeded above INTRODUCED from historical repository evidence alone.

## Learner evidence classes

Use these when considering tracker changes:

1. **DIRECT DEMONSTRATION** — Connor performs the task or produces the result.
2. **EXPLANATION** — Connor accurately explains the important concept.
3. **DECISION / SPECIFICATION** — Connor makes a meaningful design choice or gives a bounded requirement.
4. **VERIFICATION** — Connor inspects/tests evidence and judges whether work is correct.
5. **REPOSITORY ARTEFACT** — historical/source evidence; useful context but weak competence evidence.
6. **AI OUTPUT** — project evidence, not learner evidence unless Connor directs, explains or verifies it.
7. **UNVERIFIED** — insufficient evidence for promotion.

## Capability state semantics

- **NOT STARTED** — no reliable learner evidence yet.
- **INTRODUCED** — evidence of exposure in a learning context.
- **GUIDED** — performs with active help/prompts.
- **CAN EXPLAIN** — accurately explains in own words.
- **CAN USE** — applies correctly with limited help.
- **CAN DIRECT AI** — specifies bounded AI work with meaningful constraints/acceptance checks.
- **CAN VERIFY AI** — independently checks AI work using appropriate evidence.
- **INDEPENDENT** — repeated correct use across relevant situations without routine guidance.

`CAN DIRECT AI` and `CAN VERIFY AI` are deliberately separate.

## Update transaction

For a meaningful learner session:

1. read the current tracker before proposing learner-state claims;
2. gather only current-session evidence plus relevant repository evidence;
3. distinguish Connor actions from Antigravity actions;
4. identify exactly which tracker sections are materially affected;
5. propose the smallest evidence-supported change;
6. do not promote unrelated skills;
7. preserve uncertainty;
8. add one concise session-log entry;
9. inspect the tracker diff;
10. state what was not promoted and why when that distinction matters.

If the session produced no learner evidence, the tracker may remain unchanged.

## Promotion guardrails

A capability must not be promoted because:

- code compiled;
- tests passed;
- Antigravity implemented a feature;
- a project already contains advanced code;
- a mission document exists;
- Connor merely watched an action happen.

Promotion requires learner evidence appropriate to the target state.

Examples:

- **CAN EXPLAIN** needs a real explanation.
- **CAN USE** needs correct use.
- **CAN DIRECT AI** needs a useful bounded specification.
- **CAN VERIFY AI** needs Connor-led verification.
- **INDEPENDENT** needs repeated evidence, not one success.

## Start-session behaviour

`start-session` must:

- read the tracker when it exists;
- treat it as the learner-state authority;
- separately inspect current Git/project state;
- not overwrite tracker evidence with assumptions from project complexity;
- choose a next mission consistent with both learner evidence and current repository reality.

## Finish-session behaviour

`finish` must:

- validate the work first;
- review Git state/diff;
- identify Connor-specific evidence;
- apply `update-master-tracker` only when the session was meaningful;
- avoid capability promotion when evidence is insufficient;
- leave a useful next challenge.

## ThinkPad behavioural acceptance — first start test

The first Phase 3 `/start` test on the rehearsal ThinkPad confirmed that Antigravity:

- read the canonical `progress/CONNOR-MASTER-TRACKER.md`;
- reported the conservative baseline rather than inventing stronger learner state;
- identified the Phase 3 branch and a clean working tree;
- selected a bounded Python-basics next task.

The same test exposed one tooling defect: the briefing proposed Ubuntu/system `python3` for the uv-managed `python-basics` project instead of following the project's documented `uv` workflow.

Repair applied:

- `start-session` now requires inspection of the target project's declared README/pyproject/lockfile/scripts before presenting run/setup/test commands;
- uv-managed projects must use the documented `uv` workflow rather than system `python3`, raw `pip`, or an unrelated environment.

This repair requires one short `/start` re-test before continuing the tracker mutation tests.

## Phase 3 behavioural acceptance

Before Phase 3 is merged:

1. Antigravity `/start` reads `progress/CONNOR-MASTER-TRACKER.md` and reports the conservative baseline rather than saying the tracker is absent.
2. A test session with **no learner demonstration** does not promote a capability merely because Antigravity reads or modifies code.
3. A bounded simulated learner demonstration can update one relevant capability and one session-log entry without rewriting unrelated sections.
4. `CAN DIRECT AI` and `CAN VERIFY AI` remain distinct.
5. Historical mission files are not marked complete without evidence.
6. AI-built showcase/project complexity is not converted into learner competence.
7. The tracker diff is understandable and bounded.
8. Governance files remain unchanged during routine tracker updates.
9. Git status/diff after read-only acceptance tests remains clean.

Phase 3 is not complete until these behaviours are exercised on the rehearsal environment.


## Behavioural acceptance result — 2026-09-22

The Phase 3 candidate was exercised on the rehearsal ThinkPad in Connor's VS Code/Antigravity environment.

Observed:

- `/start` read `progress/CONNOR-MASTER-TRACKER.md` and used the conservative learner baseline;
- an initial `/start` suggested system `python3` for the uv-managed `python-basics` project;
- that defect was repaired by requiring project-workflow inspection before run/setup/test commands;
- the repaired `/start` used the documented `uv run python ...` workflow;
- inspection of the advanced Snake project did not promote Connor merely because complex code or AI-built work existed;
- a controlled simulated `/finish` test promoted only Linux/Terminal from NOT STARTED to GUIDED and updated the matching detail section plus one clearly labelled simulated session-log entry;
- no unrelated capability was promoted;
- `CAN DIRECT AI` and `CAN VERIFY AI` remained unchanged and distinct;
- no historical mission was marked complete;
- no governance file changed;
- nothing was staged or committed during the simulated learner-state update;
- the simulated tracker mutation was restored afterwards and the working tree returned clean.

The rehearsal terminal also auto-activated the `python-basics/.venv` environment when VS Code/Python tooling selected that project. This is not a tracker defect. Phase 4 owns the cockpit/terminal behaviour and must establish a neutral Mission Control terminal while retaining explicit project execution through `uv run ...`.

**Phase 3 behavioural acceptance: PASS.**

Phase 3 is ready for PR integration review.
