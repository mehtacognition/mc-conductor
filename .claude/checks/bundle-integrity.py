#!/usr/bin/env python3
"""
Conductor bundle-integrity check.

Asserts that the portable bundle has all 11 skill files, each skill has the
required installable YAML frontmatter, positions are complete and unique, and
portable skills do not leak private runtime dependencies, and required public
documentation stays wired into the install path.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
REQUIRED_DOCS = (
    Path("CONTRIBUTING.md"),
    Path("CHANGELOG.md"),
    Path("QUICKSTART.md"),
    Path("docs/onboarding.md"),
    Path("docs/sample-conductor-profile.md"),
    Path("docs/skill-index.md"),
    Path("docs/customization.md"),
    Path("docs/cadence-examples.md"),
    Path("docs/brand.md"),
    Path(".github/workflows/checks.yml"),
)
REQUIRED_README_LINKS = (
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "QUICKSTART.md",
    "docs/onboarding.md",
    "docs/sample-conductor-profile.md",
    "docs/skill-index.md",
    "docs/customization.md",
    "docs/cadence-examples.md",
)
BLOCKED_PUBLIC_FILES = (
    Path("docs/MC-Leadership-OS-Vision-March2026.md"),
)

EXPECTED_SKILLS = {
    1: ("1-morning-brief", "Morning Brief"),
    2: ("2-evening-hot-take", "Evening Hot Take"),
    3: ("3-friday-pattern-read", "Friday Pattern Read"),
    4: ("4-sunday-reflection", "Sunday Reflection"),
    5: ("5-monthly-review", "Monthly Review"),
    6: ("6-quarterly-positioning", "Quarterly Positioning"),
    7: ("7-exec-review", "Exec Review"),
    8: ("8-coaching-diagnostic", "Coaching Diagnostic"),
    9: ("9-one-on-one", "Weekly 1:1"),
    10: ("10-leader-pen", "Leader-Pen"),
    11: ("11-leader-edit", "Leader-Edit"),
}

REQUIRED_FRONTMATTER = ("name", "description", "bundle", "position")
REQUIRED_SKILL_PHRASES = (
    "## Conductor Profile",
    "If a Conductor Profile is available",
    "ask only the minimum context needed",
)

def blocked_term(*parts: str) -> str:
    return "".join(parts)


PRIVATE_RUNTIME_PATTERNS = (
    blocked_term("~/.config/", "mc-os"),
    blocked_term("launch", "d"),
    blocked_term("na", "vi-config"),
    blocked_term("mcp__", "q", "md"),
    blocked_term("mcp__", "no", "tion"),
    "mcp__claude_ai",
    "mcp__dayone",
    "mcp__readwise",
    "mcp__whatsapp",
    blocked_term("Q", "MD"),
    blocked_term("Limit", "less"),
    blocked_term("No", "tion"),
    blocked_term("NA", "VI"),
)
PRIVATE_EXAMPLE_PATTERNS = (
    blocked_term("Nish", "ant"),
    blocked_term("Jen", "nifer"),
    blocked_term("A", "SB"),
    blocked_term("Green", "vale"),
)
PUBLIC_SURFACE_FILES = (
    Path("README.md"),
    Path("QUICKSTART.md"),
    Path("CONTRIBUTING.md"),
    Path("CHANGELOG.md"),
    Path("CLAUDE.md"),
)
PRIVACY_SCAN_ALLOWLIST = {
    Path(".claude/checks/bundle-integrity.py"): set(PRIVATE_RUNTIME_PATTERNS + PRIVATE_EXAMPLE_PATTERNS),
    Path(".claude/checks/bundle-integrity_test.py"): {
        blocked_term("~/.config/", "mc-os"),
        blocked_term("Jen", "nifer"),
        blocked_term("Green", "vale"),
    },
}


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def collect_privacy_scan_paths(project_root: Path) -> list[Path]:
    paths: set[Path] = set()

    for rel_path in PUBLIC_SURFACE_FILES + REQUIRED_DOCS:
        full_path = project_root / rel_path
        if full_path.exists():
            paths.add(full_path)

    for pattern in (
        "skills/*/SKILL.md",
        "docs/*.md",
        ".github/workflows/*.yml",
        ".github/workflows/*.yaml",
        ".claude/checks/*.py",
    ):
        paths.update(project_root.glob(pattern))

    return sorted(paths, key=lambda path: path.relative_to(project_root).as_posix())


def scan_privacy_leaks(project_root: Path) -> list[str]:
    failures: list[str] = []
    blocked_patterns = PRIVATE_RUNTIME_PATTERNS + PRIVATE_EXAMPLE_PATTERNS

    for path in collect_privacy_scan_paths(project_root):
        rel_path = path.relative_to(project_root)
        text = path.read_text(errors="ignore")
        allowed = PRIVACY_SCAN_ALLOWLIST.get(rel_path, set())
        leaked = [
            pattern
            for pattern in blocked_patterns
            if pattern in text and pattern not in allowed
        ]
        if leaked:
            failures.append(
                f"private/personal reference(s) in {rel_path}: {', '.join(leaked)}"
            )

    return failures


def run_check(project_root: Path) -> tuple[bool, list[str]]:
    skills_dir = project_root / "skills"
    readme_path = project_root / "README.md"
    license_path = project_root / "LICENSE"
    failures: list[str] = []
    seen_positions: set[int] = set()

    for position, (folder, display_name) in EXPECTED_SKILLS.items():
        skill_path = skills_dir / folder / "SKILL.md"
        if not skill_path.exists():
            failures.append(f"missing skill file: skills/{folder}/SKILL.md")
            continue

        text = skill_path.read_text(errors="ignore")
        fm = parse_frontmatter(text)
        if fm is None:
            failures.append(f"missing YAML frontmatter: skills/{folder}/SKILL.md")
            continue

        for key in REQUIRED_FRONTMATTER:
            if key not in fm or not fm[key]:
                failures.append(f"missing frontmatter key '{key}': skills/{folder}/SKILL.md")

        if fm.get("bundle") != "mc-conductor":
            failures.append(f"bundle must be mc-conductor: skills/{folder}/SKILL.md")

        expected_position = f"{position} of 11"
        if fm.get("position") != expected_position:
            failures.append(
                f"position must be '{expected_position}': skills/{folder}/SKILL.md"
            )
        else:
            seen_positions.add(position)

        if display_name not in text:
            failures.append(
                f"display name '{display_name}' not found in body: skills/{folder}/SKILL.md"
            )

        missing_profile_phrases = [
            phrase for phrase in REQUIRED_SKILL_PHRASES if phrase not in text
        ]
        if missing_profile_phrases:
            failures.append(
                f"missing Conductor Profile rule in skills/{folder}/SKILL.md: {', '.join(missing_profile_phrases)}"
            )

    if seen_positions != set(EXPECTED_SKILLS):
        missing = sorted(set(EXPECTED_SKILLS) - seen_positions)
        if missing:
            failures.append(f"missing unique positions: {missing}")

    if not readme_path.exists():
        failures.append("missing README.md")
    else:
        readme = readme_path.read_text(errors="ignore")
        for _position, (_folder, display_name) in EXPECTED_SKILLS.items():
            if display_name not in readme:
                failures.append(f"README.md does not list skill: {display_name}")
        for link in REQUIRED_README_LINKS:
            if link not in readme:
                failures.append(f"README.md missing required link: {link}")

    for doc_path in REQUIRED_DOCS:
        full_doc_path = project_root / doc_path
        if not full_doc_path.exists():
            failures.append(f"missing required public doc: {doc_path}")

    if not license_path.exists():
        failures.append("missing LICENSE")

    for blocked_file in BLOCKED_PUBLIC_FILES:
        full_blocked_file = project_root / blocked_file
        if full_blocked_file.exists():
            failures.append(f"internal-only doc should not ship publicly: {blocked_file}")

    failures.extend(scan_privacy_leaks(project_root))

    return (len(failures) == 0, failures)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=str(PROJECT_ROOT))
    parser.add_argument("--explain", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    passed, failures = run_check(Path(args.project_root))

    if args.json:
        print(json.dumps({
            "passed": passed,
            "failures": failures,
            "project_root": args.project_root,
        }, indent=2))
        return 0 if passed else 1

    if passed:
        if args.explain:
            print("✓ Conductor bundle has all 11 installable skills")
        return 0

    print(f"✗ Bundle integrity failed ({len(failures)} issue(s)):", file=sys.stderr)
    for failure in failures:
        print(f"  - {failure}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
