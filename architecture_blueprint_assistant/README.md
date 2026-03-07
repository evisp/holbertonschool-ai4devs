# Architecture Blueprint - LocalHero

## Overview

**LocalHero** connects neighbors needing quick help (dog walking, grocery pickup, plant watering) with others happy to assist, earning community points instead of cash. Tasks appear within 2km radius, matched by skills/availability, with in-app chat and verification. Core value: building neighborhood trust through small acts of help.

**Target scale**: 1K concurrent users per neighborhood (10K total platform). Mobile-first (React Native + PWA). GDPR compliant.

**Files delivered**:
```
app_concept.md              # Product vision + constraints
monolith_description.md     # 8-component single deploy
monolith_architecture.mmd   # Monolith diagram
microservices_description.md # 6 independent services  
microservices_architecture.mmd # Microservices diagram
architecture_comparison.md  # 10-aspect tradeoff analysis
data_model.md              # Normalized PostgreSQL schema
data_model.mmd             # 4-entity ER diagram
```

## Monolithic vs Microservices Decision

**Monolith chosen for Phase 1** (8/10 aspects favor monolith):

| Aspect | Winner | LocalHero Context |
|--------|--------|------------------|
| **Cost** | Monolith | $50/mo vs $250+/mo for 6 services |
| **Speed** | Monolith | Single deploy vs 6x coordination |
| **Team** | Monolith | Solo/small team vs DevOps needed |
| **Scale** | Microservices | Tasks service needs independent scaling |

**Migration path**: Extract Tasks + Chat services at 10K+ users.

[Full comparison → architecture_comparison.md](./architecture_comparison.md)

## Data Model

**Single PostgreSQL database** (3NF normalized) supports all monolith features:

```
NEIGHBORHOODS 1---* USERS (points_total, rating_avg)
         1         *
USERS    *---*1   TASKS (lat/lng, reward_points, expires_at)
         *         *
TASKS 1---* MESSAGES (task_id, sender_id, is_read)
```

**Key design**: 
- Geo-index on `lat/lng` for 2km radius queries
- Denormalized `points_total` for leaderboard performance
- Separate `requestor_id/helper_id` for task ownership

[ER Diagram → data_model.mmd](./data_model.mmd)

## Architecture Deliverables

**Monolith** (`monolith_architecture.mmd`):
```
Mobile App → Backend Monolith (Auth+Tasks+Chat+Points+Notifications) → PostgreSQL
```

**Microservices** (`microservices_architecture.mmd`):
```
API Gateway → [Auth|Tasks|Chat|Points|Notifications] → Individual DBs
```

## AI Contribution Analysis

**Strengths**:
1. **Instant structure**: Perfect Markdown/Mermaid formatting from vague prompts
2. **Complete coverage**: Never missed user types, relationships, or constraints
3. **Visual consistency**: Diagrams matched textual descriptions perfectly

**Required human fixes**:
1. **Specificity**: "similar routes" → "2km radius queries"
2. **Count compliance**: 8→6 services, 12→8 stories
3. **Relationship clarity**: Made 4 distinct ER relationships vs 3 vague ones

**AI acceleration**: 8 files (40+ hours manual) → 2 hours with iteration. Human role: business context + validation.

## Key Architectural Decisions

1. **Monolith Phase 1**: Perfect for 1K users, solo developer, simple ops
2. **Geo-indexed PostgreSQL**: Handles 2km radius searches at scale
3. **Points denormalization**: Leaderboard performance without complex joins
4. **Clear migration path**: Tasks/Chat extract first at 10K users

## Next Steps

1. **Implementation**: Node.js + React Native + PostgreSQL
2. **Scale triggers**: 10K users → extract Tasks microservice
3. **Production**: DigitalOcean ($50/mo) + Cloudflare + Datadog
