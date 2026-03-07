# Microservices Architecture

LocalHero decomposed into 6 focused services with clear ownership.

- **API Gateway**: Routes requests, rate limits, JWT validation, service discovery
- **Auth Service**: User signup/login, neighborhood roles, JWT tokens (PostgreSQL)
- **Tasks Service**: Task CRUD, 2km radius search, helper matching (PostgreSQL + Redis)
- **Chat Service**: Real-time WebSocket messaging between matched users (MongoDB)
- **Points Service**: Points transactions, leaderboards, badge logic (PostgreSQL)
- **Notifications Service**: Push/email alerts for matches, completion (RabbitMQ)
