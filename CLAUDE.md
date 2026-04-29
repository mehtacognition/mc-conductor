# Conductor — MC Leadership OS Bundle

A bundle of 11 single-file portable AI skills for leaders. Phase 0 of NAVI productization (free demo bundle that funnels into the full setup engagement). Repo: `mehtacognition/mc-conductor`.

This is a **prompt-only project** — no code build. Verification tests prompt structural integrity, not code correctness.

## Layout

```
mc-conductor/
├── README.md                          # Conductor narrative + install instructions
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
│   ├── brand.md                       # Conductor brand spec
│   ├── MC-Leadership-OS-Vision-March2026.md  # Historical vision doc (March 2026)
│   └── test-scenarios.md              # Coaching Diagnostic scenario fixtures
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

**Phase B (next):**
- Port skills #1-6 (cadence skills) from `~/.config/mc-os/skills/` — strip Nishant-specific data sources, replace with "bring your own" patterns
- Port skills #10-11 (Leader-Pen, Leader-Edit) from `~/.claude/commands/pen.md`, `edit.md` — convert from slash commands to single-file portable skills, add voice-elicitation interview

## Verification

Used by `/go` as the criteria for Phase 1 (self-test) and Phase 2 (cold-grader). Each criterion must be testable to PASS / FAIL / UNCERTAIN.

**Always:**
- [ ] All `skills/*/SKILL.md` files parse as valid Markdown with valid YAML frontmatter (`name:`, `description:`, `bundle: mc-conductor`).
- [ ] No personal data, real client names, or real coaching-session content in committed files (run `python3 ~/.claude/checks/security/pr-personal-data-sweep.py --branch`).
- [ ] `README.md` install instructions list all 11 skills accurately (no orphans, no phantoms).

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
- [ ] Skill is fully self-contained — no dependency on Nishant's QMD, Limitless, Notion, `~/.config/mc-os/context.json`, or launchd. The skill must run as a single-file Claude Project / ChatGPT GPT for any leader.
- [ ] "Bring your own" pattern present where Nishant's NAVI version reads from his data sources.
- [ ] Closing references to other Conductor skills accurately match the bundle (no references to obsolete skills like "Monday Strategic Pulse" or "Wednesday Mid-Week Check" from the March 2026 vision doc).

**If the change touches the README:**
- [ ] Run `/edit` for voice drift.
- [ ] Run `/ce-doc-review` if the change is more than minor copy editing — README is the front door for the bundle.

**Skillify status (2026-04-26, paths updated 2026-04-29):**
- ✓ Diagnostic-output-shape check → `.claude/checks/prompt-schema.py` (now reads `skills/8-coaching-diagnostic/SKILL.md`)
- ✓ Scenario-replay deterministic half → `.claude/checks/scenario-fixtures.py` (reads `docs/test-scenarios.md`)
- TODO: LLM-eval layer that actually runs the prompt against scenarios and judges output (separate skill, not a deterministic check)
- TODO: Cross-skill consistency check — all 11 SKILL.md files have valid YAML frontmatter, `bundle: mc-conductor`, and no broken cross-references.

## Public-repo discipline

Currently **PRIVATE**. Will go public when Phase B ships (port the remaining 8 skills) and the bundle is ready for leader install. Before flipping to public:
- [ ] Scrub all SKILL.md files for any personally identifying examples ("Jennifer", "ASB", "Greenvale" — anonymize to "a head of school", "a charter network", etc.)
- [ ] Confirm MIT LICENSE file exists at root
- [ ] Verify no NAVI-internal infrastructure references leaked through (no QMD paths, no Limitless paths, no `~/.config/mc-os/`, no launchd plists)
