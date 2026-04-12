# Equities Front-Office Interview Concepts

This guide prioritizes the topics front-office technologists in equities trading are frequently quizzed on. Each section lists core ideas plus concrete sources for deep dives.

## 1. Equity Instruments & Products
- Common vs preferred shares, depositary receipts, ETFs, ADRs/GDRs, equity-linked notes.
- Lifecycle of an equity (IPO/SEO, buybacks, delistings) and float calculations.
- Corporate actions: splits, rights issues, dividends, tender offers, mergers.
- **Sources:** CFA Program Curriculum Volume 5, "Equity Valuation"; Morgan Stanley Primer on Equity Products; Investopedia Equity Instruments hub.

## 2. Market Structure & Venues
- Primary markets vs secondary markets; lit exchanges vs dark pools, systematic internalizers.
- Matching engines, price-time priority, maker/taker models, auction mechanisms (open/close auctions, volatility auctions).
- Benchmark venues (NYSE, NASDAQ, BATS/NYSE Arca) and regional specifics (MiFID II venues in EU, SEBI IFSC in India).
- **Sources:** "Market Microstructure Theory" by Maureen O’Hara; SEC Market Structure resources; FIA Market Structure primers.

## 3. Order Types & Execution Strategy
- Limit, market, IOC, FOK, pegged, iceberg, hidden, conditional orders.
- Smart order routing, algo execution styles (VWAP, POV, TWAP, Implementation Shortfall, sniper/slicer).
- Execution benchmarks (arrival price, close price, volume-weighted benchmarks) and slippage modeling.
- **Sources:** "Algorithmic Trading and DMA" by Barry Johnson; ITG/FactSet algo handbooks; CFA Institute Research Foundation notes on execution.

## 4. Market Microstructure Metrics
- Bid/ask, spread components (order-processing, inventory, adverse-selection), quoted vs effective spreads.
- Depth of book, order imbalance, price impact functions, volatility estimators (Parkinson, Yang-Zhang).
- Short interest, fail-to-deliver metrics, securities lending fees.
- **Sources:** Aitken & Comerton-Forde, "High-Frequency Trading" chapters; Bloomberg Market Structure Analytics docs; Cboe exchange specification guides.

## 5. Liquidity Provision & Market Making
- Designated market makers vs electronic liquidity providers; obligations and incentives.
- Inventory risk controls (delta, gamma, vega hedging), quoting models, skew management.
- Internalization vs routing; payment for order flow debates.
- **Sources:** Avellaneda & Stoikov market-making model; Citadel Securities whitepapers; BIS reports on liquidity provision.

## 6. Risk Management & Greeks
- Delta, gamma, vega, theta, rho for equity derivatives/hybrids; scenario/VaR/stress testing.
- Portfolio factor models (Fama-French, Barra) and exposures (size, value, momentum, quality, low vol).
- Margining (SPAN, portfolio margin), capital usage (RWA, leverage ratio) for equity books.
- **Sources:** Hull, "Options, Futures, and Other Derivatives"; MSCI Barra factor model documentation; BIS Fundamental Review of the Trading Book (FRTB) materials.

## 7. Corporate Actions & Reference Data
- Golden source hierarchies (Bloomberg, Refinitiv, Exchange feeds) and cleansing workflows.
- Event capture, ex-date vs record date, adjustments to positions and analytics.
- Dividends forecasting, stock loan recalls, proxy voting impact.
- **Sources:** DTCC corporate actions guide; ISO 15022/20022 specs; Bloomberg Event-Driven Feeds manuals.

## 8. Client & Sales Workflows
- Institutional vs retail flow segmentation, high-touch vs low-touch desks.
- Indications of interest (IOIs), risk runs, axes, internal crossing.
- TCA reporting, post-trade confirmation/affirmation (CTM, FIX, SWIFT) and settlement cycles (T+1, T+2).
- **Sources:** FIX Trading Community best practices; Broadridge post-trade guides; DTCC ITP documentation.

## 9. Regulatory & Control Topics
- Reg NMS (Rule 611 trade-through, Rule 605/606 reporting), tick-size programs, Reg SHO locate/close-out.
- MiFID II best execution, transparency (RTS 27/28), dark pool caps; Asia-specific regimes (Hong Kong Code, Japan PTS rules).
- Surveillance controls (spoofing detection, layer detection, kill-switches) and reporting (CAT, OATS historical).
- **Sources:** SEC & FINRA rule summaries; ESMA Q&A on MiFID II; FCA Market Watch newsletters.

## 10. Technology & Architecture
- Low-latency stack: feed handlers, normalized market data buses, order gateways, risk gateways, drop copies.
- Resiliency/scale patterns (hot-hot data centers, multicast vs TCP, hardware time-stamping, PTP clock sync).
- Data lakes for analytics (tick capture, TCA, anomaly detection), and integration with OMS/EMS vendor solutions.
- **Sources:** "Designing Exchanges" by Larry Harris (technology chapters); Nasdaq INET architecture papers; vendor docs (FlexTrade, Fidessa, Bloomberg EMSX).

## Suggested Study Path
1. Skim CFA Equity readings to level-set terminology.
2. Read Barry Johnson for execution/microstructure depth.
3. Pair each topic with a primary source (reg text, vendor guide) and summarize takeaways in flashcards.
4. Practice explaining concepts with business impact stories (e.g., how Reg NMS affects SOR design).

Use the sources noted per section as seed material; complement with recent sell-side primers and regulatory notices to stay current.
