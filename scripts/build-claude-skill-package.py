#!/usr/bin/env python3
"""Build the downloadable native Claude Skill package for Conductor."""
from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_NAME = "mc-conductor"
ZIP_TIMESTAMP = (2026, 1, 1, 0, 0, 0)
SOURCE_SKILL = Path("packages/claude-skill/mc-conductor/SKILL.md")
DIST_DIR = Path("dist")
DIST_SKILL_DIR = DIST_DIR / "claude-skill" / PACKAGE_NAME
DIST_ZIP = DIST_DIR / "mc-conductor-claude-skill.zip"

SKILL_FILES = (
    Path("skills/1-morning-brief/SKILL.md"),
    Path("skills/2-evening-hot-take/SKILL.md"),
    Path("skills/3-friday-pattern-read/SKILL.md"),
    Path("skills/4-sunday-reflection/SKILL.md"),
    Path("skills/5-monthly-review/SKILL.md"),
    Path("skills/6-quarterly-positioning/SKILL.md"),
    Path("skills/7-exec-review/SKILL.md"),
    Path("skills/8-coaching-diagnostic/SKILL.md"),
    Path("skills/9-one-on-one/SKILL.md"),
    Path("skills/10-leader-pen/SKILL.md"),
    Path("skills/11-leader-edit/SKILL.md"),
)

REFERENCE_FILES = (
    Path("README.md"),
    Path("QUICKSTART.md"),
    Path("INSTALL.md"),
    Path("UPDATE.md"),
    Path("CHANGELOG.md"),
    Path("LICENSE"),
    Path("docs/onboarding.md"),
    Path("docs/sample-conductor-profile.md"),
    Path("docs/skill-index.md"),
    Path("docs/customization.md"),
    Path("docs/cadence-examples.md"),
    Path("docs/brand.md"),
)


def copy_file(project_root: Path, src_rel: Path, dest_root: Path, dest_rel: Path) -> None:
    src = project_root / src_rel
    if not src.exists():
        raise FileNotFoundError(src_rel)
    dest = dest_root / dest_rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def build_tree(project_root: Path, output_dir: Path) -> Path:
    package_dir = output_dir / PACKAGE_NAME
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir(parents=True)

    copy_file(project_root, SOURCE_SKILL, package_dir, Path("SKILL.md"))

    for skill_file in SKILL_FILES:
        copy_file(project_root, skill_file, package_dir / "references", skill_file)

    for reference_file in REFERENCE_FILES:
        copy_file(project_root, reference_file, package_dir / "references", reference_file)

    return package_dir


def iter_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if path.is_file())


def write_zip(package_dir: Path, zip_path: Path) -> None:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in iter_files(package_dir):
            arcname = path.relative_to(package_dir.parent).as_posix()
            info = zipfile.ZipInfo(arcname, ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, path.read_bytes())


def build(project_root: Path, output_dir: Path, zip_path: Path) -> None:
    package_dir = build_tree(project_root, output_dir)
    write_zip(package_dir, zip_path)


def compare_trees(expected_root: Path, actual_root: Path) -> list[str]:
    failures: list[str] = []
    expected_files = {path.relative_to(expected_root) for path in iter_files(expected_root)}
    actual_files = {path.relative_to(actual_root) for path in iter_files(actual_root)}

    for missing in sorted(expected_files - actual_files):
        failures.append(f"missing package file: {missing}")
    for extra in sorted(actual_files - expected_files):
        failures.append(f"unexpected package file: {extra}")
    for rel_path in sorted(expected_files & actual_files):
        if not filecmp.cmp(expected_root / rel_path, actual_root / rel_path, shallow=False):
            failures.append(f"stale package file: {rel_path}")
    return failures


def check(project_root: Path) -> list[str]:
    failures: list[str] = []
    actual_package_dir = project_root / DIST_SKILL_DIR
    actual_zip = project_root / DIST_ZIP

    if not actual_package_dir.exists():
        failures.append(f"missing packaged skill folder: {DIST_SKILL_DIR}")
    if not actual_zip.exists():
        failures.append(f"missing downloadable package: {DIST_ZIP}")
    if failures:
        return failures

    with tempfile.TemporaryDirectory() as tmp:
        tmp_root = Path(tmp)
        expected_dist = tmp_root / "dist" / "claude-skill"
        expected_zip = tmp_root / "mc-conductor-claude-skill.zip"
        build(project_root, expected_dist, expected_zip)
        expected_package_dir = expected_dist / PACKAGE_NAME
        failures.extend(compare_trees(expected_package_dir, actual_package_dir))
        if expected_zip.read_bytes() != actual_zip.read_bytes():
            failures.append(f"stale downloadable package: {DIST_ZIP}")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=str(PROJECT_ROOT))
    parser.add_argument("--check", action="store_true", help="verify dist package is current")
    args = parser.parse_args()

    project_root = Path(args.project_root)
    if args.check:
        failures = check(project_root)
        if failures:
            print("Claude Skill package check failed:", file=sys.stderr)
            for failure in failures:
                print(f"  - {failure}", file=sys.stderr)
            return 1
        print("✓ Claude Skill package is current")
        return 0

    build(project_root, project_root / DIST_SKILL_DIR.parent, project_root / DIST_ZIP)
    print(f"Built {DIST_ZIP}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
