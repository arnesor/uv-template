# Python UV Project Template

A modern [Cookiecutter] and [Cruft] template for Python projects, optimized strictly for [uv] dependency management and builds.

This template is simplified from Statistics Norway's PyPI template by removing Poetry, Nox, and Sphinx/MyST documentation generation. It runs all testing, linting, formatting, and type checks directly via standard GitHub Actions.

## Features

- **Dependency Management & Packaging**: Pinned to [uv] and building via `uv_build` backend.
- **Continuous Integration**: Direct `uv run` invocations in GitHub Actions for tests, typeguard, mypy, pre-commit, and xdoctest.
- **Code Quality**: Linting and formatting with [ruff] and [pre-commit].
- **Static Analysis**: Type checking with [mypy].
- **Testing**: Unit testing with [pytest] and code coverage reporting integrated with [SonarCloud] (XML coverage report).
- **Automated Releases**: Publish package to PyPI/TestPyPI with [Release Drafter].
- **Automated Dependency Updates**: Monthly [Dependabot] checks targeting `uv.lock`.

## Prerequisites

- [uv] (Astral's python packaging tool) installed locally.
- [cruft] or [cookiecutter] installed locally.

## Usage

To create a new project using this template:

```console
cruft create https://github.com/your-github-org-or-username/uv-template.git
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
