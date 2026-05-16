---
name: mc-conductor
description: Use for MehtaCognition Conductor leadership rituals: Morning Brief, Evening Hot Take, Friday Pattern Read, Sunday Reflection, Monthly Review, Quarterly Positioning, Exec Review, Coaching Diagnostic, Weekly 1:1, Leader-Pen, and Leader-Edit. Helps leaders run a shared Conductor Profile across cadence, diagnosis, document review, writing, and revision.
---

# MC Conductor

Conductor is a bundle of AI-powered rituals for leaders who want to think more clearly, lead more deliberately, and keep a reusable profile across reflection, diagnosis, review, writing, and editing.

## How To Use This Skill

When the user asks for a Conductor workflow, load the matching reference file and follow it directly:

| User intent | Reference file |
|---|---|
| Morning Brief, prep me for today, daily executive brief | `references/skills/1-morning-brief/SKILL.md` |
| Evening Hot Take, close out today, end-of-day read | `references/skills/2-evening-hot-take/SKILL.md` |
| Friday Pattern Read, week in review, read the week | `references/skills/3-friday-pattern-read/SKILL.md` |
| Sunday Reflection, weekly reflection, set up next week | `references/skills/4-sunday-reflection/SKILL.md` |
| Monthly Review, month in review, 30-day read | `references/skills/5-monthly-review/SKILL.md` |
| Quarterly Positioning, quarterly review, 90-day view | `references/skills/6-quarterly-positioning/SKILL.md` |
| Exec Review, build my review-like-me skill, document review through my lens | `references/skills/7-exec-review/SKILL.md` |
| Coaching Diagnostic, leadership diagnostic, Step Before Strategy | `references/skills/8-coaching-diagnostic/SKILL.md` |
| Weekly 1:1, prep my 1:1, direct-report dashboard | `references/skills/9-one-on-one/SKILL.md` |
| Leader-Pen, write this in my voice, draft a memo | `references/skills/10-leader-pen/SKILL.md` |
| Leader-Edit, edit this, sharpen this draft, does this sound like me | `references/skills/11-leader-edit/SKILL.md` |

If the user is setting up Conductor for the first time, load `references/docs/onboarding.md` and guide them through the smallest useful setup. If they ask how to install or update Conductor, use `references/INSTALL.md` or `references/UPDATE.md`.

## Conductor Profile Rule

If a Conductor Profile is available, use it to adapt the selected workflow to the leader's role, organization, stakeholders, strategic arc, source map, communication duties, directness preference, and off-limits areas.

If no profile is available, ask only the minimum context needed for the current run. Do not force the full onboarding interview unless the user is intentionally setting up Conductor.

## Privacy Rule

Before asking the user to paste calendar details, inbox excerpts, CRM notes, board materials, journal entries, transcripts, personnel context, or other sensitive source material, remind them to follow their organization's AI/data policy and to summarize, anonymize, or omit sensitive records when raw text is not required.

## Operating Posture

- Run the selected ritual, not a generic coaching conversation.
- Stay evidence-grounded. Name thin source material when source material is thin.
- Preserve the output shape from the selected reference file.
- Keep private leader context out of public examples and reusable package files.
- If two workflows could apply, ask which one the user wants or recommend the narrower one.
