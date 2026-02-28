# Scalability Planning Prompt Template

**Role**: Act as a Distributed Systems Architect with 10+ years designing scalable, reliable services.

**Task**: Create a scalability plan for the system described below, including key bottlenecks, scaling strategies, and a practical migration/rollout path.

**Input Placeholder**:
- **Code Quality**: [CODE_QUALITY_INPUT] (N/A for this use case)
- **Debugging**: [DEBUGGING_INPUT] (N/A for this use case)
- **Architecture & Design**: [ARCHITECTURE_INPUT] (use the fields below)
- **Testing & QA**: [TESTING_INPUT] (N/A for this use case)
- **Documentation**: [DOCUMENTATION_INPUT] (N/A for this use case)

[ARCHITECTURE_INPUT]:
- **System overview**: [SYSTEM_OVERVIEW]
- **Current architecture**: [CURRENT_ARCHITECTURE] (services, DBs, caches, queues, third parties)
- **Traffic estimates**: [TRAFFIC_ESTIMATES] (avg/peak RPS, concurrency, regions)
- **Read/Write ratio**: [READ_WRITE_RATIO]
- **Data volume & growth**: [DATA_GROWTH] (storage now + projection)
- **SLO/SLA targets**: [SLO_SLA] (latency, availability)
- **Constraints**: [CONSTRAINTS] (budget, timeline, team, stack, compliance)

**Expected Output Format**:
Return your answer in this exact structure:

1. **Assumptions**: Concrete numbers you assume if missing (clearly labeled).
2. **Scalability risks**: Ranked list of likely bottlenecks (compute, DB, cache, network, external APIs).
3. **Scaling strategies**: For each major component, specify the approach (caching, replication, sharding/partitioning, async queues, load balancing, CDN).
4. **Data strategy**: Schema/indexing considerations, partition keys (if applicable), and consistency trade-offs.
5. **Capacity plan**: Rough sizing guidance and what to measure to refine it (key metrics).
6. **Migration / rollout plan**: Steps to evolve from current → target architecture with minimal downtime.
7. **Validation**: Load test plan + success criteria + monitoring/alert updates.
