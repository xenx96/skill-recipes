# Remy Skill Recipes

Engineering-grade skill recipes for working with LLMs.

This repository is a curated collection of reusable, structured prompt workflows
designed for software engineering tasks — debugging, documentation, review,
research, automation, and system analysis.

Each skill follows the [SKILL.md open standard](https://agentskills.io/) —
compatible with Claude Code, Cursor, Codex, Gemini CLI, and 27+ AI agents.

---

## Quick Start

### Browse

```
skills/
├── architecture-spec/SKILL.md          (+ subskills/)
├── change-reaudit/SKILL.md
├── competitive-feature-benchmark/SKILL.md
├── docs-finalize-and-commit/SKILL.md
├── finalize-and-commit/SKILL.md
├── oss-code-analysis/SKILL.md
└── ux-sentinel/SKILL.md
```

### Install a skill

Copy a skill folder to your agent's skills directory:

```bash
# Cursor
cp -r skills/change-reaudit ~/.cursor/skills/

# Claude Code
cp -r skills/change-reaudit ~/.claude/skills/
```

The agent will automatically discover and activate the skill when a matching task appears.

### Use directly

1. Identify whether your task needs:
   - An **Execution Skill** (single-run workflow), or
   - A **System Skill** (persistent / automation behavior).
2. Read the **Inputs Required** section carefully.
3. Provide complete context.
4. Validate output using the skill's checklist.

Most bad outputs come from incomplete inputs.

---

## Skill Format

Every skill is a folder containing a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: change-reaudit
description: >
  Re-audit code changes to identify side effects, regression risks,
  and unhandled edge cases before merging or deploying.
license: MIT
compatibility:
  - Claude Code
  - Cursor
metadata:
  type: execution
  category: review
  maturity: draft
  estimated_time: 10 min
---
```

Agents read only `name` and `description` during discovery (~100 tokens).
The full markdown body loads on activation (<5000 tokens).

---

## Skill Types

### 1. Execution Skills

Single-run structured workflows.

Used for:

- Code review
- Change auditing
- Competitive benchmarking
- Documentation writing
- Refactoring validation

These skills:

- Require explicit inputs
- Produce structured outputs
- Contain guardrails and failure patterns
- Include realistic examples

---

### 2. System Skills

Persistent or automation-oriented behaviors.

Used for:

- Continuous concept detection
- Knowledge tracking
- External DB synchronization
- Conversation-wide logic

These skills:

- Define activation rules
- Maintain state (conversation or external DB)
- Specify side effects explicitly
- Include operational guardrails

---

## Skill Categories

| Category      | Description                        |
| ------------- | ---------------------------------- |
| review        | Change audits, regression analysis |
| research      | Competitive feature analysis       |
| cleanup       | Refactor and commit structuring    |
| documentation | Architecture specs, design docs    |
| automation    | Persistent or DB-connected skills  |

---

## Skill Structure

### Execution Skill Structure

- Purpose
- When to Use
- When NOT to Use
- Inputs Required
- Output Format
- Procedure
- Guardrails
- Failure Patterns
- Examples (minimum 2)

---

### System Skill Structure

- Purpose
- Scope (triggers / non-triggers)
- Inputs / Signals
- Core Behavior (Detection → Decision → Action)
- Output / Side Effects
- Guardrails
- Failure Patterns
- Examples

---

## Skill Maturity Levels

- Draft — experimental
- Stable — reliable for repeated use
- Production — validated in real workflows

---

## Model Assumptions

Skills are model-agnostic.

Assume:

- A reasoning-capable LLM
- Structured context input
- Long-context support preferred

---

## Philosophy

LLMs are unreliable without structure.

Structure reduces:

- Hallucination
- Ambiguity
- Context loss
- Overconfidence errors

Prompting is engineering.

System skills extend this philosophy
into persistent decision-memory patterns.

---

## Contribution

This repository is primarily maintained for personal reuse,
but high-quality pull requests are welcome.

Rules:

- Use the correct template (`_template/execution-template.md` or `_template/system-template.md`)
- Follow the SKILL.md standard (YAML frontmatter required)
- Include realistic examples
- Document guardrails and failure patterns

---

## License

MIT
