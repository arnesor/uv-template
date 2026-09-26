#!/usr/bin/env python
import json
import locale
import shutil
import subprocess
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


def normalize_cookiecutter_json():
    """Sort .cookiecutter.json and indent it using two spaces."""
    path = Path(".cookiecutter.json")

    if path.exists():
        with path.open(encoding="utf-8") as io:
            data = json.load(io)

        with path.open(mode="w", encoding="utf-8") as io:
            json.dump(data, io, sort_keys=True, indent=2, ensure_ascii=False)
            io.write("\n")


def generate_uv_lock():
    """Generate the lockfile required by the generated CI workflow."""
    subprocess.run(["uv", "lock"], check=True)


def remove_unused_script_directories():
    """Remove script directories excluded by the selected template mode."""
    script_support = "{{cookiecutter.script_support}}"

    if script_support not in ("project-local", "both"):
        shutil.rmtree("scripts")
    if script_support not in ("standalone", "both"):
        shutil.rmtree("standalone")


if __name__ == "__main__":
    convert_to_utf8()
    normalize_cookiecutter_json()
    remove_unused_script_directories()
    generate_uv_lock()
