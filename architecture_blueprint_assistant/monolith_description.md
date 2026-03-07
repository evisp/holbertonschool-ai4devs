# Monolithic Architecture

LocalHero runs as a single deployable application containing all functionality. One codebase, one database, one server.

- **Frontend App**: React Native mobile app + PWA for web access
- **Authentication Module**: JWT sessions, neighborhood admin roles
- **Task Module**: Create, search, match tasks within 2km radius
- **Chat Module**: Real-time messaging between helpers/requestors
- **Points Module**: Award/revoke points, calculate leaderboards
- **Verification Module**: Photo upload + admin approval workflow
- **Notifications Module**: Push notifications for matches/chat
- **Database**: PostgreSQL storing users, tasks, chats, points
