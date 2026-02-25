#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"


# Required sections for each skill type.
EXECUTION_REQUIRED_HEADINGS = [
    "Purpose",
    "When to Use",
    "When NOT to Use",
    "Inputs Required",
    "Output Format",
    "Procedure",
    "Guardrails",
    "Failure Patterns",
    "Example 1",
    "Example 2",
]

SYSTEM_REQUIRED_HEADINGS = [
    "Purpose",
    "Scope",
    "Inputs / Signals",
    "Core Behavior",
    "Output / Side Effects",
    "Guardrails",
    "Failure Patterns",
    "Example 1",
    "Example 2",
]


TYPE_EXECUTION_PAT = re.compile(r"\*\*Type:\*\*\s*Execution\b", re.IGNORECASE)
TYPE_SYSTEM_PAT = re.compile(r"\*\*Type:\*\*\s*System\b", re.IGNORECASE)

# Match markdown headings like: "# Title", "## Purpose", "### 1) Detection"
HEADING_PAT = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


def is_template_file(path: Path) -> bool:
    # Ignore templates (they will intentionally have placeholders).
    return "_template" in path.parts


def is_readme_file(path: Path) -> bool:
    return path.name.lower() == "readme.md"


def is_subskill_file(path: Path) -> bool:
    return "subskills" in path.parts


def is_markdown_file(path: Path) -> bool:
    return path.suffix.lower() in {".md", ".markdown"}


def normalize_heading(text: str) -> str:
    # Normalize heading text for matching. Keep it simple and deterministic.
    t = text.strip()
    t = re.sub(r"\s+", " ", t)
    # Drop trailing punctuation for robustness.
    t = t.rstrip(":")
    return t


def extract_headings(md: str) -> List[str]:
    headings = []
    for _, title in HEADING_PAT.findall(md):
        headings.append(normalize_heading(title))
    return headings


def find_examples_present(headings: List[str]) -> Tuple[bool, bool]:
    # Accept headings like:
    # "Example 1 (Minimal Context)", "Example 2 (Realistic Scenario)", etc.
    ex1 = any(h.lower().startswith("example 1") for h in headings)
    ex2 = any(h.lower().startswith("example 2") for h in headings)
    return ex1, ex2


def validate_skill_file(path: Path) -> List[str]:
    errors: List[str] = []

    md = path.read_text(encoding="utf-8", errors="replace")
    headings = extract_headings(md)
    headings_lower = [h.lower() for h in headings]

    is_execution = bool(TYPE_EXECUTION_PAT.search(md))
    is_system = bool(TYPE_SYSTEM_PAT.search(md))

    if is_execution and is_system:
        errors.append(
            "Both **Type:** Execution and **Type:** System detected. Choose one."
        )
        return errors

    if not is_execution and not is_system:
        errors.append(
            'Missing skill type. Add either "**Type:** Execution" or "**Type:** System".'
        )
        return errors

    if is_execution:
        required = EXECUTION_REQUIRED_HEADINGS
    else:
        required = SYSTEM_REQUIRED_HEADINGS

    # Validate required headings
    for req in required:
        req_l = req.lower()
        if req_l in {"example 1", "example 2"}:
            # examples validated separately to allow suffixes
            continue
        if req_l not in headings_lower:
            errors.append(f'Missing required section heading: "{req}"')

    # Validate examples
    ex1, ex2 = find_examples_present(headings)
    if not ex1:
        errors.append(
            'Missing "Example 1" section (heading must start with "Example 1")'
        )
    if not ex2:
        errors.append(
            'Missing "Example 2" section (heading must start with "Example 2")'
        )

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print(f"ERROR: skills directory not found at {SKILLS_DIR}")
        return 2

    md_files = [
        p
        for p in SKILLS_DIR.rglob("*")
        if p.is_file()
        and is_markdown_file(p)
        and not is_template_file(p)
        and not is_readme_file(p)
        and not is_subskill_file(p)
    ]

    # Nothing to validate is okay (early stage repo).
    if not md_files:
        print(
            "No skill markdown files found (excluding templates). Nothing to validate."
        )
        return 0

    failed: List[Tuple[Path, List[str]]] = []
    for p in sorted(md_files):
        errs = validate_skill_file(p)
        if errs:
            failed.append((p, errs))

    if failed:
        print("Skill validation failed.\n")
        for path, errs in failed:
            rel = path.relative_to(REPO_ROOT)
            print(f"- {rel}")
            for e in errs:
                print(f"  - {e}")
            print()
        print("Fix the issues above to pass CI.")
        return 1

    print(f"Skill validation passed ({len(md_files)} file(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
