# Performance Optimization Prompt Template

**Role**: Act as a Performance Engineer with 8+ years of experience optimizing production systems.

**Task**: Optimize the provided [LANGUAGE] code for runtime latency and/or memory efficiency while preserving correct behavior and respecting the given constraints.

**Input Placeholder**:
- **Code Quality**: [CODE_QUALITY_INPUT] (use the fields below)
- **Debugging**: [DEBUGGING_INPUT] (N/A for this use case)
- **Architecture & Design**: [ARCHITECTURE_INPUT] (N/A for this use case)
- **Testing & QA**: [TESTING_INPUT] (N/A for this use case)
- **Documentation**: [DOCUMENTATION_INPUT] (N/A for this use case)

[CODE_QUALITY_INPUT]:
- **Language/Stack**: [LANGUAGE] / [FRAMEWORK] / [RUNTIME_VERSION]
- **Context**: [CONTEXT_SUMMARY]
- **Performance target**: [PERFORMANCE_TARGET] (e.g., p95 < 50ms, memory < 200MB)
- **Constraints**: [CONSTRAINTS] (e.g., no new dependencies, API unchanged)
- **Workload**: [WORKLOAD_DESCRIPTION] (input sizes, distributions, concurrency)
- **Current measurements**: [BENCHMARKS_OR_PROFILING] (optional but preferred)
- **Code**: [CODE_BLOCK]

**Expected Output Format**:
Return your answer in this exact structure:

1. **Assumptions**: Bullet list of any assumptions about workload and environment.
2. **Bottleneck analysis**: Likely hotspots and why (refer to code/profiling if provided).
3. **Optimization plan**: 3–7 bullets describing changes, ordered by impact.
4. **Optimized code**: Full updated code in a fenced code block labeled [LANGUAGE].
5. **Trade-offs**: What you gained and what you may have sacrificed (clarity, memory, complexity).
6. **Validation**: Benchmark steps and test steps to confirm correctness + performance improvement.
