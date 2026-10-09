#!/usr/bin/env python3
"""Build the portable skill's machine-readable module index."""

from __future__ import annotations

import json
from pathlib import Path

import yaml


SKILL_ROOT = Path(__file__).resolve().parents[1]


def read_frontmatter(skill_file: Path) -> dict:
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must begin with YAML frontmatter")
    _, frontmatter, _ = text.split("---", 2)
    metadata = yaml.safe_load(frontmatter)
    if not isinstance(metadata, dict):
        raise ValueError("SKILL.md frontmatter must be a YAML mapping")
    return metadata


def markdown_files(directory: str) -> list[str]:
    return sorted(
        path.relative_to(SKILL_ROOT).as_posix()
        for path in (SKILL_ROOT / directory).glob("*.md")
        if path.is_file()
    )


def build_index() -> dict:
    metadata = read_frontmatter(SKILL_ROOT / "SKILL.md")
    return {
        "name": metadata["name"],
        "version": str(metadata["version"]),
        "description": metadata["description"],
        "domain": metadata.get("domain"),
        "subdomain": metadata.get("subdomain"),
        "author": metadata.get("author"),
        "license": metadata.get("license"),
        "tags": metadata.get("tags", []),
        "frameworks": metadata.get("frameworks", {}),
        "modules": {
            "references": markdown_files("references"),
            "mappings": markdown_files("mappings"),
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
        },
    }


def main() -> None:
    index_path = SKILL_ROOT / "index.json"
    index_path.write_text(
        json.dumps(build_index(), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {index_path.relative_to(SKILL_ROOT)}")


if __name__ == "__main__":
    main()
