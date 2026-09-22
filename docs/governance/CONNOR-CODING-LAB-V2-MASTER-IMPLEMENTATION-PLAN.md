# Connor Coding Lab V2 — Approved Master Implementation Plan

**Status:** IMPLEMENTATION IN PROGRESS — PHASE 2 CANDIDATE  
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
|   |-- agents.md
|   |-- rules/
|   |   |-- core-mentor.md
|   |   |-- learning-model.md
|   |   |-- safety.md
|   |   |-- git-and-change-control.md
|   |   |-- project-engineering.md
|   |   `-- system-maintenance.md
|   |-- skills/
|   |   |-- start-session/SKILL.md
|   |   |-- teach-concept/SKILL.md
|   |   |-- prompt-coach/SKILL.md
|   |   |-- plan-feature/SKILL.md
|   |   |-- build-feature/SKILL.md
|   |   |-- debug-with-connor/SKILL.md
|   |   |-- test-and-verify/SKILL.md
|   |   |-- review-diff/SKILL.md
|   |   |-- update-master-tracker/SKILL.md
|   |   |-- create-project/SKILL.md
|   |   `-- safe-maintenance/SKILL.md
|   `-- workflows/
|       |-- start.md
|       |-- mission.md
|       |-- build.md
|       |-- debug.md
|       |-- review.md
|       |-- finish.md
|       |-- new-project.md
|       `-- maintenance.md
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

- [ ] **Phase 2 — Antigravity mentor system**
  - Branch: `agent/antigravity-mentor-v1`
  - Re-verify current Antigravity project instruction/rules/skills format against official documentation.
  - Implement persistent mentor rules under `.agents/rules/`.
  - Implement focused task skills under `.agents/skills/`.
  - Implement the approved learner slash-command experience as skills, not deprecated workflow files.
  - Implement evidence/validation behaviour.
  - Implement governance self-modification boundary.
  - Validate discovery and behaviour in a real Antigravity session before marking Phase 2 complete.

- [ ] **Phase 3 — Master tracker**
  - Branch: `learning/master-tracker-v1`
  - Implement `CONNOR-MASTER-TRACKER.md`.
  - Seed only source-supported current capabilities.
  - Implement Antigravity update protocol.
  - Validate distinction between AI-produced output and Connor-demonstrated competence.

- [ ] **Phase 4 — VS Code / cockpit UX**
  - Branch: `ux/vscode-mission-control-v1`
  - Multi-root workspace design.
  - Markdown preview-first behaviour.
  - Integrated terminal behaviour.
  - Curated extension recommendations.
  - Safe startup tasks.
  - Visual mission navigation.

- [ ] **Phase 5 — AI-native curriculum**
  - Branch: `learning/ai-native-curriculum-v1`
  - Build the multi-track curriculum.
  - Create missions and practice.
  - Introduce AI collaboration engineering from the start.
  - Preserve project-based, visible outcomes.
  - Avoid unnecessary repetitive manual coding.

- [ ] **Phase 6 — Lab control tooling**
  - Branch: `tooling/lab-control-v2`
  - Replace/evolve launcher safely.
  - Add status/doctor/project/run/help capabilities.
  - Preserve transparency of underlying tools.

- [ ] **Phase 7 — Safety, governance and CI**
  - Branch: `governance/safety-ci-v1`
  - Add minimal useful CI.
  - Finalise Git/change-control documentation.
  - Add security/dependency/internet/AI boundaries.
  - Configure branch protection if supported and appropriate.

- [ ] **Phase 8 — Historical project repository extraction**
  - Separate migration transaction.
  - Extract `python-basics` history.
  - Extract `snake-game` history.
  - Validate histories.
  - Create independent WebshopCompany repositories if required.
  - Only then remove live project copies from Mission Control working tree.

- [ ] **Phase 9 — Multi-repository workspace integration**
  - Wire Mission Control and independent projects into one workspace/Antigravity project.
  - Validate Git independence and navigation.

- [ ] **Phase 10 — ThinkPad rehearsal**
  - Fresh clone(s).
  - Full learner flow.
  - Antigravity session start/finish.
  - Tracker mutation.
  - Python/Pygame/browser execution.
  - Git/PR workflow.
  - Offline material.
  - Collect practical feedback.

- [ ] **Phase 11 — Dell handover authority V2**
  - Update future Dell build docs to match final architecture.
  - Do not execute Dell lifecycle work.

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

The next implementation session must begin with:

1. fetch CURRENT GitHub `main`;
2. verify the pre-V2 backup branch still points to `07871cbf2e96e919b63437a5c91bec8e86a2ffea`;
3. read this entire document;
4. inspect any changes made after this plan was approved;
5. begin **Phase 1 only** on a bounded branch from current `main`;
6. do not split `python-basics` or `snake-game`;
7. do not touch the Dell;
8. validate and review Phase 1 before moving to Phase 2.

A later session must continue from the phase tracker in this file rather than redesigning the programme from scratch.

---

## 25. Final principle

Connor should leave each meaningful session with increased capability, not merely more generated code.

Antigravity is expected to do substantial implementation work, but its teaching responsibility is to help Connor become increasingly capable of specifying, directing, understanding, verifying and improving real software.
