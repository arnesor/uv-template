# Standalone Scripts

Place portable, single-file scripts with [PEP 723] inline dependency metadata here.
These scripts should not import `{{cookiecutter.package_name}}`,
because they must continue to work when copied outside this repository.

Run a standalone script with:

```console
uv run standalone/example.py
```

Add a dependency to a script with:

```console
uv add --script standalone/example.py httpx
```

[pep 723]: https://peps.python.org/pep-0723/
