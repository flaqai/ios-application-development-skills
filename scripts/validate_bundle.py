#!/usr/bin/env python3
"""Validate marketplace, plugin, skills, local links, evals, and upstream hashes."""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "ios-application-development-skills"
EXPECTED_SKILLS = {
    "app-store-aso",
    "ios-app-intents",
    "ios-appstore-release-manager",
    "ios-debugger-agent",
    "ios-ettrace-performance",
    "ios-memgraph-leaks",
    "ios-simulator-browser",
    "swiftui-liquid-glass",
    "swiftui-performance-audit",
    "swiftui-ui-patterns",
    "swiftui-view-refactor",
}


def load_json(path: Path, errors: list[str]) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{path.relative_to(ROOT)}: {error}")
        return {}


def validate_skill(path: Path, errors: list[str]) -> None:
    skill_file = path / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"{path.relative_to(ROOT)}: missing SKILL.md")
        return
    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append(f"{skill_file.relative_to(ROOT)}: invalid frontmatter")
        return
    keys = [
        line.split(":", 1)[0].strip()
        for line in match.group(1).splitlines()
        if ":" in line
    ]
    if keys != ["name", "description"]:
        errors.append(
            f"{skill_file.relative_to(ROOT)}: frontmatter keys must be name, description"
        )
    name_match = re.search(r"(?m)^name:\s*(.+)$", match.group(1))
    if not name_match or name_match.group(1).strip() != path.name:
        errors.append(f"{skill_file.relative_to(ROOT)}: name must match directory")
    if not (path / "agents" / "openai.yaml").is_file():
        errors.append(f"{path.relative_to(ROOT)}: missing agents/openai.yaml")
    for markdown in path.rglob("*.md"):
        content = markdown.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^]]*\]\(([^)]+)\)", content):
            target = target.split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (markdown.parent / target).resolve().exists():
                errors.append(
                    f"{markdown.relative_to(ROOT)}: broken relative link {target}"
                )


def main() -> int:
    errors: list[str] = []
    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json", errors)
    plugin = load_json(PLUGIN / ".codex-plugin" / "plugin.json", errors)
    mcp = load_json(PLUGIN / ".mcp.json", errors)
    if isinstance(marketplace, dict):
        if marketplace.get("name") != "flaqai-ios":
            errors.append("marketplace name must be flaqai-ios")
        entries = marketplace.get("plugins", [])
        if not isinstance(entries, list) or len(entries) != 1:
            errors.append("marketplace must contain exactly one plugin")
    if isinstance(plugin, dict):
        if plugin.get("name") != "ios-application-development-skills":
            errors.append("plugin name is invalid")
        if plugin.get("version") != "0.1.0":
            errors.append("plugin version must be 0.1.0")
        if "icon" in plugin or "icons" in plugin:
            errors.append("plugin must not declare unprovided icon assets")
    if not isinstance(mcp, dict) or "xcodebuildmcp" not in mcp.get("mcpServers", {}):
        errors.append("plugin must configure xcodebuildmcp")

    skills_root = PLUGIN / "skills"
    actual_skills = {path.name for path in skills_root.iterdir() if path.is_dir()}
    if actual_skills != EXPECTED_SKILLS:
        errors.append(
            "skill set mismatch: "
            f"missing={sorted(EXPECTED_SKILLS - actual_skills)} "
            f"extra={sorted(actual_skills - EXPECTED_SKILLS)}"
        )
    for name in sorted(EXPECTED_SKILLS):
        validate_skill(skills_root / name, errors)

    evals = load_json(skills_root / "app-store-aso" / "evals" / "evals.json", errors)
    if not isinstance(evals, dict) or len(evals.get("evals", [])) < 5:
        errors.append("app-store-aso must contain at least five eval cases")

    hash_check = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "sync_openai_ios_skills.py"),
            "--target",
            str(PLUGIN),
            "--check",
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    if hash_check.returncode:
        errors.append(hash_check.stderr.strip() or hash_check.stdout.strip())

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Marketplace, plugin, 11 skills, links, evals, MCP, and upstream hashes are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
