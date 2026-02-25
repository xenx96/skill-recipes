# System Skill Title

**Category:**  
**Type:** System (Persistent / Automation)  
**Maturity:** Draft / Stable / Production  
**Activation:** automatic / command-driven / hybrid  
**State:** stateless / conversation-wide / external DB-backed  
**Dependencies:** (e.g., Notion MCP)

---

## Purpose

What continuous behavior this skill provides.

---

## Scope

When this skill should be active and what it should ignore.

**Triggers:**

-
-

**Non-triggers:**

-
-

---

## Inputs / Signals

What inputs it reads:

- Conversation content
- Manual commands
- External sources (DB, APIs)

---

## Core Behavior

### 1) Detection / Intake

- Normalization rules
- De-duplication rules

### 2) Decision Logic

- Thresholds
- Gating conditions
- Override commands

### 3) Actions

- Create/update records
- Notify/propose/ask
- Link/relate entities

---

## Output / Side Effects

Define exact outputs:

- Messages shown to the user
- External writes (DB fields, relations, counts)

---

## Guardrails

- Avoid duplicate creation (re-query before write).
- Do not treat vague words as concepts.
- Never write secrets/PII.
- Prefer conservative proposals over spam.

---

## Failure Patterns

- Duplicate entries due to alias mismatch
- Over-triggering on generic terms
- Missing updates because of strict matching

---

## Example 1 (Automatic Trigger)

**Input (conversation snippet):**

**Expected behavior:**

---

## Example 2 (Manual Command)

**Input command:**

**Expected behavior:**

---

## Notes

Migration, schema requirements, operational considerations.
