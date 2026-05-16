# Updating Conductor

Conductor has two kinds of material:

- **Public release files:** the repo docs, public skill files, and packaged Claude Skill ZIP.
- **Private local context:** your Conductor Profile, Leader Review Profile, Voice Profile, examples, source map, and sensitive notes.

Keep those separate. Public updates should never overwrite private leader context.

## If You Use The Native Claude Skill Package

1. Download the latest `dist/mc-conductor-claude-skill.zip` from the repo or latest release.
2. In Claude, open **Settings -> Skills**.
3. Replace or re-upload the `mc-conductor` skill.
4. Keep your existing Conductor Profile and private notes unchanged.
5. Run one familiar ritual, such as Sunday Reflection, to confirm the output still feels right.

If Claude shows both the old and new package, disable or remove the old one so there is only one active `mc-conductor` skill.

## If You Use Claude Projects Or Custom GPTs

Repo updates do not automatically update pasted instructions.

When a skill changes:

1. Open the updated `skills/<n>-<name>/SKILL.md`.
2. Keep your current Conductor Profile.
3. Replace the old installed skill instructions with the new file.
4. Paste the latest Conductor Profile above the skill instructions.
5. Run one test with familiar source material.

## When To Update

Update installed skills when `CHANGELOG.md` says a release changes:

- Output structure.
- Conductor Profile usage.
- Privacy guidance.
- Install or update instructions.
- Any skill you actively use.

You can skip updates for skills you are not using yet unless the changelog marks the release as a security or privacy update.

## What Not To Do

- Do not paste private leader profiles into public repo files.
- Do not edit the packaged ZIP directly.
- Do not merge public changes into private examples without reviewing them.
- Do not assume GitHub updates automatically changed Claude Projects, custom GPTs, or uploaded Skills.
