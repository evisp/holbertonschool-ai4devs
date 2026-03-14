# Monolithic Architecture

Property Pulse Albania uses a monolithic architecture for the MVP, where all core features run inside a single application. This approach keeps development simpler, faster to manage, and easier to deploy in the early stage of the project.

- **Frontend Interface**: The web interface where users search listings, apply filters, explore properties on a map, and compare homes.
- **Backend Application**: The main application that handles requests, runs business logic, serves data, and connects all system parts.
- **Property Listings Module**: Manages property data, search, filtering, and property detail views.
- **Map and Location Module**: Displays properties on an interactive map using geolocation data.
- **Price Estimation Module**: Estimates the market value of a property using available real estate data.
- **Comparison and Value Module**: Compares properties and identifies whether a listing appears underpriced, fairly priced, or overpriced.
- **Chat Assistant Module (Optional)**: Provides simple answers to user questions and suggests relevant properties.
- **Database**: Stores property listings, location data, user activity, and model-related information in one central system.
