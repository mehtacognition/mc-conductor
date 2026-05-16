# Conductor — MC Leadership OS Bundle

A bundle of 11 single-file portable AI skills for leaders. Portable leadership-rhythm bundle that can grow into a fuller MehtaCognition setup engagement. Repo: `mehtacognition/mc-conductor`.

This is a **prompt-only project** — no code build. Verification tests prompt structural integrity, not code correctness.

## Layout

```
mc-conductor/
├── README.md                          # Conductor narrative + onboarding + install instructions
├── INSTALL.md                        # Non-technical install path, including native Claude Skill ZIP
├── QUICKSTART.md                      # First-hour install and update path
├── UPDATE.md                          # Updating installed skills without overwriting private context
├── CONTRIBUTING.md                    # Contribution and anonymization guidance
├── CHANGELOG.md                       # Release notes and update guidance
├── CLAUDE.md                          # This file (verification + project rules)
├── skills/                            # 11 single-file portable skills
│   ├── 1-morning-brief/SKILL.md       # cadence — daily AM
│   ├── 2-evening-hot-take/SKILL.md    # cadence — daily PM
│   ├── 3-friday-pattern-read/SKILL.md # cadence — weekly
│   ├── 4-sunday-reflection/SKILL.md   # cadence — weekly
│   ├── 5-monthly-review/SKILL.md      # cadence — monthly
│   ├── 6-quarterly-positioning/SKILL.md # cadence — quarterly
│   ├── 7-exec-review/SKILL.md         # personalization — generates leader's review skill
│   ├── 8-coaching-diagnostic/SKILL.md # personalization — MC diagnostic
│   ├── 9-one-on-one/SKILL.md          # personalization — Klein-adapted weekly 1:1
│   ├── 10-leader-pen/SKILL.md         # voice — write in leader's voice
│   └── 11-leader-edit/SKILL.md        # voice — edit in leader's voice
├── docs/
│   ├── onboarding.md                  # Conductor Profile setup interview + template
│   ├── sample-conductor-profile.md    # Anonymized sample profile
│   ├── skill-index.md                 # Skill matrix and customization notes
│   ├── customization.md               # Local profile and update workflow
│   ├── cadence-examples.md            # Anonymized cadence examples
│   ├── brand.md                       # Conductor brand spec
│   └── test-scenarios.md              # Coaching Diagnostic scenario fixtures
├── packages/claude-skill/             # Source for native Claude Skill package
├── scripts/build-claude-skill-package.py  # Builds and checks downloadable Skill ZIP
├── dist/                              # Generated downloadable package committed for release convenience
└── .claude/checks/                    # Skillified verification checks
    ├── prompt-schema.py               # Asserts coaching diagnostic structural integrity
    └── scenario-fixtures.py           # Asserts test-scenarios.md is intact
```

## Status

**Phase A complete (2026-04-29):**
- Repo renamed from `mc-coaching-skill` to `mc-conductor`
- Restructured to bundle layout (11 skills/ folders)
- Skills #7 (Exec Review), #8 (Coaching Diagnostic), #9 (Weekly 1:1) ported
- README + brand.md written
- Skillify checks updated to point at new SKILL.md paths

**Phase B complete (2026-05-15):**
- Skills #1-6 (cadence skills) added as portable "bring your own sources" skills for C-suite and institutional leaders
- Skills #10-11 (Leader-Pen, Leader-Edit) added as portable voice skills with voice elicitation, drafting, and editing discipline
- Bundle-integrity check added to verify all 11 skills, YAML frontmatter, README coverage, unique positions, native Claude Skill package, and absence of private runtime dependencies

**Phase C complete (2026-05-15):**
- Added anonymized examples for cadence skills
- Added shared onboarding flow with Conductor Profile, Source Map, and Cadence Contract
- Made all 11 skills profile-aware without adding a 12th skill
- Added Quickstart, Skill Index, and Customization docs for cold external users and future repo updates
- Added contributing guidance, changelog, GitHub Actions checks, and anonymized sample Conductor Profile

**Phase D (next):**
- Add a cross-skill consistency pass for handoff language between daily, weekly, monthly, and quarterly rituals

## Verification

Used by `/go` as the criteria for Phase 1 (self-test) and Phase 2 (cold-grader). Each criterion must be testable to PASS / FAIL / UNCERTAIN.

**Always:**
- [ ] All `skills/*/SKILL.md` files parse as valid Markdown with valid YAML frontmatter (`name:`, `description:`, `bundle: mc-conductor`).
- [ ] Native package current: `python3 scripts/build-claude-skill-package.py --check`.
- [ ] Bundle integrity: `python3 .claude/checks/bundle-integrity.py --explain` (asserts all 11 skill files exist, positions are unique, README lists every skill, required public docs exist, each skill includes the Conductor Profile rule, native Claude Skill package is present, and portable skills do not leak private runtime dependencies).
- [ ] No personal data, real client names, or real coaching-session content in committed files (run `python3 ~/.claude/checks/security/pr-personal-data-sweep.py --branch`).
- [ ] `README.md` install instructions list all 11 skills accurately (no orphans, no phantoms) and link `INSTALL.md`, `QUICKSTART.md`, `UPDATE.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `docs/onboarding.md`, `docs/sample-conductor-profile.md`, `docs/skill-index.md`, and `docs/customization.md` as public entrypoints.

**If the change touches the Coaching Diagnostic (skill 8):**
- [ ] Prompt structural integrity: `python3 .claude/checks/prompt-schema.py --explain` (asserts all 19 load-bearing elements still present in `skills/8-coaching-diagnostic/SKILL.md` — modes, Bass Line, forcing questions, hard rules, persona).
- [ ] Scenario fixtures complete: `python3 .claude/checks/scenario-fixtures.py --explain` (asserts `docs/test-scenarios.md` has all three canonical scenarios with required subsections).
- [ ] Run prompt against the standard scenario set in `docs/test-scenarios.md`:
  - "I'm a new head of school feeling overwhelmed" — should produce diagnostic questions, not solutions
  - "My team isn't shipping" — should distinguish performance vs alignment vs capacity issue
  - "Help me think through this layoff" — should respond with care + boundary-clear scope
- [ ] Output structure matches diagnostic schema: identifies (a) presenting issue, (b) deeper pattern, (c) one accountability question, (d) recommended next conversation.
- [ ] Voice matches the MC standard: warm but direct, no consultant-speak, no AI-tells. Run `python3 ~/.claude/checks/writing/pen-voice-lint.py --file <output>` if outputs are saved.

**If the change touches the Weekly 1:1 (skill 9):**
- [ ] Dashboard has all 9 questions in the canonical order (1: state check; 2-9 owned by direct report).
- [ ] MC layer present: Subtraction Test as Q8, push-back patterns from MC Coaching Diagnostic, Conductor rhythm integration in closing.
- [ ] Attribution to Dave Kline (original framework) preserved in YAML `adapted_from` and closing footer.

**If the change touches the Exec Review meta-skill (skill 7):**
- [ ] Meta-prompt below the scissors line is unchanged in structure — leaders should always be able to copy-paste it into any AI tool and get a complete personalized skill back.
- [ ] Six required subsections in the generated skill (Core Principles, Feedback Patterns, Decision-Making Framework, Communication Style, Document Review Checklists, Example Review Comments) all named in the meta-prompt.

**If the change touches a cadence skill (1-6):**
- [ ] Skill is fully self-contained — no dependency on private retrieval tools, personal knowledge stores, local runtime config, background jobs, or automation services. The skill must run as a single-file Claude Project / ChatGPT GPT for any leader.
- [ ] "Bring your own" pattern present anywhere an internal version used private data sources.
- [ ] Conductor Profile rule present: use profile if available, ask only minimum setup questions if not.
- [ ] Closing references to other Conductor skills accurately match the bundle (no references to obsolete skills like "Monday Strategic Pulse" or "Wednesday Mid-Week Check" from the March 2026 vision doc).

**If the change touches a voice skill (10-11):**
- [ ] Leader-Pen remains a drafting tool and includes a first-time voice interview.
- [ ] Leader-Edit remains a revision tool, not a drafting tool.
- [ ] Both skills catch AI-tells, consultant-speak, generic executive prose, and unsupported claims.

**If the change touches the README:**
- [ ] Run `/edit` for voice drift.
- [ ] Run `/ce-doc-review` if the change is more than minor copy editing — README is the front door for the bundle.

**Skillify status (2026-04-26, paths updated 2026-04-29, bundle check added 2026-05-15):**
- ✓ Diagnostic-output-shape check → `.claude/checks/prompt-schema.py` (now reads `skills/8-coaching-diagnostic/SKILL.md`)
- ✓ Scenario-replay deterministic half → `.claude/checks/scenario-fixtures.py` (reads `docs/test-scenarios.md`)
- ✓ Bundle-integrity check → `.claude/checks/bundle-integrity.py` (reads skills, public docs, workflow files, and install entrypoints)
- TODO: LLM-eval layer that actually runs the prompt against scenarios and judges output (separate skill, not a deterministic check)
- TODO: Cross-skill consistency check — validate handoff language and referenced skill names across all 11 files.

## Public-repo discipline

Currently **PRIVATE**. Will go public when Phase B ships (port the remaining 8 skills) and the bundle is ready for leader install. Before flipping to public:
- [ ] Scrub all public files for personally identifying examples — anonymize to patterns such as "a head of school", "a charter network", or "a regional nonprofit".
- [ ] Confirm MIT LICENSE file exists at root
- [ ] Confirm `INSTALL.md`, `QUICKSTART.md`, `UPDATE.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `docs/onboarding.md`, `docs/sample-conductor-profile.md`, `docs/skill-index.md`, and `docs/customization.md` are linked from README and every skill can use the Conductor Profile
- [ ] Confirm `.github/workflows/checks.yml` runs bundle, schema, and scenario checks on PRs
- [ ] Verify no internal infrastructure references leaked through: private retrieval tools, personal knowledge stores, local runtime config, background jobs, automation services, or identifying example fingerprints.
