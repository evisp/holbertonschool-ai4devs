# Microservices Architecture

LocalHero decomposed into independent services, each with dedicated database for loose coupling.

- **API Gateway**: Single entry point routing requests, rate limiting, authentication
- **Auth Service**: User registration, JWT tokens, neighborhood roles (PostgreSQL)
- **Tasks Service**: Task creation, 2km radius search, matching logic (PostgreSQL + Redis cache)
- **Chat Service**: Real-time messaging, WebSocket connections (MongoDB)
- **Points Service**: Points awarding, leaderboards, badges calculation (PostgreSQL)
- **Verification Service**: Photo upload/review, admin approval workflow (S3 + PostgreSQL)
- **Notifications Service**: Push notifications, email alerts (RabbitMQ queue)
- **Maps Service**: Geolocation calculations, distance matrix (Google Maps API cache)
