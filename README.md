# Conductor

**A bundle of AI-powered rituals for leaders who'd rather conduct than control.**

A [MehtaCognition](https://mehtacognition.com) project.

---

Most "AI for leaders" content treats AI as a faster way to do the same things you've always done — write the email faster, draft the deck faster, summarize the meeting faster. **Conductor is for C-suite and institutional leaders who want something else:** a *rhythm* of structured AI rituals that make the work more deliberate, more reflective, more honest, and more shared.

A conductor doesn't play every instrument. A conductor sets the tempo, hears the pattern, and gives the orchestra the conditions to play together. Conductor (the bundle) is the same idea applied to running an institution: a small set of rituals, run on a rhythm, that put your attention where it belongs and pull the rest of your team into the conversation.

This is the **half-step** before a fuller MehtaCognition second-brain setup. The skills here run free, on infrastructure you already pay for. They are portable prompts: bring your own calendar, inbox, notes, CRM, board materials, journal, or meeting transcripts. Before pasting sensitive source material into any AI tool, confirm your organization's policy, remove what the skill does not need, and summarize or anonymize private names, financials, personnel issues, board details, student/customer data, journal entries, and transcripts when raw records are not required. Once you feel the rhythm, deeper search across reading, meetings, calendar, and reflections can be added separately.

## Start here: onboard once, then run the skills

Before installing the full bundle, create a lightweight **Conductor Profile**. It captures the leader's role, strategic context, stakeholders, communication duties, source map, and first cadence contract so the skills adapt to the person and institution without re-asking the same setup questions.

Use [`QUICKSTART.md`](QUICKSTART.md) for the first install, then [`docs/onboarding.md`](docs/onboarding.md) for the setup interview and profile template. The rule is simple: personalize Conductor once, then let each skill use that shared profile.

## What's in the bundle

Eleven skills, each a single-file portable prompt. Install once into a Claude Project, ChatGPT GPT, Gemini, or paste at the start of any AI conversation. Native Claude Skills packaging is not shipped yet; use Claude Projects for now.

### Cadence — rituals that run on your week

| Skill | Cadence | What it does |
|---|---|---|
| **1. Morning Brief** | Daily, AM | Orients the leader to what today requires, which meetings matter, and what must not get lost. |
| **2. Evening Hot Take** | Daily, PM | Names what the day revealed: the key insight, open question, small win, pattern connection, and strategic-framing candidates. |
| **3. Friday Pattern Read** | Weekly | Reads across the week to surface patterns, open loops, and framing material no single day reveals. |
| **4. Sunday Reflection** | Weekly | Turns the week's patterns into meaning, priorities, and one forcing question for the week ahead. |
| **5. Monthly Review** | Monthly | Names what is real across 30 days: repeated patterns, drift, energy, relationships, and the honest read. |
| **6. Quarterly Positioning** | Quarterly | Uses the 90-day view to ask what the leader should set up, protect, stop, or question next. |

### Personalization — train AI to think and review like you

| Skill | When | What it does |
|---|---|---|
| **7. Exec Review (Build Your Own)** | Once at setup, refresh quarterly | Generates a personalized leader-review/profile skill for your admin, chief of staff, or executive team. It helps others manage up by preparing documents through your review lens before they reach you. |
| **8. Coaching Diagnostic** | When something specific feels stuck | Structured diagnostic conversation. Surfaces the structural pattern under what feels like a strategy, people, or budget problem. Three modes: Reactive (crisis), Proactive (planning), Team Diagnostic (leadership team, each member independent). |
| **9. Weekly 1:1** | Weekly per direct report | Flips the 1:1 from manager-owned status update to direct-report-owned coaching session. Adapted from Dave Kline's framework with the MC diagnostic discipline layered in. |

### Voice — write and edit in your own voice, not in AI voice

| Skill | When | What it does |
|---|---|---|
| **10. Leader-Pen** | Whenever you're writing | Captures your voice through a structured interview, then drafts emails, board notes, community messages, speeches, op-eds, investor notes, and team messages in *your* voice. |
| **11. Leader-Edit** | Whenever you're editing a draft | Sharpens any draft against your captured voice. Catches AI-tells, consultant-speak, jargon, structural weakness, and unsupported claims. |

## Docs for operators

- [`QUICKSTART.md`](QUICKSTART.md): the 15-minute path from download to first useful ritual.
- [`docs/onboarding.md`](docs/onboarding.md): setup interview, Conductor Profile, Source Map, and Cadence Contract.
- [`docs/sample-conductor-profile.md`](docs/sample-conductor-profile.md): anonymized example of a complete profile at the right altitude.
- [`docs/skill-index.md`](docs/skill-index.md): what each skill does, what to bring, what it produces, and what to customize.
- [`docs/customization.md`](docs/customization.md): how to adapt the bundle, keep private profile data separate, and pull future updates.
- [`CONTRIBUTING.md`](CONTRIBUTING.md): how to share feedback or propose improvements without leaking private context.
- [`CHANGELOG.md`](CHANGELOG.md): what changed and whether installed skill copies should be updated.
- [`docs/cadence-examples.md`](docs/cadence-examples.md): anonymized examples of the six cadence skills at their intended altitude.

## How to install

For the first install, follow [`QUICKSTART.md`](QUICKSTART.md). Each skill is a single file at `skills/<n>-<name>/SKILL.md`. Paste that file into the instruction area of the AI environment you use.

**Claude Project (works for all Claude plans):**
1. claude.ai → Projects → Create Project
2. Name it after the skill (e.g., "Sunday Reflection")
3. Paste the full `SKILL.md` content into Project Instructions
4. Save. Any conversation in that Project now runs that skill.

**Native Claude Skills:**
Conductor does not currently ship zipped native Claude Skill packages or compatibility metadata. Use the Claude Project path above until packaged skill folders are added.

**ChatGPT:**
1. Explore GPTs → Create
2. Paste the `SKILL.md` content into Instructions
3. Save with the skill's name.

**Anywhere else (Gemini, Perplexity, etc.):**
Paste the `SKILL.md` content at the start of a new conversation.

## How to start

Don't install all eleven on day one. The point isn't volume — it's rhythm. We recommend:

1. **Week 1-2 — Sunday Reflection.** Get a feel for how a structured AI ritual lands on your week.
2. **Week 3 — add Morning Brief.** Now you have an opening and a closing rhythm.
3. **Week 4-6 — add Coaching Diagnostic** when something specific feels stuck. The brief it produces becomes the anchor for everything that follows.
4. **Week 7 — add Weekly 1:1** for one direct report. See if you can run it for a month before adding a second.
5. **Week 8 — add Exec Review** when your team asks how to ship docs that do not come back marked up. Treat it as profile deepening, not another cadence.
6. The rest fall in as they're useful.

## What this is *not*

Conductor isn't an app. It isn't a SaaS. It isn't a platform. It's a set of prompts — free, MIT-licensed, runs on infrastructure you already pay for (Claude or ChatGPT). MehtaCognition offers paid setup engagements for institutions that want help installing, customizing, and running it well — but you can run the entire bundle yourself, today, for free.

## What this leads to

Conductor is the portable subset of the second-brain and leadership-rhythm work we run inside MehtaCognition. The cadence skills, diagnostic, 1:1 framework, and voice tools are the parts most directly transferable as prompts. For institutions that want deeper search across reading, meetings, calendar, and reflections, Conductor can grow into a fuller setup engagement.

If Conductor's free rhythm is working and you want help installing, customizing, or extending it for an institution, get in touch.

## Brand

Conductor uses Montserrat and a teal/blue palette. Spec at `docs/brand.md`.

## Verification

This is a prompt-only bundle, but it still has deterministic checks:

```bash
python3 .claude/checks/bundle-integrity.py --explain
python3 .claude/checks/prompt-schema.py --explain
python3 .claude/checks/scenario-fixtures.py --explain
```

The bundle-integrity check verifies all 11 installable skills exist, have required YAML frontmatter, use `bundle: mc-conductor`, keep unique positions, are listed in the README, include the shared Conductor Profile rule, ship the required public docs and GitHub Actions workflow, and do not leak private runtime dependencies.

## Updating over time

Conductor is static once installed into Claude, ChatGPT, or another AI tool. To take future repo improvements without losing local context, keep private profiles in `local/`, pull or download the latest repo, then replace the installed skill instructions while reusing your current Conductor Profile. See [`CHANGELOG.md`](CHANGELOG.md) to decide what to update and [`docs/customization.md`](docs/customization.md) for the update workflow.

## License

MIT. Use it. Customize it. Share it. Bring it into your team. We'd love to hear how it's working through the public repo or MehtaCognition.
