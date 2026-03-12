# UX Sentinel

Continuously detect recurring UI/UX concepts during frontend discussions,
track conversation-wide recurrence, and register repeated concepts as
structured knowledge assets in a Notion database via MCP.

This skill:

- Detects UI/UX concepts in conversation with normalization and alias mapping
- Tracks recurrence globally across the conversation (threshold: 2)
- Proposes registration when threshold is met, with category, definition, and decision rules
- Writes structured entries to Notion `UI/UX Knowledge Base` database
- Supports manual commands: `@ux save`, `@ux skip`, `@ux link`
- Falls back to local-only tracking when Notion is unavailable

---

## Why

Design decisions repeat. The same UX principle surfaces across different features,
different conversations, different sprints. Without structured tracking,
these recurring patterns stay in people's heads and get re-debated every time.
UX Sentinel builds a decision-making memory system from repeated UI friction signals.

---

## How It Works

This is a **System Skill** — it runs continuously during frontend discussions,
not as a one-time execution.

1. **Detect** — recognize UI/UX concepts as they appear in conversation
2. **Track** — count recurrence across the entire conversation
3. **Propose** — when a concept appears twice, propose registration with actionable decision rules
4. **Register** — on user approval, create a structured Notion entry

---

## Notion Integration

Requires a `UI/UX Knowledge Base` database in Notion with properties:
Concept, Category, Recurrence Count, First Seen, Last Seen,
Trigger Context, UI Decision Rule, Product Context, Maturity, Related Concepts.

The database is auto-bootstrapped on first use if it does not exist.

---

## Structure

- [SKILL.md](SKILL.md) — Main skill
