# Application Concept – Property Pulse Albania

## Application
A smarter way to explore real estate in Albania — helping users find homes, compare listings, and instantly see whether a property is priced well.

## Problem Definition
- Property listings are often spread across different sources and are not easy to compare.
- Buyers can see asking prices, but they often cannot tell whether a property is fairly priced.
- Sellers and agents need a simple way to benchmark a property against similar homes in the same area.
- Most listing websites focus on showing properties, not helping users understand price value.

## Value Proposition
- Help buyers make faster and better-informed decisions by showing price context, not just listings.
- Help sellers and agents price properties more competitively using market-based estimates.
- Combine search, map exploration, comparison, and price estimation in one simple product.
- Turn Albanian real estate data into a practical tool that is easy to understand and use.

## Core Features
- Search and filter listings by city, neighborhood, price, size, property type, and key features.
- Show properties on an interactive map using location data.
- Open a property card on click with price, size, location, and main details.
- Estimate a property's market price from past and current listing data.
- Compare two properties side by side by price, size, location, and estimated value.
- Label listings as underpriced, fairly priced, or overpriced based on the estimated market price.
- Optional chat assistant to answer simple questions and help users find relevant properties.

## Users
- Buyers: want to find homes and understand whether the asking price is reasonable.
- Sellers and agents: want to compare listings and set competitive prices.
- Students and instructors: want a practical project that shows data analysis, web development, and product thinking.

## MVP Scope
- Import and clean at least \(5{,}000\) Albanian property records.
- Build listing search with basic filters.
- Display listings on an interactive map.
- Create a property detail card with the main data points.
- Build a price estimation feature for one property at a time.
- Add side-by-side comparison for \(2\) properties.
- Show a simple value label: underpriced, fair, or overpriced.

## MVP Tech Stack
- Backend: Python, Flask
- API and server logic: Flask routes, REST endpoints
- Database: PostgreSQL
- Data processing: Pandas, NumPy
- Price estimation: scikit-learn
- Frontend: HTML, CSS, JavaScript, Jinja templates
- UI framework: Bootstrap
- Maps: Leaflet.js
- Charts and simple visuals: Chart.js
- ORM and database access: SQLAlchemy
- Deployment: Docker and Render or Railway
- Version control: Git and GitHub

## Constraints
- Return search, filter, and map updates in under \(2\) seconds during normal use.
- Return price estimates in under \(3\) seconds.
- Support both mobile and desktop screens.
- Standardize location, price, size, and feature data before using it.
- Present price results as estimates, not guarantees or financial advice.
- Start with Albania-focused data and expand only after the MVP is stable.

## MVP Success Criteria
- Users can search, filter, and view properties on a map without errors.
- Users can click a listing and see a clear property summary card.
- Users can compare \(2\) properties on one screen.
- Users can request a price estimate and receive a result in under \(3\) seconds.
- The system can clearly label a listing as underpriced, fair, or overpriced.
- The application is deployed online and usable as a portfolio project demo.
