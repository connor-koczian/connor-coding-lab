# AI-Native Curriculum V1 — Phase 5 Implementation Record

**Phase:** 5 — AI-native curriculum  
**Branch:** `learning/ai-native-curriculum-v1`  
**Base:** Phase 4 merged `main` at `bfef2a2a230bad3f3f0c08337041472639d7ee80`

## Purpose

Phase 5 turns the V2 control plane into an actual learning system without pretending that a large pile of generated lessons is a curriculum.

The design uses:

- one multi-track roadmap;
- concise track guides;
- one bounded starter mission per major track;
- focused practice lanes;
- canonical learner state from `progress/CONNOR-MASTER-TRACKER.md`;
- Antigravity mission selection based on evidence and current project interest.

## Progression model

Progress is not age-based or lesson-count based.

A learner can be advanced in game design and still need guided Git practice.

Mission completion does not equal capability promotion.

The tracker should change only when Connor personally provides evidence through explanation, decisions, execution or verification.

## Starter mission set

The initial library deliberately contains one strong entry point per major track rather than dozens of repetitive exercises:

- cross-track first evidence cycle;
- Linux navigation;
- AI specification;
- Python prediction/change;
- Git inspection;
- testing interpretation;
- evidence-led debugging;
- Snake mechanic design;
- browser change;
- software-engineering planning.

Future missions should be added because the tracker or a real project needs them.

## AI role

Antigravity may implement substantial work.

For meaningful changes it should still expose:

- goal;
- relevant files;
- important concept;
- constraints;
- acceptance checks;
- validation evidence;
- Git diff/save point.

Connor should retain meaningful product and design decisions.

## Historical material

`00-CONNOR-HQ/`, `python-basics/` and `snake-game/` remain in place.

Phase 5 does not migrate or rewrite their history.

## Acceptance requirements

Before Phase 5 is marked complete:

1. all new curriculum links/paths must resolve in the branch;
2. `/start` or `/mission` on the rehearsal ThinkPad must use the tracker and V2 mission catalogue without inventing capability;
3. at least one starter mission must be readable and executable as written after current-path verification;
4. Antigravity must not mutate learner progress merely because a mission was selected;
5. a completed rehearsal mission must distinguish AI work from Connor evidence;
6. repository state must remain reviewable and clean after any controlled rehearsal;
7. no historical project migration or Dell lifecycle work may be smuggled into Phase 5.

Static documentation presence alone is not sufficient behavioural acceptance.


## Behavioural acceptance — 2026-09-23

ThinkPad rehearsal was completed against candidate head `b5ac256e531debbb9dba75993aa6d6832fe96f0a`.

### /start behaviour

Antigravity:

- read the current branch/Git state;
- read `progress/CONNOR-MASTER-TRACKER.md`;
- read the V2 mission catalogue and starter mission;
- inspected current `python-basics` files and project configuration;
- selected **Mission FND-01 — First Evidence Cycle** from the conservative baseline;
- verified the real `uv` run/test commands before presenting them;
- did not invent higher learner capability;
- did not mutate the tracker or working tree merely to select a mission.

The tracker SHA-256 observed after this rehearsal was:

`e88992f52185369bb26ef8de1f81d7a4d8160ed0d18b68f72d58860282997f9f`

and Git remained clean.

### Bounded starter-mission execution

The rehearsal then executed:

- repository location/status inspection;
- `printf 'Minecraft\n' | uv run python src/python_basics/hello.py`;
- `uv run pytest`.

Observed runtime output confirmed that `hello.py` consumed the controlled input and produced its follow-up prompts.

Pytest ran under Python 3.12.14 / pytest 9.1.1 and reported:

`1 passed in 0.01s`

The existing test was also inspected and correctly classified: it tests `python_basics.main()`, not `hello.py`. Therefore the passing pytest result is valid automated-test evidence but is **not** proof of the interactive `hello.py` behaviour. The separate runtime execution provides that evidence.

### Final state

- Tracker SHA-256 unchanged: `e88992f52185369bb26ef8de1f81d7a4d8160ed0d18b68f72d58860282997f9f`
- Working tree: clean
- Final rehearsal candidate HEAD: `b5ac256e531debbb9dba75993aa6d6832fe96f0a`
- No historical project migration performed
- No Dell lifecycle work performed

### Acceptance classification

- Static curriculum/navigation validation: **PASS**
- V2 `/start` tracker/catalogue integration: **PASS**
- No learner-state mutation on mission selection: **PASS**
- Starter mission current-path/command verification: **PASS**
- Runtime execution evidence: **PASS**
- Automated test execution: **PASS**
- Evidence-scope distinction (runtime vs pytest): **PASS**
- Final repository cleanliness: **PASS**

Phase 5 is behaviourally accepted. PR #15 may proceed through final exact-state review and normal merge if current GitHub authority remains unchanged.
