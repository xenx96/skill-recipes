# Architecture Spec (Post-Implementation)

Automatically generate a structured architecture/design document
based on implemented code changes.

This skill:

- Analyzes Git diff / changed files
- Evaluates risk and blast radius
- Selects documentation depth (A/B/C)
- Generates a Notion-ready Markdown spec
- Includes diagrams (Mermaid), tables, decisions, and operational notes

---

## Why

Documentation depth should scale with:

- Risk
- Security impact
- Infra impact
- Blast radius

This skill ensures consistency without CI enforcement.

---

## Output Levels

- A — Lightweight
- B — Standard
- C — Architecture-Level

The level is selected automatically.

---

## Structure

- [SKILL.md](SKILL.md) — Main skill (entry point)
- [subskills/diff-risk-evaluator.md](subskills/diff-risk-evaluator.md) — Risk scoring
- [subskills/notion-spec-generator.md](subskills/notion-spec-generator.md) — Document generation
- [subskills/adr-generator.md](subskills/adr-generator.md) — ADR section (Level C)
