# Conductor Skill Index

This index helps operators decide which skill to install, what to bring, what output to expect, and how each skill connects to the rest of the bundle.

## Categories

- **Cadence:** recurring rituals that create strategic rhythm.
- **Diagnose and Decide:** episodic tools that turn signal into judgment.
- **Extend Judgment:** tools that help the team work through the leader's lens.
- **Voice:** tools for writing and editing in the leader's voice.

## Skill Matrix

| # | Skill | Category | Use when | Core input | Output | Feeds into | Customization notes |
|---|---|---|---|---|---|---|---|
| 1 | Morning Brief | Cadence | Starting a workday | Calendar, meeting prep, current priorities, open loops | Daily executive orientation | Evening Hot Take, Friday Pattern Read | Customize source map and stakeholder names. Keep evidence protocol. |
| 2 | Evening Hot Take | Cadence | Closing a workday | Day notes, meetings, sent messages, observations | Daily pattern read and strategic framing candidates | Friday Pattern Read, writing tasks | Customize communication formats. Keep concise output shape. |
| 3 | Friday Pattern Read | Cadence | End of week | Daily outputs, calendar, commitments, notes | Weekly pattern synthesis | Sunday Reflection, Monthly Review | Customize what counts as a meaningful pattern. Keep cascade logic. |
| 4 | Sunday Reflection | Cadence | Weekly meaning-making | Friday Pattern Read, week notes, next week calendar | Reflection, synthesis, next-week question | Morning Brief, Monthly Review | Customize directness and reflection emphasis. Keep evidence grounding. |
| 5 | Monthly Review | Cadence | Month-end or first Sunday | Weekly outputs, calendar, operating notes | 30-day read on patterns, drift, energy, relationships | Quarterly Positioning | Customize organizational metrics. Keep monthly altitude. |
| 6 | Quarterly Positioning | Cadence | Quarter close or setup | Monthly reviews, strategy docs, board or operating materials | 90-day positioning read | Next quarter priorities | Customize strategic arc language. Keep positioning focus. |
| 7 | Coaching Diagnostic | Diagnose and Decide | A leader or team feels stuck | Situation description, context, team responses if relevant | Leadership Diagnostic Brief | Sunday, Friday, Monthly, Personal Board | Customize sector language carefully. Keep diagnostic discipline. |
| 8 | Personal Board of Advisors | Diagnose and Decide | A decision needs challenge voices, outside lenses, or meaning-level counsel | Conductor Profile, Advisor Board Profile, decision context | Single-advisor, subset, or full-board counsel with convergence and divergence | Quarterly Positioning, Sunday Reflection, Leader-Pen | Keep private advisor details in `local/advisor-board-profile.md`. Preserve distinct seats and disagreement. |
| 9 | Weekly 1:1 | Extend Judgment | Preparing for a direct-report 1:1 | Direct-report dashboard, prior notes, commitments | Listening guide and coaching prompts | Friday Pattern Read, leadership practice | Customize dashboard language. Preserve direct-report ownership. |
| 10 | Exec Review | Extend Judgment | Team needs to prepare docs through leader's lens | Feedback examples, working-with-me docs, assessments, self answers | Personalized exec-review skill plus Leader Review Profile | Conductor Profile, document prep, Leader-Edit | Customize document types and real review comments. Keep single-file generated output. |
| 11 | Leader-Pen | Voice | Drafting new writing | Voice profile, audience, source material, desired outcome | Draft plus editorial note and risk check | Leader-Edit, communication archive | Customize voice interview and formats. Keep anti-generic writing rules. |
| 12 | Leader-Edit | Voice | Revising an existing draft | Draft, voice profile, audience, purpose | Diagnosis, revision, notes or line edits | Final communications | Customize voice rules. Keep revision-before-rewrite discipline. |

## Dependency Pattern

No skill technically requires another skill. Each file is portable and can run by itself.

The bundle is designed as an operating arc:

```text
1 Morning Brief -> 2 Evening Hot Take -> 3 Friday Pattern Read -> 4 Sunday Reflection -> 5 Monthly Review -> 6 Quarterly Positioning
```

The cadence creates signal. Skills 7-8 turn signal into judgment:

```text
Cadence signal + 7 Coaching Diagnostic -> structural pattern
Structural pattern or strategic trade-off + 8 Personal Board of Advisors -> sharper decision questions
```

Skills 9-10 extend the leader's judgment into team practice:

```text
7 Coaching Diagnostic -> 9 Weekly 1:1 practice
10 Exec Review -> Leader Review Profile -> better document preparation and review
```

Skills 11-12 turn the accumulated clarity into communication:

```text
Cadence + Diagnostic Brief + Advisor Board counsel + Voice Profile -> 11 Leader-Pen -> 12 Leader-Edit
```

## What To Preserve

When customizing skills, preserve:

- YAML frontmatter.
- `bundle: mc-conductor` and `position: N of 12` if you want integrity checks to pass.
- The Conductor Profile rule.
- Evidence protocol and source transparency.
- Output section names when other skills reference them.
- Attribution notes for adapted frameworks.

## What To Customize

Customize:

- Stakeholder names.
- Source lists.
- Communication formats.
- Sector language.
- Directness preference.
- Voice examples.
- Advisor names, seat functions, signature questions, and vacant seats.
- Document review checklists.
- Local operating cadence.

Keep customization in the Conductor Profile when possible. Edit skill files only when the change should apply every time that skill runs.
