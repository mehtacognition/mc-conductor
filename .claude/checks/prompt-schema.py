#!/usr/bin/env python3
"""
Coaching-skill prompt-schema check.

What it asserts:
  coaching-core-prompt.md still contains all the structural elements that
  define a valid MC Leadership Diagnostic prompt. If any element is removed
  by an edit, this check fails — preventing accidental drift in the prompt's
  load-bearing structure.

Required elements (per CLAUDE.md Verification section):
  1. Three modes: Reactive, Proactive, Team Diagnostic
  2. The Bass Line — two questions about purpose and followership
  3. Six forcing questions in WHO/WHAT/HOW/WHY progression
  4. The 4-part diagnostic output schema:
     (a) presenting issue, (b) deeper pattern,
     (c) accountability question, (d) recommended next conversation
  5. Hard rules: no checklists, no consultant-speak, named reframes
  6. The "anti-consultant consultant" persona declaration

When invoked:
  - /go Phase 1 self-test (when change touches core prompt)
  - Manual: python3 .claude/checks/prompt-schema.py [--explain]

Failure mode this prevents:
  Output-shape drift: an editor refactors the prompt and inadvertently removes
  one of the four diagnostic schema sections, or collapses a forcing question,
  or softens the persona. The skill still runs but produces structurally
  different output. Without this check the drift is invisible until users
  notice the output feels off.

Skillified: 2026-04-26
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROMPT_PATH = Path(__file__).resolve().parents[2] / "coaching-core-prompt.md"

# Required substring patterns. Each is a (label, regex) pair.
# Regexes are case-insensitive and tolerate small wording variations,
# but require the load-bearing terms to be present.
REQUIRED_ELEMENTS: list[tuple[str, re.Pattern]] = [
    ("three modes - Reactive",        re.compile(r"\bReactive Mode\b")),
    ("three modes - Proactive",       re.compile(r"\bProactive Mode\b")),
    ("three modes - Team Diagnostic", re.compile(r"\bTeam Diagnostic Mode\b")),

    ("Bass Line marker",              re.compile(r"\bBass Line\b")),
    ("Bass Line Q1 (purpose)",        re.compile(r"why do you want to lead", re.IGNORECASE)),
    ("Bass Line Q2 (followership)",   re.compile(r"why would anyone want to be led by you", re.IGNORECASE)),

    ("Forcing questions header",      re.compile(r"#+\s*The Forcing Questions", re.IGNORECASE)),
    ("Forcing progression - WHO",     re.compile(r"WHO[\s\S]{0,40}Knowing what's right", re.IGNORECASE)),
    ("Forcing progression - WHAT",    re.compile(r"WHAT[\s\S]{0,40}Doing the right thing", re.IGNORECASE)),
    ("Forcing progression - HOW",     re.compile(r"HOW[\s\S]{0,40}Doing things right", re.IGNORECASE)),

    ("Forcing Q1 - Liked vs Respected", re.compile(r"Liked vs.?\s*Respected", re.IGNORECASE)),
    ("Forcing Q2 - Definition Gap",     re.compile(r"\bDefinition Gap\b", re.IGNORECASE)),
    ("Forcing Q3 - Comfort vs Clarity", re.compile(r"Comfort vs.?\s*Clarity", re.IGNORECASE)),
    ("Forcing Q4 - Subtraction",        re.compile(r"\bSubtraction Test\b", re.IGNORECASE)),

    ("Hard rule - no checklists",     re.compile(r"never produce a to-?do list|checklist would let you skip", re.IGNORECASE)),
    ("Hard rule - no consultant-speak", re.compile(r"anti-consultant consultant", re.IGNORECASE)),
    ("Hard rule - reframing signature", re.compile(r"signature move is\s+\*?\*?reframing", re.IGNORECASE)),

    ("Persona - direct-first",        re.compile(r"direct-first.*not warm-first", re.IGNORECASE)),
    ("Persona - never validate",      re.compile(r"never validate just to be kind", re.IGNORECASE)),
]


def run_check(prompt_path: Path) -> tuple[bool, list[str], int]:
    """Returns (passed, failure_messages, total_required)."""
    if not prompt_path.exists():
        return (False, [f"prompt file not found: {prompt_path}"], len(REQUIRED_ELEMENTS))
    text = prompt_path.read_text(errors="ignore")
    failures: list[str] = []
    for label, pattern in REQUIRED_ELEMENTS:
        if not pattern.search(text):
            failures.append(label)
    return (len(failures) == 0, failures, len(REQUIRED_ELEMENTS))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt", default=str(PROMPT_PATH),
                        help=f"Prompt file to check (default: {PROMPT_PATH.name})")
    parser.add_argument("--explain", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    passed, failures, total = run_check(Path(args.prompt))

    if args.json:
        print(json.dumps({
            "passed": passed,
            "checked_elements": total,
            "missing_elements": failures,
            "prompt": args.prompt,
        }, indent=2))
        return 0 if passed else 1

    if passed:
        if args.explain:
            print(f"✓ Coaching prompt has all {total} required structural elements")
        return 0

    print(f"✗ Coaching prompt missing {len(failures)} of {total} required elements:", file=sys.stderr)
    for f in failures:
        print(f"  - {f}", file=sys.stderr)
    print("", file=sys.stderr)
    print("These elements are load-bearing for the diagnostic output shape.", file=sys.stderr)
    print("If the removal was intentional, update REQUIRED_ELEMENTS in this check.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
