# Finalize Documentation and Commit

Finalize Docusaurus documentation changes for production readiness
by discovering existing conventions, verifying code-doc alignment,
and structuring clean commits.

This skill:

- Samples existing docs to discover conventions (tone, terminology, structure)
- Verifies code-documentation alignment when source code also changed
- Reviews format, terminology, tone, and completeness consistency
- Validates Docusaurus-specific syntax and build integrity
- Structures commits by change type: `docs(fix)`, `docs(style)`, `docs(content)`, `docs(sync)`

---

## Why

Documentation quality degrades when convention discovery is skipped.
Inconsistent terminology, broken links, and misaligned code references
erode user trust. This skill ensures every documentation commit meets
the project's established standards — inferred from the existing corpus,
not imposed from outside.

---

## Procedure (7 Gates)

0. **Working Set Validation** — isolate session changes, protect out-of-scope files
1. **Convention Discovery** — sample 10–15 existing docs to infer style, tone, terminology
2. **Code-Documentation Alignment** — map source code changes to documentation references
3. **Documentation Quality Review** — structural, terminology, tone, completeness, syntax, images, links, sidebar
4. **Auto-Fix** — apply judgment-free fixes, present judgment-required items
5. **Build Verification** — run Docusaurus build, capture output
6. **Commit Structuring** — separate commits by change type with Conventional Commits format

---

## Structure

- [SKILL.md](SKILL.md) — Main skill
