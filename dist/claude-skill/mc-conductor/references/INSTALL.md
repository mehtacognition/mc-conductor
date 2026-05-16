# Installing Conductor

This guide is for leaders and operators who want the shortest path from download to first use.

## Recommended: One-Package Claude Skill

If your Claude account supports custom Skills, use the bundled package:

1. Download `dist/mc-conductor-claude-skill.zip` from this repo or from the latest GitHub release.
2. In Claude, open **Settings -> Skills**.
3. Choose **Upload skill**.
4. Upload `mc-conductor-claude-skill.zip`.
5. Enable the skill if Claude asks.
6. Start a new chat and say: `Run Sunday Reflection for this week.`

This installs one native Claude Skill called **mc-conductor**. It contains all eleven Conductor rituals and loads the relevant one when you ask for Morning Brief, Sunday Reflection, Leader-Pen, Exec Review, Coaching Diagnostic, or another Conductor workflow.

## First-Time Setup

Before running the full rhythm, create a Conductor Profile:

1. Open `docs/onboarding.md`.
2. Answer the setup questions lightly. Short answers are fine.
3. Save the profile somewhere private, such as a local note or secure team document.
4. Paste the current profile into Conductor chats when Claude does not already have it.

Use `docs/sample-conductor-profile.md` as a model for the right level of detail. Do not put real leader profiles into public repo files.

## If Claude Skills Are Not Available

Use a Claude Project instead:

1. Create a Claude Project named after the ritual, such as `Conductor - Sunday Reflection`.
2. Paste your Conductor Profile first.
3. Paste the relevant `skills/<n>-<name>/SKILL.md` below it.
4. Start a new chat in that project each time you run the ritual.

For ChatGPT, use the same pattern with a custom GPT: paste the Conductor Profile first, then paste the skill file into the GPT instructions.

## What To Install First

Do not install everything into separate projects on day one. Start with one of these:

- **Sunday Reflection** if you want a weekly rhythm.
- **Morning Brief** if you need daily orientation.
- **Leader-Pen** if your first need is writing in your own voice.
- **Coaching Diagnostic** if something specific feels stuck.

The native Claude Skill package includes all eleven workflows, but you should still start with one ritual.

## Privacy Before Pasting Sources

Before pasting calendar details, inbox excerpts, CRM notes, board materials, journal entries, transcripts, or personnel context into any AI tool, confirm your organization's policy. Remove unnecessary identifiers, summarize sensitive records when raw text is not required, and keep regulated or confidential material out of tools that are not approved for that use.
