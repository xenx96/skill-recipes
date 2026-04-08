# CJK Text Wrap Audit

Diagnose and fix CJK (Korean, Japanese, Chinese) text-wrapping bugs in
web UIs through a layered, evidence-first audit. Produces a structured
diagnosis and verification plan before any code is changed.

This skill:

- Captures the symptom precisely (locale, breakpoint, zoom, screenshot)
- Dumps the offending translation string as Unicode codepoints to
  surface hidden NBSP / ZWJ / soft hyphens
- Traces the computed `word-break` / `overflow-wrap` / `text-wrap`
  cascade to find the *winning* declaration
- Identifies UI-library injectors (Ant Design `cssinjs`, MUI, Mantine,
  Chakra, …) that override global rules
- Proposes the minimum number of fix layers — global cascade →
  library override → headline balancing → translation NBSP
- Verifies the fix across a zoom × breakpoint × locale × theme matrix

---

## Why

CJK wrap bugs are a class of cross-cutting cascade defects: a missing
`word-break` rule on `body`, a UI-library `cssinjs` rule that wins on
specificity, an over-eager `text-wrap` algorithm, and a translation
string with no phrase boundary can each independently cause text to
shatter mid-syllable or strand a single glyph at line edge.

Ad-hoc fixes (`<br>` tags, `!important`, hardcoded widths,
`:where()` overrides that silently lose) leave the next engineer to
rediscover the same problem. This skill turns the recurring debugging
journey into a fixed sequence of gates so the audit produces an
evidence-backed report — not guesses.

---

## Procedure (7 Gates)

0. **Symptom Capture** — collect screenshot, URL, locale, breakpoint,
   browser, and zoom. Halt if any are missing.
1. **Raw String Forensics** — dump the translation string as Unicode
   codepoints; mark phrase boundaries.
2. **Computed Style Inspection** — trace the cascade for `word-break`,
   `overflow-wrap`, `text-wrap`, `hyphens`, `line-break`. Identify the
   *winning* declaration with its specificity.
3. **Override Tracing** — identify UI-library `cssinjs` injectors and
   pick a safe override location (doubled-class trick, never `:where()`,
   never `!important`).
4. **Layered Fix Proposal** — propose the minimum layers needed:
   global cascade → library override → headline `text-balance` →
   translation NBSP. Stop at the first layer that resolves the symptom.
5. **Verification Matrix** — re-test across zoom × breakpoint ×
   locale × theme. The fix is complete only when every cell passes
   (including a Latin-locale control).
6. **Approval Gate** — present the report and wait for explicit user
   approval before editing code.

---

## Structure

- [SKILL.md](SKILL.md) — Main skill
- [README.ko.md](README.ko.md) — 한국어 설명서
