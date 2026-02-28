# Architecture Decision Record (ADR) Prompt Template

**Use Case**: Architecture decision record (ADR)  

**Role**: Staff Software Architect with 10+ years of experience designing and evolving production systems.  

**Task**: Create an Architecture Decision Record (ADR) for the decision described below, comparing options and producing a clear recommendation with consequences.  

**Input Placeholder**: [USER_INPUT]  

[USER_INPUT]:  
- **Code Quality**: [CODE_QUALITY_INPUT] (N/A for this use case)  
- **Debugging**: [DEBUGGING_INPUT] (N/A for this use case)  
- **Architecture & Design**: [ARCHITECTURE_INPUT] (use the fields below)  
- **Testing & QA**: [TESTING_INPUT] (N/A for this use case)  
- **Documentation**: [DOCUMENTATION_INPUT] (N/A for this use case)  

[ARCHITECTURE_INPUT]:  
- **Decision title**: [DECISION_TITLE]  
- **Status**: [STATUS] (Proposed/Accepted/Deprecated/Superseded)  
- **Date**: [TODAY_DATE]  
- **Context**: [CONTEXT] (current state, problem to solve, constraints)  
- **Functional requirements**: [FUNCTIONAL_REQUIREMENTS]  
- **Non-functional requirements**: [NON_FUNCTIONAL_REQUIREMENTS] (latency, availability, security, compliance)  
- **Options considered**: [OPTIONS_CONSIDERED] (Option A, B, C…)  
- **Decision drivers**: [DECISION_DRIVERS] (criteria + weights if any)  
- **Constraints**: [CONSTRAINTS] (budget, timeline, stack, team skills)  
- **Open questions**: [OPEN_QUESTIONS] (optional)  

**Expected Output**: An ADR in the following structure.  

Return your answer in this exact structure:

1. **Title**: [DECISION_TITLE]  
2. **Date**: [TODAY_DATE]  
3. **Status**: [STATUS]  
4. **Context**  
5. **Decision**  
6. **Rationale**  
7. **Consequences**  
   - **Positive**: What improves and why.  
   - **Negative**: What worsens/costs and why.  
8. **Risks & Mitigations**  
9. **Alternatives Considered** (why not chosen)  
10. **Validation / Rollout Plan** (how to prove it works; migration steps)  
11. **Follow-ups** (next ADRs, tasks, review date)  
