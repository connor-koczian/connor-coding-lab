# Connor Coding Lab V2 — Approved Master Implementation Plan

**Status:** IMPLEMENTATION IN PROGRESS — PHASE 11 IMPLEMENTED / ACCEPTANCE PR  
**Approved by:** Geza  
**Approval date:** 2026-09-22  
**Canonical preparation repository:** `WebshopCompany/connor-coding-lab`  
**Frozen pre-V2 baseline commit:** `07871cbf2e96e919b63437a5c91bec8e86a2ffea`  
**Frozen pre-V2 backup branch:** `backup/pre-v2-2026-09-22`

This document is the canonical implementation authority for Connor Coding Lab V2.

Do not reconstruct the V2 design from chat history. Future implementation sessions must begin by reading this file, inspecting CURRENT GitHub `main`, and checking the phase tracker below.

The Dell remains outside implementation authority until Geza explicitly confirms Father's ASUS migration is accepted and the Dell is released for Connor.

---

## 1. Purpose

Connor Coding Lab V2 is a long-term AI-native programming and engineering environment for Connor.

Connor is not being trained to type large amounts of code manually merely because that was historically normal.

The target capability is:

> Connor can turn an idea into functioning software by designing it, communicating requirements to Antigravity, understanding the important concepts and architecture, directing implementation, testing behaviour, diagnosing failures, reviewing changes, managing Git history, and improving the product.

Antigravity is the primary day-to-day teacher, mentor, coding agent, debugger, tester and reviewer.

Connor remains the learner, product owner, designer, decision-maker, tester, reviewer and eventual technical director of his projects.

Antigravity may write substantial code once Connor understands the relevant concepts. Manual typing is not an achievement in itself.

The learning standard is:

> Can Connor direct and verify the engineering?

not:

> Can Connor manually type every implementation?

Connor should advance as rapidly as demonstrated understanding, curiosity and capability permit. Age must not impose an artificial ceiling, but no capability is considered mastered merely because AI completed the work.

---

## 2. Core learning principle

The operating loop is:

`Understand -> Specify -> Plan -> Build -> Run -> Break -> Debug -> Improve -> Test -> Review -> Commit -> Explain -> Update Progress`

For AI-assisted work:

`Connor chooses -> Antigravity helps/builds -> Connor runs/tests -> evidence is inspected -> Connor understands enough to direct/verify -> Git records the save point`

Antigravity must not optimise for code volume.

---

## 3. Repository strategy

The long-term architecture is **Mission Control + independent serious project repositories**, not one permanent monorepo containing Connor's entire development life.

Target local topology:

```text
~/Projects/Connor/
|
|-- connor-coding-lab/          # Mission Control / learning control-plane repo
|
`-- projects/
    |-- python-basics/           # independent Git repo eventually
    |-- snake-game/              # independent Git repo eventually
    |-- neon-city/               # created only when Connor starts it
    |-- future-game/
    |-- future-website/
    `-- ...
```

Small exercises and disposable practice remain in the Mission Control repository.

Meaningful continuing products become independent repositories.

Do not introduce Git submodules initially. Use sibling repositories plus a multi-root workspace.

---

## 4. Preparation and ownership authority

Until final acceptance:

- canonical authority remains `WebshopCompany/connor-coding-lab`;
- any extracted project repositories remain under `WebshopCompany`;
- do not assume transfer to `connor-koczian` has happened;
- current GitHub state always wins over chat history;
- imported `python-basics` and `snake-game` history must be preserved.

Only after the complete environment is implemented, rehearsed and accepted should repositories be deliberately handed over to Connor's GitHub ownership.

---

## 5. Target Mission Control architecture

Target structure:

```text
connor-coding-lab/
|
|-- README.md
|-- START-HERE.md
|-- GEMINI.md
|-- AI-CODING-RULES.md
|-- Connor-Coding-Lab.code-workspace
|
|-- .agents/
|   |-- rules/
|   |   |-- core-mentor.md
|   |   |-- learning-model.md
|   |   |-- safety.md
|   |   |-- git-and-change-control.md
|   |   |-- project-engineering.md
|   |   `-- system-maintenance.md
|   `-- skills/
|       |-- start-session/SKILL.md
|       |-- teach-concept/SKILL.md
|       |-- prompt-coach/SKILL.md
|       |-- plan-feature/SKILL.md
|       |-- build-feature/SKILL.md
|       |-- debug-with-connor/SKILL.md
|       |-- test-and-verify/SKILL.md
|       |-- review-diff/SKILL.md
|       |-- update-master-tracker/SKILL.md
|       |-- create-project/SKILL.md
|       |-- safe-maintenance/SKILL.md
|       |-- start/SKILL.md
|       |-- mission/SKILL.md
|       |-- build/SKILL.md
|       |-- debug/SKILL.md
|       |-- review/SKILL.md
|       |-- finish/SKILL.md
|       |-- new-project/SKILL.md
|       `-- maintenance/SKILL.md
|
|-- missions/
|   |-- README.md
|   |-- foundations/
|   |-- ai-native-development/
|   |-- python/
|   |-- debugging/
|   |-- git-github/
|   |-- linux/
|   |-- game-development/
|   |-- web/
|   `-- engineering/
|
|-- learning/
|   |-- ROADMAP.md
|   |-- AI-AND-PROMPTING.md
|   |-- PYTHON.md
|   |-- GIT-AND-GITHUB.md
|   |-- DEBUGGING.md
|   |-- LINUX.md
|   |-- TESTING.md
|   |-- GAME-DEVELOPMENT.md
|   |-- WEB-DEVELOPMENT.md
|   `-- SOFTWARE-ENGINEERING.md
|
|-- practice/
|   |-- python/
|   |-- debugging/
|   |-- terminal/
|   |-- git/
|   `-- web/
|
|-- progress/
|   `-- CONNOR-MASTER-TRACKER.md
|
|-- showcase/
|   |-- neon-city-preview/
|   `-- snake-overdrive/
|
|-- docs/
|   |-- mentor/
|   |-- admin/
|   `-- governance/
|
|-- scripts/
|   |-- lab
|   |-- learner/
|   `-- admin/
|
|-- .vscode/
|   |-- settings.json
|   |-- extensions.json
|   `-- tasks.json
|
`-- .github/
    `-- workflows/
```

This is a target. Do not bulk-move historical material in the first implementation PR.

---

## 6. Antigravity is the primary mentor

Antigravity must be configured as a persistent, structured mentor system rather than a generic chat assistant.

Three control layers are required.

### Layer 1 — persistent rules

Always-relevant teaching, safety, Git and engineering policy.

Core expectations include:

- Connor is the learner and decision-maker.
- Teach real terminology.
- Do not underestimate Connor because of age.
- Do not advance solely because AI completed a task.
- Do not require unnecessary manual typing.
- Explain important architecture and concepts.
- Prefer visible, motivating projects.
- Never hide failures.
- Never fabricate validation.
- Protect secrets.
- Respect Git/change-control boundaries.
- Do not perform system administration without appropriate authority.

### Layer 2 — skills

Task-specific mentor behaviours loaded when relevant, including:

- start session;
- teach a concept;
- coach AI prompting/specification;
- plan a feature;
- build a bounded feature;
- debug with Connor;
- test and verify;
- review a diff;
- update the master tracker;
- create a new project correctly;
- guide safe maintenance.

### Layer 3 — learner command skills

Connor should have memorable operating commands such as:

- `/start`
- `/mission`
- `/build`
- `/debug`
- `/review`
- `/finish`
- `/new-project`
- `/maintenance`

**Current implementation decision (verified 2026-09-22):** Google Antigravity now treats Agent Skills as the durable mechanism for reusable procedures and slash commands. Legacy `.agents/workflows/*.md` are deprecated and scheduled for retirement on 2026-11-01. Therefore V2 implements these learner commands as skills under `.agents/skills/<command>/SKILL.md` rather than creating new deprecated workflow files.

This preserves the approved learner-facing slash-command experience while following current Antigravity conventions.

---

## 7. Canonical learner state

There must be exactly one canonical current learner-state/planner file:

`progress/CONNOR-MASTER-TRACKER.md`

Connor does not maintain it manually.

Antigravity is responsible for maintaining it after meaningful sessions and milestones.

Git history provides the audit trail.

Required sections:

- Current Position
- Current Objectives
- Skills Dashboard
- AI-Native Development
- Programming Concepts
- Debugging
- Git / GitHub
- Linux / Terminal
- Testing
- Software Design
- Game Development
- Web Development
- System Maintenance
- Active Projects
- Current Tasks
- Completed Missions
- Achievements
- Bugs Connor Has Solved
- Things Connor Can Do Without Help
- Things Connor Can Direct Antigravity To Do
- Areas Needing More Practice
- Session Log
- Next Recommended Challenges

Capability states should include:

- NOT STARTED
- INTRODUCED
- GUIDED
- CAN EXPLAIN
- CAN USE
- CAN DIRECT AI
- CAN VERIFY AI
- INDEPENDENT

`CAN DIRECT AI` and `CAN VERIFY AI` are intentionally separate.

No skill should be promoted merely because Antigravity performed it successfully.

---

## 8. Antigravity session responsibility

At the beginning of a session Antigravity should establish from current evidence:

- Connor's demonstrated current level;
- the last meaningful work;
- current active projects;
- unfinished work;
- concepts already introduced;
- current mission;
- sensible next stretch;
- Git/project state relevant to the task.

At the end of meaningful work Antigravity should:

1. review what happened;
2. run/inspect applicable checks;
3. inspect relevant Git changes;
4. test Connor's understanding proportionately;
5. distinguish AI work from Connor-demonstrated competence;
6. update `CONNOR-MASTER-TRACKER.md`;
7. recommend the next bounded challenge.

A future Connor should be able to return after a gap, invoke `/start`, and continue without Geza reconstructing the previous session.

---

## 9. AI-native development curriculum

Prompt engineering is included, but the curriculum is broader: **AI collaboration engineering**.

Connor should progressively learn:

### Early

- WHAT is wanted;
- WHY it is wanted;
- WHAT must not change;
- HOW success will be verified.

### Then

- goal;
- context;
- requirement;
- constraint;
- example;
- acceptance criterion.

### Then

- request a plan before code;
- decompose a feature;
- compare options;
- ask for explanations;
- challenge assumptions;
- identify uncertainty;
- request tests;
- request diff review;
- debug from evidence.

### Later

- persistent instructions;
- context engineering;
- skills;
- workflows;
- tool permissions;
- MCP;
- specialised agents;
- model choice;
- agent orchestration.

Connor should learn enough manual operation to build correct mental models, then progressively delegate mechanical execution to Antigravity.

---

## 10. Curriculum tracks

The learning system is multi-track.

### A. Computer and Linux

Files, paths, processes, terminal, permissions, installation concepts, networking and maintenance.

### B. AI-native development

Prompting, specification, context, planning, agent workflows, verification and orchestration.

### C. Programming

Variables, types, conditions, loops, functions, data structures, modules, files and objects where useful.

Manual typing is used to build understanding, not as an endurance exercise.

### D. Debugging

`reproduce -> observe -> hypothesise -> isolate -> smallest reliable fix -> rerun -> verify`

### E. Git and GitHub

Understand progressively:

`status -> diff -> specific-file stage -> commit -> log -> branch -> merge -> remote -> push/pull -> PR -> review`

Once Connor understands an operation, Antigravity may increasingly execute it while Connor reviews intent and result.

### F. Testing and verification

Primary question:

> How can I prove the thing Antigravity built actually works?

### G. Game development

Movement, state, collision, UI, assets, game loops, levels, sound, persistence and architecture.

### H. Web development

HTML, CSS, JavaScript, browser debugging and progressively richer frontend work.

### I. Software engineering

Requirements, architecture, dependencies, APIs, review, documentation, CI and project organisation.

### J. Safety and maintenance

Dependencies, updates, credentials, permissions, safe internet use, safe AI use and operating-system maintenance.

---

## 11. Project categories

### Practice

Short exercises and investigations live inside Mission Control.

### Projects

Continuing products get independent Git repositories.

Examples:

- `python-basics`
- `snake-game`
- `neon-city`
- future games
- websites
- utilities
- automation

### Showcase

AI-built reference material remains clearly labelled as showcase/reference work.

Current technology previews should ultimately live under `showcase/`.

Connor may inspect, modify and reverse-engineer them, but their existence is not evidence that he created or mastered them.

---

## 12. Historical project migration

Current imported `python-basics` and `snake-game` histories are meaningful and must be preserved.

They should eventually be extracted into independent repositories through a dedicated history-preserving migration.

Do not implement this by simply copying directories and deleting the originals.

The migration must verify history and resulting Git identity before the Mission Control working tree removes the historical folders.

This is a separate phase, not part of the first V2 foundation PR.

---

## 13. VS Code / Antigravity cockpit

Connor should open one coherent workspace.

The target experience should expose:

- Mission Control;
- current independent projects;
- rendered current mission;
- Git/source-control view;
- Antigravity;
- integrated terminal.

Markdown should open in rendered preview by default, while source/raw mode remains available when Connor is ready to edit Markdown directly.

Missions should use visual Markdown where useful:

- headings;
- emojis;
- diagrams;
- Mermaid where supported;
- concise tables;
- code blocks;
- commands;
- expected outputs;
- checklists;
- screenshots when genuinely useful;
- clickable navigation.

The integrated terminal should be visible/available from workspace start.

Workspace startup tasks must be safe and must not silently mutate environments or install software.

---

## 14. Extensions

Use a curated extension baseline, not a large extension collection.

At implementation time verify current extension IDs and current Antigravity integration.

Initial capabilities should cover:

- Python;
- Ruff;
- Antigravity/current supported integration;
- Git/GitHub integration when pedagogically useful.

Add web, formatting, database, container or other tooling only when the learning/project stage justifies it.

---

## 15. `lab` control command

Evolve the current launcher into one learner-friendly control entry point, likely:

`./scripts/lab`

Potential functions:

- `lab start`
- `lab status`
- `lab projects`
- `lab run`
- `lab doctor`
- `lab git`
- `lab maintenance`
- `lab help`

Exact commands are implementation details. Do not hide concepts Connor is actively learning behind wrappers prematurely.

Antigravity may invoke the same tooling.

---

## 16. GitHub governance

Before Connor works independently:

- keep `main` stable;
- protect `main` where the current GitHub plan/permissions support it;
- disable force-push/deletion where possible;
- use bounded branches for substantive work;
- introduce small, understandable CI;
- use PRs progressively;
- avoid enterprise bureaucracy that adds no learning value.

Automation should be explained as independent verification of a save point.

---

## 17. System administration model

Connor should initially remain a normal non-admin Linux user.

This does not require logging out of Connor's graphical session whenever Geza needs administrative access.

Future model:

```text
Connor desktop remains active
    -> Geza deliberately authenticates/administers
    -> system-level maintenance is performed
    -> admin authority ends
    -> Connor continues
```

Connor may observe and progressively learn system maintenance.

Do not give Antigravity unrestricted root authority.

The privilege model may later evolve if Connor demonstrates appropriate competence.

---

## 18. Safety boundaries

Antigravity may operate broadly inside the Connor coding workspace subject to Git/change-control rules.

It must not autonomously:

- use `sudo`;
- change system configuration;
- change accounts;
- alter BIOS/storage settings;
- install arbitrary system packages;
- expose network services externally;
- retrieve/expose secrets;
- modify SSH/private keys;
- bypass permissions;
- disable security controls;
- make destructive machine changes.

Never commit passwords, tokens, API keys, private keys, secret `.env` values, private family information or credentials.

Unknown packages, extensions, install scripts and external code must be treated as dependencies that require understanding and appropriate review.

---

## 19. Control-plane integrity

Antigravity may routinely update:

`progress/CONNOR-MASTER-TRACKER.md`

and legitimate project documentation.

Antigravity must **not silently redefine its own governance**.

Changes to core mentor/safety/change-control instructions require a deliberate reviewed Git change.

The governance layer and learner state are intentionally separate.

---

## 20. Dell boundary

The Dell still belongs to Father's migration fallback.

Until Geza explicitly confirms Father's ASUS migration is accepted and the Dell is released for Connor, do not:

- wipe;
- repartition;
- erase;
- install Ubuntu;
- change BIOS storage/SATA settings;
- perform other destructive machine-lifecycle work.

Repository redesign, curriculum, VS Code configuration and provisioning-script design may proceed.

The separate `gk-home-lab` authority remains responsible for the physical machine lifecycle.

---

## 21. Implementation programme

Implementation must be phased. Do not perform one uncontrolled bulk rewrite.

### Phase tracker

- [x] **Phase 0 — Architecture approval**
  - V2 architecture approved by Geza.
  - Current pre-V2 `main` frozen at `07871cbf2e96e919b63437a5c91bec8e86a2ffea`.
  - Backup branch: `backup/pre-v2-2026-09-22`.

- [x] **Phase 1 — Mission Control foundation**
  - Branch: `foundation/mission-control-v2`
  - PR: `#11`
  - Established the target control-plane information architecture.
  - Added root visual Mission Control entry point.
  - Established governance, mentor, learning, missions, practice, progress and showcase boundaries.
  - Preserved historical project directories unchanged.
  - Replaced the old HQ start page with a compatibility pointer.
  - Documented transition debt instead of opportunistically rewriting later-phase material.

- [x] **Phase 2 — Antigravity mentor system**
  - Branch: `agent/antigravity-mentor-v1`
  - PR: `#12`
  - Re-verified current Antigravity project instruction/rules/skills format against official documentation.
  - Implemented 6 persistent mentor rules under `.agents/rules/`.
  - Implemented 19 workspace skills under `.agents/skills/`, including the 8 approved learner command skills.
  - Preserved the learner command model as skills rather than deprecated workflow files.
  - Implemented evidence/validation behaviour and governance self-modification boundaries.
  - ThinkPad behavioural acceptance found and repaired evidence-grounding defects in `start` and `mission`.
  - Re-test passed on 2026-09-22: verified paths/commands, evidence-qualified runtime claims, no invented tracker state, and a clean Git working tree.
  - After the repaired branch was reloaded in VS Code, Antigravity slash autocomplete displayed the workspace `start`, `start-session` and other skills; `/start` discovery therefore passed on the rehearsal surface. Natural-language invocation remains a valid fallback.
  - Phase 2 merged into `main` at `32c8b62a80d3c1f2a62cd680bbd7e3abe8e019c1` after behavioural acceptance.

- [x] **Phase 3 — Master tracker**
  - Branch: `learning/master-tracker-v1`
  - PR: `#13`
  - Added canonical `progress/CONNOR-MASTER-TRACKER.md`.
  - Seeded a conservative repository-supported baseline with no capability above INTRODUCED from historical artefacts alone.
  - Implemented learner evidence classes and guarded capability-state promotion.
  - Activated the `update-master-tracker` protocol.
  - Integrated tracker authority into `start-session` and evidence-based updates into `finish`.
  - Rehearsal `/start` read the tracker correctly and preserved the conservative baseline.
  - First `/start` exposed an incorrect system-`python3` suggestion for the uv-managed Python project; repaired by requiring declared project-workflow inspection before run/setup/test commands.
  - Re-test used the documented `uv` workflow correctly.
  - Anti-inflation test confirmed that advanced Snake/AI artefacts do not promote Connor's competence.
  - Controlled simulated `/finish` test changed only the relevant Linux/Terminal capability, its detail section and one clearly labelled session-log entry; unrelated capabilities, historical missions and governance remained unchanged.
  - The simulated learner-state mutation was restored completely; the rehearsal working tree returned clean.
  - `CAN DIRECT AI` and `CAN VERIFY AI` remained distinct throughout acceptance.
  - Phase 3 merged into `main` at `f5866c7e29195ed1a4dee4e5d0ecff87f4b98a64` after behavioural acceptance.

- [x] **Phase 4 — VS Code / cockpit UX**
  - Branch: `ux/vscode-mission-control-v1`
  - PR: `#14`
  - Added canonical `Connor-Coding-Lab.code-workspace`.
  - Added a transitional three-root cockpit: Mission Control, Python Basics and Snake Game, without submodules.
  - Hid nested historical project folders from the Mission Control root to avoid duplicate Explorer/search results.
  - Added Markdown preview-first editing while preserving raw Markdown Git diffs.
  - Added a safe automatic interactive Mission Control terminal task for trusted workspaces.
  - Kept the Mission Control terminal neutral; ThinkPad rehearsal confirmed `VIRTUAL_ENV=<none>`.
  - Added curated Antigravity/Python/Pylance/Python-Environments/debugpy/Ruff extension recommendations.
  - Added visible Git-status, lab-menu, Python run/test/lint and Snake run tasks.
  - Disabled smart commit and automatic fetch to preserve Git learning and avoid private-remote authentication noise.
  - ThinkPad behavioural acceptance on 2026-09-23 confirmed the intended three-root Explorer layout without duplicates, rendered `START-HERE.md`, Antigravity `/start` discovery, Git-status task execution, `Python Basics: Tests` with 1 passing test, and a clean final working tree at the accepted candidate head.
  - Phase 4 merged into `main` at `bfef2a2a230bad3f3f0c08337041472639d7ee80` after behavioural acceptance.

- [x] **Phase 5 — AI-native curriculum**
  - Branch: `learning/ai-native-curriculum-v1`
  - PR: `#15`
  - Candidate implementation in progress from Phase 4 merged `main`.
  - Expanded `learning/ROADMAP.md` into a demonstrated-capability, multi-track progression model.
  - Added track guides for AI collaboration, Python, Linux, Git/GitHub, debugging, testing, game development, web development and software engineering.
  - Added one bounded starter mission per major track plus a cross-track first evidence cycle.
  - Added focused practice lanes for Python, debugging, terminal, Git and web work.
  - Integrated mission selection with the canonical master tracker without mutating learner state during curriculum construction.
  - Updated `/start` and `/mission` behaviour to use the V2 mission catalogue and evidence rules.
  - Preserved Connor as designer/decision-maker while allowing Antigravity substantial implementation work with explicit validation.
  - Preserved historical `00-CONNOR-HQ/`, `python-basics/` and `snake-game/` material unchanged.
  - Added `docs/mentor/AI-NATIVE-CURRICULUM-V1-IMPLEMENTATION.md` with Phase 5 design and behavioural acceptance requirements.
  - Static validation resolved 43 internal Markdown navigation targets with 0 failures and confirmed the tracker, historical Python/Snake projects and Dell lifecycle files were unchanged.
  - ThinkPad `/start` rehearsal read the canonical tracker and V2 mission catalogue, selected `FND-01 — First Evidence Cycle`, verified current paths/`uv` commands, and did not mutate learner state.
  - Bounded mission execution ran `hello.py` with controlled input and `uv run pytest`; runtime output was observed, pytest reported 1 passing test, and the test scope was correctly distinguished from `hello.py` behaviour.
  - Tracker SHA-256 remained `e88992f52185369bb26ef8de1f81d7a4d8160ed0d18b68f72d58860282997f9f`; final Git state was clean at candidate head `b5ac256e531debbb9dba75993aa6d6832fe96f0a`.
  - Phase 5 merged into `main` at `9c3fa2ceefa1cf203d0bf9ab547b17b1478ca003` after behavioural acceptance.

- [x] **Phase 6 — Lab control tooling**
  - Branch: `tooling/lab-control-v2`
  - PR: `#16`
  - Candidate implementation in progress from Phase 5 merged `main`.
  - Added executable learner control entry point at `./scripts/lab`.
  - Added help/start/status/projects/run/doctor/git/computer/maintenance/menu capabilities.
  - Delegated run/Git actions print the real working directory and command before execution.
  - `lab doctor` is read-only and does not silently install, sync, repair or mutate Git.
  - `lab git` is deliberately inspection-only; staging/commit/pull/push remain explicit Git work.
  - Converted `scripts/run-lab.sh` and `scripts/check-environment.sh` into compatibility shims to the V2 control command.
  - Updated VS Code tasks to expose Lab Status, Lab Doctor and the V2 Lab Menu.
  - Added `docs/mentor/LAB-CONTROL-V2-IMPLEMENTATION.md` with design and ThinkPad acceptance requirements.
  - Static validation confirmed executable script modes, valid VS Code task JSON, no hidden `uv sync`, and no Git fetch/pull/push/add/commit operations in the new control command.
  - ThinkPad rehearsal completed the prescribed Phase 6 command set, including syntax/help/status/projects/doctor/Git-inspection/Python-run and compatibility checks.
  - `lab doctor` reported `DOCTOR: PASS` as normal user `connor`, with Git, uv, VS Code, Python 3.12 and required repository metadata present, a clean working tree, and no active project virtual environment.
  - Legacy `run-lab.sh` compatibility menu exited cleanly; legacy `check-environment.sh` visibly forwarded to the read-only doctor.
  - Tracker SHA-256 remained `e88992f52185369bb26ef8de1f81d7a4d8160ed0d18b68f72d58860282997f9f`; final Git state was clean at candidate head `084f9220b3a1fcf5255343b81dfd9d5adcf1e07a`.
  - Phase 6 merged into `main` at `9f62b7fea276f98a463ddd23bd3e3281b7fad0fb` after behavioural acceptance.

- [x] **Phase 7 — Safety, governance and CI**
  - Branch: `governance/safety-ci-v1`
  - Candidate implementation in progress from Phase 6 merged `main`.
  - Added minimal GitHub Actions CI for repository policy, shell syntax, read-only lab doctor, Python Basics Ruff/pytest and Snake Pygame import.
  - CI uses read-only `contents` permission and pinned action revisions.
  - Added executable `scripts/check-repo-policy.sh` to reject tracked secret/private-key style files, detect private-key headers without printing secret contents, verify core control files and executable script modes.
  - Added `SECURITY.md` covering secrets, credential response, dependencies/downloaded code, internet/network exposure, AI/connector data sharing and administrator boundaries.
  - Extended Antigravity safety and Git/change-control rules with external-service, credential-incident and CI/protected-main expectations.
  - Added `docs/governance/MAIN-BRANCH-PROTECTION.md` with the deliberately small target ruleset for `main`.
  - No repository ruleset existed at Phase 7 start. Classic branch-protection inspection returned 403 because the current GitHub integration lacks administration permission.
  - Branch protection therefore remains a post-merge manual GitHub setting: require PR + Phase 7 CI check, block force pushes and block deletion.
  - Added `docs/mentor/SAFETY-GOVERNANCE-CI-V1-IMPLEMENTATION.md` with acceptance sequence.
  - PR CI run `35834432161` / job `validate` completed successfully. Logs confirmed read-only `contents` token permission, repository-policy PASS, shell-syntax PASS, Lab Doctor PASS WITH EXPECTED CI WARNING (no VS Code CLI), Python Basics Ruff PASS + pytest `1 passed`, and Snake Pygame 2.6.1 import PASS.
  - ThinkPad rehearsal passed repository policy, Bash syntax and Lab Doctor as normal user `connor`; `.env` and `*.pem` ignore rules were observed; tracker SHA-256 remained `e88992f52185369bb26ef8de1f81d7a4d8160ed0d18b68f72d58860282997f9f`; final tree was clean at candidate head `fb9d09e014faa86a1cb7e22639ef8a5062c68d5e`.
  - Phase 7 implementation merged through PR #17 into `main` at `63c1c14a99eb5568e7c88a0b6f079abe78bf7804`.
  - Post-merge push CI run `35835236186` completed successfully on that exact `main` commit; check-run name is `validate` from GitHub Actions.
  - Geza created repository ruleset `Main branch protection` (ID `23868188`) and CURRENT GitHub verification confirmed it is active on the default branch with no bypass actors, PR required, 0 required approvals, deletion blocked, force-push blocked, and required status check `validate` bound to GitHub Actions integration `15368`.
  - Phase 7 is complete. Phase 8 may begin only as a read-only history/extraction assessment before any migration transaction.

- [x] **Phase 8 — Historical project repository extraction**
  - Separate history-preserving migration completed from protected Mission Control `main`.
  - Created private `WebshopCompany/python-basics` and `WebshopCompany/snake-game` repositories without synthetic initial commits.
  - Python Basics preserves Connor's original 3 commits unchanged through original head `97c51706c44b521f3473c8936f4931850c11ef69`; two bounded post-import commits reproduce the current project state.
  - Python Basics extracted head: `82f11181755839cac40c50419e972f534c0cf634`; final tree: `91f57117b5cafc2c88c3e86e3dd9bc6d49658706`.
  - Python validation passed with uv-managed Python 3.12.14, Ruff, pytest (`1 passed`) and controlled interactive runtime input.
  - Snake preserves Connor's original 10 commits unchanged through original head `a31761a0ea3503c71db8eea6d3279ef0bc8ab8ab`; one bounded post-import commit applies the Python 3.12 baseline.
  - Snake extracted head: `7d6fa8b0c1b13d1bad14028be3556b4d6035449b`; final tree: `43330b81e8afab839ead624f5e0f0f12e1453c5e`.
  - Snake validation passed with uv-managed Python 3.12.14, Pygame 2.6.1 import and Python bytecode compilation.
  - GitHub verification independently confirmed commit counts (Python 5, Snake 11), exact original lineage and exact final tree identities.
  - Mission Control `main` remained unchanged during extraction.
  - Embedded project directories remain temporarily in Mission Control until Phase 9 rewires the cockpit, tooling, CI, missions and documentation to the independent repositories and validates the replacement topology.

- [x] **Phase 9 — Multi-repository workspace integration**
  - Branch: `integration/multi-repo-workspace-v1`; PR: `#20`.
  - Target topology accepted on the ThinkPad: `~/Projects/Connor/connor-coding-lab` plus `~/Projects/Connor/projects/python-basics` and `~/Projects/Connor/projects/snake-game`.
  - Rewired `Connor-Coding-Lab.code-workspace` to the two sibling independent repositories; no Git submodules.
  - Rewired VS Code Python/Snake tasks to named independent workspace roots.
  - Reworked `scripts/lab` to discover the sibling project repositories, show independent Git state, run targets from the correct repository and perform a read-only multi-repository doctor.
  - Added explicit `--mission-control-only` doctor mode for Mission Control CI; local full doctor still requires the two project repositories.
  - Scoped Mission Control CI to the control plane and workspace JSON. Python Basics and Snake each have their own independent `validate` CI workflow.
  - Retired the old destructive `cleanup-legacy-workspace.sh` behaviour because independent project directories must never be treated as disposable legacy folders.
  - Updated current learner missions, tracker repository references, security text and fresh-clone acceptance to the independent-repository model without promoting learner capability.
  - Removed the duplicate embedded `python-basics/` and `snake-game/` trees after Phase 8 history preservation and independent project CI were established.
  - Candidate CI run `35839739778` passed.
  - ThinkPad target-layout rehearsal passed: full multi-repo doctor, independent clean Git state, Python runtime/Ruff/pytest, Snake static validation, all launcher menu targets, Classic Snake, Campaign Snake and browser Snake.
  - Antigravity `/start` correctly read the canonical Mission Control tracker, discovered `/home/connor/Projects/Connor/projects/python-basics` as an independent project root, ran its current pytest workflow, and did not fall back to the removed monorepo project paths.
  - Learner tracker SHA remained unchanged during the system rehearsal.
  - Phase 9 accepted. Phase 10 is the next incomplete phase.

- [x] **Phase 10 — ThinkPad rehearsal**
  - Fresh-cloned Mission Control, Python Basics and Snake Game from final `main` into the target `~/Projects/Connor/` topology.
  - Verified exact expected heads, `main` branches and clean working trees in all three repositories.
  - Full multi-repository `./scripts/lab doctor` passed.
  - Python Basics ran through Mission Control using uv-managed Python 3.12.14; Ruff passed and pytest reported `1 passed`.
  - Snake Game created its uv environment under Python 3.12.14 and passed static compilation.
  - All learner menu items and interactive games/showcases were exercised successfully, including Pygame and browser targets.
  - Antigravity `/start` read the canonical tracker, discovered the independent project roots and selected Mission FND-01 from current evidence.
  - Antigravity `/finish` correctly detected that no Connor learner evidence had been produced and left capability states unchanged; the evidence gate was therefore exercised without fabricating progress.
  - Git workflow rehearsal covered branch creation, `git status`, exact-file diff, specific-file staging and cached-diff inspection. This Phase 10 closeout PR supplies the real PR/CI/merge portion of the workflow evidence rather than creating a meaningless rehearsal PR.
  - Offline navigation and local learning material were verified without depending on GitHub/web access.
  - Practical feedback: target paths, project discovery, menu/runtime behaviour and mentor session flow were usable on the ThinkPad; no Phase 10 blocker was observed.
  - Phase 10 accepted on 2026-09-23.

- [x] **Phase 11 — Dell handover authority V2**
  - Final Dell software/account/workstation authority added at `docs/admin/DELL-WORKSTATION-V2.md`.
  - Dell setup, Ubuntu runbook, next-build handover, recovery guide, hardware baseline and acceptance checklist updated to the accepted three-repository topology.
  - Final workspace path is `/home/connor/Projects/Connor/` with independent Mission Control, Python Basics and Snake repositories.
  - Antigravity remains the intended primary mentor; Copilot is not part of the baseline.
  - Connor-user VS Code baseline includes neutral Python terminal behaviour, uv preference and telemetry disabled.
  - Curated extension baseline is Antigravity + Python/Pylance/Python Environments/Python Debugger + Ruff.
  - `scripts/setup-connor-user.sh` now configures the final topology/tooling/user-settings model without creating accounts, credentials or GitHub ownership.
  - `scripts/show-my-computer.sh` now uses the final Mission Control path.
  - GitHub/VS Code identity and credential separation are explicitly deferred to Phase 12 and final Dell acceptance.
  - No Dell lifecycle work was executed; physical Dell authority remains with `gk-home-lab`.
  - Phase 11 implementation complete on bounded branch `docs/phase11-dell-handover-v2`; merge requires normal CI/PR acceptance.

- [ ] **Phase 12 — GitHub ownership handover**
  - Only after the system is accepted.
  - Deliberately transfer appropriate repositories to Connor.
  - Preserve history and remotes.
  - Revalidate workspace/CI/access.

- [ ] **Phase 13 — Dell deployment**
  - Only after separate explicit Dell release.
  - Physical lifecycle remains governed by `gk-home-lab`.
  - Complete fresh-machine acceptance.

---

## 22. Acceptance standard before handover

Do not call V2 ready until evidence demonstrates, as applicable:

- fresh clone works;
- Mission Control navigation works;
- workspace opens correctly;
- Markdown opens visually as intended;
- terminal experience works;
- Antigravity loads current rules;
- Antigravity discovers skills/workflows;
- `/start` or its verified equivalent reads current learner state;
- finish-session workflow updates the correct tracker;
- tracker updates are evidence-based;
- governance files are not silently altered by routine mentor operation;
- Python tooling works;
- historical Snake works where retained;
- browser showcases work;
- multi-repository Git operates correctly;
- diffs are reviewable;
- CI passes;
- ordinary coding needs no admin privileges;
- agent safety boundaries are effective;
- no secrets are tracked;
- offline learning content remains usable;
- one complete session can be performed without Geza acting as the primary teacher.

---

## 23. Definition of Done for the whole V2 programme

V2 is complete only when:

1. Mission Control is implemented and understandable.
2. Antigravity is configured as a reliable primary mentor.
3. The master tracker functions as canonical learner state.
4. AI-native development is a first-class learning track.
5. Programming, debugging, Git, Linux, testing, games, web and engineering progression exist.
6. Serious projects have clean repository boundaries.
7. Existing meaningful history is preserved.
8. VS Code/Antigravity presents a coherent visual cockpit.
9. Safety and governance are enforced without unnecessary bureaucracy.
10. Fresh-clone and ThinkPad rehearsal pass.
11. Dell handover documentation matches the final design.
12. GitHub ownership is transferred only after acceptance.
13. Dell deployment occurs only after explicit external release.

---

## 24. Next-session restart instruction

Every implementation session must begin with:

1. fetch CURRENT GitHub `main`;
2. verify the pre-V2 backup branch still points to `07871cbf2e96e919b63437a5c91bec8e86a2ffea`;
3. read this entire document;
4. inspect changes made since the previous phase;
5. continue the **first incomplete phase** in the tracker above on its bounded branch;
6. do not skip behavioural acceptance requirements merely because static implementation exists;
7. do not split `python-basics` or `snake-game` before their dedicated migration phase;
8. do not touch the Dell without separate `gk-home-lab` release authority.

Continue from the phase tracker in this file rather than reconstructing or redesigning the programme from chat history.

---

## 25. Final principle

Connor should leave each meaningful session with increased capability, not merely more generated code.

Antigravity is expected to do substantial implementation work, but its teaching responsibility is to help Connor become increasingly capable of specifying, directing, understanding, verifying and improving real software.
