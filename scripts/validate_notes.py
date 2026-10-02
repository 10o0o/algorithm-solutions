#!/usr/bin/env python3
"""Validate learning-note metadata and repository-local Markdown links."""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

import yaml
from markdown_it import MarkdownIt


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PLATFORM_DIRECTORIES = {"atcoder", "codeforces", "cses", "leetcode"}
DEFAULT_DIRECTORIES = ("knowledge", "contests", *sorted(PLATFORM_DIRECTORIES))
EXCLUDED_DEFAULT_NAMES = {"README.md", "template.md"}
PROHIBITED_COMPONENTS = {".local", ".venv", ".venv-pypy", ".cph", "private", ".git"}
PROHIBITED_ROOT_FILES = {"main.py", "ex.in"}
REQUIRED_CONCEPT_SECTIONS = ("핵심 요약", "개념 정리")
FRONTMATTER_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s|$)")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MARKDOWN = MarkdownIt("commonmark")


class FrontmatterLoader(yaml.SafeLoader):
    """Safe YAML loader that leaves date scalars for explicit strict validation."""

    def construct_mapping(self, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
        seen: set[Any] = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                duplicate = key in seen
            except TypeError:
                # The base loader will report an unhashable mapping key.
                continue
            if duplicate:
                raise yaml.constructor.ConstructorError(
                    "while constructing a mapping",
                    node.start_mark,
                    f"found duplicate key {key!r}",
                    key_node.start_mark,
                )
            seen.add(key)
        return super().construct_mapping(node, deep=deep)


FrontmatterLoader.yaml_implicit_resolvers = {
    first: [
        (tag, regexp)
        for tag, regexp in resolvers
        if tag != "tag:yaml.org,2002:timestamp"
    ]
    for first, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def format_error(path: Path, line: int, message: str) -> str:
    return f"{path}:{line}: {message}"


def split_frontmatter(path: Path, text: str) -> tuple[str | None, str, int, list[str]]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text, 0, [format_error(path, 1, "file must start with YAML frontmatter")]

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "".join(lines[1:index]), "".join(lines[index + 1 :]), index + 1, []
    return None, "", 0, [format_error(path, 1, "YAML frontmatter is not closed")]


def key_lines(frontmatter: str) -> dict[str, int]:
    result: dict[str, int] = {}
    for index, line in enumerate(frontmatter.splitlines(), start=2):
        match = FRONTMATTER_KEY_RE.match(line)
        if match:
            result.setdefault(match.group(1), index)
    return result


def parse_metadata(path: Path, frontmatter: str) -> tuple[dict[str, Any], dict[str, int], list[str]]:
    lines = key_lines(frontmatter)
    try:
        loaded = yaml.load(frontmatter, Loader=FrontmatterLoader)
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        line = (mark.line + 2) if mark is not None else 1
        problem = getattr(exc, "problem", None) or str(exc).splitlines()[0]
        return {}, lines, [format_error(path, line, f"invalid YAML frontmatter: {problem}")]

    if loaded is None:
        return {}, lines, []
    if not isinstance(loaded, dict):
        return {}, lines, [format_error(path, 2, "YAML frontmatter must be a mapping")]
    return loaded, lines, []


def classify(path: Path, root: Path) -> str:
    try:
        top_level = path.absolute().relative_to(root.resolve()).parts[0]
    except (ValueError, IndexError):
        return "record"
    if top_level == "knowledge":
        return "concept"
    if top_level == "contests":
        return "contest"
    if top_level in PLATFORM_DIRECTORIES:
        return "problem"
    return "record"


def required_fields(kind: str) -> tuple[str, ...]:
    common = ("title", "updated", "tags")
    if kind == "contest":
        return (*common, "url")
    if kind == "problem":
        return (*common, "url", "solution")
    return common


def valid_iso_date(value: object) -> bool:
    if isinstance(value, dt.datetime):
        return False
    if isinstance(value, dt.date):
        return True
    if not isinstance(value, str) or DATE_RE.fullmatch(value) is None:
        return False
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def safe_urlparse(value: object):
    if not isinstance(value, str):
        return None
    try:
        return urlparse(value)
    except ValueError:
        return None


def validate_metadata(
    path: Path,
    root: Path,
    metadata: dict[str, Any],
    lines: dict[str, int],
    kind: str,
) -> list[str]:
    errors: list[str] = []
    for field in required_fields(kind):
        if field not in metadata:
            errors.append(format_error(path, 1, f"missing frontmatter field: {field}"))

    if "title" in metadata and (
        not isinstance(metadata["title"], str) or not metadata["title"].strip()
    ):
        errors.append(format_error(path, lines.get("title", 1), "title must be a non-empty string"))

    if "updated" in metadata and not valid_iso_date(metadata["updated"]):
        errors.append(
            format_error(path, lines.get("updated", 1), "updated must be a real YYYY-MM-DD date")
        )

    if "tags" in metadata:
        tags = metadata["tags"]
        if not isinstance(tags, list) or any(not isinstance(tag, str) for tag in tags):
            errors.append(format_error(path, lines.get("tags", 1), "tags must be a list of strings"))

    if kind in {"contest", "problem"} and "url" in metadata:
        url = metadata["url"]
        parsed = safe_urlparse(url)
        if parsed is None or parsed.scheme != "https" or not parsed.netloc:
            errors.append(
                format_error(path, lines.get("url", 1), "url must be an external https URL")
            )

    if kind == "problem" and "solution" in metadata:
        solution = metadata["solution"]
        line = lines.get("solution", 1)
        if not isinstance(solution, str) or not solution.strip():
            errors.append(format_error(path, line, "solution must be a relative path to a .py file"))
        else:
            raw = unquote(solution)
            parsed = safe_urlparse(raw)
            if (
                parsed is None
                or parsed.scheme
                or parsed.netloc
                or Path(parsed.path).is_absolute()
            ):
                errors.append(format_error(path, line, "solution must be a relative path to a .py file"))
            else:
                target_path = lexical_absolute(path.parent / parsed.path)
                target = target_path.resolve(strict=False)
                if target_path.suffix.lower() != ".py":
                    errors.append(format_error(path, line, "solution must point to a .py file"))
                elif not is_within(target_path, root.resolve()) or not is_within(
                    target, root.resolve()
                ):
                    errors.append(format_error(path, line, "solution path is outside repository"))
                elif is_prohibited_path(target_path, root) or is_prohibited_path(target, root):
                    errors.append(format_error(path, line, "solution path is prohibited"))
                elif has_symlink_component(target_path, root):
                    errors.append(format_error(path, line, "solution path must not traverse a symlink"))
                elif target.relative_to(root.resolve()).parts[0] not in PLATFORM_DIRECTORIES:
                    errors.append(
                        format_error(path, line, "solution must be inside a platform directory")
                    )
                elif not target.is_file():
                    errors.append(format_error(path, line, f"solution file does not exist: {solution}"))
    return errors


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def lexical_absolute(path: Path) -> Path:
    """Return an absolute normalized path without resolving symlinks."""

    return Path(os.path.abspath(path))


def has_prohibited_component(path: Path, root: Path) -> bool:
    try:
        parts = path.relative_to(root.resolve()).parts
    except ValueError:
        return False
    return any(part in PROHIBITED_COMPONENTS for part in parts)


def is_prohibited_path(path: Path, root: Path) -> bool:
    if has_prohibited_component(path, root):
        return True
    try:
        relative = path.relative_to(root.resolve())
    except ValueError:
        return False
    return len(relative.parts) == 1 and relative.name in PROHIBITED_ROOT_FILES


def has_symlink_component(path: Path, root: Path) -> bool:
    try:
        relative = lexical_absolute(path).relative_to(root.resolve())
    except ValueError:
        return False
    current = root.resolve()
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            return True
    return False


def heading_data(tokens: list[Any], level: str) -> list[tuple[int, str]]:
    headings: list[tuple[int, str]] = []
    for index, token in enumerate(tokens[:-1]):
        if token.type == "heading_open" and token.tag == level:
            line = token.map[0] + 1 if token.map else 1
            headings.append((line, tokens[index + 1].content.strip()))
    return headings


def validate_concept_headings(
    path: Path, metadata: dict[str, Any], tokens: list[Any], body_start_line: int
) -> list[str]:
    errors: list[str] = []
    h1s = heading_data(tokens, "h1")
    title = metadata.get("title")
    if len(h1s) != 1:
        errors.append(format_error(path, body_start_line, f"expected exactly one top-level heading, found {len(h1s)}"))
    elif not isinstance(title, str) or h1s[0][1] != title.strip():
        errors.append(
            format_error(path, body_start_line + h1s[0][0] - 1, "top-level heading must match frontmatter title")
        )

    h2_names = {name for _, name in heading_data(tokens, "h2")}
    for section in REQUIRED_CONCEPT_SECTIONS:
        if section not in h2_names:
            errors.append(format_error(path, body_start_line, f"missing required section: {section}"))
    return errors


def target_line(token: Any, target: str, references: dict[str, Any]) -> int:
    start = token.map[0] + 1 if token.map else 1
    for offset, source_line in enumerate(token.content.splitlines()):
        if target in source_line:
            return start + offset
    for reference in references.values():
        if reference.get("href") == target and reference.get("map"):
            return reference["map"][0] + 1
    return start


def iter_link_targets(tokens: list[Any], references: dict[str, Any]):
    for token in tokens:
        if token.type != "inline" or not token.children:
            continue
        for child in token.children:
            if child.type == "link_open":
                target = child.attrGet("href")
            elif child.type == "image":
                target = child.attrGet("src")
            else:
                continue
            if target is not None:
                yield target_line(token, target, references), target


def validate_raw_html(path: Path, tokens: list[Any], body_start_line: int) -> list[str]:
    lines: set[int] = set()
    for token in tokens:
        if token.type == "html_block":
            lines.add(token.map[0] + 1 if token.map else 1)
        elif token.type == "inline" and token.children:
            if any(child.type == "html_inline" for child in token.children):
                lines.add(token.map[0] + 1 if token.map else 1)
    return [
        format_error(path, body_start_line + line - 1, "raw HTML is prohibited in public notes")
        for line in sorted(lines)
    ]


def normalize_local_target(target: str) -> str:
    return unquote(target.split("#", maxsplit=1)[0].split("?", maxsplit=1)[0])


def validate_links(
    path: Path,
    root: Path,
    tokens: list[Any],
    references: dict[str, Any],
    body_start_line: int,
) -> list[str]:
    errors: list[str] = []
    resolved_root = root.resolve()
    for body_line, raw_target in iter_link_targets(tokens, references):
        parsed = safe_urlparse(raw_target)
        if (
            not raw_target
            or raw_target.startswith("#")
            or raw_target.lower().startswith(("http://", "https://"))
            or (parsed is not None and parsed.scheme in {"mailto", "data"})
        ):
            continue
        target_text = normalize_local_target(raw_target)
        if not target_text:
            continue
        target_path = lexical_absolute(path.parent / target_text)
        target = target_path.resolve(strict=False)
        line = body_start_line + body_line - 1
        if not is_within(target_path, resolved_root) or not is_within(target, resolved_root):
            errors.append(format_error(path, line, f"local link is outside repository: {raw_target}"))
        elif is_prohibited_path(target_path, resolved_root) or is_prohibited_path(
            target, resolved_root
        ):
            errors.append(format_error(path, line, f"local link target is prohibited: {raw_target}"))
        elif has_symlink_component(target_path, resolved_root):
            errors.append(
                format_error(path, line, f"local link target must not traverse a symlink: {raw_target}")
            )
        elif not target.exists():
            errors.append(format_error(path, line, f"local link target does not exist: {raw_target}"))
    return errors


def validate_file(path: Path, root: Path) -> list[str]:
    resolved_root = root.resolve()
    lexical_path = lexical_absolute(path)
    if not is_within(lexical_path, resolved_root) or not is_within(
        lexical_path.resolve(strict=False), resolved_root
    ):
        return [format_error(path, 1, "Markdown file is outside repository")]
    if is_prohibited_path(lexical_path, resolved_root):
        return [format_error(path, 1, "Markdown file path is prohibited")]
    kind = classify(lexical_path, resolved_root)
    if kind != "record" and has_symlink_component(lexical_path, resolved_root):
        return [format_error(path, 1, "public Markdown file must not traverse a symlink")]

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [format_error(path, 1, f"cannot read Markdown file: {exc}")]

    frontmatter, body, closing_line, errors = split_frontmatter(path, text)
    if frontmatter is None:
        return errors
    metadata, lines, metadata_errors = parse_metadata(path, frontmatter)
    errors.extend(metadata_errors)
    if metadata_errors:
        return errors

    errors.extend(validate_metadata(path, root, metadata, lines, kind))
    environment: dict[str, Any] = {}
    tokens = MARKDOWN.parse(body, environment)
    body_start_line = closing_line + 1
    if kind == "concept":
        errors.extend(validate_concept_headings(path, metadata, tokens, body_start_line))
    if kind != "record":
        errors.extend(validate_raw_html(path, tokens, body_start_line))
    errors.extend(
        validate_links(path, root, tokens, environment.get("references", {}), body_start_line)
    )
    return errors


def default_paths(root: Path) -> tuple[list[Path], list[str]]:
    paths: list[Path] = []
    errors: list[str] = []
    resolved_root = root.resolve()
    for directory in DEFAULT_DIRECTORIES:
        base = root / directory
        if base.is_dir():
            for path in base.rglob("*.md"):
                if path.name in EXCLUDED_DEFAULT_NAMES:
                    continue
                relative_parts = path.absolute().relative_to(resolved_root).parts
                if any(part in PROHIBITED_COMPONENTS for part in relative_parts):
                    continue
                if not is_within(path.resolve(strict=False), resolved_root):
                    errors.append(
                        format_error(
                            path,
                            1,
                            "discovered Markdown file resolves outside repository",
                        )
                    )
                    continue
                if has_symlink_component(path, resolved_root):
                    errors.append(
                        format_error(path, 1, "public Markdown file must not traverse a symlink")
                    )
                    continue
                paths.append(path)
    return sorted(set(paths)), errors


def explicit_paths(arguments: list[Path], root: Path) -> tuple[list[Path], list[str]]:
    paths: list[Path] = []
    errors: list[str] = []
    resolved_root = root.resolve()

    def add_file(path: Path) -> None:
        lexical_path = lexical_absolute(path)
        resolved_path = lexical_path.resolve(strict=False)
        if not is_within(lexical_path, resolved_root) or not is_within(
            resolved_path, resolved_root
        ):
            errors.append(format_error(path, 1, "path is outside repository"))
        elif is_prohibited_path(lexical_path, resolved_root) or is_prohibited_path(
            resolved_path, resolved_root
        ):
            errors.append(format_error(path, 1, "path is prohibited"))
        elif classify(lexical_path, resolved_root) != "record" and has_symlink_component(
            lexical_path, resolved_root
        ):
            errors.append(format_error(path, 1, "public Markdown file must not traverse a symlink"))
        elif lexical_path.suffix.lower() != ".md":
            errors.append(format_error(path, 1, "expected a Markdown file"))
        else:
            paths.append(lexical_path)

    for argument in arguments:
        lexical_argument = lexical_absolute(argument)
        resolved_argument = lexical_argument.resolve(strict=False)
        if not is_within(lexical_argument, resolved_root) or not is_within(
            resolved_argument, resolved_root
        ):
            errors.append(format_error(argument, 1, "path is outside repository"))
        elif is_prohibited_path(lexical_argument, resolved_root) or is_prohibited_path(
            resolved_argument, resolved_root
        ):
            errors.append(format_error(argument, 1, "path is prohibited"))
        elif lexical_argument.is_file():
            add_file(lexical_argument)
        elif lexical_argument.is_dir():
            for path in lexical_argument.rglob("*.md"):
                add_file(path)
        else:
            errors.append(format_error(argument, 1, "path does not exist"))
    return sorted(set(paths)), errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = REPOSITORY_ROOT
    if args.paths:
        paths, errors = explicit_paths(args.paths, root)
    else:
        paths, errors = default_paths(root)

    for path in paths:
        errors.extend(validate_file(path, root))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"FAILED: {len(errors)} error(s) in {len(paths)} note(s).", file=sys.stderr)
        return 1
    print(f"OK: validated {len(paths)} note(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
