# Project-Local Scripts

Place scripts that use this project's dependencies or import `{{cookiecutter.package_name}}` here.
Keep reusable logic under `src/{{cookiecutter.package_name}}` and make scripts thin entry points.

Run a script from the project root:

```console
uv run scripts/example.py
```

Import the installed package name, not `src`:

```python
from {{cookiecutter.package_name}} import functions
```
