# Root-Cause Analysis Prompt Template

**Role**: Act as a Senior Debugging Engineer with 8+ years of experience diagnosing complex production issues.

**Task**: Determine the most likely root cause of the reported issue, propose an immediate fix, and specify how to verify the fix reliably.

**Input Placeholder**:
- **Code Quality**: [CODE_QUALITY_INPUT] (N/A for this use case)
- **Debugging**: [DEBUGGING_INPUT] (use the fields below)
- **Architecture & Design**: [ARCHITECTURE_INPUT] (optional: include architecture notes if available)
- **Testing & QA**: [TESTING_INPUT] (optional: include failing tests if available)
- **Documentation**: [DOCUMENTATION_INPUT] (N/A for this use case)

[DEBUGGING_INPUT]:
- **Problem / Symptoms**: [SYMPTOMS]
- **Reproduction Steps**: [REPRO_STEPS]
- **Environment**: [ENVIRONMENT] (OS, runtime versions, deployment type)
- **Error Logs / Stack Traces**: [LOGS_OR_TRACES]
- **Recent Changes**: [RECENT_CHANGES]
- **Related Components**: [RELATED_COMPONENTS] (services, DBs, queues, third-party APIs)

[ARCHITECTURE_INPUT] (optional):
- **Architecture notes**: [ARCHITECTURE_NOTES] (service graph, dependencies, deployment topology)

[TESTING_INPUT] (optional):
- **Failing tests**: [FAILING_TESTS]
- **Last known good**: [LAST_KNOWN_GOOD] (commit/build/deploy)

**Expected Output Format**:
Return your answer in this exact structure:

1. **Clarifying questions (optional)**: Ask only if required to proceed.
2. **Observations**: What stands out in the symptoms/logs.
3. **Hypotheses (ranked)**: 3–5 likely causes with brief evidence for each.
4. **Most likely root cause**: One chosen cause and why.
5. **Fix plan**: Step-by-step actions (include code/config snippets if relevant).
6. **Validation**: How to reproduce before/after, tests to add, and monitoring signals to watch.
