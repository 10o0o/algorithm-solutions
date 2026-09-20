import json
import os
from pathlib import Path
import shutil
import shlex
import subprocess
import sys
import tempfile
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class SetupWorkspaceTests(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary_directory = tempfile.TemporaryDirectory()
        self.checkout = Path(self._temporary_directory.name) / "checkout with spaces"
        (self.checkout / "scripts").mkdir(parents=True)
        (self.checkout / "templates").mkdir()
        (self.checkout / "atcoder").mkdir()
        (self.checkout / "codeforces").mkdir()
        shutil.copy2(
            PROJECT_ROOT / "scripts" / "setup_workspace.py",
            self.checkout / "scripts" / "setup_workspace.py",
        )
        shutil.copy2(
            PROJECT_ROOT / "templates" / "python.py",
            self.checkout / "templates" / "python.py",
        )
        multi_template = PROJECT_ROOT / "templates" / "python-multi.py"
        if multi_template.exists():
            shutil.copy2(
                multi_template,
                self.checkout / "templates" / "python-multi.py",
            )

    def tearDown(self) -> None:
        self._temporary_directory.cleanup()

    def run_setup(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(self.checkout / "scripts" / "setup_workspace.py"), *arguments],
            cwd=self.checkout.parent,
            text=True,
            capture_output=True,
            check=False,
        )

    def read_workspace(self, platform: str) -> dict[str, object]:
        workspace = self.checkout / ".local" / f"{platform}.code-workspace"
        return json.loads(workspace.read_text(encoding="utf-8"))

    def test_default_generates_both_portable_workspaces(self) -> None:
        result = self.run_setup()

        self.assertEqual(result.returncode, 0, result.stderr)
        expected_settings = {
            "editor.codeLens": True,
            "python.defaultInterpreterPath": os.path.abspath(sys.executable),
            "cph.general.defaultLanguage": "python",
            "cph.general.menuChoices": "python",
            "cph.language.python.Command": os.path.abspath(sys.executable),
            "cph.general.timeOut": 5000,
            "cph.general.saveLocation": "",
            "cph.general.defaultLanguageTemplateFileLocation": str(
                self.checkout / "templates" / "python.py"
            ),
            "cph.general.doTemplateFileVariableReplacement": True,
            "cph.general.useShortCodeForcesName": True,
            "cph.general.useShortAtCoderName": True,
            "cph.general.autoShowJudge": True,
            "cph.companion.enableServer": True,
            "cph.general.showLiveUserCount": False,
        }
        for platform, display_name in (
            ("atcoder", "AtCoder (CPH target)"),
            ("codeforces", "Codeforces (CPH target)"),
        ):
            workspace = self.read_workspace(platform)
            self.assertEqual(
                workspace["folders"],
                [
                    {"name": display_name, "path": f"../{platform}"},
                    {"name": "algorithm-solutions", "path": ".."},
                ],
            )
            self.assertEqual(workspace["settings"], expected_settings)
            self.assertEqual(
                workspace["extensions"]["recommendations"],
                [
                    "divyanshuagrawal.competitive-programming-helper",
                    "leetcode.vscode-leetcode",
                    "ms-python.python",
                ],
            )

    def test_platform_subset_and_multi_template(self) -> None:
        result = self.run_setup("--platform", "atcoder", "--template", "multi")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.checkout / ".local" / "atcoder.code-workspace").is_file())
        self.assertFalse((self.checkout / ".local" / "codeforces.code-workspace").exists())
        settings = self.read_workspace("atcoder")["settings"]
        self.assertEqual(
            settings["cph.general.defaultLanguageTemplateFileLocation"],
            str(self.checkout / "templates" / "python-multi.py"),
        )

    def test_repeated_generation_is_a_byte_and_metadata_no_op(self) -> None:
        first = self.run_setup()
        self.assertEqual(first.returncode, 0, first.stderr)
        workspace = self.checkout / ".local" / "atcoder.code-workspace"
        before = (workspace.read_bytes(), workspace.stat().st_ino, workspace.stat().st_mtime_ns)

        second = self.run_setup()

        self.assertEqual(second.returncode, 0, second.stderr)
        after = (workspace.read_bytes(), workspace.stat().st_ino, workspace.stat().st_mtime_ns)
        self.assertEqual(after, before)

    def test_python_symlink_with_spaces_is_kept_as_the_configured_identity(self) -> None:
        interpreter = self.checkout / ".venv with spaces" / "bin" / "python"
        interpreter.parent.mkdir(parents=True)
        interpreter.symlink_to(sys.executable)

        result = self.run_setup("--python", str(interpreter), "--platform", "codeforces")

        self.assertEqual(result.returncode, 0, result.stderr)
        settings = self.read_workspace("codeforces")["settings"]
        self.assertEqual(settings["python.defaultInterpreterPath"], str(interpreter))
        self.assertEqual(settings["cph.language.python.Command"], str(interpreter))

    def test_invalid_interpreter_preserves_existing_generated_outputs(self) -> None:
        existing = self.checkout / ".local" / "atcoder.code-workspace"
        existing.parent.mkdir()
        original = b"custom generated workspace\n"
        existing.write_bytes(original)
        invalid = self.checkout / "not-python"
        invalid.write_text("#!/bin/sh\necho definitely-not-python\n", encoding="utf-8")
        invalid.chmod(0o755)

        result = self.run_setup("--python", str(invalid))

        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(existing.read_bytes(), original)
        self.assertFalse((self.checkout / ".local" / "codeforces.code-workspace").exists())

    def test_pypy_version_banner_is_accepted(self) -> None:
        interpreter = self.checkout / "pypy"
        interpreter.write_text(
            "#!/bin/sh\n"
            'if [ "$1" = "--version" ]; then\n'
            f"  echo 'Python {sys.version_info.major}.{sys.version_info.minor}.0 (build, date)'\n"
            "  echo '[PyPy 7.3.19 with GCC 10.2.1]'\n"
            "else\n"
            f'  exec {shlex.quote(sys.executable)} "$@"\n'
            "fi\n",
            encoding="utf-8",
        )
        interpreter.chmod(0o755)
        result = self.run_setup("--python", str(interpreter))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            self.read_workspace("codeforces")["settings"]["cph.language.python.Command"],
            str(interpreter),
        )

    def test_missing_selected_template_preserves_existing_generated_outputs(self) -> None:
        existing = self.checkout / ".local" / "codeforces.code-workspace"
        existing.parent.mkdir()
        original = b"keep this workspace\n"
        existing.write_bytes(original)
        (self.checkout / "templates" / "python-multi.py").unlink(missing_ok=True)

        result = self.run_setup("--template", "multi")

        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(existing.read_bytes(), original)
        self.assertFalse((self.checkout / ".local" / "atcoder.code-workspace").exists())

    def test_existing_solutions_and_cph_data_are_byte_preserved(self) -> None:
        solution = self.checkout / "atcoder" / "answer.py"
        cph_data = self.checkout / "atcoder" / ".cph" / ".answer.py_abcd.prob"
        solution_bytes = b"print('learner solution')\n"
        cph_bytes = b"{\"tests\":[{\"input\":\"1\\n\"}]}\n"
        solution.write_bytes(solution_bytes)
        cph_data.parent.mkdir()
        cph_data.write_bytes(cph_bytes)

        result = self.run_setup()

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(solution.read_bytes(), solution_bytes)
        self.assertEqual(cph_data.read_bytes(), cph_bytes)


if __name__ == "__main__":
    unittest.main()
