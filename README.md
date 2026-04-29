# Conductor

**A bundle of AI-powered rituals for leaders who'd rather conduct than control.**

A [MehtaCognition](https://mehtacognition.com) project.

---

Most "AI for leaders" content treats AI as a faster way to do the same things you've always done — write the email faster, draft the deck faster, summarize the meeting faster. **Conductor is for the leaders who want something else:** a *rhythm* of structured AI rituals that make the work more deliberate, more reflective, more honest, and more shared.

A conductor doesn't play every instrument. A conductor sets the tempo, hears the pattern, and gives the orchestra the conditions to play together. Conductor (the bundle) is the same idea applied to running an institution: a small set of rituals, run on a rhythm, that put your attention where it belongs and pull the rest of your team into the conversation.

This is the **half-step** before MehtaCognition's full NAVI engagement. The skills here run free, on infrastructure you already pay for. Once you feel the rhythm, the full system — with deep search across your reading, meetings, calendar, and reflections — is a separate setup engagement.

## What's in the bundle

Eleven skills, each a single-file portable prompt. Install once into Claude Project, Claude Skill, ChatGPT GPT, Gemini, or paste at the start of any AI conversation.

### Cadence — rituals that run on your week

| Skill | Cadence | What it does |
|---|---|---|
| **1. Morning Brief** | Daily, AM | Surfaces what to focus on today, drawing from your calendar, inbox, and prior week's open threads. |
| **2. Evening Hot Take** | Daily, PM | A one-paragraph honest read of the day. What happened, what you noticed, what to bring forward. |
| **3. Friday Pattern Read** | Weekly | Reads across the week to surface patterns no single day reveals. |
| **4. Sunday Reflection** | Weekly | A quiet ritual that surfaces the question you've been avoiding, and the one specific thing to try next week. |
| **5. Monthly Review** | Monthly | Deeper retrospective. Which decisions stuck? Which patterns repeated? What stopped? |
| **6. Quarterly Positioning** | Quarterly | Re-grounds you in medium-arc questions: where is the institution headed, what's the position you're earning, what do you need to stop? |

### Personalization — train AI to think and review like you

| Skill | When | What it does |
|---|---|---|
| **7. Exec Review (Build Your Own)** | Once at setup, refresh quarterly | Generates a personalized exec-review skill for your admin or executive team. They run any document through your lens before it reaches you. |
| **8. Coaching Diagnostic** | When something specific feels stuck | Structured diagnostic conversation. Surfaces the structural pattern under what feels like a strategy, people, or budget problem. Three modes: Reactive (crisis), Proactive (planning), Team Diagnostic (leadership team, each member independent). |
| **9. Weekly 1:1** | Weekly per direct report | Flips the 1:1 from manager-owned status update to direct-report-owned coaching session. Adapted from Dave Kline's framework with the MC diagnostic discipline layered in. |

### Voice — write and edit in your own voice, not in AI voice

| Skill | When | What it does |
|---|---|---|
| **10. Leader-Pen** | Whenever you're writing | Captures your voice through a structured interview, then drafts emails, board notes, op-eds, and faculty messages in *your* voice. |
| **11. Leader-Edit** | Whenever you're editing a draft | Sharpens any draft against your captured voice. Catches AI-tells, consultant-speak, jargon, and structural weakness. |

## How to install

Each skill is a single file at `skills/<n>-<name>/SKILL.md`. The YAML frontmatter at the top lets Claude install it as a Skill automatically.

**Claude Project (works for all Claude plans):**
1. claude.ai → Projects → Create Project
2. Name it after the skill (e.g., "Sunday Reflection")
3. Paste the full `SKILL.md` content into Project Instructions
4. Save. Any conversation in that Project now runs that skill.

**Claude Skill (if you have the Skills feature):**
1. Settings → Skills → Add Skill → upload the `SKILL.md` file
2. Claude reads the YAML frontmatter and installs automatically.

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
5. **Week 8 — add Exec Review** when your team asks how to ship docs that don't come back marked up.
6. The rest fall in as they're useful.

## What this is *not*

Conductor isn't an app. It isn't a SaaS. It isn't a platform. It's a set of prompts — free, MIT-licensed, runs on infrastructure you already pay for (Claude or ChatGPT). MehtaCognition offers paid setup engagements for institutions that want help installing, customizing, and running it well — but you can run the entire bundle yourself, today, for free.

## What this leads to

Conductor is the working subset of the [NAVI second-brain system](https://mehtacognition.com) we run inside MehtaCognition. The cadence skills, the diagnostic, and the 1:1 framework are the parts most directly transferable to leaders we work with as portable prompts. The full NAVI system — with deep search across your reading, meetings, calendar, and reflections, plus automated daily and weekly synthesis — is a separate setup engagement (typically $15–20K for the install, with optional ongoing curation).

If Conductor's free rhythm is working for you and you want the full system installed at your institution, get in touch.

## Brand

Conductor uses Montserrat and a teal/blue palette. Spec at `docs/brand.md`.

## License

MIT. Use it. Customize it. Share it. Bring it into your team. We'd love to hear how it's working — `nishant@mehtacognition.com`.
