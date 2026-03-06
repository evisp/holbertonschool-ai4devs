# Technical Specification

## System Components
- **Authentication Service**: Handles corporate SSO login (Okta, Azure AD), user provisioning, and role-based access
- **Matching Engine**: Finds compatible carpools using route, schedule, and preferences. Updates matches daily
- **Analytics Dashboard**: Calculates CO2 savings, cost reductions, and parking metrics. Generates reports
- **Parking Manager**: Assigns reserved spots to verified carpool groups and tracks usage
- **Notification Service**: Sends schedule changes, ride confirmations, and report alerts via push/email

## Data Models
- **User**: 
  - id, email, name, department, role (employee/manager), home_address, work_address, schedule_flexibility_minutes
- **CarpoolGroup**:
  - id, leader_id, member_ids[], route_summary, typical_schedule, vehicle_capacity, parking_spot_id
- **DailyMatch**:
  - id, group_id, date, confirmed_status, co2_saved, cost_saved_per_person, parking_used
- **Company**:
  - id, name, sso_provider, parking_total_spaces, baseline_emissions_tons, target_participation_pct

## API Endpoints
- **POST /auth/sso-login**  
  Parameters: sso_token, company_id  
  Returns: user_jwt, role, permissions  

- **GET /matching/my-commutes**  
  Parameters: date (optional)  
  Returns: available_matches[], compatibility_scores, suggested_groups  

- **POST /carpools/join**  
  Parameters: match_id, preferred_schedule  
  Returns: group_id, updated_calendar_events  

- **GET /analytics/company-report**  
  Parameters: month, year, department_filter  
  Returns: participation_rate, co2_saved, parking_utilization, cost_savings  

- **PUT /parking/assign**  
  Parameters: group_id, date  
  Returns: parking_spot_assignment, availability_status  

- **POST /notifications/group-message**  
  Parameters: group_id, message_text  
  Returns: message_id, delivery_status[]
