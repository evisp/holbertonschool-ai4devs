# Application Concept – LocalHero

## Application
LocalHero connects neighbors needing quick help (dog walking, groceries, plant watering) with others happy to assist. Helpers earn community points instead of cash, building trust and neighborhood connections.

## Core Features
- Post tasks visible within 2km radius with clear completion requirements
- Real-time matching shows available helpers by skills and distance
- In-app chat for task coordination and verification photos
- Points system rewards reliable helpers with badges and leaderboards
- Task completion verification prevents abuse

## Users
- **Helpers**: Neighbors earning points for dog walking, shopping, repairs
- **Requestors**: Post urgent tasks needing same-day neighborhood help
- **Neighborhood Admins**: Resolve disputes, verify completions, manage points

## Constraints
- Scale to 1K concurrent users per neighborhood (10K total)
- GDPR compliance for personal task details and chat history
- Mobile-first design (iOS/Android PWA)
- Simple deployment (single server initially, microservices later)
