# Changelog

All notable changes to Conductor will be tracked here.

The repo can change after a leader installs the skills into Claude, ChatGPT, Gemini, or another AI tool. Installed copies do not update automatically. When a release changes a skill you use, replace the installed skill instructions manually and keep your local Conductor Profile.

## Unreleased

No released changes yet.

## 0.1.0 - 2026-05-16

Initial public bundle release candidate for Conductor.

### Added

- Full 11-skill Conductor bundle: cadence, personalization, and voice skills.
- Shared Conductor Profile, Source Map, and Cadence Contract onboarding model.
- Exec Review profile-deepening path with reusable Leader Review Profile.
- Quickstart, skill index, customization guide, and anonymized sample Conductor Profile.
- Bundle integrity checks for installable skills, required docs, README links, public-surface privacy scanning, and private runtime references.
- GitHub Actions workflow for pull-request verification.

### Changed

- Public docs now recommend keeping private leader context in `local/` and updating installed skills manually when repo improvements land.
- Install docs now use Claude Projects, GPTs, or pasted prompts; zipped native Claude Skill packages are not shipped yet.

### Removed

- Internal-only leadership OS vision document from the public bundle surface.
