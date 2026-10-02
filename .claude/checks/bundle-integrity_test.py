#!/usr/bin/env python3
"""
Tests for bundle-integrity check.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CHECK = Path(__file__).parent / "bundle-integrity.py"
PROJECT_ROOT = Path(__file__).resolve().parents[2]


def blocked_term(*parts: str) -> str:
    return "".join(parts)


def run(project_root: Path, *extra: str) -> tuple[int, str, str]:
    proc = subprocess.run(
        [sys.executable, str(CHECK), "--project-root", str(project_root), *extra],
        capture_output=True,
        text=True,
    )
    return proc.returncode, proc.stdout, proc.stderr


def main() -> None:
    print("Running bundle-integrity check tests:")

    code, _out, err = run(PROJECT_ROOT)
    if code != 0:
        print(f"FAIL [live bundle -> pass]: exit {code}\n{err}", file=sys.stderr)
        sys.exit(1)
    print("  ✓ live bundle passes")

    code, out, _err = run(PROJECT_ROOT, "--json")
    if code != 0 or '"passed": true' not in out:
        print(f"FAIL [json live -> passed true]\n{out}", file=sys.stderr)
        sys.exit(1)
    print("  ✓ --json reports passed=true on live bundle")

    with tempfile.TemporaryDirectory() as tmp:
        temp_root = Path(tmp) / "mc-conductor"
        shutil.copytree(PROJECT_ROOT, temp_root, ignore=shutil.ignore_patterns(".git"))
        (temp_root / "skills" / "1-morning-brief" / "SKILL.md").unlink()
        code, _out, err = run(temp_root)
        if code != 1 or "missing skill file" not in err:
            print(f"FAIL [missing skill -> fail]\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ missing skill fails")


    with tempfile.TemporaryDirectory() as tmp:
        temp_root = Path(tmp) / "mc-conductor"
        shutil.copytree(PROJECT_ROOT, temp_root, ignore=shutil.ignore_patterns(".git"))
        (temp_root / "docs" / "onboarding.md").unlink()
        code, _out, err = run(temp_root)
        if code != 1 or "missing required public doc" not in err:
            print(f"FAIL [missing onboarding doc -> fail]\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ missing onboarding doc fails")

    with tempfile.TemporaryDirectory() as tmp:
        temp_root = Path(tmp) / "mc-conductor"
        shutil.copytree(PROJECT_ROOT, temp_root, ignore=shutil.ignore_patterns(".git"))
        skill = temp_root / "skills" / "3-friday-pattern-read" / "SKILL.md"
        skill.write_text(skill.read_text().replace("## Conductor Profile", "## Setup Context", 1))
        code, _out, err = run(temp_root)
        if code != 1 or "missing Conductor Profile rule" not in err:
            print(f"FAIL [missing profile rule -> fail]\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ missing Conductor Profile rule fails")

    with tempfile.TemporaryDirectory() as tmp:
        temp_root = Path(tmp) / "mc-conductor"
        shutil.copytree(PROJECT_ROOT, temp_root, ignore=shutil.ignore_patterns(".git"))
        skill = temp_root / "skills" / "2-evening-hot-take" / "SKILL.md"
        skill.write_text(
            skill.read_text() + f"\nPrivate leak: {blocked_term('~/.config/', 'mc-os')}\n"
        )
        code, _out, err = run(temp_root)
        if code != 1 or "private/personal reference" not in err:
            print(f"FAIL [private reference -> fail]\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ private runtime references fail")


    with tempfile.TemporaryDirectory() as tmp:
        temp_root = Path(tmp) / "mc-conductor"
        shutil.copytree(PROJECT_ROOT, temp_root, ignore=shutil.ignore_patterns(".git"))
        (temp_root / "dist" / "mc-conductor-claude-skill.zip").unlink()
        code, _out, err = run(temp_root)
        if code != 1 or "downloadable native Claude Skill ZIP" not in err:
            print(f"FAIL [missing native package -> fail]\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ missing native package fails")

    with tempfile.TemporaryDirectory() as tmp:
        temp_root = Path(tmp) / "mc-conductor"
        shutil.copytree(PROJECT_ROOT, temp_root, ignore=shutil.ignore_patterns(".git"))
        package_skill = temp_root / "dist" / "claude-skill" / "mc-conductor" / "SKILL.md"
        package_skill.write_text(package_skill.read_text() + "\nStale local package copy.\n")
        code, _out, err = run(temp_root)
        if code != 1 or "built native Claude Skill source is stale" not in err:
            print(f"FAIL [stale native package folder -> fail]\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ stale native package folder fails")

    with tempfile.TemporaryDirectory() as tmp:
        temp_root = Path(tmp) / "mc-conductor"
        shutil.copytree(PROJECT_ROOT, temp_root, ignore=shutil.ignore_patterns(".git"))
        readme = temp_root / "README.md"
        example_person = blocked_term("Jen", "nifer")
        example_place = blocked_term("Green", "vale")
        readme.write_text(
            readme.read_text() + f"\nExample leak: {example_person} at {example_place}.\n"
        )
        code, _out, err = run(temp_root)
        if code != 1 or "README.md" not in err or example_person not in err:
            print(f"FAIL [public doc privacy reference -> fail]\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ public docs are privacy-scanned")

    with tempfile.TemporaryDirectory() as tmp:
        temp_root = Path(tmp) / "mc-conductor"
        shutil.copytree(PROJECT_ROOT, temp_root, ignore=shutil.ignore_patterns(".git"))
        policy = temp_root / "docs" / "conductor-privacy-notice.md"
        original = policy.read_text()
        approved = (
            "Messages to contact@mehtacognition.com are received by "
            + blocked_term("Nish", "ant")
            + " Mehta and Allen Broyles through Google Workspace. "
            "We receive your contact details and whatever information you choose to share, "
            "and use support messages only to respond to and resolve support inquiries. "
            "Please avoid sending confidential student, personnel or client records."
        )
        policy.write_text("# Privacy notice\n\n" + approved + "\n\n## Updates\n")
        code, _out, err = run(temp_root)
        if code != 0:
            print(f"FAIL [exact approved support paragraph -> pass]\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ exact approved support paragraph passes in policy file")

        cases = (
            ("altered disclosure", original.replace("only to respond", "also to respond", 1)),
            ("extra personal name", original + "\n" + blocked_term("Nish", "ant") + "\n"),
            ("other private name", original + "\n" + blocked_term("Jen", "nifer") + "\n"),
            ("duplicate disclosure", original + "\n" + approved + "\n\n"),
            ("private runtime reference", original + "\n" + blocked_term("~/.config/", "mc-os") + "\n"),
            ("paragraph boundary changed", original.replace("\n\n" + approved, "\n" + approved, 1)),
        )
        for label, content in cases:
            policy.write_text(content)
            code, _out, err = run(temp_root)
            if code != 1 or "private/personal reference" not in err or str(policy.relative_to(temp_root)) not in err:
                print(f"FAIL [{label} -> privacy failure]\n{err}", file=sys.stderr)
                sys.exit(1)
            print(f"  ✓ {label} still fails")

        policy.write_text(original)
        (temp_root / "docs" / "unapproved-support-copy.md").write_text("# Copy\n\n" + approved + "\n\n")
        code, _out, err = run(temp_root)
        if code != 1 or "unapproved-support-copy.md" not in err:
            print(f"FAIL [approved text in another file -> fail]\n{err}", file=sys.stderr)
            sys.exit(1)
        print("  ✓ approved text in another file remains blocked")

    print("\nAll tests passed.")


if __name__ == "__main__":
    main()
