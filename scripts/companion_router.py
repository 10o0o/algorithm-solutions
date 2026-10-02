#!/usr/bin/env python3
"""Route Competitive Companion JSON into platform folders; never run solution code."""
from __future__ import annotations

import argparse
from collections import Counter
from contextlib import contextmanager
import fcntl
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
MAX_BODY = 2 * 1024 * 1024
REQUEST_TIMEOUT = 5
PLATFORMS = ("atcoder", "codeforces", "cses")


class ImportError(ValueError):
    """Invalid data or a conflict that must preserve existing files."""


def route(url: str, name: str) -> tuple[str, str, str]:
    try:
        parsed = urlsplit(url)
        host = (parsed.hostname or "").removeprefix("www.")
        if parsed.scheme != "https" or parsed.username or parsed.password or parsed.port not in (None, 443):
            raise ValueError
    except ValueError as error:
        raise ImportError("Expected an HTTPS problem URL without credentials or a custom port") from error
    path = parsed.path.rstrip("/")
    if host == "atcoder.jp":
        match = re.fullmatch(r"/contests/([A-Za-z0-9_-]+)/tasks/([A-Za-z0-9_]+)", path)
        if match:
            task = match[2]
            stem = task.replace("_", "")
            return "atcoder", stem + ".py", f"https://atcoder.jp{path}"
    elif host == "codeforces.com":
        match = re.fullmatch(r"/(contest|gym)/(\d+)/problem/([A-Za-z0-9]+)", path)
        if match:
            kind, number, index = match.groups()
            return "codeforces", number + index + ".py", f"https://codeforces.com/{kind}/{number}/problem/{index}"
        match = re.fullmatch(r"/problemset/(problem|gymProblem)/(\d+)/([A-Za-z0-9]+)", path)
        if match:
            kind, number, index = match.groups()
            kind = "gym" if kind == "gymProblem" else "contest"
            return "codeforces", number + index + ".py", f"https://codeforces.com/{kind}/{number}/problem/{index}"
    elif host == "cses.fi":
        match = re.fullmatch(r"/problemset/task/(\d+)", path)
        if match:
            stem = "_".join(re.findall(r"[A-Za-z0-9]+", name))
            if not stem or len(stem) > 160:
                raise ImportError("CSES problem name must produce a filename of 1–160 ASCII characters")
            return "cses", stem + ".py", f"https://cses.fi/problemset/task/{match[1]}/"
    raise ImportError("Unsupported problem URL; only AtCoder, Codeforces and CSES problem pages are accepted")


def validate_payload(value: object) -> dict:
    if not isinstance(value, dict):
        raise ImportError("Problem must be a JSON object")
    for key in ("name", "url", "group"):
        if not isinstance(value.get(key), str) or not value[key].strip() or len(value[key]) > 1000:
            raise ImportError(f"Invalid {key}")
        if any(ord(character) < 32 for character in value[key]):
            raise ImportError(f"Control characters are not allowed in {key}")
    route(value["url"], value["name"])
    if value.get("interactive", False) is not False:
        raise ImportError("Interactive problems are not supported by this sample runner")
    for key in ("timeLimit", "memoryLimit"):
        number = value.get(key)
        if type(number) not in (int, float) or not 0 < number <= 1_000_000_000:
            raise ImportError(f"Invalid {key}")
    tests = value.get("tests")
    if not isinstance(tests, list) or len(tests) > 100:
        raise ImportError("tests must be a list of at most 100 cases")
    clean_tests = []
    for index, case in enumerate(tests):
        if not isinstance(case, dict) or not all(isinstance(case.get(key), str) for key in ("input", "output")):
            raise ImportError("Every test needs string input and output")
        clean_tests.append({"input": case["input"], "output": case["output"], "id": index + 1})
    # Do not copy payload paths, custom checkers, commands or arbitrary properties.
    return {**{key: value[key] for key in ("name", "url", "group", "timeLimit", "memoryLimit")},
            "interactive": False, "tests": clean_tests}


def checked(root: Path, path: Path) -> Path:
    path = path.absolute()
    try:
        parts = path.relative_to(root).parts
    except ValueError as error:
        raise ImportError("Path is outside this repository") from error
    cursor = root
    for part in parts:
        if part in (".", ".."):
            raise ImportError("Relative traversal is not allowed")
        cursor /= part
        if cursor.is_symlink():
            raise ImportError(f"Refusing symlink: {cursor}")
    return path


def metadata_path(source: Path) -> Path:
    # CPH src/parser.ts: md5 of the exact absolute source path, UTF-8, lowercase hex.
    digest = hashlib.md5(str(source).encode("utf-8"), usedforsecurity=False).hexdigest()
    return source.parent / ".cph" / f".{source.name}_{digest}.prob"


def identity(problem: dict) -> str:
    return route(problem["url"], problem.get("name", "problem"))[2]


def read_metadata(root: Path, source: Path) -> dict | None:
    path = checked(root, metadata_path(source))
    if not path.exists():
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise ValueError
        identity(value)
        return value
    except (ValueError, KeyError, OSError) as error:
        raise ImportError(f"Invalid existing CPH metadata; preserved: {path}") from error


def source_identity(root: Path, source: Path) -> str | None:
    checked(root, source)
    metadata = read_metadata(root, source)
    if metadata:
        return identity(metadata)
    if source.exists():
        with source.open(encoding="utf-8") as stream:
            for _ in range(8):
                line = stream.readline(4096).strip()
                if re.fullmatch(r"#\s+https://\S+", line):
                    try:
                        return route(line.lstrip("# "), source.stem)[2]
                    except ImportError:
                        pass
    return None


def destination(root: Path, problem: dict) -> Path:
    platform, filename, key = route(problem["url"], problem["name"])
    directory = checked(root, root / platform)
    if not directory.is_dir():
        raise ImportError(f"Platform folder is missing: {directory}")
    # Retain an existing source with this URL even if its title/filename changed.
    matches = []
    for source in directory.glob("*.py"):
        if source_identity(root, source) == key:
            matches.append(source)
    if len(matches) > 1:
        raise ImportError("Multiple files have this problem URL; resolve the duplicate manually")
    target = checked(root, matches[0] if matches else directory / filename)
    known = source_identity(root, target)
    if target.exists() and known != key:
        raise ImportError(f"Existing filename has an unknown/different problem URL; preserved: {target}")
    if known is not None and known != key:
        raise ImportError(f"Existing metadata belongs to another problem; preserved: {target}")
    return target


def write_new(path: Path, content: bytes) -> None:
    # Publish complete bytes exclusively: existing files are never replaced.
    descriptor, name = tempfile.mkstemp(prefix=".companion-", suffix=".tmp", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.chmod(0o644)
        os.link(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


@contextmanager
def repository_lock(root: Path):
    directory = checked(root, root / ".local")
    directory.mkdir(exist_ok=True)
    path = checked(root, directory / "companion-router.lock")
    descriptor = os.open(path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise ImportError("Another importer is writing in this repository; retry after it finishes") from error
        yield
    finally:
        os.close(descriptor)
        # Keep the lock inode: unlinking it would allow two different locks.


def store(root: Path, problem: dict, source_bytes: bytes | None = None) -> tuple[Path, str]:
    with repository_lock(root):
        return store_locked(root, problem, source_bytes)


def store_locked(root: Path, problem: dict, source_bytes: bytes | None = None) -> tuple[Path, str]:
    recovering = source_bytes is not None
    target = destination(root, problem)
    meta = checked(root, metadata_path(target))
    existing = read_metadata(root, target)
    if target.exists() and source_bytes is not None and target.read_bytes() != source_bytes:
        raise ImportError(f"Recovery target contains different code; neither file changed: {target}")
    if source_bytes is None:
        template = checked(root, root / "templates" / "python.py").read_text(encoding="utf-8")
        source_bytes = ("# -*- coding: utf-8 -*-\n" + template.replace("$name$", problem["name"]).replace("$url$", problem["url"])
                        .replace("$CURSOR_PLACEHOLDER", "")).encode("utf-8")
    if existing is not None and recovering:
        def cases(value: dict) -> Counter:
            return Counter((case["input"], case["output"]) for case in value["tests"])
        try:
            if cases(problem) - cases(existing):
                raise ImportError("Recovery target is missing original test cases; neither file changed")
        except (KeyError, TypeError) as error:
            raise ImportError("Invalid target test cases; neither file changed") from error
    created = not target.exists()
    if created:
        write_new(target, source_bytes)
    if existing is None:
        meta.parent.mkdir(exist_ok=True)
        data = {**problem, "srcPath": str(target)}
        write_new(meta, (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode())
    # On an I/O error/concurrent import, retain every published file. Retry is safe.
    return target, "created" if created else "preserved"


def recover(root: Path, source: Path) -> tuple[Path, str]:
    source = checked(root, source if source.is_absolute() else root / source)
    if source.suffix != ".py" or source.relative_to(root).parts[0] not in PLATFORMS:
        raise ImportError("Recovery input must be a platform Python file inside this repository")
    metadata = read_metadata(root, source)
    if metadata is None:
        raise ImportError("Recovery needs the original source-adjacent .cph metadata; no files changed")
    clean = validate_payload(metadata)
    # Preserve local test IDs in the copy, never alter the original.
    if "customCheckerPath" in metadata:
        raise ImportError("Custom checker recovery needs manual review; no files changed")
    clean["tests"] = metadata["tests"]
    return store(root, clean, source.read_bytes())


def open_editor(path: Path) -> None:
    code = shutil.which("code")
    if code is None:
        print(f"Open manually in VS Code: {path}", flush=True)
        return
    try:
        subprocess.run([code, "--reuse-window", str(path)], check=True, timeout=10,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except (OSError, subprocess.SubprocessError):
        print(f"Saved successfully; open manually in VS Code: {path}", flush=True)


def handler_for(root: Path, open_files: bool = False):
    class Handler(BaseHTTPRequestHandler):
        def setup(self):
            super().setup()
            self.connection.settimeout(REQUEST_TIMEOUT)

        def log_message(self, *_args):
            pass

        def trusted(self) -> bool:
            host = self.headers.get("Host", "").split(":")[0]
            origin = self.headers.get("Origin", "")
            return host in ("localhost", "127.0.0.1") and (not origin or origin.startswith(("chrome-extension://", "moz-extension://")))

        def reply(self, status: int, message: str = "") -> None:
            body = json.dumps({"empty": True, "message": message}).encode()
            self.send_response(status)
            origin = self.headers.get("Origin")
            if origin and self.trusted():
                self.send_header("Access-Control-Allow-Origin", origin)
                self.send_header("Access-Control-Allow-Headers", "Content-Type")
                self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_OPTIONS(self):
            self.reply(200 if self.path == "/" and self.trusted() else 403)

        def do_POST(self):
            if self.path != "/" or not self.trusted():
                self.reply(403, "Only local extension requests to / are accepted")
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= MAX_BODY or self.headers.get("Transfer-Encoding"):
                    raise ImportError("Request size must be 1 byte–2 MiB; chunked requests are not accepted")
                if self.headers.get_content_type() != "application/json":
                    raise ImportError("Content-Type must be application/json")
                self.connection.settimeout(REQUEST_TIMEOUT)
                data = self.rfile.read(length)
                if len(data) != length:
                    raise ImportError("Incomplete request")
                target, action = store(root, validate_payload(json.loads(data)))
                print(f"{action}: {target.relative_to(root)}", flush=True)
                self.reply(200, f"{action}: {target.relative_to(root)}")
                if open_files:
                    open_editor(target)
            except (ValueError, OSError) as error:
                print(f"rejected: {error}", file=sys.stderr, flush=True)
                self.reply(400, str(error))
    return Handler


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=27121)
    parser.add_argument("--open", action="store_true", help="open saved files with code --reuse-window")
    parser.add_argument("--recover", type=Path, help="copy a misfiled solution and CPH tests to the correct platform; retain originals")
    args = parser.parse_args()
    try:
        if args.recover:
            target, action = recover(ROOT, args.recover)
            print(f"{action}: {target}; original source and metadata retained")
            return 0
        if not 1 <= args.port <= 65535:
            raise ImportError("Port must be 1–65535")
        with HTTPServer(("127.0.0.1", args.port), handler_for(ROOT, args.open)) as server:
            print(f"Companion router ready on 127.0.0.1:{args.port} | {ROOT}", flush=True)
            print("CPH companion server must stay disabled; Ctrl+C stops this listener.", flush=True)
            server.serve_forever()
    except KeyboardInterrupt:
        return 0
    except (ImportError, OSError) as error:
        print(f"error: {error}\nIf port 27121 is busy, close old CPH workspace/listener windows; do not start a second receiver.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
