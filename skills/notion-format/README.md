# Notion Format

Format content into richly structured Notion documents
with automatic content-type detection.

This skill:

- Detects content type (tech-doc, meeting-notes, analysis, tutorial, bug-report)
- Applies appropriate formatting templates with sections, code blocks, tables, callouts, quotes, mermaid diagrams, and emojis
- Adapts formatting depth to content length (short → callout-heavy, long → toggle sections)
- Outputs a well-structured Notion-ready document
- Optionally publishes to Notion via MCP (API-post-page / API-patch-block-children)

---

## Why

Asking an agent to "organize this in Notion" without specifying format
often results in plain, flat text with no visual structure. This skill
ensures every Notion document gets the right formatting elements for
its content type — automatically.

---

## Supported Content Types

| Type | Key Elements |
|---|---|
| `bug-report` 🐛 | timeline table, error code block, severity callout |
| `meeting-notes` 📋 | agenda list, action item table, quote |
| `tutorial` 📖 | numbered steps, code block, tip callout, FAQ table |
| `tech-doc` 🏗️ | mermaid diagram, code block, spec table |
| `analysis` 📊 | summary callout, data table, conclusions |
| `general` 📝 | section headings, bullet lists, callouts |

Types are listed in detection priority order (first match wins).

---

## Structure

- [SKILL.md](SKILL.md) — Main skill
