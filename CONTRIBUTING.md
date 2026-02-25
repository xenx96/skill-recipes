# Contributing to Remy Skill Recipes

Thank you for contributing.

This repository is not a casual prompt list.

It is a structured LLM workflow framework.
Contributions must preserve architectural integrity.

Before submitting a pull request, read this document carefully.

---

# 1. Contribution Philosophy

This repository prioritizes:

- Structure over style
- Determinism over creativity
- Guardrails over optimism
- Reusability over novelty

If your contribution weakens structure, it will be rejected.

---

# 2. Skill Types (Mandatory Distinction)

Every new skill must be classified as one of:

## A. Execution Skill

Single-run, deterministic workflow.

Used for:

- Review
- Analysis
- Refactoring
- Documentation
- Benchmarking

## B. System Skill

Persistent or automation-oriented behavior.

Used for:

- Continuous detection
- State tracking
- External system synchronization
- Conversation-wide logic

You must use the correct template.

---

# 3. Required Templates

Use one of:

- `skills/_template/execution-skill.md`
- `skills/_template/system-skill.md`

Do NOT:

- Create custom formats
- Omit required sections
- Merge execution and system concepts improperly

---

# 4. Execution Skill Requirements

Must include:

- Purpose
- When to Use
- When NOT to Use
- Inputs Required (checklist format)
- Output Format (strict structure)
- Procedure
- Guardrails
- Failure Patterns
- Minimum 2 Examples (minimal + realistic)

Common rejection reasons:

- Missing examples
- Vague output format
- No guardrails
- Generic advice
- Overly model-specific wording

---

# 5. System Skill Requirements

Must include:

- Purpose
- Scope (triggers / non-triggers)
- Inputs / Signals
- Core Behavior:
  - Detection
  - Decision logic
  - Actions
- Output / Side Effects (explicit)
- Guardrails
- Failure Patterns
- Examples

If the skill interacts with external systems:

You must define:

- State model
- Deduplication logic
- Race-condition prevention
- Explicit side effects

---

# 6. Structural Rules (Non-Negotiable)

When contributing:

- Do not remove required sections.
- Do not simplify template structure.
- Do not collapse guardrails.
- Do not omit failure patterns.
- Do not weaken output contracts.
- Do not introduce vendor lock-in language.

If unsure → choose stricter structure.

---

# 7. Output Contract Discipline

Every skill must define:

- Exact output structure
- Deterministic section ordering
- Clear reviewability

Avoid:

- Open-ended prose responses
- “Be creative” instructions
- Ambiguous formatting

---

# 8. Model Neutrality

Skills must be:

- Model-agnostic
- Compatible with reasoning-capable LLMs
- Free from vendor-specific hacks unless explicitly justified

If model dependency exists,
it must be clearly documented.

---

# 9. Maturity Declaration

Every skill must declare:

- Draft
- Stable
- Production

Do not mark Production without real-world validation.

---

# 10. Categories

Skills must be placed under appropriate domain categories:

Examples:

- review
- research
- cleanup
- ux
- automation

Type (Execution / System) is separate from category.

---

# 11. Pull Request Guidelines

Your PR must include:

- Clear summary of what was added/changed
- Skill Type (Execution or System)
- Category
- Maturity level
- Rationale for addition
- Confirmation that all required sections are present

PRs missing required sections will be closed without review.

---

# 12. What Not to Contribute

Do NOT submit:

- Motivational prompt hacks
- Model-specific trick prompts
- Marketing-style content
- Opinion-based UX essays without structure
- “Top 10 prompts” style additions

This repository is not a prompt gallery.

---

# 13. Quality Checklist (Self-Review Before PR)

Before submitting:

- [ ] Correct template used
- [ ] All required sections present
- [ ] Guardrails defined
- [ ] Failure patterns defined
- [ ] Output contract explicit
- [ ] Examples included
- [ ] No vendor lock-in language
- [ ] Category assigned
- [ ] Maturity declared

If any box is unchecked, revise before submission.

---

# 14. Final Principle

This repository behaves like a lightweight decision framework.

If a contribution increases ambiguity,
reduces structure,
or weakens guardrails,

it will not be merged.

Maintain discipline.
