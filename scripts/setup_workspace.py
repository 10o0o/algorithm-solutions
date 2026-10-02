#!/usr/bin/env python3
"""Generate portable VS Code workspaces for Competitive Programming Helper."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


PLATFORMS = ("atcoder", "codeforces", "cses")
PLATFORM_NAMES = {
    "atcoder": "AtCoder (CPH target)",
    "codeforces": "Codeforces (CPH target)",
    "cses": "CSES (CPH target)",
}
EXTENSION_RECOMMENDATIONS = [
    "divyanshuagrawal.competitive-programming-helper",
    "leetcode.vscode-leetcode",
    "ms-python.python",
]


class SetupError(Exception):
    """A configuration problem that must not modify generated files."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate local CPH workspaces for this checkout."
    )
    parser.add_argument(
        "--python",
        default=sys.executable,
        metavar="EXECUTABLE",
        help="Python executable used by VS Code and CPH (default: this Python)",
    )
    parser.add_argument(
        "--platform",
        choices=PLATFORMS,
        help="generate only one platform workspace (default: all platforms)",
    )
    parser.add_argument(
        "--template",
        choices=("single", "multi"),
        default="single",
        help="submission template (default: single)",
    )
    return parser.parse_args()


def absolute_executable(value: str) -> Path:
    expanded = os.path.expanduser(value)
    if os.path.isabs(expanded) or os.sep in expanded:
        return Path(os.path.abspath(expanded))

    located = shutil.which(expanded)
    if located is None:
        raise SetupError(f"Python executable was not found: {value}")
    return Path(os.path.abspath(located))


def validate_python(value: str) -> Path:
    executable = absolute_executable(value)
    if not executable.is_file() or not os.access(executable, os.X_OK):
        raise SetupError(f"Python executable is not an executable file: {executable}")

    try:
        version_result = subprocess.run(
            [str(executable), "--version"],
            text=True,
            capture_output=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise SetupError(f"Could not run Python executable: {executable}: {error}") from error

    version_output = (version_result.stdout + version_result.stderr).strip()
    # PyPy includes build details and a second implementation/version line.
    match = re.match(r"Python (\d+)\.(\d+)(?=[.\s]|$)", version_output)
    if version_result.returncode != 0 or match is None:
        raise SetupError(f"Executable did not report a Python version: {executable}")

    version = (int(match.group(1)), int(match.group(2)))
    if version < (3, 10):
        raise SetupError(
            f"Python 3.10 or newer is required; {executable} reports {version_output}"
        )

    try:
        identity_result = subprocess.run(
            [
                str(executable),
                "-c",
                "import sys; print(f'CPH_PYTHON:{sys.version_info.major}:{sys.version_info.minor}')",
            ],
            text=True,
            capture_output=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise SetupError(f"Could not verify Python executable: {executable}: {error}") from error

    expected_identity = f"CPH_PYTHON:{version[0]}:{version[1]}"
    if identity_result.returncode != 0 or identity_result.stdout.strip() != expected_identity:
        raise SetupError(f"Executable failed the Python runtime check: {executable}")

    # Do not resolve symlinks: a .venv/bin/python path is part of the selected
    # environment's identity even when it ultimately points to another binary.
    return executable


def validate_inputs(
    root: Path, platforms: tuple[str, ...], template_name: str, python_value: str
) -> tuple[Path, Path]:
    template_filename = "python.py" if template_name == "single" else "python-multi.py"
    template = root / "templates" / template_filename
    if not template.is_file():
        raise SetupError(f"Template file does not exist: {template}")
    if not os.access(template, os.R_OK):
        raise SetupError(f"Template file is not readable: {template}")

    for platform in platforms:
        platform_directory = root / platform
        if not platform_directory.is_dir():
            raise SetupError(f"Platform directory does not exist: {platform_directory}")

    return validate_python(python_value), template


def workspace_document(platform: str, executable: Path, template: Path) -> dict[str, object]:
    executable_text = str(executable)
    return {
        "folders": [
            {"name": PLATFORM_NAMES[platform], "path": f"../{platform}"},
            {"name": "algorithm-solutions", "path": ".."},
        ],
        "settings": {
            "editor.codeLens": True,
            "python.defaultInterpreterPath": executable_text,
            "cph.general.defaultLanguage": "python",
            "cph.general.menuChoices": "python",
            "cph.language.python.Command": executable_text,
            "cph.general.timeOut": 5000,
            "cph.general.saveLocation": "",
            "cph.general.defaultLanguageTemplateFileLocation": str(template),
            "cph.general.doTemplateFileVariableReplacement": True,
            "cph.general.useShortCodeForcesName": True,
            "cph.general.useShortAtCoderName": True,
            "cph.general.autoShowJudge": True,
            "cph.companion.enableServer": True,
            "cph.general.showLiveUserCount": False,
        },
        "extensions": {"recommendations": EXTENSION_RECOMMENDATIONS},
    }


def encoded_workspace(platform: str, executable: Path, template: Path) -> bytes:
    document = workspace_document(platform, executable, template)
    return (json.dumps(document, indent=4, ensure_ascii=False) + "\n").encode("utf-8")


def replace_if_changed(destination: Path, content: bytes) -> bool:
    try:
        if destination.read_bytes() == content:
            return False
    except FileNotFoundError:
        pass

    descriptor, temporary_name = tempfile.mkstemp(
        dir=destination.parent,
        prefix=f".{destination.name}.",
        suffix=".tmp",
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as temporary_file:
            temporary_file.write(content)
            temporary_file.flush()
            os.fsync(temporary_file.fileno())
        temporary_path.chmod(0o644)
        os.replace(temporary_path, destination)
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise
    return True


def main() -> int:
    arguments = parse_args()
    root = Path(__file__).absolute().parent.parent
    platforms = (arguments.platform,) if arguments.platform else PLATFORMS

    try:
        executable, template = validate_inputs(
            root, platforms, arguments.template, arguments.python
        )
        generated = {
            platform: encoded_workspace(platform, executable, template)
            for platform in platforms
        }
    except SetupError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    output_directory = root / ".local"
    output_directory.mkdir(exist_ok=True)
    for platform, content in generated.items():
        destination = output_directory / f"{platform}.code-workspace"
        changed = replace_if_changed(destination, content)
        action = "updated" if changed else "unchanged"
        print(f"{action}: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
