# Antigravity V2 Implementation Record

**Phase:** 2 — Antigravity mentor system  
**Branch:** `agent/antigravity-mentor-v1`  
**Verification date:** 2026-09-22

## Official convention check

Current Google Antigravity documentation was checked before implementation.

Observed current conventions:

- workspace rules: `.agents/rules/`;
- workspace Agent Skills: `.agents/skills/<skill-name>/SKILL.md`;
- each skill requires a useful `description` in YAML frontmatter;
- skills are available by autonomous discovery and slash command;
- legacy `.agents/workflows/*.md` are deprecated;
- Google states legacy workflows retire on 2026-11-01.

Official references:

- https://www.antigravity.google/docs/rules-workflows/
- https://www.antigravity.google/docs/skills
- https://antigravity.google/docs/migration/workflows-to-skills

## Implementation decision

The approved V2 learner commands are preserved:

`/start /mission /build /debug /review /finish /new-project /maintenance`

They are implemented as Agent Skills instead of legacy workflow files.

This is an implementation-format change, not a learning-model change.

## Persistent rules

- `core-mentor.md`
- `learning-model.md`
- `safety.md`
- `git-and-change-control.md`
- `project-engineering.md`
- `system-maintenance.md`

## Focused task skills

- `start-session`
- `teach-concept`
- `prompt-coach`
- `plan-feature`
- `build-feature`
- `debug-with-connor`
- `test-and-verify`
- `review-diff`
- `update-master-tracker`
- `create-project`
- `safe-maintenance`

## Learner command skills

- `start`
- `mission`
- `build`
- `debug`
- `review`
- `finish`
- `new-project`
- `maintenance`

## Evidence and validation behaviour

The mentor system must not collapse all checks into "works".

It must distinguish static inspection, automated checks, runtime validation, interactive or GUI validation, physical hardware validation and unverified behaviour.

The `update-master-tracker` skill is intentionally gated. If `progress/CONNOR-MASTER-TRACKER.md` does not exist, the skill must stop rather than invent learner state.

## Governance self-modification boundary

The mentor may not silently weaken its own governance.

Changes to root `GEMINI.md`, `.agents/rules/` or the canonical V2 implementation authority require deliberate Git review.

## Manual acceptance checks before Phase 2 completion

On a fresh clone or check-out of this branch with the target current Antigravity surface:

1. open the Antigravity Customizations/Rules view and confirm all six workspace rules are discovered;
2. verify the intended activation behaviour: core mentor, learning, safety, Git/change-control, project-engineering and system-maintenance governance must be continuously enforced (use **Always On** where the target Antigravity surface requires an explicit activation mode);
3. confirm all 19 skills are discovered;
4. confirm root `GEMINI.md` is respected on the chosen target surface, or treat `.agents/rules/` as the enforceable workspace authority if that surface does not consume root project context;
5. invoke `/start` and verify it does not invent a tracker;
6. invoke `/mission` and verify it proposes one bounded visible mission;
7. invoke `/build` with a harmless test request and verify it states goal, files, concept and acceptance checks before editing;
8. invoke `/debug` and verify it follows reproduce, observe, hypothesise, isolate, fix, rerun, verify;
9. invoke `/maintenance` with a hypothetical system-package request and verify it stops at the admin boundary;
10. inspect the resulting Git diff and ensure the mentor does not silently change governance files.

Phase 2 must not be marked complete until these behavioural checks are run in a real Antigravity environment.
