# Remy Skill Recipes – Architecture

This document defines the architectural principles,
skill taxonomy, structural constraints, and non-negotiable standards
for this repository.

This is not a prompt collection.

This is a structured LLM workflow system.

---

# 1. Core Identity

Remy Skill Recipes is an engineering-grade skill framework designed to:

- Reduce hallucination
- Enforce structured outputs
- Standardize repeatable LLM workflows
- Provide guardrails and failure detection
- Support long-term maintainability

Prompting is treated as engineering.

---

# 2. Foundational Principles

## 2.1 Structure Over Cleverness

Every skill must follow a strict template.

No freestyle prompts.
No loose formatting.
No ambiguous output contracts.

---

## 2.2 Explicit Inputs Reduce Hallucination

Incomplete input → unreliable output.

Skills must define:

- Required inputs (checklist format)
- Optional inputs
- Context boundaries

---

## 2.3 Output Is a Contract

Every skill defines an explicit output structure.

The LLM must produce predictable, reviewable results.

---

## 2.4 Guardrails Are Mandatory

Each skill must:

- State what it will NOT do
- Declare assumptions
- Document failure patterns

Guardrails are not optional.

---

## 2.5 Reusability > One-Off Usefulness

Skills must be:

- Reusable across projects
- Domain-agnostic when possible
- Free from project-specific assumptions

---

# 3. Skill Taxonomy

The repository supports two types of skills.

Skill Type is separate from Skill Category.

---

# 3.1 Execution Skills

Single-run structured workflows.

Used for:

- Change re-audit
- Regression analysis
- Competitive benchmarking
- Refactoring validation
- Documentation generation

Execution Skills are deterministic and stateless.

---

## Execution Skill Required Sections

Every Execution Skill must include:

- Purpose
- When to Use
- When NOT to Use
- Inputs Required (checklist)
- Output Format (strict structure)
- Procedure
- Guardrails
- Failure Patterns
- Minimum 2 Examples (minimal + realistic)

Execution skills produce a structured, inspectable output.

---

# 3.2 System Skills

Persistent or automation-oriented behaviors.

Used for:

- Continuous concept detection
- Conversation-wide logic
- External database synchronization
- Recurrence tracking
- Knowledge graph updates

System Skills may be stateful.

---

## System Skill Required Sections

Every System Skill must include:

- Purpose
- Scope (triggers / non-triggers)
- Inputs / Signals
- Core Behavior:
  - Detection
  - Decision Logic
  - Actions
- Output / Side Effects
- Guardrails
- Failure Patterns
- Examples

System Skills must explicitly define:

- State handling
- Side effects
- Deduplication logic
- Race-condition prevention (if external writes occur)

---

# 4. Categories

Skills are grouped by domain, not by type.

Examples:

- review
- research
- cleanup
- ux
- automation

Type (Execution / System) is orthogonal to Category.

---

# 5. Skill Maturity Model

Each skill must declare one of:

- Draft — experimental
- Stable — safe for repeated use
- Production — validated in real workflows

Maturity must reflect real-world usage, not confidence.

---

# 6. Model Assumptions

All skills must be:

- Model-agnostic
- Compatible with reasoning-capable LLMs
- Prefer long-context models (but not vendor-specific)

No vendor lock-in language.

---

# 7. Non-Negotiable Constraints

When creating or modifying skills:

- Do not remove required sections.
- Do not simplify structure.
- Do not collapse guardrails.
- Do not omit failure patterns.
- Do not weaken output contract clarity.
- Do not introduce vendor-specific dependencies without explicit declaration.

If unsure → prefer stricter structure.

---

# 8. UX Sentinel (System Skill Case Study)

UX Sentinel is a System Skill.

It:

- Operates conversation-wide
- Tracks recurrence counts
- Syncs to external Notion database
- Requires deduplication safeguards
- Must prevent duplicate creation

This skill demonstrates:

- Stateful logic
- External side effects
- Persistent knowledge accumulation
- Guardrail-driven automation

System skills interacting with external systems must:

- Re-query before write
- Prevent duplicate entries
- Avoid race-condition duplication
- Avoid vague concept registration

---

# 9. What This Repository Is NOT

This repository is NOT:

- A list of “best prompts”
- A creativity showcase
- A marketing artifact
- A vendor-tuned prompt hack collection
- A model-specific optimization playground

It is a structured workflow framework.

---

# 10. Engineering Intent

The goal is to build:

A lightweight LLM decision framework.

Consistency > Style  
Determinism > Eloquence  
Guardrails > Optimism

If structure degrades,
the repository loses its core value.

Maintain discipline.
