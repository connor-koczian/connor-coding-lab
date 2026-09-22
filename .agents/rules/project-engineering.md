# Project Engineering Rule

Use current repository authority, not stale chat assumptions.

## Before implementation

- inspect relevant files and current Git state;
- identify the actual toolchain;
- state assumptions;
- prefer the smallest safe coherent diff;
- preserve existing behaviour unless the requirement changes it.

## Evidence grounding

Before naming a file, directory, command, executable, project entry point or current capability as fact:

- verify it against the current repository or current environment;
- do not invent plausible-looking paths, filenames or commands;
- prefer repository metadata, current source, scripts and documented commands over memory;
- if a path or command has not been verified, label it as a suggestion rather than an established fact.

Existence is not runtime validation.

Do not describe software, a feature, a command or an environment as working, passing, healthy or verified unless the relevant behaviour was actually validated in the stated current environment. If only static evidence exists, say that it is present, configured or documented instead.

## Python

Use the project's declared environment and dependency workflow.

Current target baseline is Python 3.12.

Prefer `uv` commands where the project is uv-managed:

- `uv sync`
- `uv run python ...`
- `uv run pytest`
- `uv run ruff check .`

Do not teach raw `pip` as the normal project workflow.

Do not copy `.venv` directories between machines.

## Debugging

Use:

`reproduce -> observe -> hypothesise -> isolate -> smallest reliable fix -> rerun -> verify`

Distinguish syntax, runtime, logic, state, input, rendering and environment failures.

Do not default to rewriting the whole feature.

## Verification

Report validation by type:

- static inspection;
- automated tests/checks;
- runtime validation;
- interactive GUI validation;
- physical hardware validation.

Never claim unperformed checks passed.
