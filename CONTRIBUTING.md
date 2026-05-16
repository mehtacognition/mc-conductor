# Contributing To Conductor

Conductor improves when leaders and teams use the skills, notice what works, and share what should change. Contributions are welcome, but this repo should never become a place where private leadership context leaks into public history.

## Good Contributions

Helpful contributions include:

- Clearer skill instructions.
- Better onboarding or customization docs.
- Anonymized examples that show the intended altitude.
- Fixes to broken links, skill references, or install guidance.
- Improvements to checks that protect portability and privacy.
- Sector adaptations that remain broadly useful.

## Do Not Submit Private Data

Do not include:

- Real names of leaders, staff, board members, students, customers, donors, or families.
- Real personnel issues.
- Confidential board materials.
- Private financials or operating data.
- Calendar details that identify a person or institution.
- Raw emails, transcripts, messages, or journal entries.
- Assessment reports unless fully anonymized and summarized.

If an example depends on a private situation, turn it into a composite. Change names, dates, organizational details, geography, and any identifying sequence of events.

## Anonymization Standard

A good anonymized example keeps the leadership pattern and removes the fingerprint.

Before submitting, ask:

- Could someone identify the leader or organization from this?
- Are there unusual events, phrases, or details that create a fingerprint?
- Did I remove private names from examples, file paths, and comments?
- Does the example teach the skill without exposing the source context?

When in doubt, generalize more.

## How To Propose A Change

1. Open an issue or pull request describing the skill or doc you used.
2. Explain what happened in use: what was helpful, confusing, too generic, or too sharp.
3. Include the proposed wording or an anonymized before/after excerpt.
4. Run the verification checks before submitting a PR.

```bash
python3 .claude/checks/bundle-integrity.py --explain
python3 .claude/checks/prompt-schema.py --explain
python3 .claude/checks/scenario-fixtures.py --explain
```

## Pull Request Checklist

Before opening a PR:

- [ ] The change keeps all 12 skills installable as single-file prompts.
- [ ] No private leader, client, student, customer, personnel, or board data is included.
- [ ] README links still point to real files.
- [ ] The Conductor Profile rule remains in every skill.
- [ ] Attribution remains where a skill cites an adapted framework.
- [ ] Verification checks pass locally.

## Versioning And Updates

Installed skills are static. Public repo updates only help users after they pull the latest files and update their installed Claude Project, GPT, or pasted prompt.

Use `CHANGELOG.md` to understand what changed and whether an update is worth applying to installed copies.
