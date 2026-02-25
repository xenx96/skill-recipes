# Skill: Finalize Changes and Commit (Cleanup, Deduplication, Hardcoded Audit)

**Category:** cleanup  
**Type:** Execution  
**Maturity:** Draft  
**Estimated Time:** 15 min  
**Model Assumption:** Model-agnostic

---

## Purpose

Finalize current changes for production readiness.

Tasks:

- Remove duplicate logic
- Eliminate unnecessary code
- Audit and resolve hardcoded values
- Ensure consistency and build integrity
- Prepare structured commits

---

## When to Use

- Before committing finalized work to a shared branch
- Before submitting a pull request for review
- After completing a refactoring session that touched multiple files
- When preparing a clean commit history from messy working changes

---

## When NOT to Use

- Work-in-progress code that is still actively being developed
- Trivial single-line fixes (typo, formatting) that need no audit
- Initial prototyping or exploratory coding phases
- Changes already reviewed and approved through another skill

---

## Inputs Required

Do not run this skill without:

- [ ] Working tree with uncommitted or staged changes
- [ ] Access to project build, lint, and test commands
- [ ] Knowledge of project commit conventions (if any)

Optional but recommended:

- [ ] Target branch context (e.g., main, release)
- [ ] List of intended change scope (files or modules)

---

## Output Format

1. Issues Found
2. Actions Taken
3. Verification Results
4. Commit Plan
5. Final Commit Messages

---

## Procedure

### Gate 0 – Working Set Validation

- Confirm modified files match intended scope
- Ensure no unintended changes are included
- Validate new/deleted files do not break entrypoints

---

### Gate 1 – Duplicate & Dead Code Detection

- Identify repeated logic blocks
  - If repeated ≥ 3 times → extract helper
  - Avoid over-abstraction
- Remove:
  - Unused variables
  - Dead branches
  - Debug prints
  - Stale TODOs without references

---

### Gate 2 – Hardcoded Value Audit

Classify hardcoded values into:

A) Algorithmic constants → Extract to named constant + documentation  
B) Operational policies → Move to config/env + default fallback  
C) Test-only values → Restrict to test scope

Ensure:

- No hidden policy decisions remain hardcoded
- Retry limits, timeouts, thresholds are explicit

---

### Gate 3 – Consistency & Quality Review

Verify:

- Error handling patterns consistent
- Logging structure aligned with project conventions
- No PII/secrets exposed
- Public interface compatibility preserved
- No accidental performance regression

---

### Gate 4 – Verification Proof

Run relevant project checks:

- Tests
- Lint
- Typecheck
- Build

If failures occur:

- Fix root cause
- Do not silence or bypass checks

---

### Gate 5 – Commit Structuring

Separate commits logically:

1. Refactor (no behavior change)
2. Functional change
3. Tests / documentation

Use Conventional Commits:

- fix(scope):
- feat(scope):
- refactor(scope):
- test(scope):
- docs(scope):
- chore(scope):

Each commit must explain:

- What changed
- Why it changed
- Risk considerations (if any)
- Test proof

---

## Guardrails

- Do not silence or bypass failing checks.
- Do not combine unrelated changes in a single commit.
- Do not over-abstract when extracting helpers (repeated ≥ 3 times threshold).
- Explicitly state assumptions when classifying hardcoded values.
- If context is insufficient to determine intent, ask for clarification.
- Do not remove code without verifying it is truly unused.
- Respect existing project conventions for commit messages and structure.

---

## Failure Patterns

Common bad outputs:

- Lumping all changes into a single large commit without logical separation
- Skipping build/lint/test verification before committing
- Ignoring hardcoded values because they "look fine"
- Over-extracting helpers for code repeated only once or twice
- Removing code that appears dead but is used via reflection or dynamic imports
- Producing commit messages that describe "what" but not "why"

---

## Example 1 (Minimal Context)

**Input:**

3 files changed: a utility function was refactored, an unused import was found, and a debug `console.log` was left in.

**Output:**

1. Issues Found: unused import in `utils/parse.ts`, debug log in `api/handler.ts`
2. Actions Taken: removed unused import, removed debug log
3. Verification Results: lint pass, tests pass, build pass
4. Commit Plan: single refactor commit (scope is small)
5. Final Commit Messages: `refactor(utils): clean up unused import and debug log`

---

## Example 2 (Realistic Scenario)

**Input:**

12 files changed across 3 modules. Includes a retry timeout hardcoded as `3000`, duplicated validation logic in 4 handlers, and a new API endpoint.

**Output:**

1. Issues Found: hardcoded retry timeout (3000ms) in `services/retry.ts`, duplicated input validation in 4 route handlers, unused helper `formatLegacy` in `utils/format.ts`
2. Actions Taken: extracted retry timeout to config (`RETRY_TIMEOUT_MS`), created shared `validateInput()` helper, removed `formatLegacy`
3. Verification Results: all tests pass, lint pass, typecheck pass, build pass
4. Commit Plan: 3 commits — (a) refactor: extract shared validation, (b) refactor: move retry timeout to config, (c) feat: add new API endpoint
5. Final Commit Messages:
   - `refactor(validation): extract shared validateInput helper from route handlers`
   - `refactor(retry): move hardcoded timeout to config as RETRY_TIMEOUT_MS`
   - `feat(api): add POST /items endpoint with input validation`

---

## Notes

**FAST MODE** (only if explicitly requested):

- Skip deep hardcoded classification
- Allow single commit only if scope is small
