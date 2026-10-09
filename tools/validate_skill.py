#!/usr/bin/env python3
"""Validate skill metadata, module paths, package versions, and script syntax."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "plugins/enterprise-ai-security/skills/enterprise-ai-security"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must begin with YAML frontmatter")
    try:
        _, raw, _ = text.split("---", 2)
        metadata = yaml.safe_load(raw)
    except (ValueError, yaml.YAMLError) as exc:
        fail(f"invalid SKILL.md frontmatter: {exc}")
    if not isinstance(metadata, dict):
        fail("SKILL.md frontmatter must be a YAML mapping")
    return metadata


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read valid JSON from {path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def main() -> None:
    metadata = read_frontmatter(SKILL_ROOT / "SKILL.md")
    required = ("name", "description", "version", "license", "domain", "subdomain")
    missing = [field for field in required if not metadata.get(field)]
    if missing:
        fail(f"missing frontmatter fields: {', '.join(missing)}")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(metadata["name"])):
        fail("skill name must use kebab-case")
    if len(metadata["description"]) < 40 or len(metadata["description"]) > 2000:
        fail("skill description must be between 40 and 2000 characters")
    if not isinstance(metadata.get("tags"), list) or not isinstance(metadata.get("frameworks"), dict):
        fail("tags must be a list and frameworks must be a mapping")

    skill_file = SKILL_ROOT / "SKILL.md"
    body = skill_file.read_text(encoding="utf-8")
    for module in re.findall(r"references/([A-Za-z0-9_.-]+\.md)", body):
        if not (SKILL_ROOT / "references" / module).is_file():
            fail(f"SKILL.md references missing module: references/{module}")

    index = load_json(SKILL_ROOT / "index.json")
    if index.get("name") != metadata["name"] or str(index.get("version")) != str(metadata["version"]):
        fail("index.json name/version must match SKILL.md")
    for field in ("description", "domain", "subdomain", "author", "license", "tags", "frameworks"):
        if index.get(field) != metadata.get(field):
            fail(f"index.json {field} must match SKILL.md")

    expected_modules = {
        "references": sorted(
            path.relative_to(SKILL_ROOT).as_posix()
            for path in (SKILL_ROOT / "references").glob("*.md")
            if path.is_file()
        ),
        "mappings": sorted(
            path.relative_to(SKILL_ROOT).as_posix()
            for path in (SKILL_ROOT / "mappings").glob("*.md")
            if path.is_file()
        ),
        "assets": sorted(
            path.relative_to(SKILL_ROOT).as_posix()
            for path in (SKILL_ROOT / "assets").rglob("*")
            if path.is_file()
        ),
        "scripts": sorted(
            path.relative_to(SKILL_ROOT).as_posix()
            for path in (SKILL_ROOT / "scripts").glob("*.py")
            if path.name != "build_index.py" and path.is_file()
        ),
    }
    if index.get("modules") != expected_modules:
        fail("index.json module inventory is stale; run scripts/build_index.py")

    plugin = load_json(ROOT / "plugins/enterprise-ai-security/.claude-plugin/plugin.json")
    marketplace = load_json(ROOT / ".claude-plugin/marketplace.json")
    if plugin.get("name") != metadata["name"] or str(plugin.get("version")) != str(metadata["version"]):
        fail("plugin.json name/version must match SKILL.md")
    if plugin.get("license") != metadata["license"]:
        fail("plugin.json license must match SKILL.md")
    marketplace_version = marketplace.get("metadata", {}).get("version")
    if str(marketplace_version) != str(metadata["version"]):
        fail("marketplace.json metadata.version must match SKILL.md")
    declared_plugins = marketplace.get("plugins", [])
    if not any(item.get("name") == plugin.get("name") for item in declared_plugins):
        fail("marketplace.json must register the plugin")

    scripts = sorted((SKILL_ROOT / "scripts").glob("*.py"))
    for script in scripts:
        try:
            compile(script.read_text(encoding="utf-8"), str(script), "exec")
        except SyntaxError as exc:
            fail(f"Python syntax error in {script.relative_to(ROOT)}: {exc}")
    print(
        f"Valid: {metadata['name']} {metadata['version']}; "
        f"{len(index.get('modules', {}).get('references', []))} references, "
        f"{len(index.get('modules', {}).get('mappings', []))} mapping notes, "
        f"{len(scripts)} scripts."
    )


if __name__ == "__main__":
    main()
