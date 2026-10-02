from __future__ import annotations

import hashlib
import http.client
from http.server import HTTPServer
import json
from pathlib import Path
import shutil
import socket
import time
import tempfile
import threading
import unittest
from unittest.mock import patch

from scripts import companion_router as router


class RouterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "checkout with spaces"
        for name in (*router.PLATFORMS, "templates"):
            (self.root / name).mkdir(parents=True)
        shutil.copy2(Path(__file__).resolve().parents[1] / "templates/python.py", self.root / "templates/python.py")

    def tearDown(self):
        self.temp.cleanup()

    def payload(self, url="https://cses.fi/problemset/task/1651/", name="Range Update Queries"):
        return {"name": name, "url": url, "group": "CSES - Range Queries", "interactive": False,
                "memoryLimit": 512, "timeLimit": 1000,
                "tests": [{"input": "1\n", "output": "2\n"}]}

    def test_routes_three_platforms_and_codeforces_aliases(self):
        for url, name, platform, filename in [
            ("https://atcoder.jp/contests/abc470/tasks/abc470_a", "A. Test", "atcoder", "abc470a.py"),
            ("https://codeforces.com/contest/4/problem/A", "A. Watermelon", "codeforces", "4A.py"),
            ("https://www.codeforces.com/problemset/problem/4/A", "A. Watermelon", "codeforces", "4A.py"),
            ("https://codeforces.com/gym/100001/problem/A", "A", "codeforces", "100001A.py"),
            ("https://cses.fi/problemset/task/1651/", "Range Update Queries", "cses", "Range_Update_Queries.py"),
        ]:
            with self.subTest(url=url):
                self.assertEqual(router.route(url, name)[:2], (platform, filename))
        self.assertEqual(router.route("https://codeforces.com/contest/4/problem/A", "A")[2],
                         router.route("https://codeforces.com/problemset/problem/4/A", "A")[2])

    def test_untrusted_urls_and_invalid_schemas_do_not_write(self):
        bad_urls = ["http://cses.fi/problemset/task/1651", "https://cses.fi.evil.test/problemset/task/1651",
                    "https://evilcses.fi/problemset/task/1651", "https://user@cses.fi/problemset/task/1651",
                    "https://cses.fi:444/problemset/task/1651", "https://cses.fi/problemset/task/../a",
                    "https://atcoder.jp/contests/abc/tasks/../../x", "https://codeforces.com/profile/user"]
        for url in bad_urls:
            with self.subTest(url=url), self.assertRaises(router.ImportError):
                router.validate_payload(self.payload(url))
        for key, value in [("name", "title\nprint(1)"), ("interactive", True), ("tests", [{}]),
                           ("timeLimit", True), ("memoryLimit", float("inf")), ("timeLimit", 10**400),
                           ("tests", [{}] * 101), ("group", None)]:
            with self.subTest(key=key, value=str(value)[:40]), self.assertRaises(router.ImportError):
                router.validate_payload({**self.payload(), key: value})
        self.assertEqual(list((self.root / "cses").iterdir()), [])

    def test_cph_metadata_hash_matches_node_md5_rule(self):
        fixed = router.metadata_path(Path("/tmp/check out/cses/Range_Update_Queries.py"))
        self.assertEqual(fixed.name, ".Range_Update_Queries.py_d03b3cc3f462c85a00392f11468ff18b.prob")
        source = self.root / "cses/Range_Update_Queries.py"
        expected = hashlib.md5(str(source).encode(), usedforsecurity=False).hexdigest()
        self.assertEqual(router.metadata_path(source).name, f".{source.name}_{expected}.prob")
        target, action = router.store(self.root, router.validate_payload(self.payload()))
        self.assertEqual(action, "created")
        metadata = json.loads(router.metadata_path(target).read_text())
        self.assertEqual(metadata["srcPath"], str(target))
        self.assertEqual(metadata["tests"], [{"input": "1\n", "output": "2\n", "id": 1}])
        self.assertIn("# https://cses.fi/problemset/task/1651/", target.read_text())
        self.assertNotIn("$CURSOR_PLACEHOLDER", target.read_text())
        compile(target.read_bytes(), str(target), "exec")

    def test_duplicate_preserves_code_tests_ids_and_file_metadata(self):
        problem = router.validate_payload(self.payload())
        target, _ = router.store(self.root, problem)
        target.write_text("# learner changed everything\nprint('keep')\n")
        meta = router.metadata_path(target)
        saved = json.loads(meta.read_text())
        saved["tests"].append({"input": "edge\n", "output": "keep\n", "id": 847})
        meta.write_text(json.dumps(saved))
        before = [(path.read_bytes(), path.stat().st_mtime_ns) for path in (target, meta)]
        self.assertEqual(router.store(self.root, router.validate_payload(self.payload(name="Renamed problem"))), (target, "preserved"))
        self.assertEqual(before, [(path.read_bytes(), path.stat().st_mtime_ns) for path in (target, meta)])

    def test_existing_code_without_metadata_can_receive_samples_but_is_not_overwritten(self):
        source = self.root / "cses/Range_Update_Queries.py"
        original = b"# user code\n# https://cses.fi/problemset/task/1651/\nprint('keep')\n"
        source.write_bytes(original)
        router.store(self.root, router.validate_payload(self.payload()))
        self.assertEqual(source.read_bytes(), original)
        self.assertTrue(router.metadata_path(source).is_file())

    def test_unknown_or_different_existing_file_is_preserved(self):
        source = self.root / "cses/Range_Update_Queries.py"
        for text in ("print('keep')\n", "# https://cses.fi/problemset/task/1648/\n"):
            source.write_text(text)
            with self.assertRaises(router.ImportError):
                router.store(self.root, router.validate_payload(self.payload()))
            self.assertEqual(source.read_text(), text)
            self.assertFalse(router.metadata_path(source).exists())

    def test_payload_paths_and_checkers_are_never_copied(self):
        value = {**self.payload(), "srcPath": "/tmp/escape.py", "customCheckerPath": "sh evil", "command": "bad"}
        target, _ = router.store(self.root, router.validate_payload(value))
        metadata = json.loads(router.metadata_path(target).read_text())
        self.assertEqual(metadata["srcPath"], str(target))
        self.assertNotIn("customCheckerPath", metadata)
        self.assertNotIn("command", metadata)

    def test_comment_encoding_cannot_turn_name_into_executable_code(self):
        value = self.payload(name=r"coding: unicode_escape \x0aprint('untrusted')")
        target, _ = router.store(self.root, router.validate_payload(value))
        self.assertTrue(target.read_text().startswith("# -*- coding: utf-8 -*-\n"))
        import ast
        tree = ast.parse(target.read_text())
        self.assertFalse(any(isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) for node in tree.body))

    def test_symlink_source_folder_and_metadata_are_rejected(self):
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        (self.root / "cses").rmdir()
        (self.root / "cses").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(router.ImportError):
            router.store(self.root, router.validate_payload(self.payload()))
        (self.root / "cses").unlink()
        (self.root / "cses").mkdir()
        (self.root / "cses/.cph").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(router.ImportError):
            router.store(self.root, router.validate_payload(self.payload()))
        self.assertEqual(list(outside.iterdir()), [])

    def test_recovery_copies_original_source_and_all_tests_without_deleting(self):
        source = self.root / "atcoder/Range_Update_Queries.py"
        source.write_text("# learner code\nprint('keep')\n")
        meta = router.metadata_path(source)
        meta.parent.mkdir()
        data = router.validate_payload(self.payload())
        data["tests"].append({"input": "edge\n", "output": "custom\n", "id": 90})
        data["srcPath"] = str(source)
        meta.write_text(json.dumps(data))
        originals = [source.read_bytes(), meta.read_bytes()]
        target, action = router.recover(self.root, source)
        self.assertEqual(target.parent.name, "cses")
        self.assertEqual(action, "created")
        self.assertEqual(target.read_bytes(), originals[0])
        copied = json.loads(router.metadata_path(target).read_text())
        self.assertEqual(copied["tests"], data["tests"])
        self.assertEqual(copied["srcPath"], str(target))
        self.assertEqual([source.read_bytes(), meta.read_bytes()], originals)
        self.assertEqual(router.recover(self.root, source), (target, "preserved"))
        target.write_text("other user changes\n")
        with self.assertRaises(router.ImportError):
            router.recover(self.root, source)
        self.assertEqual(target.read_text(), "other user changes\n")

    def test_recovery_refuses_success_when_target_is_missing_original_cases(self):
        target, _ = router.store(self.root, router.validate_payload(self.payload()))
        source = self.root / "atcoder/Range_Update_Queries.py"
        source.write_bytes(target.read_bytes())
        original = router.validate_payload(self.payload())
        original["tests"].append({"input": "custom\n", "output": "edge\n", "id": 9})
        meta = router.metadata_path(source)
        meta.parent.mkdir()
        meta.write_text(json.dumps({**original, "srcPath": str(source)}))
        before = router.metadata_path(target).read_bytes()
        with self.assertRaisesRegex(router.ImportError, "missing original test cases"):
            router.recover(self.root, source)
        self.assertEqual(router.metadata_path(target).read_bytes(), before)
        self.assertEqual(source.read_bytes(), target.read_bytes())

    def test_concurrent_import_never_rolls_back_another_successful_import(self):
        problem = router.validate_payload(self.payload())
        source_created = threading.Event()
        resume_first = threading.Event()
        original_write = router.write_new
        errors = []
        def paused_write(path, content):
            original_write(path, content)
            if path.suffix == ".py" and threading.current_thread().name == "first-import":
                source_created.set()
                if not resume_first.wait(5):
                    raise RuntimeError("test synchronization failed")
        def first():
            try:
                router.store(self.root, problem)
            except OSError as error:
                errors.append(error)
        with patch.object(router, "write_new", side_effect=paused_write):
            worker = threading.Thread(target=first, name="first-import")
            worker.start()
            try:
                self.assertTrue(source_created.wait(5))
                with self.assertRaisesRegex(router.ImportError, "Another importer"):
                    router.store(self.root, problem)
                other_url = router.validate_payload(self.payload(url="https://cses.fi/problemset/task/1648/"))
                with self.assertRaisesRegex(router.ImportError, "Another importer"):
                    router.store(self.root, other_url)
            finally:
                resume_first.set()
                worker.join(5)
        self.assertFalse(worker.is_alive())
        self.assertEqual(errors, [])
        target = self.root / "cses/Range_Update_Queries.py"
        self.assertTrue(target.is_file())
        self.assertTrue(router.metadata_path(target).is_file())
        self.assertEqual(json.loads(router.metadata_path(target).read_text())["url"], problem["url"])
        with self.assertRaises(router.ImportError):
            router.store(self.root, other_url)
        self.assertEqual(router.store(self.root, problem), (target, "preserved"))
        self.assertEqual(list(target.parent.glob(".companion-*.tmp")), [])

    def test_idle_connection_times_out_before_headers_and_allows_next_request(self):
        try:
            server = HTTPServer(("127.0.0.1", 0), router.handler_for(self.root))
        except PermissionError:
            self.skipTest("This executor forbids local sockets")
        with patch.object(router, "REQUEST_TIMEOUT", 0.1):
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            idle = socket.create_connection(server.server_address, timeout=2)
            try:
                started = time.monotonic()
                connection = http.client.HTTPConnection(*server.server_address, timeout=2)
                connection.request("POST", "/", body=json.dumps(self.payload()), headers={"Content-Type": "application/json"})
                response = connection.getresponse()
                self.assertEqual(response.status, 200)
                response.read()
                connection.close()
                self.assertLess(time.monotonic() - started, 2)
            finally:
                idle.close()
                server.shutdown()
                thread.join(5)
                server.server_close()

    def test_recovery_without_metadata_fails_without_guessing(self):
        source = self.root / "atcoder/Range_Update_Queries.py"
        source.write_text("# https://cses.fi/problemset/task/1651/\n")
        with self.assertRaises(router.ImportError):
            router.recover(self.root, source)
        self.assertEqual(list((self.root / "cses").iterdir()), [])

    def test_editor_is_argv_only_and_never_runs_solution(self):
        source = self.root / "cses/a name.py"
        with patch.object(router.shutil, "which", return_value="/usr/bin/code"), patch.object(router.subprocess, "run") as run:
            router.open_editor(source)
        self.assertEqual(run.call_args.args[0], ["/usr/bin/code", "--reuse-window", str(source)])
        self.assertNotIn("shell", run.call_args.kwargs)

    def test_root_task_uses_local_interpreter_without_automatic_run_or_cph_listener(self):
        root = Path(__file__).resolve().parents[1]
        tasks = json.loads((root / ".vscode/tasks.json").read_text())["tasks"]
        self.assertEqual(len(tasks), 1)
        task = tasks[0]
        self.assertEqual(task["type"], "process")
        self.assertEqual(task["command"], "${workspaceFolder}/.venv/bin/python")
        self.assertNotIn("runOn", task["runOptions"])
        self.assertEqual(task["runOptions"]["instanceLimit"], 1)
        settings = json.loads((root / ".vscode/settings.json").read_text())
        self.assertFalse(settings["cph.companion.enableServer"])
        self.assertEqual(settings["cph.general.saveLocation"], "")

    def test_http_protocol_rejects_web_origins_hosts_and_oversized_requests(self):
        try:
            server = HTTPServer(("127.0.0.1", 0), router.handler_for(self.root))
        except PermissionError:
            self.skipTest("This executor forbids local sockets; CI runs the HTTP test")
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        def post(headers, body=b"{}"):
            connection = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=5)
            connection.request("POST", "/", body=body, headers=headers)
            response = connection.getresponse()
            status = response.status
            response.read()
            connection.close()
            return status
        try:
            headers = {"Content-Type": "application/json"}
            self.assertEqual(post({**headers, "Origin": "https://evil.test"}), 403)
            self.assertEqual(post({**headers, "Host": "evil.test"}), 403)
            self.assertEqual(post({**headers, "Content-Length": str(router.MAX_BODY + 1)}), 400)
            self.assertEqual(post(headers, b"not json"), 400)
            self.assertEqual(post({"Content-Type": "text/plain"}), 400)
            self.assertEqual(post({**headers, "Origin": "chrome-extension://test"}, json.dumps(self.payload()).encode()), 200)
            self.assertEqual(post(headers, json.dumps(self.payload()).encode()), 200)
            for url, name, expected in [
                ("https://atcoder.jp/contests/abc470/tasks/abc470_a", "A Test", "atcoder/abc470a.py"),
                ("https://codeforces.com/problemset/problem/4/A", "A Watermelon", "codeforces/4A.py"),
            ]:
                self.assertEqual(post(headers, json.dumps(self.payload(url, name)).encode()), 200)
                self.assertTrue((self.root / expected).is_file())
            with self.assertRaises(OSError):
                HTTPServer(("127.0.0.1", server.server_port), router.handler_for(self.root))
        finally:
            server.shutdown()
            thread.join(timeout=5)
            server.server_close()


if __name__ == "__main__":
    unittest.main()
