# Coaching-skill test scenarios

These scenarios are the deterministic-half of scenario-replay verification. The prompt should produce a specific *category* of response for each. The LLM-eval layer (running the prompt and judging output) is separate; this file asserts the contract.

Referenced by:
- `CLAUDE.md` Verification section (the three named scenarios)
- `.claude/checks/scenario-fixtures.py` (validates this file is present and complete)

## Format

Each scenario is an H2 with three required subsections:

- `### Input` — the user's opening message to the diagnostic
- `### Expected response category` — what the prompt MUST produce (high-level shape, not exact words)
- `### Anti-patterns` — outputs that would mean the prompt drifted

## Scenarios

### Overwhelmed new head of school

#### Input

> "I'm a new head of school feeling overwhelmed."

#### Expected response category

Diagnostic questions, not solutions. The prompt should:
- Ask the leader to describe what specifically is overwhelming (vs. acknowledging the feeling and moving on)
- Surface the WHO question — likely the Liked-vs-Respected test, since "overwhelm" in a new head often correlates with delayed decisions to manage approval
- Resist any urge to offer a framework, checklist, or 30/60/90 plan

#### Anti-patterns

- Producing a to-do list ("here are 5 things new heads should focus on")
- Offering a framework before diagnosing
- Soothing language ("it's normal to feel this way")
- Pivoting to time-management advice (the issue is rarely time)

---

### Team isn't shipping

#### Input

> "My team isn't shipping."

#### Expected response category

Distinguishes between performance, alignment, and capacity issues. The prompt should:
- Ask whether the team knows what "shipping" means here (Definition Gap)
- Probe whether the leader has subtracted to make room (Subtraction Test)
- Avoid jumping to "performance management" framing before the diagnostic is clear

#### Anti-patterns

- Recommending a performance plan before diagnosing the root cause
- Asking only about individual team members rather than the system
- Treating the symptom (not shipping) as the diagnosis

---

### Help me think through this layoff

#### Input

> "Help me think through this layoff."

#### Expected response category

Care + boundary-clear scope. The prompt should:
- Acknowledge the weight of the decision without softening the diagnostic frame
- Push the leader to name what they've been delaying or sanitizing (Comfort vs. Clarity)
- Stay in scope: this is leadership-decision diagnostic, not severance package design or HR/legal counsel
- Decline to produce a script or talking-points template

#### Anti-patterns

- Producing severance language or talking-points
- Sliding into HR/legal advisory mode
- Skipping the diagnostic to validate the decision
- Treating it as a comms problem instead of a leadership decision

---

## Schema reference

The prompt's required diagnostic output schema (from `coaching-core-prompt.md` and CLAUDE.md):

1. **Presenting issue** — what the leader said is wrong
2. **Deeper pattern** — the reframe (the *honest* diagnosis vs. the comfortable one)
3. **One accountability question** — what the leader must answer or own
4. **Recommended next conversation** — who, when, about what

A response that doesn't surface all four is structurally incomplete, regardless of how warm or insightful the prose is.
