---
name: build-exec-review-skill
description: Use when a leader wants their admin team or executive team to review documents through the leader's lens before meetings — surfacing the questions, pushbacks, and decision criteria the leader would apply. Generates a single-file personalized exec-review skill from the leader's behavioral data, working-with-me docs, and feedback patterns. Trigger phrases — "build my exec review skill", "make a review-like-me skill for my team", "generate a doc-review prompt that reviews like I would", "exec review template for my admin".
bundle: mc-conductor
position: 7 of 11
adapted_from: Pattern from Peter Yang's exec-review skill (Meta VP example), generalized for leader use.
---

# Conductor — Exec Review (Build Your Own)

Part of the **MC Conductor** bundle. Conductor is a set of AI-powered rituals for leaders who want to think more clearly, lead more deliberately, and stop being their own bottleneck. This is the skill that frees your admin team from guessing what you'll say in the meeting.

## What this skill does

Generates a single-file *exec-review skill* personalized to **you** — your decision criteria, your common pushbacks, your voice on document review. Your team installs it once. From then on, any document they hand to Claude (or ChatGPT) gets reviewed through your lens *before* it reaches your inbox.

The output is one file. It works in Claude Project, Claude Skill, ChatGPT GPT, Gemini, or any AI tool.

## When to run this

Run it once when you set up Conductor. Re-run it every quarter (the maintenance section explains why). Hand the resulting skill file to your admin or executive team.

## What you need

At least one of the following. More is better.

1. **A behavioral assessment** — Birkman, DISC, StrengthsFinder, Enneagram, Myers-Briggs. Upload the full report if you have it.
2. **A "working with me" document** — Leadership credo, user manual, onboarding guide, team norms.
3. **Examples of your actual feedback** — 5-10 real comments from document reviews. Email threads, meeting notes, margin comments. Most valuable input for voice accuracy.
4. **Self-assessment answers** — If you don't have formal data, answer the ten questions below.

### Self-assessment questions

*Use these if you don't have a behavioral assessment. Answer honestly — the skill is only useful if it's accurate.*

1. When someone brings you a document to review, what do you look at first?
2. What feedback do you give most often? (The comments you repeat.)
3. What makes you say yes quickly? What makes you push back?
4. Written summaries or verbal presentations? How long should they be?
5. Complex decisions — decide quickly, or need time?
6. What frustrates you in a meeting? What energizes you?
7. How direct are you? Soften feedback or give it straight?
8. Big picture or details? Does it depend?
9. What values or principles do you return to most often when evaluating work?
10. What do people on your team most often get wrong about what you want?

## How to build it

### Step 1 — Generate your complete skill file

Copy everything below the scissors line into a new AI conversation (Claude, ChatGPT, Gemini — any tool). Then upload or paste your source material.

The AI will generate a single, complete skill file you can install directly.

### Step 2 — Review and revise

Read the output carefully. Correct anything that doesn't sound like you. Ask the AI to revise until it's accurate. Pay special attention to the *Example Review Comments* — those should sound like words you'd actually say.

### Step 3 — Install it

**Claude Project (works for all Claude plans):**

1. claude.ai → Projects → Create Project
2. Name it "Exec Review — \[Your Name\]"
3. Paste the entire skill file into Project Instructions
4. Save. Any conversation in that Project now has your profile loaded.

**Claude Skill (if you have the Skills feature):**

1. Save the output as a `.md` file (e.g., `exec-review-[your-name].md`)
2. Settings → Skills → Add Skill → Upload the file
3. Claude reads the YAML frontmatter and installs automatically.

**ChatGPT:**

1. ChatGPT → Explore GPTs → Create
2. Paste the skill file contents into Instructions
3. Name it "Exec Review — \[Your Name\]" and save

**Other AI tools:** Paste the skill file at the start of any new conversation, then upload your document.

### Step 4 — Share with your team

Forward the skill file and these installation instructions to your admin or executive team. They install it once and use it whenever they're preparing a document for your review.

### Step 5 — Maintain over time

- **After review meetings:** Note 1-2 things you actually said. Add them to the *Actual Quotes* section.
- **Every quarter:** Re-read the profile. Update what's changed.
- **Ask your team:** *"Does the skill predict my reactions accurately? What does it miss?"*

---

## ✂️ COPY EVERYTHING BELOW THIS LINE INTO YOUR AI TOOL ✂️

---

I need you to build a complete **Exec Review Skill file** for me — a single document my admin team can install in Claude (or use in any AI tool) to review their documents through my lens before meetings.

I'm going to provide source material about my leadership and review style. Use it to build the skill.

**The output must be a single, self-contained file with this exact structure:**

```
---
name: exec-review-[my-last-name]
description: [Write a description that tells Claude when to use this skill. Include trigger phrases like "exec review," "run this by [my name]," "review this like [my name] would," "how would [my name] react to this," and "pressure-test this document." Be specific to my name and role.]
---
```

Then the body of the file, which must include ALL of the following:

**Section 1: What This Skill Does** — 2-3 sentences explaining the skill.

**Section 2: How to Use** — Tell the AI to produce five outputs when a document is shared: Overall Assessment (2-3 sentences), Specific Feedback (section-by-section in my voice), Likely Questions (drawn from my feedback patterns), Recommendations (3-5 prioritized suggestions tied to my profile), and Checklist Results (based on my document review checklists).

**Section 3: My Complete Leader Review Profile** — with these six subsections:

**3a. Core Principles** — 3-5 beliefs that drive my feedback. For each: a short name and 1-2 sentences. If derived from assessment data, note the score. Three strong ones beat five weak ones.

**3b. Feedback Patterns** — 5-8 questions I ask repeatedly when reviewing work. Formatted as quoted questions with a note on why each matters to me.

**3c. Decision-Making Framework** — Green Light Signals (5-7 things that earn a yes), Pushback Triggers (5-7 things that cause pushback), Decision Speed (how I handle simple vs. complex decisions).

**3d. Communication Style** — How I communicate (4-5 patterns), how I need others to communicate with me (4-5 patterns), and an Actual Quotes placeholder with instructions to collect real quotes over time.

**3e. Document Review Checklists** — For each document type I review (ask me which apply — common types: board presentations, parent communications, faculty proposals, budget documents, strategic plan updates, external communications), 5-8 checklist items specific to my priorities.

**3f. Example Review Comments** — 6-8 examples of what I might say in specific scenarios. Mark each as **\[INFERRED\]** until I validate. These should sound like me.

**Section 4: Stress Signals** — 4-6 behaviors that emerge when my needs aren't met, what causes them, and how the team can help.

**Section 5: Profile Maintenance** — Instructions for updating the profile over time (monthly quote collection, quarterly review, team feedback).

**Important guidelines:**

- The entire output must be one file. No references to external files.
- Be specific and concrete. Generic leadership advice is useless. The profile should sound like *me*.
- Where you're inferring from assessment data rather than my direct input, flag it with **\[INFERRED\]**.
- If something is ambiguous, ask me rather than guessing.
- Keep the language plain and direct.
- The YAML frontmatter at the top is required — without it, Claude can't install it as a skill.

Please generate the complete skill file now.

---

## Source Material Log

*Track what was used so future updates know what's grounded in data vs. inference.*

| Source | Used? | Notes |
| :---- | :---- | :---- |
| Behavioral assessment |  | Which one, when taken |
| Working-with-me document |  | Date, author |
| Real feedback examples |  | How many, from when |
| Self-assessment answers |  | Date |
| Direct interview |  | Date |
| Team input |  | How collected |

---

## Where this fits in the Conductor rhythm

Once installed, this skill quietly does the work that used to fill your inbox. The **Friday Pattern Read** will surface when document reviews are creating bottlenecks (*"Three docs sat in your inbox more than 5 days this week — your team is queuing on you again"*). Your **Sunday Reflection** sometimes asks: *what did you push back on this week, and why?* The Exec Review skill is the lever your team uses to self-correct **before** either of those rituals catches the bottleneck.

If your team is using this skill well, you should notice fewer *"can you take a quick look at this?"* asks in your week, and more docs that arrive in your inbox already pre-aligned with what you'd say.

---

*Conductor is a [MehtaCognition](https://mehtacognition.com) bundle. MIT-licensed. Use it, customize it, share it.*
