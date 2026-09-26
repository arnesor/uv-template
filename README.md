# Python UV Project Template

A modern [Cookiecutter] and [Cruft] template for Python projects, optimized strictly for [uv] dependency management and builds.

It runs all testing, linting, formatting, and type checks directly via standard GitHub Actions without Nox or Tox.

## Features

- **Dependency Management & Packaging**: Pinned to [uv] and building via `uv_build` backend.
- **Continuous Integration**: Direct `uv run` invocations in GitHub Actions for tests, mypy, pre-commit, deptry, and xdoctest.
- **Code Quality**: Linting and formatting with [ruff] and [pre-commit].
- **Static Analysis**: Type checking with [mypy].
- **Testing**: Unit testing with [pytest] and code coverage reporting integrated with [SonarCloud] (XML coverage report).
- **Automated Releases**: Publish categorized GitHub releases with [Release Drafter] when the project version changes.
- **Automated Dependency Updates**: Monthly [Dependabot] checks targeting `uv.lock`.

## Prerequisites

- [uv] (Astral's python packaging tool) installed locally.
- [cruft] or [cookiecutter] installed locally.

## Usage

To create a new project using this template:

```console
cruft create https://github.com/arnesor/uv-template.git
```

`script_support` defaults to `project-local`, with options for `none`, `standalone`, or `both` script layouts.

Generated projects create a categorized GitHub release after a version change in `pyproject.toml` reaches `main` or `master` and all CI checks pass. Releases contain GitHub's source archives only.

### Windows

If you are on Windows you need to set the PYTHONUTF8 environment variable to 1 first:

```console
$env:PYTHONUTF8=1
cruft create https://github.com/arnesor/uv-template.git
```

### Checking and Updating Template Changes

Cruft tracks template changes, allowing you to update your project easily as this template evolves:

```console
cruft check
cruft update
```

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[cruft]: https://github.com/cruft/cruft
[uv]: https://github.com/astral-sh/uv
[ruff]: https://github.com/astral-sh/ruff
[pre-commit]: https://pre-commit.com/
[mypy]: https://mypy.org/
[pytest]: https://pytest.org/
[sonarcloud]: https://sonarcloud.io
[release drafter]: https://github.com/release-drafter/release-drafter
[dependabot]: https://github.com/dependabot
