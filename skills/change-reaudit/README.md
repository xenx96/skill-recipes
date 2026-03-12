# Change Re-Audit

Re-audit code changes to identify side effects, regression risks,
and unhandled edge cases before merging or deploying.

This skill:

- Breaks changes into logical Change Units
- Evaluates side effects across 7 risk dimensions
- Builds an edge case verification matrix
- Identifies regression gaps and proposes minimal test additions
- Classifies findings as P0 / P1 / P2 with file:line evidence

---

## Why

Code reviews catch obvious issues. But side effects, hidden regressions,
and edge cases often slip through — especially in complex refactors
or multi-module changes. This skill provides a systematic second pass
with structured risk analysis.

---

## Procedure (5 Gates)

0. **Change Mapping** — decompose diff into Change Units
1. **Side Effect Analysis** — public contracts, state mutations, concurrency, resources, security, observability, operational risk
2. **Edge Case Matrix** — null/empty, boundaries, large inputs, partial failures, duplicates, permissions, backward compatibility
3. **Regression Proof** — covered vs uncovered scenarios, minimal test proposals
4. **Code Hygiene Check** — dead code, unnecessary abstraction, silent drift

---

## Structure

- [SKILL.md](SKILL.md) — Main skill
