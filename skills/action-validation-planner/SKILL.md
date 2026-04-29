---
name: action-validation-planner
description: >
  Convert analysis, architecture decisions, or design notes into a compact,
  execution-ready action and validation plan for coding agents. Optimized for
  performance-sensitive backend/data engineering tasks and Claude-to-Codex
  handoffs.
license: MIT
compatibility:
  - Claude Code
  - Codex CLI
  - Cursor
metadata:
  type: execution
  category: planning
  maturity: draft
  estimated_time: 5 min
---

# Skill: Action Validation Planner

**Type:** Execution / Handoff

## Purpose

Transform a reasoning output, design decision, bug analysis, or architecture note into a **bounded implementation plan** that another CLI coding agent can execute safely.

The generated plan must include:

- what to inspect,
- what to change,
- what not to change,
- how to test correctness,
- how to measure performance,
- how to detect failure,
- how to roll back,
- a compact execution prompt for Codex or another coding agent.

This skill is optimized for work where **performance and correctness matter**, especially backend/data engineering tasks such as ClickHouse queries, Delta Lake integrations, DDS/Kafka pipelines, WASM UDFs, Docker/WSL workflows, and ETL systems.

---

## When to Use

Use this skill when the user asks for any of the following:

- Convert a design into an implementation plan.
- Add Action / Validation / Rollback sections to a recipe.
- Prepare a Codex-ready prompt from Claude's analysis.
- Make a plan that includes testing and performance checks.
- Turn an explanation into executable steps.
- Define how to validate a query, pipeline, API, or system change.
- Prepare a safe agent handoff between planning and implementation.

Also use it when the task has at least one of these signals:

- database query optimization,
- ETL or data pipeline change,
- concurrency or memory concern,
- Docker/Kubernetes/runtime environment change,
- distributed system behavior,
- file or schema migration,
- performance benchmark,
- production-impacting refactor.

---

## When NOT to Use

Do not use this skill for:

- pure conceptual explanation,
- short answers with no implementation target,
- casual advice,
- non-technical writing,
- trivial edits where validation is obvious,
- tasks where no repository, command, file, query, or runtime exists.

If the user only wants explanation, answer normally. Do not force an execution plan.

---

## Core Principle

The output must be **short enough to be pasted into another agent**, but complete enough that the agent does not need to guess.

Prefer:

- concrete files over broad descriptions,
- concrete commands over vague testing advice,
- measurable performance checks over subjective claims,
- bounded scope over open-ended exploration,
- explicit assumptions over invented facts.

Avoid:

- long background lectures,
- repeating the original analysis,
- generic best practices not tied to the task,
- commands that may damage the environment,
- broad refactors unless the task requires them.

---

## Input Handling

### Required Input

At least one of the following must be available:

- design notes,
- bug analysis,
- architecture decision,
- target behavior,
- code change request,
- performance problem,
- query/pipeline/API example.

### Useful Optional Inputs

Use these if available:

- repository path,
- stack/language,
- target files,
- current command used to run the system,
- failing logs,
- sample input/output,
- benchmark baseline,
- deployment/runtime constraints.

### Missing Information Policy

Do not block on missing information unless execution would be unsafe.

If details are missing, include an **Assumptions / Unknowns** section and produce a best-effort plan.

Ask a follow-up only when one of these is true:

- the target repository or system is ambiguous,
- multiple destructive paths are possible,
- validation requires credentials or production access,
- the user explicitly asks for exact commands but no stack/runtime is known.

---

## Output Modes

Select one output mode based on task size.

### Mode A — Compact Handoff

Use for small to medium tasks.

Sections:

1. Task Summary
2. Scope
3. Action Plan
4. Validation Plan
5. Rollback Plan
6. Codex Execution Prompt

### Mode B — Performance-Sensitive Handoff

Use when performance, query speed, memory, throughput, latency, or large data is involved.

Sections:

1. Task Summary
2. Assumptions / Unknowns
3. Scope
4. Action Plan
5. Correctness Validation
6. Performance Validation
7. Failure Modes
8. Rollback Plan
9. Codex Execution Prompt

### Mode C — High-Risk Handoff

Use when auth, secrets, migrations, infra, production, distributed systems, or data loss are involved.

Sections:

1. Task Summary
2. Risk Summary
3. Assumptions / Unknowns
4. Scope / Non-Goals
5. Action Plan
6. Correctness Validation
7. Performance / Load Validation
8. Observability Checks
9. Failure Modes
10. Rollback Plan
11. Codex Execution Prompt

---

## Mode Selection Rules

Choose Mode B if any keyword or context suggests:

- performance,
- latency,
- throughput,
- CPU,
- memory,
- query speed,
- ClickHouse,
- Delta Lake,
- ETL,
- benchmark,
- batch size,
- concurrency,
- index,
- partition,
- aggregation,
- WASM/UDF.

Choose Mode C if any keyword or context suggests:

- production,
- migration,
- schema change,
- secrets,
- auth,
- permissions,
- Kubernetes,
- Docker runtime base image,
- distributed system,
- DDS/Kafka delivery semantics,
- data loss,
- rollback risk,
- irreversible command.

If both B and C match, choose C.

If unsure, choose B for engineering work.

---

## Procedure

### Step 1 — Extract the Task

Identify and compress the task into 1–3 sentences.

Include:

- objective,
- target system,
- expected outcome,
- main risk.

Do not repeat the full user prompt.

### Step 2 — Identify Scope

Split scope into three groups.

#### Inspect First

Files, directories, commands, or queries the implementation agent should inspect before editing.

Examples:

```text
- Dockerfile / docker-compose.yml
- src/**/*.rs
- udf configuration files
- ClickHouse function config
- existing integration tests
```

#### Likely to Modify

Files expected to change.

If unknown, list patterns instead of inventing exact paths.

#### Do Not Touch

Always include safety boundaries.

Default boundaries:

```text
- .env, .env.*, secrets, credentials
- generated files unless required
- unrelated formatting changes
- production data
- destructive cleanup commands
```

### Step 3 — Build the Action Plan

The Action Plan must be ordered and minimal.

Use this structure:

```text
1. Check current repository state.
2. Inspect existing implementation and tests.
3. Make the smallest code/config/query change that satisfies the task.
4. Add or update focused tests.
5. Run validation commands.
6. Summarize changed files and results.
```

For performance-sensitive tasks, include:

```text
- capture baseline before changing,
- change only one variable at a time when possible,
- compare output equality before comparing speed,
- report measurement environment and caveats.
```

### Step 4 — Define Correctness Validation

Correctness validation must prove that behavior did not regress.

Prefer exact commands.

Common command patterns:

```bash
git status --short
git diff --stat
git diff --check
```

Language-specific examples:

```bash
go test ./...
cargo test
cargo clippy --all-targets -- -D warnings
python -m pytest
npm test
npm run lint
mvn test
gradle test
```

Database/query examples:

```bash
clickhouse-client --query "SELECT 1"
clickhouse-client --queries-file ./queries/validation.sql
```

If exact commands are unknown, instruct the agent to discover existing commands from:

```text
- README.md
- Makefile
- package.json
- pyproject.toml
- Cargo.toml
- go.mod
- docker-compose.yml
- CI workflow files
```

### Step 5 — Define Performance Validation

Performance validation must be concrete and avoid fake precision.

Require baseline and after-change measurement when possible.

#### Basic CLI Timing

```bash
/usr/bin/time -v <command>
```

#### ClickHouse Query Timing

```bash
clickhouse-client --time --query "<query>"
```

#### ClickHouse Query Log

```sql
SELECT
    query_duration_ms,
    read_rows,
    read_bytes,
    memory_usage,
    query
FROM system.query_log
WHERE type = 'QueryFinish'
ORDER BY event_time DESC
LIMIT 10;
```

#### Docker Resource Check

```bash
docker stats --no-stream
```

#### Rust Benchmark Hint

```bash
cargo test --release
cargo bench
```

#### Go Benchmark Hint

```bash
go test -bench=. -benchmem ./...
```

Performance output must include:

- baseline command,
- after-change command,
- measured metric,
- number of runs if repeated,
- caveat if environment is local or noisy.

Do not claim performance improvement without measurement.

### Step 6 — Define Failure Modes

List likely failure modes tied to the task.

Examples:

```text
- result mismatch: aggregation/filter condition changed semantics
- slower query: predicate pushdown or partition pruning no longer works
- memory spike: larger intermediate aggregation state
- Docker failure: runtime library missing from image
- DDS compatibility issue: QoS/profile mismatch between versions
- WASM failure: ABI/runtime mismatch
```

Keep this section short and specific.

### Step 7 — Define Rollback Plan

Rollback must be safe.

Default local rollback:

```bash
git status --short
git checkout -- <changed-file>
```

For all local changes:

```bash
git restore .
git clean -fd
```

Use `git clean -fd` only with a warning because it deletes untracked files.

For migration/config/runtime tasks, include task-specific rollback:

```text
- revert config file to previous value,
- stop new container and restart previous image tag,
- disable new UDF registration,
- restore previous query path,
- do not drop or rewrite production data.
```

Never suggest destructive production rollback without explicit backup/restore details.

### Step 8 — Produce Codex Execution Prompt

The final section must be copy-ready.

It must include:

- role,
- scope,
- constraints,
- ordered steps,
- commands to run,
- reporting format.

Keep it concise. Avoid unnecessary explanation.

Template:

```text
Follow AGENTS.md and the rules below.

Task:
<one-paragraph task summary>

Scope:
- Inspect first: <items>
- Likely modify: <items>
- Do not touch: <items>

Implementation:
1. Run git status --short.
2. Inspect existing code/config/tests before editing.
3. Make the minimal change needed.
4. Add or update focused tests.
5. Run validation commands.
6. Report results.

Validation commands:
<commands>

Performance checks:
<commands or 'Not applicable'>

Rollback:
<rollback steps>

Report back with:
- Changed files
- Commands run
- Correctness result
- Performance result
- Remaining risks
```

---

## Token Efficiency Rules

This skill must save tokens by default.

### Required Compression

- Summarize the task in 1–3 sentences.
- Do not repeat long source analysis.
- Use tables only when they reduce text.
- Use placeholders for unknown paths instead of inventing many examples.
- Keep examples short unless user asks for detailed examples.
- Put the final reusable prompt at the end only once.

### Do Not Include

- full tutorial explanations,
- broad technology background,
- long lists of every possible test command,
- unrelated best practices,
- duplicate Action Plan and Codex Prompt content with different wording.

### Expand Only When

The user explicitly asks for:

- very detailed version,
- reusable template,
- team standard document,
- onboarding documentation.

---

## Safety Guardrails

Always include these constraints unless clearly irrelevant:

```text
- Do not modify .env, secrets, credentials, or unrelated files.
- Do not run destructive commands without explicit approval.
- Do not rewrite history.
- Do not change production data.
- Prefer minimal diff.
- Stop and report if validation requires missing credentials or external access.
```

For Docker and system tasks, additionally include:

```text
- Do not use sudo unless explicitly required and approved.
- Do not pipe remote scripts directly into shell.
- Prefer pinned versions over latest for reproducibility.
```

For database tasks, additionally include:

```text
- Validate result equality before measuring speed.
- Avoid destructive DDL/DML on production data.
- Use sample/local/test data unless user explicitly provides safe target.
```

---

## Quality Bar

A valid output must answer:

- What exactly should be done?
- Where should the agent look first?
- What is allowed to change?
- What is forbidden?
- How will correctness be proven?
- How will performance be measured?
- What can fail?
- How can we roll back?
- What should Codex report after execution?

If any answer is missing, the plan is incomplete.

---

## Output Template

Use this template unless the user asks for a different format.

```markdown
# Action Validation Plan

## 1. Task Summary
<1–3 sentences.>

## 2. Assumptions / Unknowns
- <Only list important assumptions. Omit if none.>

## 3. Scope

### Inspect First
- <file/dir/command/query>

### Likely to Modify
- <file/dir/pattern>

### Do Not Touch
- .env, .env.*, secrets, credentials
- unrelated files or broad formatting changes
- production data or destructive commands

## 4. Action Plan
1. Run `git status --short`.
2. Inspect the existing implementation and tests.
3. Capture baseline behavior/performance if relevant.
4. Apply the minimal change.
5. Add or update focused tests.
6. Run validation and summarize results.

## 5. Correctness Validation
```bash
<commands>
```

Expected result:
- <expected behavior>

## 6. Performance Validation
```bash
<commands or Not applicable>
```

Metrics:
- <latency/throughput/memory/read_rows/read_bytes/etc.>

## 7. Failure Modes
- <specific failure mode and likely cause>

## 8. Rollback Plan
```bash
git status --short
git checkout -- <changed-file>
```

## 9. Codex Execution Prompt
```text
Follow AGENTS.md and the rules below.

Task:
<task summary>

Scope:
- Inspect first: <items>
- Likely modify: <items>
- Do not touch: .env, secrets, credentials, unrelated files, production data

Implementation:
1. Run git status --short.
2. Inspect existing code/config/tests before editing.
3. Capture baseline if performance is relevant.
4. Make the minimal change needed.
5. Add or update focused tests.
6. Run validation commands.
7. Report results.

Validation commands:
<commands>

Performance checks:
<commands or Not applicable>

Rollback:
<steps>

Report back with:
- Changed files
- Commands run
- Correctness result
- Performance result
- Remaining risks
```
```

---

## Examples

### Example 1 — ClickHouse Query Optimization

User intent:

> Convert this ClickHouse WHERE vs sumIf analysis into a Codex-ready test plan.

Expected output characteristics:

- Choose Mode B.
- Include baseline query and candidate query.
- Validate result equality first.
- Measure `query_duration_ms`, `read_rows`, `read_bytes`, `memory_usage`.
- Do not claim one query is faster before measurement.

Validation commands may include:

```bash
clickhouse-client --time --query "<baseline query>"
clickhouse-client --time --query "<candidate query>"
```

Query-log check:

```sql
SELECT
    query_duration_ms,
    read_rows,
    read_bytes,
    memory_usage,
    query
FROM system.query_log
WHERE type = 'QueryFinish'
ORDER BY event_time DESC
LIMIT 10;
```

### Example 2 — WASM UDF Runtime Change

User intent:

> Prepare an implementation plan for testing WasmEdge vs Wasmtime in a ClickHouse UDF Docker sample.

Expected output characteristics:

- Choose Mode C if Docker base image/runtime config changes.
- Inspect Dockerfile, docker-compose.yml, UDF config, sample SQL, README.
- Validate container startup, function registration, sample query result.
- Measure cold start, query runtime, memory.
- Roll back by reverting runtime config and image tag.

### Example 3 — DDS Version Compatibility Test

User intent:

> Prepare Codex instructions for testing RTI Connext 7.7 → 7.3 → 7.7 message transfer.

Expected output characteristics:

- Choose Mode C due to distributed compatibility and data-loss risk.
- Explicitly define publisher/subscriber matrix.
- Validate QoS/profile compatibility.
- Include packet/log capture commands if available.
- Compare message count, order, latency, serialization compatibility.
- Avoid modifying production DDS profiles.

---

## Failure Patterns

Bad outputs include:

- no validation commands,
- performance claims without measurement,
- broad refactor instructions,
- missing rollback plan,
- missing forbidden-file constraints,
- generic failure modes not tied to the task,
- asking unnecessary questions despite enough context,
- copying long analysis into the Codex prompt,
- using destructive commands as default rollback,
- failing to validate data/query result equality before speed comparison.
