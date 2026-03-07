# Data Model

Single PostgreSQL database for LocalHero monolith. Normalized 3NF with geo-indexing.

- **Users**: 
  - id (UUID PK), email (unique), name, phone, role (helper|requestor|admin)
  - neighborhood_id (FK), points_total, rating_avg, created_at

- **Tasks**: 
  - id (UUID PK), title, description, reward_points, status (open|assigned|completed)
  - requestor_id (FK), helper_id (FK nullable), lat, lng, radius_km, expires_at

- **Messages**: 
  - id (UUID PK), task_id (FK), sender_id (FK), message_text, timestamp, is_read

- **Neighborhoods**: 
  - id (UUID PK), name, lat_center, lng_center, admin_user_id (FK), member_count
