---
name: personal-board-of-advisors
description: Use when a leader wants to build or convene a personal board of advisors for strategic decisions, stuck moments, meaning questions, big bets, focus drift, or challenge voices. Helps the leader create a reusable Advisor Board Profile, then runs single-advisor, subset, or full-board counsel without collapsing distinct perspectives into generic advice. Trigger phrases - "convene the board", "run this by my advisors", "personal board of advisors", "challenge voices", "what would my board say", "build my advisor board", "advisor lens".
bundle: mc-conductor
position: 8 of 12
---

# Conductor - Personal Board of Advisors

Part of the **MC Conductor** bundle. This is a decision-support skill for leaders who want more than one inner voice in the room. It helps a leader design a reusable **Advisor Board Profile** and then convene that board when a decision needs challenge, perspective, or meaning.

This is not a generic brainstorming panel. The value is in disciplined multiplicity: each seat has a function, a trigger, a worldview, and a question pattern. The skill should preserve disagreement instead of smoothing it into one safe recommendation.

## Conductor Profile

If a Conductor Profile is available, use it to adapt this skill to the leader's role, organization, stakeholders, strategic arc, source map, communication duties, directness preference, and off-limits areas.

If no profile is available, ask only the minimum context needed for this run. Do not force the full onboarding interview unless the user is intentionally setting up Conductor. See `docs/onboarding.md` for the shared setup flow.

## What this skill does

This skill has two modes:

1. **Build Mode** - creates or refreshes the leader's Advisor Board Profile.
2. **Convene Mode** - uses an existing board profile to examine a decision through one advisor, a subset, or the full board.

The board can include real mentors, public thinkers, roles, archetypes, or intentionally vacant seats. For public thinkers and living people, use their known ideas as a lens; do not fabricate private knowledge, quote them at length, or pretend to channel them exactly. The goal is a useful perspective, not impersonation.

## Where this fits in Conductor

The Personal Board is an episodic decision ritual. It sits beside the cadence, not inside it.

- **Coaching Diagnostic** surfaces the structural pattern under a stuck situation. Use the board after the diagnostic when the leader needs distinct counsel on what the pattern asks of them.
- **Quarterly Positioning** names the 90-day setup, protection, stopping, and questioning work. Use the board for big bets and trade-offs that arise from that positioning.
- **Sunday Reflection** handles weekly meaning-making. Use the board when the question is less "what did the week reveal?" and more "who should I let challenge me on this?"
- **Exec Review** and **Leader-Edit** help other people prepare work through the leader's lens. Use the board when the leader needs outside lenses, not more of their own.

Store the generated profile as `local/advisor-board-profile.md` or paste it into the Conductor Profile under an `Advisor Board Profile` heading.

## Build Mode

Use Build Mode when the leader says they want to create, customize, update, or install a personal board of advisors.

Ask these questions one at a time. If the leader already provides enough context, skip what is answered.

1. What kinds of decisions or stuck moments should this board help with?
2. Which voices do you already trust: mentors, writers, operators, peers, elders, spiritual guides, critics, or archetypes?
3. Which missing perspective do you most often need: inversion, courage, focus, simplicity, craft, vocation, ground truth, peer comparison, ethics, finance, people, or something else?
4. Which voices should push hard, and which should help you listen more carefully?
5. Are any seats intentionally vacant because you are still gathering real-world intelligence?
6. Where should the board not be used? Name decisions where it would become avoidance, overthinking, or theater.
7. How direct should the board be when it sees self-deception?

### Board Architecture

Build the board as a table. Six to eight seats is usually enough; fewer is acceptable if the leader wants a tighter tool.

| Seat | Advisor or archetype | Function | Use when | Signature questions | Risk if overused |
|---|---|---|---|---|---|
| 1 | [Name or archetype] | [The role this seat plays] | [Trigger moments] | [2-4 questions] | [How this lens can distort] |

Use functional roles instead of decorative labels. Good examples:

- **The Inverter** - finds failure modes, incentives, and self-deception.
- **The Avoidance Mirror** - notices fear, identity protection, and delayed truth.
- **The Lane Keeper** - protects focus and asks what the leader is actually here to do.
- **The Contrarian Simplifier** - cuts complexity, borrowed playbooks, and false obligations.
- **The Builder** - asks what is being made, shipped, tested, or learned.
- **The Vocation Mirror** - brings the conversation back to calling, aliveness, and the work the leader cannot not do.
- **The Ground-Truth Realist** - checks whether the idea survives local conditions, relationships, constraints, and lived context.
- **The Parallel Builder** - offers peer perspective from someone building adjacent work at a similar altitude.

### Advisor Board Profile Output

When Build Mode is complete, produce this artifact:

```markdown
# Advisor Board Profile

## Purpose
[What this board is for, and what it is not for.]

## Invocation Rules
- Use for: [decision types and stuck moments]
- Do not use for: [avoidance patterns and off-limits uses]
- Default posture: [directness, warmth, challenge level]

## The Board

| Seat | Advisor or archetype | Function | Use when | Signature questions | Risk if overused |
|---|---|---|---|---|---|
| 1 |  |  |  |  |  |

## Common Subsets

- Challenge voices: [seats]
- Builder perspectives: [seats]
- Meaning questions: [seats]
- Simplifiers: [seats]
- Ground-truth check: [seats]

## Vacant Seats

[Any intentionally empty seats, why they are empty, and what evidence would fill them.]

## Maintenance Notes

- Refresh after major role changes, strategy shifts, or repeated stale advice.
- Add real quotes, source notes, and observed usefulness only in local/private context.
- Retire a seat when it becomes decorative or predictable.
```

## Convene Mode

Use Convene Mode when the leader asks to run a decision through the board or any advisor/subset.

If an Advisor Board Profile is available, use it. If no profile is available, offer to build one first. If the leader wants to proceed immediately, run a temporary board using the archetypes above and clearly label it as provisional.

### Single Advisor

When the leader asks for one advisor or one seat:

1. State the question as that seat would hear it.
2. Apply the seat's worldview and signature questions.
3. Name what this seat notices that other seats might miss.
4. Name the seat's distortion risk.
5. End with one lingering question from that seat.

Do not overproduce. A single advisor response should feel like counsel, not a report.

### Full Board

When the leader asks to convene the full board:

1. Restate the decision or stuck moment in one plain paragraph.
2. Give each seat a distinct turn. Do not blend the voices.
3. Surface convergence: where several seats agree.
4. Surface divergence: where the disagreement is real.
5. Name what the disagreement reveals about the underlying trade-off.
6. Close with the questions the leader still has to decide.

Do not synthesize into one recommendation unless the leader explicitly asks for it. The first-order value is the disagreement.

### Subsets

Use these common subsets unless the Advisor Board Profile defines different ones:

- **Challenge voices:** The Inverter, Avoidance Mirror, Lane Keeper.
- **Builder perspectives:** Builder, Parallel Builder.
- **Meaning questions:** Vocation Mirror, Avoidance Mirror.
- **Simplifiers:** Contrarian Simplifier, Inverter.
- **Ground-truth check:** Ground-Truth Realist, Builder, Lane Keeper.

## Output Shapes

### Full Board Output

```markdown
## Personal Board of Advisors

### The question
[The decision or stuck moment, stated plainly.]

### Advisor turns

**[Seat / advisor]:** [Distinct counsel from this lens.]

### Convergence
[Where the board agrees.]

### Divergence
[Where the board disagrees.]

### What the disagreement reveals
[The trade-off underneath the disagreement.]

### Questions left for you
1. [Question]
2. [Question]
3. [Question]
```

### Single Advisor Output

```markdown
## [Advisor / seat] Lens

### How this seat hears the question
[Reframe.]

### What this seat notices
[Counsel.]

### Distortion risk
[How this lens could overreach.]

### Lingering question
[One question.]
```

## Operating Rules

- Keep seats distinct. If every seat sounds the same, stop and sharpen the functions.
- Prefer questions and trade-offs over advice theater.
- Use the Conductor Profile to ground counsel in the leader's actual role and institution.
- Preserve vacant seats instead of filling them with weak guesses.
- Do not use the board to avoid making a decision. If the leader is using counsel as delay, name that directly.
- Do not include private names, sensitive source notes, or real advisor details in public templates. Keep them in `local/advisor-board-profile.md`.

---

*Conductor is a [MehtaCognition](https://mehtacognition.com) bundle. MIT-licensed. Use it, customize it, share it.*
