# Security Hardening Prompt Template

**Role / Perspective**: Act as an Application Security Engineer with 8+ years of experience securing production web services and APIs.

**Task Description**: Review the provided code and identify security vulnerabilities, then propose fixes that preserve intended functionality and comply with the given constraints.

## Input Placeholder
- **Language/Stack**: [LANGUAGE] / [FRAMEWORK] / [RUNTIME_VERSION]
- **Context**: [CONTEXT_SUMMARY]
- **Threat model**: [THREAT_MODEL] (assets, attackers, trust boundaries)
- **Constraints**: [CONSTRAINTS] (e.g., no new dependencies, must keep API stable)
- **Code / Config**: [CODE_BLOCK]
- **Entry points**: [ENTRY_POINTS] (routes, handlers, jobs, CLI commands)
- **Data flows**: [DATA_FLOWS] (where user input enters; where it is stored/used)

## Expected Output Format
Return your answer in this exact structure:

1. **Assumptions**: Bullet list.
2. **Findings**: A prioritized list (Critical/High/Medium/Low). For each finding include: what it is, where it is, why it matters, and how it can be exploited.
3. **Fixes**: Concrete code changes (fenced code blocks labeled [LANGUAGE]) and configuration changes as needed.
4. **Validation**: Security test plan (unit/integration tests, negative tests, and manual checks) to confirm issues are fixed.
5. **Hardening recommendations**: Defensive defaults to add next (input validation, authz checks, secret handling, logging hygiene).
