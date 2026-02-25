# Pull Request

Thank you for contributing to Remy Skill Recipes.

Before submitting, ensure you have read:

- ARCHITECTURE.md
- CONTRIBUTING.md

This repository enforces strict structural discipline.

---

# 1. Summary

What is being added or modified?

Provide a concise, technical description.

---

# 2. Skill Type

Select one:

- [ ] Execution Skill
- [ ] System Skill
- [ ] Documentation Update
- [ ] Refactor (no structural change)

If this is a skill, continue below.

---

# 3. Skill Metadata

**Category:**  
(e.g., review / research / cleanup / ux / automation)

**Maturity:**

- [ ] Draft
- [ ] Stable
- [ ] Production

**Estimated Time:**

**Model Assumption:**

---

# 4. Template Compliance

Confirm all required sections are present.

## Execution Skill Checklist

- [ ] Purpose
- [ ] When to Use
- [ ] When NOT to Use
- [ ] Inputs Required (checklist format)
- [ ] Output Format (strict structure)
- [ ] Procedure
- [ ] Guardrails
- [ ] Failure Patterns
- [ ] Minimum 2 Examples

## System Skill Checklist

- [ ] Purpose
- [ ] Scope (triggers / non-triggers)
- [ ] Inputs / Signals
- [ ] Core Behavior (Detection → Decision → Action)
- [ ] Output / Side Effects explicitly defined
- [ ] Guardrails
- [ ] Failure Patterns
- [ ] Examples
- [ ] State handling defined (if applicable)
- [ ] Deduplication logic defined (if applicable)

---

# 5. Output Contract

Describe the expected output structure in 2–3 lines.

Confirm it is:

- Deterministic
- Explicitly structured
- Reviewable

---

# 6. Guardrail Summary

Briefly summarize:

- Main hallucination risks
- Primary misuse scenarios
- Key constraint boundaries

---

# 7. Rationale

Why is this skill needed?

- What recurring problem does it solve?
- Why can’t an existing skill cover it?

---

# 8. Validation

Confirm:

- [ ] No vendor lock-in language introduced
- [ ] No template sections removed
- [ ] No structural weakening occurred
- [ ] Category correctly assigned
- [ ] Maturity level justified

---

# 9. Breaking Changes (if any)

Does this modify existing skill behavior?

- [ ] No
- [ ] Yes (describe below)

If yes, explain impact and migration considerations.

---

# 10. Final Self-Review

If this PR:

- Increases ambiguity
- Reduces structural rigor
- Weakens guardrails
- Removes failure pattern documentation

It will be rejected.

Maintain discipline.
