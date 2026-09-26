# Repository Guide

## Template Boundaries

- This repository is a Cookiecutter source, not an installable Python project. Generated-project files live under `{{cookiecutter.project_name}}/`; template inputs are in `cookiecutter.json`, and `hooks/post_gen_project.py` normalizes generated metadata to UTF-8 and two-space JSON.
- Preserve Jinja escaping in generated GitHub Actions expressions, for example `${{"{{"}} matrix.python {{"}}"}}`. An unescaped `${{ ... }}` is evaluated by Cookiecutter instead of GitHub Actions.
- License files use Jinja in their filenames and are emitted conditionally. `code_quality_level` also changes Ruff's selected rules and the coverage threshold in `pyproject.toml`; render affected choices when editing these branches.
- `script_support` controls whether `scripts/`, `standalone/`, both, or neither survive `hooks/post_gen_project.py`; both source directories intentionally remain in the template.
- A separate release workflow updates the Release Drafter draft after successful pushes to `main` or `master`, and publishes it only when `project.version` changes. It verifies the tested commit is still the branch head and does not build or publish distribution artifacts.
- The console-script name uses `project_name`, while imports and the `src/` directory use `package_name` (hyphens become underscores by default).

## Verification

- Root pre-commit excludes `{{cookiecutter.project_name}}/`, so a clean root run does not validate the generated project.
- On Windows PowerShell only, run `$env:PYTHONUTF8=1` before `cruft create` or `cookiecutter` creates a project from this template.
- Render a smoke project from the repository root with `uvx cookiecutter --no-input . project_name=agent-smoke --output-dir <outside-repo-dir>`. If rendering inside this worktree, run `git init` in the generated project before pre-commit; otherwise it discovers the parent Git root and checks the unrendered Jinja sources.
- `hooks/post_gen_project.py` runs `uv lock`, so a successful render includes the lockfile required by generated CI's `uv sync --locked`.
- Render all `script_support` choices when changing their Jinja branches or post-generation pruning.
- Match generated CI with: `uv run pre-commit run --all-files --hook-stage=manual --show-diff-on-failure`, `uv run mypy src tests`, `uv run deptry .`, `uv run coverage run --parallel-mode -m pytest`, `uv run coverage combine`, and `uv run python -m xdoctest --modname=<package_name> --command=all --colored=1`.
- For a focused test, run `uv run pytest tests/test_functions.py -q` (replace the path as needed).

## Toolchain Details

- Generated projects require Python 3.12+, default locally to 3.13 via `.python-version`, and CI tests 3.12-3.14 plus Linux/macOS/Windows combinations defined in the generated workflow.
- The CI uv version is pinned separately in `{{cookiecutter.project_name}}/.github/workflows/constraints.txt`; keep it aligned with workflow/setup changes.
- Generated pre-commit hooks use `language: system`; dependencies must therefore be installed in the active uv environment before running them.
