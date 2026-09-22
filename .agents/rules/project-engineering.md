# Project Engineering Rule

Use current repository authority, not stale chat assumptions.

## Before implementation

- inspect relevant files and current Git state;
- identify the actual toolchain;
- state assumptions;
- prefer the smallest safe coherent diff;
- preserve existing behaviour unless the requirement changes it.

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
