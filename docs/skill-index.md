# Conductor Skill Index

This index helps operators decide which skill to install, what to bring, what output to expect, and how each skill connects to the rest of the bundle.

## Categories

- **Cadence:** recurring rituals that create strategic rhythm.
- **Personalization:** tools that create or deepen leader-specific context.
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
| 7 | Exec Review | Personalization | Team needs to prepare docs through leader's lens | Feedback examples, working-with-me docs, assessments, self answers | Personalized exec-review skill plus Leader Review Profile | Conductor Profile, document prep | Customize document types and real review comments. Keep single-file generated output. |
| 8 | Coaching Diagnostic | Personalization | A leader or team feels stuck | Situation description, context, team responses if relevant | Leadership Diagnostic Brief | Sunday, Friday, Monthly | Customize sector language carefully. Keep diagnostic discipline. |
| 9 | Weekly 1:1 | Personalization | Preparing for a direct-report 1:1 | Direct-report dashboard, prior notes, commitments | Listening guide and coaching prompts | Friday Pattern Read, leadership practice | Customize dashboard language. Preserve direct-report ownership. |
| 10 | Leader-Pen | Voice | Drafting new writing | Voice profile, audience, source material, desired outcome | Draft plus editorial note and risk check | Leader-Edit, communication archive | Customize voice interview and formats. Keep anti-generic writing rules. |
| 11 | Leader-Edit | Voice | Revising an existing draft | Draft, voice profile, audience, purpose | Diagnosis, revision, notes or line edits | Final communications | Customize voice rules. Keep revision-before-rewrite discipline. |

## Dependency Pattern

No skill technically requires another skill. Each file is portable and can run by itself.

The bundle works better when outputs cascade:

```text
Morning Brief -> Evening Hot Take -> Friday Pattern Read -> Sunday Reflection -> Monthly Review -> Quarterly Positioning
```

Personalization skills improve the signal across the cadence:

```text
Conductor Profile + Leader Review Profile + Voice Profile -> better cadence, writing, and review outputs
```

## What To Preserve

When customizing skills, preserve:

- YAML frontmatter.
- `bundle: mc-conductor` and `position: N of 11` if you want integrity checks to pass.
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
- Document review checklists.
- Local operating cadence.

Keep customization in the Conductor Profile when possible. Edit skill files only when the change should apply every time that skill runs.
