#!/usr/bin/env python3
"""
Coaching-skill scenario-fixtures check.

What it asserts:
  docs/test-scenarios.md exists and contains all three required scenarios
  with the mandated subsections (Input, Expected response category,
  Anti-patterns). Each scenario's Input matches the canonical phrasing
  named in CLAUDE.md Verification.

When invoked:
  - /go Phase 1 self-test (when change touches core prompt)
  - Manual: python3 .claude/checks/scenario-fixtures.py [--explain]

Failure mode this prevents:
  Scenario drift: the test-scenarios fixture file gets out of sync with the
  Verification section, OR the file is silently deleted / its scenarios
  renamed, leaving /go without the contract it's supposed to enforce.

  This check covers the deterministic half of "scenario replay." The LLM-eval
  half (run the prompt against each scenario, judge output) is a separate
  layer and lives outside this check.

Skillified: 2026-04-26
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
FIXTURE_PATH = PROJECT_ROOT / "docs" / "test-scenarios.md"

# Canonical scenario inputs (verbatim from CLAUDE.md Verification section).
# The fixture must contain each input exactly so /go has a stable contract.
REQUIRED_SCENARIO_INPUTS: list[str] = [
    "I'm a new head of school feeling overwhelmed",
    "My team isn't shipping",
    "Help me think through this layoff",
]

REQUIRED_SUBSECTIONS: list[str] = [
    "Input",
    "Expected response category",
    "Anti-patterns",
]


def run_check(fixture_path: Path) -> tuple[bool, list[str]]:
    if not fixture_path.exists():
        return (False, [
            f"fixture file missing: {fixture_path}",
            "Action: create docs/test-scenarios.md with the three named scenarios "
            "per CLAUDE.md Verification section.",
        ])

    text = fixture_path.read_text(errors="ignore")
    failures: list[str] = []

    # Each canonical input must appear somewhere
    for canonical in REQUIRED_SCENARIO_INPUTS:
        if canonical not in text:
            failures.append(
                f"missing canonical scenario input: \"{canonical}\""
            )

    # Each required subsection must appear at least N=3 times (one per scenario).
    # Tolerate variation: ### or #### markers and trailing whitespace/colon.
    for subsection in REQUIRED_SUBSECTIONS:
        # Count headings whose text contains the required subsection name
        pattern = re.compile(
            rf"^#{{2,4}}\s+{re.escape(subsection)}\b", re.MULTILINE | re.IGNORECASE,
        )
        n = len(pattern.findall(text))
        if n < len(REQUIRED_SCENARIO_INPUTS):
            failures.append(
                f"subsection '{subsection}' present {n} times, "
                f"expected ≥ {len(REQUIRED_SCENARIO_INPUTS)} (one per scenario)"
            )

    return (len(failures) == 0, failures)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", default=str(FIXTURE_PATH),
                        help=f"Fixture path (default: {FIXTURE_PATH})")
    parser.add_argument("--explain", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    passed, failures = run_check(Path(args.fixture))

    if args.json:
        print(json.dumps({
            "passed": passed,
            "fixture": args.fixture,
            "failures": failures,
        }, indent=2))
        return 0 if passed else 1

    if passed:
        if args.explain:
            print(f"✓ Scenario fixtures complete ({len(REQUIRED_SCENARIO_INPUTS)} scenarios, "
                  f"{len(REQUIRED_SUBSECTIONS)} required subsections each)")
        return 0

    print(f"✗ Scenario fixtures incomplete ({len(failures)} issue(s)):", file=sys.stderr)
    for f in failures:
        print(f"  - {f}", file=sys.stderr)
    print("", file=sys.stderr)
    print("Reference: docs/test-scenarios.md template + CLAUDE.md Verification section.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
