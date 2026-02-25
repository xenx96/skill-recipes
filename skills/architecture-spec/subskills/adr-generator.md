# Subskill: ADR Generator

**Parent:** [SKILL.md](../SKILL.md)  
**Role:** ADR section generation (Level C only)

---

## Purpose

Generate an Architecture Decision Record (ADR) for high-impact changes
(typically Level C).

---

## When to Use

- Security/auth changes
- Infra changes
- Schema migrations
- Global behavior changes
- Financial-impact logic

---

## Inputs

- feature_name (required)
- decision context from the diff (required)
- risk_summary from diff-risk-evaluator (required)
- repo_context (optional)

---

## ADR Template

### ADR: \<Decision Title\>

**Status:** Proposed / Accepted / Superseded

**Context:**
Describe the problem, constraints, and forces.

**Options Considered:**

| Option | Description | Pros | Cons |
|---|---|---|---|
| A | ... | ... | ... |
| B | ... | ... | ... |

**Decision:**
State the selected option clearly.

**Consequences:**

| Type | Impact |
|---|---|
| Technical | ... |
| Operational | ... |
| Security | ... |
| Long-term | ... |

**Rollback Considerations:**

- Can this be reverted?
- Data impact?
- Migration strategy?

---

## Guardrails

- Always present at least 2 realistic options (do not fabricate a strawman option just to fill the table).
- Consequences must cover all four types (Technical, Operational, Security, Long-term); write "N/A" if truly not applicable.
- Do not recommend an option without explicit justification tied to the project context.

---

## Failure Patterns

- Listing only one option and presenting it as a "decision" (no real trade-off analysis)
- Omitting rollback considerations for irreversible changes (e.g., schema migrations)
- Generic consequences not tied to the actual change (e.g., "may cause issues" without specifics)

---

## Example

**Input:**

feature_name: "Migrate user auth from session to JWT"
decision context: Replacing server-side session store with stateless JWT tokens.
risk_summary: Level C, auth + migration + multi-layer.

**Output:**

### ADR: Migrate authentication from server-side sessions to JWT

**Status:** Proposed

**Context:**
Current session-based auth requires Redis for session storage, adding operational complexity and a single point of failure. The team wants stateless auth to simplify horizontal scaling.

**Options Considered:**

| Option | Description | Pros | Cons |
|---|---|---|---|
| A | Keep sessions + Redis | No migration risk, proven | Redis SPOF, session affinity needed |
| B | JWT (access only) | Stateless, simple | No revocation without blacklist |
| C | JWT + refresh token | Stateless + revocation via refresh rotation | Higher implementation complexity |

**Decision:**
Option C — JWT with refresh token rotation. Provides stateless scaling while maintaining revocation capability through refresh token rotation.

**Consequences:**

| Type | Impact |
|---|---|
| Technical | New token refresh endpoint, refresh token storage in DB |
| Operational | Remove Redis dependency, add token expiry monitoring |
| Security | Short-lived access tokens (15min), refresh rotation mitigates theft |
| Long-term | Enables multi-service auth without shared session store |

**Rollback Considerations:**

- Revert requires restoring session table and Redis config
- Existing JWTs will be invalid after rollback; force re-login required
- Run dual-auth (session + JWT) for 1 sprint before full cutover
