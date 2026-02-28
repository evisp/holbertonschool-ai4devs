# API Design Prompt Template

**Role**: Act as an API Architect with 10+ years of experience designing production-grade REST APIs.

**Task**: Design a RESTful API for the described domain, including resources, endpoints, authentication, error model, versioning, and operational considerations.

**Input Placeholder**:
- **Code Quality**: [CODE_QUALITY_INPUT] (N/A for this use case)
- **Debugging**: [DEBUGGING_INPUT] (N/A for this use case)
- **Architecture & Design**: [ARCHITECTURE_INPUT] (use the fields below)
- **Testing & QA**: [TESTING_INPUT] (N/A for this use case)
- **Documentation**: [DOCUMENTATION_INPUT] (N/A for this use case)

[ARCHITECTURE_INPUT]:
- **Domain**: [DOMAIN_DESCRIPTION]
- **Primary users/clients**: [CLIENT_TYPES] (web app, mobile, partners, internal services)
- **Core resources/entities**: [RESOURCES] (e.g., User, Order, Product)
- **Operations**: [OPERATIONS] (CRUD + custom actions)
- **AuthN/AuthZ model**: [AUTH_MODEL] (JWT/OAuth2/keys; roles/scopes/tenancy)
- **Data ownership rules**: [OWNERSHIP_RULES] (who can read/write which resources)
- **Performance targets**: [PERFORMANCE_TARGETS] (RPS, p95 latency, SLA)
- **Constraints**: [CONSTRAINTS] (naming conventions, stack, backward compatibility)
- **Pagination/sorting/filtering needs**: [QUERY_CAPABILITIES]
- **Idempotency needs**: [IDEMPOTENCY_REQUIREMENTS] (which operations need it)
- **Versioning preference**: [VERSIONING_PREFERENCE] (path/header/media-type)

**Expected Output Format**:
Return your answer in this exact structure:

1. **Assumptions**: Bullet list (explicitly state missing info you assumed).
2. **Resource model**: List resources and relationships (IDs, ownership, lifecycle).
3. **Endpoints**: Markdown table with Method, Path, Description, Auth, Notes.
4. **Request/Response examples**: For 3–5 key endpoints, show JSON examples.
5. **Error handling model**: Standard error schema + mapping of common errors (400/401/403/404/409/422/429/500).
6. **Rate limiting & idempotency**: Proposed limits and idempotency keys where needed.
7. **Versioning & compatibility**: How versions evolve and deprecation policy.
8. **Validation**: Contract testing approach and what to verify in CI.
