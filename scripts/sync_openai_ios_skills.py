#!/usr/bin/env python3
"""Synchronize the allowlisted OpenAI Build iOS Apps skills and verify hashes."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys


SKILLS = (
    "ios-app-intents",
    "ios-debugger-agent",
    "ios-ettrace-performance",
    "ios-memgraph-leaks",
    "ios-simulator-browser",
    "swiftui-liquid-glass",
    "swiftui-performance-audit",
    "swiftui-ui-patterns",
    "swiftui-view-refactor",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_files(source: Path) -> dict[str, Path]:
    files = {".mcp.json": source / ".mcp.json"}
    for skill in SKILLS:
        root = source / "skills" / skill
        if not root.is_dir():
            raise ValueError(f"missing upstream skill directory: {root}")
        for path in sorted(root.rglob("*")):
            if path.is_file():
                files[str(path.relative_to(source))] = path
    missing = [name for name, path in files.items() if not path.is_file()]
    if missing:
        raise ValueError("missing upstream files: " + ", ".join(missing))
    return files


def manifest(source: Path, upstream_sha: str) -> dict:
    files = source_files(source)
    return {
        "upstream": "https://github.com/openai/plugins/tree/main/plugins/build-ios-apps",
        "baseline_version": "0.1.2",
        "commit": upstream_sha,
        "skills": list(SKILLS),
        "files": {name: digest(path) for name, path in sorted(files.items())},
    }


def apply_sync(source: Path, target: Path, data: dict, notice: Path | None) -> bool:
    manifest_path = target / "OPENAI_UPSTREAM.json"
    if manifest_path.is_file():
        try:
            current = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            current = {}
        if current.get("files") == data.get("files"):
            return False
    for skill in SKILLS:
        destination = target / "skills" / skill
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(source / "skills" / skill, destination)
    shutil.copy2(source / ".mcp.json", target / ".mcp.json")
    manifest_path.write_text(
        json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if notice:
        text = notice.read_text(encoding="utf-8")
        updated, count = re.subn(
            r"(?m)^OpenAI upstream commit: `[0-9a-f]+` <!-- sync-openai-sha -->$",
            f"OpenAI upstream commit: `{data['commit']}` <!-- sync-openai-sha -->",
            text,
            count=1,
        )
        if count != 1:
            raise ValueError("THIRD_PARTY_NOTICES.md is missing the sync SHA marker")
        notice.write_text(updated, encoding="utf-8")
    return True


def verify(target: Path) -> list[str]:
    manifest_path = target / "OPENAI_UPSTREAM.json"
    if not manifest_path.is_file():
        return ["missing OPENAI_UPSTREAM.json"]
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return [f"invalid OPENAI_UPSTREAM.json: {error}"]
    errors: list[str] = []
    expected = data.get("files", {})
    if not isinstance(expected, dict):
        return ["OPENAI_UPSTREAM.json files must be an object"]
    for name, expected_hash in expected.items():
        path = target / name
        if not path.is_file():
            errors.append(f"missing synchronized file: {name}")
        elif digest(path) != expected_hash:
            errors.append(f"hash mismatch: {name}")
    actual = {
        str(path.relative_to(target))
        for skill in SKILLS
        for path in (target / "skills" / skill).rglob("*")
        if path.is_file()
    }
    actual.add(".mcp.json")
    extras = sorted(actual - set(expected))
    if extras:
        errors.append("unrecorded synchronized files: " + ", ".join(extras))
    return errors


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--target", required=True, type=Path)
    result.add_argument("--check", action="store_true")
    result.add_argument("--source", type=Path)
    result.add_argument("--upstream-sha")
    result.add_argument("--notice", type=Path)
    return result


def main() -> int:
    args = parser().parse_args()
    target = args.target.resolve()
    if args.check:
        errors = verify(target)
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        if not errors:
            print("OpenAI synchronized file hashes are valid.")
        return 1 if errors else 0
    if not args.source or not args.upstream_sha:
        print("--source and --upstream-sha are required when applying a sync", file=sys.stderr)
        return 2
    try:
        data = manifest(args.source.resolve(), args.upstream_sha)
        changed = apply_sync(
            args.source.resolve(),
            target,
            data,
            args.notice.resolve() if args.notice else None,
        )
    except (OSError, ValueError) as error:
        print(f"Sync failed: {error}", file=sys.stderr)
        return 1
    if changed:
        print(f"Synchronized OpenAI Build iOS Apps at {args.upstream_sha}.")
    else:
        print("No allowlisted OpenAI Build iOS Apps file changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
