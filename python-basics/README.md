# Python Basics

This is Connor's small Python learning project.

Keep examples understandable and focused. Do not turn this directory into a large application.

## Set up

From the repository root:

    cd python-basics
    uv sync

The project currently follows its checked-in Python requirement. A later Python 3.12 migration must update and validate the project deliberately.

## Run the interactive exercise

    uv run python src/python_basics/hello.py

## Run the package entry point

    uv run python-basics

## Check the code

    uv run ruff check .

## Run the tests

    uv run pytest

The first test is intentionally small so Connor can see what an automated check looks like before writing more complicated tests.

## Learning rule

When adding an exercise:

1. predict what it should do;
2. run it;
3. change one thing;
4. inspect `git diff`;
5. explain the result.
