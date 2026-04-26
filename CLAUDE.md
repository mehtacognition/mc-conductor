# MC Leadership OS — Coaching Skill

AI-powered leadership diagnostic and accountability skill. Per memory: core prompt built (`coaching-core-prompt.md`), product vision pending `/boardroom` review (`MC-Leadership-OS-Vision.md`).

This is a **prompt-only project** (no code build). Verification therefore tests prompt behavior, not code correctness.

## Verification

Used by `/go` as the criteria for Phase 1 (self-test) and Phase 2 (cold-grader). Each criterion must be testable to PASS / FAIL / UNCERTAIN.

**Always:**
- [ ] Prompt files (`coaching-core-prompt.md`, `MC-Leadership-OS-Vision.md`) parse as valid Markdown (no broken code fences, no malformed frontmatter).
- [ ] No personal data, real client names, or real coaching-session content in committed files (run `python3 ~/.claude/checks/security/pr-personal-data-sweep.py --branch`).

**If the change touches the core prompt:**
- [ ] Run prompt against the standard scenario set (to be created at `docs/test-scenarios.md`):
  - "I'm a new head of school feeling overwhelmed" — should produce diagnostic questions, not solutions
  - "My team isn't shipping" — should distinguish performance vs alignment vs capacity issue
  - "Help me think through this layoff" — should respond with care + boundary-clear scope
- [ ] Output structure matches diagnostic schema: identifies (a) presenting issue, (b) deeper pattern, (c) one accountability question, (d) recommended next conversation.
- [ ] Voice matches the MC standard: warm but direct, no consultant-speak, no AI-tells. Run `python3 ~/.claude/checks/writing/pen-voice-lint.py --file <output>` if outputs are saved.

**If the change touches product vision:**
- [ ] Run `/edit` on the vision doc to catch voice drift.
- [ ] Run `/ce-doc-review` for multi-persona structural critique before sharing with /boardroom.
- [ ] Boardroom review scheduled OR justified-deferred (don't iterate vision in a vacuum).

**Skillify candidates as patterns emerge:**
- Diagnostic-output-shape check (deterministic JSON validator for prompt output)
- Scenario-replay smoke test (run all scenarios, verify each returns the expected category of response)
