# Log/Trace Interpretation Prompt Template

**Role**: Act as a Site Reliability Engineer (SRE) with 8+ years of experience operating and troubleshooting distributed systems.

**Task**: Analyze the provided logs/traces/metrics to identify the most likely failure point, explain what is happening, and propose the next best debugging actions.

**Input Placeholder**:
- **Code Quality**: [CODE_QUALITY_INPUT] (N/A for this use case)
- **Debugging**: [DEBUGGING_INPUT] (use the fields below)
- **Architecture & Design**: [ARCHITECTURE_INPUT] (optional: include architecture notes if available)
- **Testing & QA**: [TESTING_INPUT] (N/A for this use case)
- **Documentation**: [DOCUMENTATION_INPUT] (N/A for this use case)

[DEBUGGING_INPUT]:
- **System/Service**: [SERVICE_NAME]
- **Context**: [CONTEXT_SUMMARY] (what changed, what users see)
- **Environment**: [ENVIRONMENT] (prod/staging, region, versions)
- **Time window**: [TIME_WINDOW] (start/end, timezone)
- **Logs**: [LOG_SNIPPETS]
- **Traces**: [TRACE_SNIPPETS] (optional)
- **Metrics**: [METRICS_SNAPSHOT] (optional: error rate, latency, saturation)
- **Recent changes**: [RECENT_CHANGES] (deploys, config flags, infra)

[ARCHITECTURE_INPUT] (optional):
- **Architecture notes**: [ARCHITECTURE_NOTES] (service graph, dependencies, failure domains)

**Expected Output Format**:
Return your answer in this exact structure:

1. **Assumptions**: Bullet list (what you assume about topology and traffic).
2. **Signal summary**: What the logs/traces/metrics indicate (errors, latency, retries, timeouts).
3. **Likely failure point(s)**: Ranked list; for each include evidence (log lines/trace spans) and scope (one node, one region, all traffic).
4. **Next actions (priority order)**: 5–10 concrete checks/commands/queries to run next (what to look for and why).
5. **Immediate mitigations (optional)**: Safe short-term mitigations if severity is high (rollback, feature flag off, rate limiting), include risk notes.
6. **Instrumentation improvements**: What to add to make future incidents easier to diagnose (log fields, trace spans, metrics, alerts).
