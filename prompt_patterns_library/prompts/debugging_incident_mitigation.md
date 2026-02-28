# Incident Mitigation Prompt Template

**Role**: Act as an Incident Commander (SRE) with 8+ years of experience mitigating high-severity production incidents.

**Task**: Triage the incident, propose the safest immediate mitigations to reduce user impact, and define a follow-up plan to prevent recurrence.

**Input Placeholder**:
- **Code Quality**: [CODE_QUALITY_INPUT] (N/A for this use case)
- **Debugging**: [DEBUGGING_INPUT] (use the fields below)
- **Architecture & Design**: [ARCHITECTURE_INPUT] (optional: include architecture notes if available)
- **Testing & QA**: [TESTING_INPUT] (N/A for this use case)
- **Documentation**: [DOCUMENTATION_INPUT] (N/A for this use case)

[DEBUGGING_INPUT]:
- **Incident summary**: [INCIDENT_SUMMARY]
- **Severity / Impact**: [SEVERITY_AND_IMPACT] (users affected, error rate, latency, regions)
- **Time window**: [TIME_WINDOW]
- **Architecture overview**: [ARCHITECTURE_OVERVIEW] (services, DBs, queues, third parties)
- **Signals**: [SIGNALS] (alerts, dashboards, logs, traces)
- **Recent changes**: [RECENT_CHANGES] (deploys, config, feature flags, infra)
- **Constraints**: [CONSTRAINTS] (e.g., cannot restart DB, no downtime window)

[ARCHITECTURE_INPUT] (optional):
- **Architecture notes**: [ARCHITECTURE_NOTES] (service graph, dependencies, failover options)

**Expected Output Format**:
Return your answer in this exact structure:

1. **Triage**: What is failing, scope/blast radius, and the most likely component at fault.
2. **Immediate mitigations (ranked)**: 3–7 actions (e.g., rollback, disable feature flag, traffic shift, rate limiting, scale up). For each action include:
   - **Action**
   - **Expected effect**
   - **Risk/side effects**
   - **How to verify** (metrics/logs that must improve)
3. **Communication snippet**: A concise status update template (Impact / Action / Next update time).
4. **Stabilization checklist**: Conditions required to declare stable (metrics back to baseline for X minutes).
5. **Follow-up actions**: Long-term fixes, tests, and monitoring/alert improvements to prevent recurrence.
