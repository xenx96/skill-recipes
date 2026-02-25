# Remy Skill Recipes

Engineering-grade skill recipes for working with LLMs.

This repository is a curated collection of reusable, structured prompt workflows
designed for software engineering tasks — debugging, documentation, review,
research, and system analysis.

Each skill is written as a **recipe**:
- Clear purpose
- Required inputs
- Expected output format
- Guardrails
- Failure patterns
- Realistic examples

This is not a random prompt list.
It is a structured cookbook for reliable reuse.

---

## Quick Start

1. Browse the `skills/` directory.
2. Open a skill relevant to your task.
3. Read the **Inputs Required** section carefully.
4. Provide all required context to your LLM.
5. Validate output using the checklist provided in the skill.

Do not skip the input checklist.
Most bad outputs come from incomplete context.

---

## Skill Categories

| Category | Description |
|----------|------------|
| debugging | UI, browser, runtime debugging workflows |
| docs | Spec writing, architecture documentation |
| ux | UI/UX review and design critique |
| research | Competitive analysis, feature comparison |
| review | Code review and side-effect analysis |

---

## Skill Structure

Each skill follows a strict format:

- Purpose
- When to Use
- When NOT to Use
- Inputs Required
- Output Format
- Procedure
- Guardrails
- Failure Patterns
- Examples

Consistency matters more than creativity.

---

## Model Assumptions

These recipes assume:
- A reasoning-capable LLM
- Ability to paste structured context
- Long-context support preferred

They are model-agnostic by design.

---

## Skill Maturity Levels

- Draft — experimental, may evolve
- Stable — reliable for repeated use
- Production — validated across real workflows

---

## Philosophy

LLMs are unreliable without structure.

Structure reduces:
- Hallucination
- Ambiguity
- Context loss
- Overconfidence errors

Good prompting is engineering, not magic.

---

## Contribution

This repository is primarily maintained for personal reuse,
but high-quality pull requests are welcome.

Rules:
- Follow the skill template exactly
- Include at least 2 realistic examples
- Explicitly document failure patterns

---

## License

MIT
