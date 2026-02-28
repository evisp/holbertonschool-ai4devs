# Prompt Use Cases

## Category 1: Code Quality
- **Use Case: Refactoring for readability**
  - **Goal**: Improve maintainability and clarity without changing behavior
  - **Input**: Function/class/module in [LANGUAGE] + expected behavior notes
  - **Expected output**: Refactored code + brief rationale + key changes list

- **Use Case: Performance optimization**
  - **Goal**: Reduce latency and/or memory usage in a target code path
  - **Input**: Hot-path code + constraints (latency/memory) + typical input sizes
  - **Expected output**: Optimized code + complexity notes + trade-offs

- **Use Case: Security hardening**
  - **Goal**: Identify and remediate vulnerabilities (e.g., injection, authz flaws)
  - **Input**: Relevant code paths + threat model assumptions + frameworks used
  - **Expected output**: Findings list + patched code + mitigation recommendations

## Category 2: Debugging
- **Use Case: Root-cause analysis**
  - **Goal**: Determine why a bug occurs and how to reproduce it reliably
  - **Input**: Symptom description + environment + repro steps + logs/traces
  - **Expected output**: Ranked root-cause hypotheses + most likely cause + fix plan

- **Use Case: Log/trace interpretation**
  - **Goal**: Convert noisy logs into actionable next checks
  - **Input**: Stack traces/log excerpts + timestamps + recent changes
  - **Expected output**: Likely failure points + next diagnostic steps + quick experiments

- **Use Case: Incident mitigation**
  - **Goal**: Stabilize a degraded system quickly while preserving correctness
  - **Input**: Current symptoms + SLO/SLA targets + architecture overview
  - **Expected output**: Immediate mitigations + rollback guidance + follow-up actions

## Category 3: Architecture & Design
- **Use Case: Architecture decision record (ADR)**
  - **Goal**: Compare options and document a decision with rationale
  - **Input**: Requirements + constraints + candidate solutions
  - **Expected output**: ADR with decision, alternatives, pros/cons, risks, and rationale

- **Use Case: Scalability planning**
  - **Goal**: Design a system that handles projected growth and peak load
  - **Input**: Traffic estimates + read/write ratios + data volume + peak patterns
  - **Expected output**: Scaling strategy + component plan + capacity assumptions and limits

- **Use Case: API design**
  - **Goal**: Define a consistent, maintainable API surface for a domain
  - **Input**: Domain entities + operations + auth model + performance targets
  - **Expected output**: API spec (endpoints/schemas) + examples + error handling model

## Category 4: Testing & QA
- **Use Case: Test strategy creation**
  - **Goal**: Ensure coverage across unit, integration, and E2E testing
  - **Input**: Component description + risks + supported environments
  - **Expected output**: Test matrix + prioritized test cases + coverage targets

- **Use Case: Edge-case generation**
  - **Goal**: Identify boundary conditions and failure cases early
  - **Input**: Spec or function signature + invariants + constraints
  - **Expected output**: Edge-case list + sample inputs + expected outcomes

- **Use Case: Regression test writing**
  - **Goal**: Prevent reintroduction of a fixed bug
  - **Input**: Bug report + minimal reproducer + fix details (optional)
  - **Expected output**: Automated regression test(s) + assertions + CI integration notes

## Category 5: Documentation
- **Use Case: Developer documentation drafting**
  - **Goal**: Provide onboarding and operational guidance for engineers
  - **Input**: System overview + setup steps + env vars + common workflows
  - **Expected output**: Markdown docs with quickstart, examples, and troubleshooting

- **Use Case: Code walkthrough**
  - **Goal**: Explain how a module works for reviewers and new contributors
  - **Input**: Target module/directory + intended behavior + key design choices
  - **Expected output**: Structured walkthrough (components, call flow, data flow) + notes on pitfalls

- **Use Case: Release notes generation**
  - **Goal**: Summarize changes clearly for users and stakeholders
  - **Input**: PR/commit list + feature flags + breaking changes + known issues
  - **Expected output**: Release notes with highlights, fixes, breaking changes, and upgrade steps

- **Use Case: API reference generation**
  - **Goal**: Produce a precise API reference that matches implementation
  - **Input**: Source code annotations (or OpenAPI draft) + endpoint list + auth details
  - **Expected output**: API reference section with endpoints, parameters, examples, and common errors
