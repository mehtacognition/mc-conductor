#!/usr/bin/env python3
"""
Tests for prompt-schema check.

Asserts:
  - Live coaching-core-prompt.md → exit 0 (passes all required elements)
  - A synthetic prompt missing one element → exit 1 (and the missing element is named)
  - --json output reports passed=false on failure
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

CHECK = Path(__file__).parent / "prompt-schema.py"
LIVE_PROMPT = Path(__file__).resolve().parents[2] / "coaching-core-prompt.md"


def run(prompt_path: Path, *extra: str) -> tuple[int, str, str]:
    proc = subprocess.run(
        [sys.executable, str(CHECK), "--prompt", str(prompt_path), *extra],
        capture_output=True, text=True,
    )
    return proc.returncode, proc.stdout, proc.stderr


def main() -> None:
    print("Running prompt-schema check tests:")

    # 1. Live prompt should pass
    code, out, err = run(LIVE_PROMPT)
    if code != 0:
        print(f"FAIL [live prompt → pass]: exit {code}", file=sys.stderr)
        print(err, file=sys.stderr)
        sys.exit(1)
    print("  ✓ live coaching-core-prompt.md passes")

    # 2. Synthetic minimal prompt → should fail
    with tempfile.TemporaryDirectory() as tmp:
        synthetic = Path(tmp) / "minimal.md"
        synthetic.write_text("# Minimal prompt\n\nNot a coaching skill.\n")
        code, out, err = run(synthetic)
        if code != 1:
            print(f"FAIL [synthetic minimal → fail]: exit {code}", file=sys.stderr)
            sys.exit(1)
        if "missing" not in err:
            print(f"FAIL [error message]: expected 'missing' in stderr\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ synthetic minimal prompt fails with element list")

    # 3. JSON output shape
    with tempfile.TemporaryDirectory() as tmp:
        synthetic = Path(tmp) / "minimal.md"
        synthetic.write_text("# Minimal\n")
        code, out, _ = run(synthetic, "--json")
        if code != 1 or '"passed": false' not in out:
            print(f"FAIL [json output]: missing 'passed: false'\n{out}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ --json reports passed=false on failure")

    # 4. Live prompt with --json should report passed=true
    code, out, _ = run(LIVE_PROMPT, "--json")
    if code != 0 or '"passed": true' not in out:
        print(f"FAIL [json on live]: expected 'passed: true'\n{out}", file=sys.stderr)
        sys.exit(1)
    print("  ✓ --json reports passed=true on live prompt")

    # 5. Missing prompt file → exit 1 with clear message
    with tempfile.TemporaryDirectory() as tmp:
        nonexistent = Path(tmp) / "nope.md"
        code, _, err = run(nonexistent)
        if code != 1 or "not found" not in err:
            print(f"FAIL [missing prompt]: expected 'not found' in stderr\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ missing prompt file fails with clear message")

    print("\nAll tests passed.")


if __name__ == "__main__":
    main()
