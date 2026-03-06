# CarPool Connect Refined User Stories

## User Stories

### Story 1 - Employee Matching
- **Original**: "As a corporate employee, I want to find colleagues with similar commute routes so that I can save money and drive less."
- **Refined**: **As a corporate employee, I want to see coworkers with matching routes (within 2 miles) and schedules so I can save on gas and parking costs.**

**Improvement**: Added specific measurements (2 miles), changed "drive less" to concrete benefits (gas/parking).

### Story 4 - Parking Assignment  
- **Original**: "As a facility manager, I want to reserve parking spots for carpoolers so that single drivers park farther out."
- **Refined**: **As a facility manager, I want verified carpool groups to get preferred parking spots so I can reduce total parking demand by 25%.**

**Improvement**: Added "verified" for security, specific 25% target, clearer benefit.

### Story 6 - SSO Login
- **Original**: "As an IT administrator, I want employees to login with company accounts so that no one needs new passwords."
- **Refined**: **As an IT administrator, I want Single Sign-On with Okta/Azure AD so employees access instantly when hired and lose access when terminated.**

**Improvement**: Named specific SSO providers, added lifecycle management (hire/terminate).

## Data Models

### User Model
- **Original**: `User: id, email, name, department, role (employee/manager), home_address, work_address, schedule_flexibility_minutes`
- **Refined**: ```User: 
  - id (UUID)
  - email (unique, verified) 
  - name
  - department
  - role (employee|manager|admin)
  - home_lat, home_lng (coordinates)
  - work_lat, work_lng (coordinates)
  - schedule_flex (0-60 minutes)```

**Improvement**: Added data types, coordinates instead of addresses, enum for role, validation rules.

### CarpoolGroup Model
- **Original**: `CarpoolGroup: id, leader_id, member_ids[], route_summary, typical_schedule, vehicle_capacity, parking_spot_id`
- **Refined**: ```CarpoolGroup:
  - id (UUID)
  - leader_id (User)
  - members (User[] max 6)
  - avg_route_distance_km
  - typical_departure_time 
  - vehicle_seats (2-8)
  - parking_spot_id (nullable)```

**Improvement**: Concrete fields, limits (max 6 members), nullable parking.

## API Endpoints

### Matching Endpoint
- **Original**: `GET /matching/my-commutes date (optional) Returns: available_matches[], compatibility_scores, suggested_groups`
- **Refined**: ```
  GET /v1/matching/commutes?date=2026-03-10
  Response: 200 OK
  {
    "matches": [{
      "group_id": "uuid",
      "route_similarity": 92,
      "schedule_fit": "perfect",
      "driver_rating": 4.8,
      "seats_available": 2
    }]
  }```

**Improvement**: Full URL with version, concrete JSON response, specific fields.

### Analytics Endpoint
- **Original**: `GET /analytics/company-report month, year, department_filter`
- **Refined**: ```
  GET /v1/analytics/reports?company_id=abc&year=2026&month=3&department=engineering
  Response: {
    "participation_rate": "42%",
    "co2_saved_tons": 15.3,
    "parking_spaces_freed": 23,
    "total_savings_usd": 24500
  }```

**Improvement**: Added company_id parameter, specific measurable metrics.

## System Components

### Analytics Dashboard
- **Original**: "Analytics Dashboard: Calculates CO2 savings, cost reductions, and parking metrics. Generates reports"
- **Refined**: **Analytics Engine**: Real-time calculations (<2s response) for CO2 (EPA formula), cost savings (IRS mileage rate), parking utilization. PDF/CSV export.

**Improvement**: Added performance requirement, specific calculation standards, export formats.
