# MC Leadership OS — Product Vision Document

*Prepared for MehtaCognition Advisory Board Review*
*Date: March 25, 2026*

---

## What This Document Is

This is a product vision for review — not a decided plan. It emerged from a brainstorming and CEO review session that started with designing a single coaching skill and surfaced a much larger opportunity. The advisory board is being asked to pressure-test the vision, the business model, and the go-to-market before any product decisions are made.

## The Origin

MehtaCognition is a leadership consultancy that works with school leaders and nonprofit executives on strategy, leadership, and organizational design. The practice is built on Nishant Mehta's methodology — a diagnostic approach developed from his experience as a head of school and refined across dozens of institutional engagements.

The consultancy's constraint is Nishant's calendar. He can work deeply with 10-15 institutions at a time. Meanwhile, thousands of school leaders and nonprofit executives who would benefit from this kind of diagnostic thinking have no access to it.

We designed a Claude-powered coaching diagnostic that codifies Nishant's methodology — his forcing questions, his reframing patterns, his voice. In testing the design, a larger opportunity emerged: not just a diagnostic tool, but a full leadership operating system.

## The Core Methodology (Already Built)

A coaching diagnostic prompt has been written and reviewed. It includes:

- **Nishant's persona** — direct-first, reframing as the primary move, anti-consultant consultant identity. Synthesized from 7 Substack posts and confirmed by Nishant.
- **Six forcing questions** ordered Who → What → How → Why:
  1. The Liked vs. Respected Test (delayed decisions)
  2. The Definition Gap (undefined shared language)
  3. The Comfort vs. Clarity Test (softened truths)
  4. The Subtraction Test (what have you stopped?)
  5. The Decision Ownership Question (reopened decisions)
  6. The Mission-as-Management Check (boundaries as loyalty tests)
- **Two bass-line questions** threading throughout: "Why do you want to lead?" and "Why would anyone want to be led by you?"
- **Nine push-back patterns** for when leaders deflect, perform, or give polished answers
- **Framework references** (Heifetz, Senge, Edmondson, Kegan & Lahey, Collins, Lencioni) woven in when relevant
- **Three modes**: Reactive (crisis), Proactive (planning), Team Diagnostic (leadership team, each member answers independently — codifies the "Step Before Strategy" pre-planning diagnostic)
- **Leadership Diagnostic Brief** output with five sections: What I Heard, The Question to Sit With, Questions for Reflection, Before We Meet Again, Muscle Memory Log

The prompt is at: `~/Documents/MehtaCognition/Projects/coaching-skill/coaching-core-prompt.md`

## The Product Vision: MC Leadership OS

A Leadership Operating System for school leaders and nonprofit executives. Not coaching — infrastructure. The way a CFO has QuickBooks and a developer has GitHub, a school leader has the MC Leadership OS.

### Layer 1: The Diagnostic (built)

The entry point. A leader runs the coaching diagnostic and gets a Leadership Diagnostic Brief — the spine of everything that follows. This is the foundation that all other components reference.

### Layer 2: The Rhythm (designed, not built)

Scheduled touchpoints that turn a one-time diagnostic into an ongoing practice:

| Touchpoint | Cadence | Purpose |
|---|---|---|
| Monday Strategic Pulse | Weekly | Connects the leader's commitment to the week ahead |
| Wednesday Mid-Week Check | Weekly | Progress check — did you do what you said? What got in the way? |
| Friday Pattern Read | Weekly | Reflects on decisions made/avoided this week against diagnostic patterns |
| Sunday Reflection | Weekly | Resurfaces the Question to Sit With from the brief |
| Monthly Diagnostic Refresh | Monthly | Lighter forcing questions, updates the Muscle Memory Log |
| Quarterly Strategic Review | Quarterly | Full diagnostic re-run, timed to school year inflection points (board meetings, enrollment cycles, budget season) |

The rhythm is what turns diagnosis into muscle. Repetition, not a single conversation, is how strategic capacity is built.

### Layer 3: The Toolkit (conceptual)

Companion skills for specific leadership moments:

- **/board-prep** — Help frame uncomfortable truths for a board presentation. "Your board meeting is in two weeks. Based on your diagnostic patterns, here's the honest version of what you need to present — and how to frame it so it drives action instead of anxiety."
- **/team-diagnostic** — Run the Step Before Strategy diagnostic with the full leadership team. Each member answers independently. The system synthesizes convergences and divergences.
- **/strategic-read** — Curated reading connected to the leader's diagnostic patterns. A leader struggling with the Subtraction Test gets an article about additive bias. A leader wrestling with the Definition Gap gets a piece on shared mental models.
- **/decision-log** — Tracks decisions made and avoided over time. Makes the pattern of avoidance visible in a way that a single session cannot.
- **/evaluation-design** — Builds feedback and evaluation systems (codifies the Definition Gap methodology for teacher evaluation)
- **/subtraction-audit** — Annual review of what to stop doing, connected to the Subtraction Test forcing question

### Layer 4: The Community (future)

Leaders using the OS anonymously contribute to pattern data:
- "73% of leaders in your cohort couldn't name something they stopped doing. You're not alone — but you can be different."
- Peer cohorts of similar-stage leaders
- Benchmarking against comparable institutions (school size, type, geography)

### Layer 5: The Consultancy (Nishant stays in the picture)

The OS handles the 80% — diagnosis, rhythm, accountability. When a leader hits the 20% that requires human judgment (a crisis, a board conflict, a leadership transition, a sensitive personnel issue), the OS connects them to Nishant directly.

The product is the top of the funnel. The consultancy is the premium tier.

## Open Questions for the Board

### Business Model

1. **Is this a product company or a consulting-enhancement tool?** A product company scales beyond Nishant. A consulting tool makes Nishant more effective. These are different businesses with different capital requirements, different timelines, and different risks.

2. **Pricing model?** Subscription (monthly/annual)? Per-institution? Tiered (self-serve diagnostic → scheduled rhythm → full OS with consultancy access)? The school/nonprofit market is price-sensitive — what's the willingness to pay?

3. **Does the consultancy cannibalize the product, or does the product feed the consultancy?** If leaders get 80% of the value from the OS, do fewer of them hire Nishant? Or do more of them hire him because they've already done the diagnostic work and know exactly what they need?

### The 10% Problem

4. **Is AI-delivered coaching honest about its limitations?** Gary Tan says /office-hours captures maybe 10% of what a real YC partner delivers. Our diagnostic has the same constraint — it can't read the room, build trust through presence, or handle real-time emotional nuance. Is 10-20% of Nishant's diagnostic ability still more valuable than what these leaders currently have (which is usually nothing)?

5. **How do we position it honestly?** The proposed framing: "This isn't a replacement for working with a consultant. It's what every leader should do before, between, and after working with one." Does this hold up, or does it undersell the product?

### IP and Protection

6. **The methodology is in a prompt. Prompts can be copied.** The forcing questions, push-back patterns, and brief format are all in a text file. Anyone with access can extract and replicate it. How do we protect the IP?

   Current thinking on protection:
   - The methodology is already partly public (Substack posts describe the thinking behind each question)
   - Brand/reputation is the primary moat
   - Compound data (Muscle Memory Log, decision history) creates switching costs
   - Legal baseline (copyright, trademark "Leadership Diagnostic Brief" and "Step Before Strategy")
   - **Technical protection requires moving to a web app** where the prompt runs server-side and never leaves the server

7. **When does it need to become a web app?** A Claude Project is a prototype, not a defensible product. The question is whether to build a proper web application (Next.js on Vercel) from the start, or validate with Claude Projects first and migrate later.

### Market and Competitive Landscape

8. **Who else is doing this?** Executive coaching platforms (BetterUp, CoachHub) serve enterprises. Generic AI coaching bots exist but lack domain specificity. Nobody is building for the independent school and nonprofit executive market specifically. Is that a feature (untapped market) or a signal (market too small)?

9. **What's the total addressable market?** Roughly 1,600 NAIS member schools, plus religiously affiliated schools, charter networks, and nonprofit organizations. How many would pay for a leadership OS?

10. **Does this compete with or complement NAIS, ISCA, and other association offerings?** These organizations offer conferences and professional development. Does the MC Leadership OS partner with them or compete?

### Nishant's Role

11. **Can Nishant build a product company while running a consultancy?** These require different skills, different time commitments, and different mindsets. Is there a path where both coexist, or does one eventually need to be primary?

12. **What if the product works too well?** If leaders get genuine value from the OS without ever hiring Nishant, has MehtaCognition succeeded or cannibalized itself? What does success look like?

---

## What We're Asking the Board

Review this vision on three dimensions:

1. **Is this the right product?** Does the five-layer architecture make sense? Is the ordering right? What's missing? What should be cut?

2. **Is this the right business?** Product company vs. consulting tool vs. hybrid. What's the business model? What's the risk profile?

3. **Is this the right time?** Nishant has the ASB Growth Portal in active development, an established consultancy, and a growing Substack. Is adding a product to the portfolio the right move now, or should the diagnostic tool be validated as a consulting enhancement first?

---

*This document was prepared from a brainstorming and CEO review session conducted on March 25, 2026. The coaching diagnostic core prompt has been written and reviewed. Everything beyond Layer 1 is vision, not commitment.*
