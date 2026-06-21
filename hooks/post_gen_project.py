#!/usr/bin/env python
import json
import locale
import sys
from pathlib import Path


def convert_to_utf8():
    """Ensure specific generated files are encoded in UTF-8.

    On Windows, cookiecutter may write files using the system default encoding (like cp1252)
    instead of UTF-8. This function reads specific metadata files using the default/preferred
    system encoding and rewrites them in UTF-8.
    """
    sys_encoding = locale.getpreferredencoding(False) or sys.getdefaultencoding()
    if sys_encoding.lower() in ("utf-8", "utf8"):
        return

    target_files = (".cookiecutter.json", "pyproject.toml")

    for filename in target_files:
        path = Path(filename)
        if path.is_file():
            # Check if file is already valid UTF-8 to prevent double-encoding
            try:
                path.read_text(encoding="utf-8")
                continue
            except UnicodeDecodeError:
                pass

            # If not valid UTF-8, decode with system encoding and write as UTF-8
            try:
                content = path.read_text(encoding=sys_encoding)
                path.write_text(content, encoding="utf-8")
            except Exception:
                pass


def reindent_cookiecutter_json():
    """Indent .cookiecutter.json using two spaces.

    The jsonify extension distributed with Cookiecutter uses an indentation
    width of four spaces. This conflicts with the default indentation width of
    Prettier for JSON files. Prettier is run as a pre-commit hook in CI.
    """
    path = Path(".cookiecutter.json")

    if path.exists():
        with path.open(encoding="utf-8") as io:
            data = json.load(io)

        with path.open(mode="w", encoding="utf-8") as io:
            json.dump(data, io, sort_keys=True, indent=2, ensure_ascii=False)
            io.write("\n")


if __name__ == "__main__":
    convert_to_utf8()
    reindent_cookiecutter_json()
