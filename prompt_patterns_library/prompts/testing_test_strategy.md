# Test Strategy Creation Prompt Template

**Role / Perspective**: Act as a QA Lead / Test Architect with 8+ years of experience designing test strategies for production software.

**Task Description**: Create a comprehensive test strategy for the described component/system, covering unit, integration, end-to-end, and performance testing, with tools and CI/CD integration guidance.

## Input Placeholder
- **Component/System**: [COMPONENT_NAME]
- **Description**: [COMPONENT_DESCRIPTION]
- **Critical user flows**: [CRITICAL_FLOWS]
- **Dependencies**: [DEPENDENCIES] (DBs, services, third-party APIs)
- **Risk level**: [RISK_LEVEL] (Low/Medium/High) + [RISK_NOTES]
- **Environments**: [ENVIRONMENTS] (local, CI, staging, prod)
- **Constraints**: [CONSTRAINTS] (timeline, tooling, team skills)

## Expected Output Format
Return your answer in this exact structure:

1. **Scope & goals**: What is in-scope/out-of-scope and the quality goals.
2. **Risk-based priorities**: Ranked risks and how tests address them.
3. **Test pyramid plan**: Recommended distribution (unit/integration/E2E) and rationale.
4. **Test categories**:
   - **Unit tests**: What to cover + example test cases.
   - **Integration tests**: Key integration points + example test cases.
   - **E2E tests**: Key journeys + example scenarios.
   - **Performance tests**: Load/stress targets + scenarios.
5. **Tooling**: Suggested frameworks and libraries per test layer.
6. **CI/CD integration**: What runs on PR vs merge vs nightly; expected runtime budgets.
7. **Metrics & coverage targets**: Coverage expectations and reporting.
8. **Exit criteria**: When testing is “good enough” to release.
