from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "validate_notes.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_notes", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class ValidateNotesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write(self, relative: str, text: str = "") -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def copy_validator(self) -> Path:
        destination = self.root / "scripts" / "validate_notes.py"
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SCRIPT, destination)
        return destination

    def concept(self, **overrides: str) -> str:
        values = {
            "title": "이분 탐색",
            "updated": "2026-09-20",
            "tags": "[algorithm, search]",
            "body": "# 이분 탐색\n\n## 핵심 요약\n요약\n\n## 개념 정리\n정리\n",
        }
        values.update(overrides)
        return (
            "---\n"
            f"title: {values['title']}\n"
            f"updated: {values['updated']}\n"
            f"tags: {values['tags']}\n"
            "---\n\n"
            f"{values['body']}"
        )

    def problem(self, solution: str = "solution.py", url: str = "https://example.com/problems/1") -> str:
        return (
            "---\n"
            "title: 문제 1\n"
            "updated: 2026-09-20\n"
            "tags: []\n"
            f"url: {url}\n"
            f"solution: {solution}\n"
            "---\n\n"
            "# 문제 1\n\n자유 형식 풀이 기록\n"
        )

    def errors(self, relative: str, text: str) -> list[str]:
        path = self.write(relative, text)
        return load_validator().validate_file(path, self.root)

    def test_valid_concept_accepts_empty_tag_list_and_required_headings(self) -> None:
        errors = self.errors("knowledge/algorithms/binary-search.md", self.concept(tags="[]"))
        self.assertEqual([], errors)

    def test_reports_missing_field_bad_date_and_non_list_tags_with_lines(self) -> None:
        note = "---\ntitle: Test\nupdated: 2026-02-30\ntags: algorithms\n---\n"
        errors = self.errors("knowledge/test.md", note)
        self.assertTrue(any(":3:" in error and "YYYY-MM-DD" in error for error in errors))
        self.assertTrue(any(":4:" in error and "tags" in error for error in errors))

        missing = self.errors("knowledge/missing.md", "---\ntitle: Test\ntags: []\n---\n")
        self.assertTrue(any(":1:" in error and "updated" in error for error in missing))

    def test_concept_requires_matching_h1_and_two_sections(self) -> None:
        body = "# 다른 제목\n\n## 핵심 요약\n요약\n"
        errors = self.errors("knowledge/test.md", self.concept(body=body))
        self.assertTrue(any("top-level heading" in error for error in errors))
        self.assertTrue(any("개념 정리" in error for error in errors))

    def test_platform_note_requires_https_url_and_existing_python_solution(self) -> None:
        errors = self.errors("leetcode/easy/problem.md", self.problem(solution="missing.py", url="http://example.com/1"))
        self.assertTrue(any("url" in error and "https" in error for error in errors))
        self.assertTrue(any("solution" in error and "does not exist" in error for error in errors))

        self.write("leetcode/easy/solution.txt", "placeholder")
        extension = self.errors("leetcode/easy/wrong-extension.md", self.problem(solution="solution.txt"))
        self.assertTrue(any("solution" in error and ".py" in error for error in extension))

    def test_malformed_https_url_is_an_actionable_error_not_a_traceback(self) -> None:
        self.write("codeforces/solution.py", "print(0)\n")
        errors = self.errors(
            "codeforces/problem.md",
            self.problem(solution="solution.py", url='"https://[broken"'),
        )
        self.assertTrue(any(":5:" in error and "url" in error for error in errors))

    def test_platform_note_accepts_relative_existing_python_solution(self) -> None:
        self.write("atcoder/abc001/a.py", "print(0)\n")
        errors = self.errors("atcoder/abc001/a.md", self.problem(solution="a.py"))
        self.assertEqual([], errors)

    def test_problem_solution_must_be_a_real_platform_python_file(self) -> None:
        self.write("knowledge/helper.py", "print(0)\n")
        outside_platform = self.errors(
            "leetcode/easy/outside-platform.md",
            self.problem(solution="../../knowledge/helper.py"),
        )
        self.assertTrue(any("platform directory" in error for error in outside_platform))

        self.write("leetcode/easy/real.py", "print(0)\n")
        (self.root / "leetcode/easy/linked.py").symlink_to(self.root / "leetcode/easy/real.py")
        symlink = self.errors(
            "leetcode/easy/symlink.md", self.problem(solution="linked.py")
        )
        self.assertTrue(any("symlink" in error for error in symlink))

    def test_contest_requires_https_url_but_not_solution(self) -> None:
        note = "---\ntitle: ABC 001\nupdated: 2026-09-20\ntags: [contest]\n---\n\n# ABC 001\n"
        errors = self.errors("contests/atcoder/abc001.md", note)
        self.assertTrue(any("missing frontmatter field: url" in error for error in errors))
        self.assertFalse(any("solution" in error for error in errors))

    def test_checks_inline_image_reference_and_percent_encoded_local_links(self) -> None:
        self.write("knowledge/assets/has space.png", "image")
        body = (
            "# 링크\n\n## 핵심 요약\n"
            "[있는 파일](../assets/has%20space.png)\n"
            "![없는 그림](../assets/missing.png)\n"
            "[없는 참조][missing-ref]\n\n"
            "[missing-ref]: ../missing.md\n\n"
            "## 개념 정리\n정리\n"
        )
        errors = self.errors("knowledge/topic/links.md", self.concept(title="링크", body=body))
        self.assertEqual(2, sum("does not exist" in error for error in errors))
        self.assertTrue(all(":11:" in error or ":14:" in error for error in errors if "does not exist" in error))

    def test_ignores_links_inside_inline_and_fenced_code(self) -> None:
        body = (
            "# 코드\n\n## 핵심 요약\n"
            "`[예시](missing-inline.md)`\n\n"
            "```markdown\n[예시](missing-fence.md)\n```\n\n"
            "## 개념 정리\n정리\n"
        )
        errors = self.errors("knowledge/topic/code.md", self.concept(title="코드", body=body))
        self.assertEqual([], errors)

    def test_rejects_raw_html_but_allows_html_shown_as_code(self) -> None:
        body = (
            "# HTML\n\n## 핵심 요약\n"
            "문장 안의 <span>인라인 HTML</span>\n\n"
            "<div>블록</div>\n\n"
            "`<span>인라인 코드</span>`\n\n"
            "```html\n<section>펜스 코드</section>\n```\n\n"
            "## 개념 정리\n정리\n"
        )
        errors = self.errors("knowledge/topic/html.md", self.concept(title="HTML", body=body))
        self.assertEqual(2, sum("raw HTML" in error for error in errors))

    def test_rejects_links_outside_repository_and_ignored_private_paths(self) -> None:
        self.write(".local/secret.md", "secret")
        self.write(".venv/lib/note.md", "secret")
        body = (
            "# 경계\n\n## 핵심 요약\n"
            "[외부](../../../outside.md) [로컬](../../.local/secret.md) "
            "[가상환경](../../.venv/lib/note.md)\n\n"
            "## 개념 정리\n정리\n"
        )
        errors = self.errors("knowledge/topic/boundary.md", self.concept(title="경계", body=body))
        self.assertTrue(any("outside repository" in error for error in errors))
        self.assertEqual(2, sum("prohibited" in error for error in errors))

    def test_rejects_root_scratch_git_and_symlink_link_targets(self) -> None:
        self.write("main.py", "print(0)\n")
        self.write("ex.in", "sample\n")
        self.write(".git/description", "private\n")
        self.write("knowledge/assets/real.txt", "public\n")
        (self.root / "knowledge/assets/linked.txt").symlink_to(
            self.root / "knowledge/assets/real.txt"
        )
        body = (
            "# 경계\n\n## 핵심 요약\n"
            "[작업 코드](../../main.py) [입력](../../ex.in) "
            "[Git](../../.git/description) [링크](../assets/linked.txt)\n\n"
            "## 개념 정리\n정리\n"
        )
        errors = self.errors("knowledge/topic/boundary.md", self.concept(title="경계", body=body))
        self.assertEqual(3, sum("prohibited" in error for error in errors))
        self.assertEqual(1, sum("symlink" in error for error in errors))

    def test_rejects_public_note_that_traverses_an_internal_symlink(self) -> None:
        real_note = self.write("knowledge/real.md", self.concept())
        linked_note = self.root / "knowledge/linked.md"
        linked_note.symlink_to(real_note)
        errors = load_validator().validate_file(linked_note, self.root)
        self.assertTrue(any("symlink" in error for error in errors))

    def test_explicit_outside_and_prohibited_paths_fail_before_content_validation(self) -> None:
        script = self.copy_validator()
        prohibited = self.write(".local/invalid.md", "not frontmatter")
        with tempfile.TemporaryDirectory() as outside:
            outside_note = Path(outside) / "invalid.md"
            outside_note.write_text("not frontmatter", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(script), str(outside_note), str(prohibited)],
                cwd=self.root,
                text=True,
                capture_output=True,
                check=False,
            )
        self.assertEqual(1, result.returncode)
        self.assertIn("outside repository", result.stderr)
        self.assertIn("prohibited", result.stderr)
        self.assertNotIn("frontmatter", result.stderr)

    def test_default_mode_with_empty_collections_succeeds_as_zero_notes(self) -> None:
        script = self.copy_validator()
        with tempfile.TemporaryDirectory() as external_cwd:
            result = subprocess.run(
                [sys.executable, str(script)],
                cwd=external_cwd,
                text=True,
                capture_output=True,
                check=False,
            )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("0 note", result.stdout)
        self.assertNotIn("complete", result.stdout.lower())
        self.assertNotIn("학습 완료", result.stdout)

    def test_default_mode_uses_script_repo_root_when_run_elsewhere(self) -> None:
        script = self.copy_validator()
        self.write(
            "leetcode/problem.md",
            "---\ntitle: Problem\nupdated: 2026-09-20\ntags: []\n---\n",
        )
        with tempfile.TemporaryDirectory() as external_cwd:
            result = subprocess.run(
                [sys.executable, str(script)],
                cwd=external_cwd,
                text=True,
                capture_output=True,
                check=False,
            )
        self.assertEqual(1, result.returncode)
        self.assertIn("missing frontmatter field: url", result.stderr)
        self.assertIn("missing frontmatter field: solution", result.stderr)

    def test_default_discovery_rejects_external_symlink_and_skips_private_notes(self) -> None:
        script = self.copy_validator()
        self.write("knowledge/private/ignored.md", "invalid")
        self.write("knowledge/.venv-pypy/ignored.md", "invalid")
        with tempfile.TemporaryDirectory() as outside:
            outside_note = Path(outside) / "outside.md"
            outside_note.write_text("invalid", encoding="utf-8")
            symlink = self.root / "knowledge" / "external.md"
            symlink.symlink_to(outside_note)
            result = subprocess.run(
                [sys.executable, str(script)],
                cwd=self.root,
                text=True,
                capture_output=True,
                check=False,
            )
        self.assertEqual(1, result.returncode)
        self.assertIn("outside repository", result.stderr)
        self.assertNotIn("knowledge/private/ignored.md", result.stderr)
        self.assertNotIn("knowledge/.venv-pypy/ignored.md", result.stderr)


if __name__ == "__main__":
    unittest.main()
