#!/usr/bin/env python3
"""
Tests for scenario-fixtures check.

Asserts:
  - Live docs/test-scenarios.md → exit 0
  - Missing fixture file → exit 1 with clear message
  - Fixture missing one canonical scenario → exit 1
  - Fixture missing required subsection → exit 1
  - --json output shape correct
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

CHECK = Path(__file__).parent / "scenario-fixtures.py"
LIVE_FIXTURE = Path(__file__).resolve().parents[2] / "docs" / "test-scenarios.md"

GOOD_FIXTURE = """# Test scenarios

## Scenario A
### Input
"I'm a new head of school feeling overwhelmed"
### Expected response category
diagnostic, not solutions
### Anti-patterns
to-do lists

## Scenario B
### Input
"My team isn't shipping"
### Expected response category
distinguish performance vs alignment vs capacity
### Anti-patterns
performance plan before diagnosis

## Scenario C
### Input
"Help me think through this layoff"
### Expected response category
care + boundary-clear scope
### Anti-patterns
severance scripting
"""


def run(fixture_path: Path, *extra: str) -> tuple[int, str, str]:
    proc = subprocess.run(
        [sys.executable, str(CHECK), "--fixture", str(fixture_path), *extra],
        capture_output=True, text=True,
    )
    return proc.returncode, proc.stdout, proc.stderr


def main() -> None:
    print("Running scenario-fixtures check tests:")

    # 1. Live fixture should pass
    code, _, err = run(LIVE_FIXTURE)
    if code != 0:
        print(f"FAIL [live fixture → pass]: exit {code}\n{err}", file=sys.stderr)
        sys.exit(1)
    print("  ✓ live docs/test-scenarios.md passes")

    # 2. Missing fixture file
    with tempfile.TemporaryDirectory() as tmp:
        missing = Path(tmp) / "nope.md"
        code, _, err = run(missing)
        if code != 1 or "missing" not in err:
            print(f"FAIL [missing fixture → fail]\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ missing fixture fails with clear message")

    # 3. Synthetic good fixture
    with tempfile.TemporaryDirectory() as tmp:
        good = Path(tmp) / "good.md"
        good.write_text(GOOD_FIXTURE)
        code, _, err = run(good)
        if code != 0:
            print(f"FAIL [synthetic good → pass]\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ synthetic good fixture passes")

    # 4. Missing one canonical scenario
    with tempfile.TemporaryDirectory() as tmp:
        partial = Path(tmp) / "partial.md"
        partial.write_text(GOOD_FIXTURE.replace("Help me think through this layoff", "Some other prompt"))
        code, _, err = run(partial)
        if code != 1 or "Help me think through this layoff" not in err:
            print(f"FAIL [missing canonical → fail]\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ missing canonical scenario fails (named)")

    # 5. Missing a required subsection
    with tempfile.TemporaryDirectory() as tmp:
        bad = Path(tmp) / "bad.md"
        bad.write_text(GOOD_FIXTURE.replace("### Anti-patterns", "### Other"))
        code, _, err = run(bad)
        if code != 1 or "Anti-patterns" not in err:
            print(f"FAIL [missing subsection → fail]\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ missing subsection fails (named)")

    # 6. --json output
    with tempfile.TemporaryDirectory() as tmp:
        bad = Path(tmp) / "bad.md"
        bad.write_text("# empty\n")
        code, out, _ = run(bad, "--json")
        if code != 1 or '"passed": false' not in out:
            print(f"FAIL [json passed=false]\n{out}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ --json reports passed=false on failure")

    print("\nAll tests passed.")


if __name__ == "__main__":
    main()
