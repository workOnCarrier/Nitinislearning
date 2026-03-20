# software engineer
Design a system that powers a “crypto explore/home” page (like an exchange’s market page) that:
Shows a list of crypto assets (e.g., BTC, ETH, SOL, …)
Displays near real-time price updates (and optionally 24h change, volume, etc.)
Updates many concurrent clients efficiently (web + mobile)
Assume you have access to upstream market data (from exchanges/market makers/internal pricing service) that produces frequent ticks.
What to cover
Requirements (latency, freshness, accuracy, ordering)
APIs for initial page load and live updates
Data ingestion/normalization and internal price computation
Fanout strategy to clients (WebSockets/SSE/push)
Storage, caching, and historical needs (optional)
Scalability, multi-region, reliability, and monitoring