# Subskill: Notion Page Publisher

**Parent:** [SKILL.md](../SKILL.md)  
**Role:** Notion publishing (Step 4 of parent skill)

---

## Purpose

Persist the generated architecture spec into Notion.

This subskill assumes Notion MCP integration is available.

---

## Inputs

- title
- content_markdown
- database_id
- level (A/B/C)
- feature_name
- risk_score
- tags (optional)

---

## Step 1 — Determine Parent

If database_id provided:
→ create page inside database

Else:
→ create page under default "Architecture Specs" parent page

---

## Step 2 — Map Properties

Example property mapping:

| Property   | Value        |
| ---------- | ------------ |
| Name       | title        |
| Level      | A/B/C        |
| Status     | Draft        |
| Risk Score | number       |
| Feature    | feature_name |
| Created At | now()        |

---

## Step 3 — Create Page

Use:

notion.create_page({
parent: { database_id },
properties: { ... },
children: markdown_to_blocks(content_markdown)
})

---

## Step 4 — ADR Handling

If level == C:

- Append ADR section to same page
  OR
- Create child page under spec

---

## Behavior

- If page already exists (same feature name, Draft status):
  → update instead of create
- Always return Notion URL

---

## Guardrails

- Do not create a page if content_markdown is empty or only whitespace.
- If Notion MCP is unavailable, skip publishing and return a warning instead of failing.
- Always verify database_id exists before attempting page creation.
- Do not overwrite pages in non-Draft status without explicit confirmation.

---

## Failure Patterns

- Creating a duplicate page instead of updating an existing Draft with the same feature name
- Silently failing when Notion MCP is unavailable instead of reporting the issue
- Publishing with missing required properties (Level, Risk Score) causing incomplete Notion entries

---

## Example

**Input:**

title: "Add rate limiting to public API — Technical Spec"
content_markdown: (generated Level B spec)
database_id: "abc123"
level: B
feature_name: "Add rate limiting to public API"
risk_score: 10

**Output:**

Notion page created: https://notion.so/add-rate-limiting-spec-xyz789
Properties: Level=B, Status=Draft, Risk Score=10, Feature="Add rate limiting to public API"
