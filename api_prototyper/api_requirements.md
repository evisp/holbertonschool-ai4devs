# API Requirements – Property Pulse Albania API

## Domain
Albanian real estate listing and property price analysis platform

## Target Users
- Buyers: search properties and check whether listing prices look fair
- Sellers: understand how their property compares with the market
- Agents: browse listings and compare homes for clients
- Admins: manage property data and platform records

## Core Operations
- Create user account
- Log in user
- Get current user profile
- List properties
- Get property by ID
- Search properties by filters
- Get map-ready property results
- Save favorite property
- Compare two properties
- Estimate property price
- Get price status for a property
- Admin create, update, or delete property

## Data Rules
- Property ID must be unique
- Price must be greater than 0
- Size must be greater than 0
- Latitude must be between -90 and 90
- Longitude must be between -180 and 180
- Rooms, bathrooms, and floors must be non-negative integers
- Required fields must be clearly defined by name, type, format, and validation rules in the API specification 

## Non-Functional
- Property list and detail responses should be under 1 second for normal requests
- Price estimation responses should be under 3 seconds for normal requests
- JWT authentication required for protected endpoints
- Role-based access required for admin actions
- Rate limits should be enforced, and over-limit requests should return HTTP 429 with documented limit behavior 
- List endpoints should support pagination with consistent query parameters 
