# Action Validation Planner

Convert an analysis or design decision into an execution-ready plan for coding agents such as Codex, Claude Code, Cursor, or other CLI agents.

This skill focuses on **performance-sensitive engineering work** where an answer must not stop at explanation. It produces a compact but complete handoff containing:

- Implementation scope
- Minimal-diff action plan
- Validation commands
- Performance checks
- Correctness checks
- Failure modes
- Rollback plan
- Copy-ready execution prompt for another agent

---

## Why

Many agent outputs are good for reasoning but weak for execution. They explain the idea, but they do not tell another agent exactly:

- which files to inspect first,
- which files may be changed,
- what must not be touched,
- which commands prove the change is correct,
- how to measure performance impact,
- how to roll back safely.

This skill closes that gap. It turns a design into a **bounded, testable, performance-aware work order**.

---

## Best Fit

Use this skill for:

- Backend/data engineering changes
- Query optimization
- ETL/data pipeline changes
- ClickHouse, Delta Lake, DDS, Kafka, WASM UDF, Docker, Kubernetes work
- Refactors where regression risk matters
- Claude → Codex handoff flows
- Any task where performance, correctness, or rollback matters

---

## Not for

Do not use this skill for:

- Pure conceptual explanations
- Brainstorming with no implementation target
- Simple one-line edits
- Non-technical writing tasks
- Tasks where no repository, command, or validation path exists

---

## Output Philosophy

The output must be:

1. **Executable** — another CLI agent can act on it directly.
2. **Bounded** — scope and non-goals are explicit.
3. **Verifiable** — correctness and performance checks are specified.
4. **Token-efficient** — no repeated background explanation unless needed.
5. **Safe** — destructive commands, secrets, and unrelated files are protected.

---

## Structure

- [SKILL.md](SKILL.md) — Main skill definition and operating procedure
- [README.ko.md](README.ko.md) — Korean documentation

---

## Typical Output Sections

1. Task Summary
2. Assumptions / Unknowns
3. Scope
4. Action Plan
5. Validation Plan
6. Performance Plan
7. Failure Modes
8. Rollback Plan
9. Codex Execution Prompt

---

## Example Use

User asks:

> Claude produced this design. Convert it into a Codex-ready implementation and validation plan.

The skill returns:

- files to inspect,
- files likely to modify,
- ordered implementation steps,
- exact test/build/query commands,
- performance measurement commands,
- rollback commands,
- final prompt to paste into Codex.

