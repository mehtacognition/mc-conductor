---
name: mc-leader-edit
description: Use when a leader has a draft that needs sharpening for voice, clarity, structure, credibility, audience fit, consultant-speak, AI tells, jargon, and unsupported claims. Trigger phrases - "edit this", "sharpen this draft", "does this sound like me", "leader edit", "clean up this memo", "make this stronger".
bundle: mc-conductor
position: 11 of 11
---

# Conductor - Leader-Edit

Part of the **MC Conductor** bundle. Leader-Edit sharpens existing writing. It is a revision tool, not a drafting tool.

Use **Leader-Pen** when the leader needs a new draft. Use Leader-Edit when there is already text on the page.

## Conductor Profile

If a Conductor Profile is available, use it to adapt this skill to the leader's role, organization, stakeholders, strategic arc, source map, communication duties, directness preference, and off-limits areas.

If no profile is available, ask only the minimum context needed for this run. Do not force the full onboarding interview unless the user is intentionally setting up Conductor. See `docs/onboarding.md` for the shared setup flow.

## What this skill does

Leader-Edit reviews and revises:

- Board notes.
- Investor updates.
- Team memos.
- Customer or community messages.
- Op-eds and public essays.
- Speeches.
- Sensitive emails.
- Strategy documents.

The goal is authentic, clear, valuable writing that sounds like the leader thinking clearly. Not sanitized. Not generic. Not AI-smooth.

## Inputs

Ask for:

1. The draft.
2. Audience.
3. Purpose.
4. Desired action or reader shift.
5. Voice profile, if one exists.
6. Any source material or facts the draft must preserve.

If the user asks for a fast edit, do not over-interview. Edit with the context provided and name assumptions.

## If no Voice Profile exists

Run Leader-Pen's first-time voice interview first, or ask for 2-3 examples that sound like the leader and 1 example that does not. Create a lightweight Voice Profile before doing a full rewrite.

## What to catch

### 1. Consultant-speak and jargon

Flag and replace:

- leverage
- synergy
- best practices
- moving forward
- ecosystem
- value proposition
- strategic imperative
- stakeholder engagement
- right-sizing
- opportunity for growth
- robust solution

Use plain language.

### 2. AI tells

Remove:

- delve
- tapestry
- pivotal
- crucial
- foster
- enhance
- underscore
- highlight in every paragraph
- "not only... but also"
- "in conclusion"
- "in today's rapidly changing..."
- "let's explore"
- "it is important to note"

Break fake symmetry. AI writing often sounds assembled. Good executive writing sounds chosen.

### 3. Voice drift

Flag where the draft loses the leader:

- Too formal.
- Too soft.
- Too polished.
- Too academic.
- Too vague.
- Too many abstractions.
- Too much moralizing.
- Too many bullets for a piece that needs an argument.

### 4. Structural weakness

Check:

- Does the opening start with the real point?
- Does the piece have a claim?
- Does each section earn its place?
- Is the reader's resistance addressed?
- Does the ending move forward instead of summarizing?

### 5. Unsupported claims

Flag claims that need evidence. Do not let the draft overstate certainty.

### 6. Sensitive-context risk

For board, investor, employee, customer, legal, personnel, or crisis communication:

- What could be misread?
- What should be said live instead of in writing?
- Where does the draft create avoidable exposure?
- What does the audience need to hear that the draft is avoiding?

## Editing modes

### Diagnostic edit

Use when the user wants feedback before revision.

Output:

- 3-5 sentence diagnosis.
- Biggest structural issue.
- Voice issues.
- Claims needing evidence.
- Recommended revision strategy.

### Surgical edit

Use when the draft is close.

Output:

- Problem passages.
- Suggested edits.
- Why each edit matters.

### Full rewrite

Use when the draft's structure is wrong or voice has drifted badly.

Output:

- Revised version.
- Short note on what changed.
- Remaining choices for the leader.

If the user does not specify mode, choose the narrowest mode that will solve the problem.

## Output format

For most edits:

```
## Editorial Diagnosis
[3-5 sentences. Lead with the main issue, not praise.]

## Revised Draft
[Clean revised version.]

## Notes
- [What changed and why.]
- [Any claim or judgment still requiring leader confirmation.]
```

For line edits:

```
## Line Edits

Original:
[text]

Suggested:
[text]

Why:
[direct explanation]
```

## Quality bar

- Cut before adding.
- Preserve the leader's edge.
- Prefer concrete nouns and active verbs.
- Keep intentional fragments when they work.
- Do not make writing more formal by default.
- Do not flatten an interesting voice into "professional."
- The best edit should make the writing sound more like the leader, not more like an editor.

## Where this fits in the Conductor rhythm

The cadence skills surface material worth saying. **Leader-Pen** drafts from that material. **Leader-Edit** makes the draft clear enough and true enough to send.

---

*Conductor is a [MehtaCognition](https://mehtacognition.com) bundle. MIT-licensed. Use it, customize it, share it.*
