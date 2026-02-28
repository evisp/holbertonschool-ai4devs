# Prompt Use Cases

## Category 1: Code Quality
- **Use Case: Refactoring for readability**
  - **Goal**: Improve maintainability and clarity without changing external behavior.
  - **Input**: A code snippet (function/class/module) in [LANGUAGE], plus a short note describing expected behavior and any constraints (public API must remain stable).
  - **Expected output**: Refactored code that preserves behavior, plus a short explanation of changes and why they improve readability.

- **Use Case: Performance optimization**
  - **Goal**: Reduce runtime latency and/or memory usage in a target code path.
  - **Input**: The slow code section in [LANGUAGE], representative input sizes, and a constraint (e.g., “must stay O(n log n)” or “no new dependencies”).
  - **Expected output**: An optimized implementation, with a brief complexity/performance discussion and any trade-offs (readability vs speed).

- **Use Case: Security hardening**
  - **Goal**: Identify and fix security weaknesses in application code.
  - **Input**: The relevant endpoints/functions, how data enters the system (request params/body/files), and the security context (authn/authz model, framework).
  - **Expected output**: A list of concrete vulnerabilities found, patched code changes, and recommended mitigations (validation, escaping, headers, secrets handling).

## Category 2: Debugging
- **Use Case: Root-cause analysis**
  - **Goal**: Determine the most likely cause of a bug and propose a fix.
  - **Input**: Symptom description, exact steps to reproduce, environment details (OS/runtime/version), and error logs/stack traces.
  - **Expected output**: Ranked hypotheses, the most likely root cause, and a step-by-step fix plan (including what to verify after the change).

- **Use Case: Log/trace interpretation**
  - **Goal**: Turn logs/traces into actionable next debugging steps.
  - **Input**: Log excerpts or traces (with timestamps), the component/service name, and any recent changes or deployments.
  - **Expected output**: A diagnosis narrative (what failed and where), 3–5 concrete checks to run next, and suggested instrumentation improvements if logs are insufficient.

- **Use Case: Incident mitigation**
  - **Goal**: Stabilize a degraded production system quickly and safely.
  - **Input**: Current symptoms (timeouts, error rate), service SLO/SLA targets, and a brief architecture summary (dependencies, databases, queues).
  - **Expected output**: Immediate mitigation options (rollback, feature flag off, rate limiting, timeouts), with risks, and a follow-up plan for permanent prevention.

## Category 3: Architecture & Design
- **Use Case: Architecture Decision Record (ADR)**
  - **Goal**: Decide between architectural options and document the decision.
  - **Input**: Functional requirements, non-functional requirements (performance/scalability/security), constraints (budget/timeline/stack), and the candidate options.
  - **Expected output**: An ADR-style write-up: decision, alternatives, pros/cons, risks, and a clear rationale tied to requirements.

- **Use Case: Scalability planning**
  - **Goal**: Design how a system scales from current load to projected load.
  - **Input**: Expected traffic (avg/peak), read/write ratio, data volume growth, and bottleneck suspects (DB, cache, external APIs).
  - **Expected output**: A scaling plan (caching, partitioning, async queues, horizontal scaling), plus key assumptions and limits (what breaks first).

- **Use Case: API design**
  - **Goal**: Define a consistent, maintainable API for a domain.
  - **Input**: Domain entities/resources, operations (CRUD + custom actions), authentication/authorization needs, and performance targets (rate, latency).
  - **Expected output**: API definition (endpoints or schema), example requests/responses, and an error-handling strategy (status codes, error shapes).

## Category 4: Testing & QA
- **Use Case: Test strategy creation**
  - **Goal**: Ensure appropriate coverage across unit, integration, and end-to-end tests.
  - **Input**: Component description, critical user flows, dependencies (DB/services), and release risk level (low/medium/high).
  - **Expected output**: A test strategy outlining what to test at each level, recommended tools/frameworks, and a coverage target (e.g., “80% unit for core logic”).

- **Use Case: Edge-case generation**
  - **Goal**: Identify boundary conditions and failure scenarios before release.
  - **Input**: Function signature/specification, constraints (valid ranges, nullability), and invariants (must always hold true).
  - **Expected output**: A structured list of edge cases with example inputs and the expected behavior/output for each.

- **Use Case: Regression test writing**
  - **Goal**: Prevent a previously fixed bug from reappearing.
  - **Input**: Bug report, minimal reproduction steps or sample input, and a short description of the fix.
  - **Expected output**: One or more automated regression tests (in the project’s test framework) with clear assertions and notes for CI integration.

## Category 5: Documentation
- **Use Case: Developer documentation drafting**
  - **Goal**: Produce onboarding-ready docs that engineers can follow end-to-end.
  - **Input**: System overview, prerequisites (runtime/tools), setup steps, environment variables, and common workflows.
  - **Expected output**: A Markdown document with Overview, Quick Start, configuration details, and Troubleshooting (FAQs + common errors).

- **Use Case: Code walkthrough**
  - **Goal**: Explain a codebase/module to speed up onboarding and review.
  - **Input**: Target directory/module, entry points, key abstractions, and a short description of intended behavior.
  - **Expected output**: A walkthrough describing the call flow and data flow, with key files/functions highlighted and common pitfalls called out.

- **Use Case: Release notes generation**
  - **Goal**: Communicate changes clearly to users and stakeholders.
  - **Input**: List of PRs/commits, feature flags, breaking changes, known issues, and upgrade requirements.
  - **Expected output**: Release notes including highlights, bug fixes, breaking changes, upgrade steps, and any operational notes.
