# Prompt Use Cases

## Code Quality
- **Refactoring for readability**
  - **Goal**: Make code easier to understand and maintain without changing behavior
  - **Input**: Function/class/module in [LANGUAGE] + expected behavior notes
  - **Output**: Refactored code + brief rationale + before/after highlights

- **Performance optimization**
  - **Goal**: Reduce time/memory usage and remove bottlenecks
  - **Input**: Hot path code + constraints (latency, memory) + sample input sizes
  - **Output**: Optimized implementation + complexity notes + trade-offs

- **Security hardening**
  - **Goal**: Find and fix common vulnerabilities (injection, authz, secrets)
  - **Input**: Relevant code paths + threat model assumptions + frameworks used
  - **Output**: Vulnerability list + patched code + recommended mitigations

## Debugging & Incident Response
- **Root-cause analysis**
  - **Goal**: Identify why a bug occurs and how to reproduce it reliably
  - **Input**: Symptom description + environment + steps to reproduce + logs/traces
  - **Output**: Likely root cause(s) + reproduction steps + fix plan

- **Log/trace interpretation**
  - **Goal**: Turn noisy logs into actionable hypotheses
  - **Input**: Error logs, stack traces, metrics snapshots, recent changes
  - **Output**: Ranked hypotheses + what to check next + quick experiments

- **Failure-mode mitigation**
  - **Goal**: Stabilize a failing system quickly (timeouts, retries, fallbacks)
  - **Input**: SLO/SLA targets + current failure symptoms + architecture overview
  - **Output**: Immediate mitigations + longer-term prevention + monitoring updates

## Architecture & Design
- **Architecture decision records (ADR)**
  - **Goal**: Compare options and document a decision clearly
  - **Input**: Requirements + constraints + candidate approaches
  - **Output**: ADR-style decision with pros/cons, risks, and rationale

- **Scalability planning**
  - **Goal**: Design for growth and load patterns
  - **Input**: Expected traffic, data volume, read/write ratios, peak patterns
  - **Output**: Scaling strategy + component choices + capacity assumptions

- **API design**
  - **Goal**: Produce consistent, maintainable REST/GraphQL APIs
  - **Input**: Domain entities + operations + auth model + performance targets
  - **Output**: Endpoint/schema spec + example requests/responses + error model

## Testing & Quality Assurance
- **Test plan creation**
  - **Goal**: Define what to test at unit/integration/E2E levels
  - **Input**: Component description + key risks + target environments
  - **Output**: Test matrix + priority order + coverage targets

- **Edge-case generation**
  - **Goal**: Find hidden failures and boundary conditions
  - **Input**: Function signature/spec + invariants + constraints
  - **Output**: Edge-case list + example inputs + expected outputs

- **Regression test writing**
  - **Goal**: Prevent a fixed bug from returning
  - **Input**: Bug description + minimal reproducer + fix diff (optional)
  - **Output**: Automated test(s) + assertions + CI notes

## Documentation & Knowledge Transfer
- **Developer documentation drafting**
  - **Goal**: Create onboarding and usage docs that engineers can follow
  - **Input**: System overview + setup steps + env variables + common workflows
  - **Output**: Markdown docs with quickstart, examples, and troubleshooting

- **Code walkthroughs**
  - **Goal**: Explain how a module works for reviewers or new team members
  - **Input**: Code directory/module + intended behavior + key design choices
  - **Output**: Structured explanation + call flow + key abstractions

- **Changelog / release notes**
  - **Goal**: Summarize changes for users and stakeholders
  - **Input**: PR list/commit messages + feature flags + breaking changes info
  - **Output**: Release notes with highlights, fixes, known issues, upgrade steps
