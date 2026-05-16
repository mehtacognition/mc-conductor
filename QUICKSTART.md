# Conductor Quickstart

Use this when you want to download Conductor and run the first useful ritual without understanding the whole bundle first.

## The 15-Minute Path

1. Download or clone the repo.
2. Create a local profile file from the template in `docs/onboarding.md`; use `docs/sample-conductor-profile.md` as a model for specificity.
3. Install one starter skill, not all eleven.
4. Run the first session with your profile and real source material.
5. Save the output where you will actually see it again.

The recommended first install is **Sunday Reflection**. If the leader needs daily orientation right away, start with **Morning Brief** instead.

## Where The Profile Lives

Keep the canonical Conductor Profile outside the public skill files. Recommended local paths:

```text
local/conductor-profile.md
local/leader-review-profile.md
local/voice-profile.md
```

The `local/` folder is ignored by git so leader-specific context, private examples, and source maps do not get committed by mistake.

When installing a skill into Claude, ChatGPT, Gemini, or another AI tool, paste the current Conductor Profile above the skill instructions or into the project/custom GPT instructions alongside the skill. If the profile changes, update the installed skill instructions from the local profile.

## Claude Project Setup

For the first two weeks, use one project per active skill:

1. Create a Claude Project named `Conductor - Sunday Reflection`.
2. Paste the Conductor Profile first.
3. Paste `skills/4-sunday-reflection/SKILL.md` under it.
4. Start a new chat in that project each week.
5. Save the output as that week's Sunday Reflection.

When you add Morning Brief or another skill, repeat the same pattern with a new project. This keeps each ritual focused while using the same shared profile.

## ChatGPT Setup

Use one custom GPT per active skill:

1. Create a GPT named after the skill.
2. Paste the Conductor Profile first.
3. Paste the skill file below it.
4. Add any recurring source instructions you want the GPT to remember.

If you do not want to create GPTs, paste the Conductor Profile and the skill file into a normal chat each time.

## First Run Prompt

After installing Sunday Reflection, start with:

```text
Run Sunday Reflection for this week. I am pasting my calendar highlights, meeting notes, and any daily Conductor outputs I have. If the source base is thin, say so and produce a lighter read rather than filling gaps.
```

Then paste whatever source material you have. Imperfect input is fine. The point is to start the rhythm.

Before pasting calendar details, inbox excerpts, CRM notes, board materials, journal entries, or meeting transcripts into any AI tool, do a privacy pass: follow your organization's AI/data policy, remove unnecessary names and identifiers, summarize sensitive records when raw text is not required, and keep regulated, personnel, student/customer, financial, or confidential board material out of tools that are not approved for that use.

## Updating Over Time

Conductor is a static repo, but the public skills may improve over time as leaders use them and share feedback.

If you cloned with git:

```bash
git remote -v
git pull
python3 .claude/checks/bundle-integrity.py --explain
```

If you forked the repo, keep your local leader profile in `local/` and pull upstream changes into your fork. Do not put private leader data directly into skill files unless you intend to maintain a private fork.

If you downloaded a ZIP, download the latest ZIP later and compare these files first:

```text
README.md
QUICKSTART.md
docs/onboarding.md
docs/customization.md
docs/skill-index.md
skills/*/SKILL.md
```

When a skill changes, update the installed copy in Claude or ChatGPT manually. Your local Conductor Profile should remain separate and reusable.
