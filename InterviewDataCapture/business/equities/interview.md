## Question: How do you differentiate between primary and secondary equity markets?
* Interviewer: Walk me through how capital is raised in primary markets versus how shares trade later.
* Interviewee: The primary market involves issuers selling new shares via IPOs or follow-ons through book-builds or auctions, while the secondary market is where existing holders trade those shares on exchanges or off-exchange venues, providing liquidity and price discovery without raising new capital.

## Question: What role do underwriters play in an IPO?
* Interviewer: Describe their responsibilities beyond marketing.
* Interviewee: Syndicate banks underwrite risk by committing to buy unsold shares, perform due diligence, stabilize prices through greenshoe options, allocate shares to investor tiers, and coordinate regulatory filings with exchanges and securities commissions.

## Question: Explain the difference between common and preferred stock.
* Interviewer: Highlight voting, dividend, and capital structure distinctions.
* Interviewee: Common stock carries voting rights and residual claim on profits, with dividends varying, while preferred stock usually has fixed dividends, priority in distributions, often no votes, and may include conversion or call features.

## Question: How does market microstructure impact execution quality?
* Interviewer: Connect spread, depth, and latency to fills.
* Interviewee: Narrow spreads, deep books, and low latency matching engines reduce slippage, whereas fragmented liquidity and stale quotes raise impact costs, so technology choices and venue routing affect realized execution.

## Question: What are the main order types equities desks rely on?
* Interviewer: Give examples of protective and opportunistic orders.
* Interviewee: Core types include market, limit, stop, stop-limit, IOC, FOK, pegged, iceberg, and conditional orders like VWAP or percentage-of-volume instructions used when targeting benchmarks or hiding size.

## Question: Describe how a smart order router works.
* Interviewer: Focus on decision inputs.
* Interviewee: The router consumes real-time market data and fee schedules, evaluates venue-specific liquidity, applies constraints (latency, fill probability, dark pool priority), and slices or sequences child orders to meet execution goals while adhering to Reg NMS or MiFID best-ex rules.

## Question: How do VWAP and TWAP algorithms differ?
* Interviewer: Why choose one over the other?
* Interviewee: VWAP targets the market volume profile, allocating slices proportional to expected volume each interval, while TWAP spreads evenly across time; VWAP minimizes slippage when volume curves are known, whereas TWAP is simpler when liquidity is flat or unpredictable.

## Question: What is implementation shortfall?
* Interviewer: Explain components.
* Interviewee: Implementation shortfall is the difference between a decision price and the final execution cost, decomposed into delay cost, market impact, and opportunity cost from unfilled shares, serving as a trading-performance KPI.

## Question: How do market makers manage inventory risk?
* Interviewer: Discuss hedging knobs.
* Interviewee: They dynamically adjust quotes, skew spreads, delta-hedge with futures or ETFs, set inventory limits, and use risk models (Avellaneda-Stoikov) that trade off spread versus inventory deviation to keep net exposure near targets.

## Question: What is payment for order flow and why is it controversial?
* Interviewer: Provide pros and cons.
* Interviewee: PFOF is compensation from wholesalers to brokers for routing retail flow; proponents cite price improvement and commission-free trading, critics argue it creates conflicts of interest and fragments price discovery, drawing scrutiny from the SEC and EU regulators.

## Question: How does Reg NMS affect routing decisions?
* Interviewer: Focus on Rule 611.
* Interviewee: Rule 611 imposes trade-through protection, forcing routers to check protected quotes and avoid executing at inferior prices, so routers must access top-of-book NBBO quotes or use intermarket sweep orders with proper tagging and exception logic.

## Question: Contrast lit exchanges with dark pools.
* Interviewer: Discuss transparency and use cases.
* Interviewee: Lit venues display quotes and contribute to NBBO formation, ideal for price discovery, whereas dark pools hide orders to minimize impact, often executing at midpoints; however, dark pools face regulatory limits (MiFID II double volume caps) and require surveillance to prevent information leakage.

## Question: What is the purpose of opening and closing auctions?
* Interviewer: Why do desks care?
* Interviewee: Auctions consolidate liquidity at the open and close, generating reference prices for index funds and TCA benchmarks; many algos schedule participation near the close due to high volume concentration and ETF rebalance activity.

## Question: Explain short selling mechanics.
* Interviewer: Touch on borrow, locate, and close-out.
* Interviewee: Shorting requires borrowing shares from a lender via prime brokers, booking a locate per Reg SHO, paying stock-loan fees, delivering borrowed shares at settlement, and covering the position later, while monitoring recalls and close-out rules to avoid fails-to-deliver.

## Question: How do corporate actions impact trading systems?
* Interviewer: Give practical adjustments.
* Interviewee: Systems must apply factors for splits, dividends, spin-offs, and rights, adjusting order quantities, position sizes, and analytics (VWAP histories, Greeks) so that risk, PnL, and execution benchmarks remain consistent post-event.

## Question: What are dark liquidity indicators like D-quote or conditional order ack?
* Interviewer: Explain signaling management.
* Interviewee: Conditional orders allow traders to rest size in dark pools but require firm-up acknowledgments when contra liquidity is found, helping to minimize signaling by limiting when firm orders are exposed; D-quotes at NYSE similarly enable reserve-style participation in auctions.

## Question: Why do equities desks monitor index rebalances?
* Interviewer: Discuss trading impact.
* Interviewee: Additions/deletions trigger mechanical demand from passive funds, causing predictable volume spikes and price pressure, so traders pre-position inventory, provide liquidity to indexers, or run risk-transfer trades to capture spread.

## Question: Outline key equities risk measures beyond VaR.
* Interviewer: Include sensitivities.
* Interviewee: Desks track factor exposures (beta, style factors), stress scenarios (shock by historical crises), liquidity-adjusted VaR, concentration limits, and scenario-specific Greeks for derivative overlays tied to equity positions.

## Question: How do you interpret alpha and beta in performance attribution?
* Interviewer: Keep it quant but intuitive.
* Interviewee: Beta quantifies systematic exposure to market moves, so beta-adjusted performance isolates alpha, the excess return from security selection or timing; attribution decomposes contributions by factor, sector, or trade idea to show where alpha originates.

## Question: What is the role of equity swaps in front-office workflows?
* Interviewer: Why use swaps instead of cash positions?
* Interviewee: Total return swaps give synthetic exposure without balance-sheet usage, enabling leverage, hedging, or confidentiality; desks must manage financing, dividend adjustments, and counterparty credit risk while booking delta-equivalent hedges in cash markets.

## Question: How does securities lending generate revenue for an equities desk?
* Interviewer: Mention term lending and collateral.
* Interviewee: The desk lends hard-to-borrow shares to shorts against cash or non-cash collateral, charging borrow fees that depend on utilization, specialness, and corporate action risk, while managing recalls and collateral reinvestment.

## Question: Explain how tick size influences liquidity.
* Interviewer: Tie to queue priority and spreads.
* Interviewee: Larger ticks widen quoted spreads and may incentivize displayed liquidity but can penalize price competition, while smaller ticks tighten spreads but can fragment depth; studies like the Tick Pilot evaluate optimal increments per stock liquidity bucket.

## Question: What technology components make up an equities EMS?
* Interviewer: Walk through flow.
* Interviewee: An EMS includes market data adapters, order blotters, algo parameter GUIs, SOR engines, risk checks (price collars, fat-finger, credit), FIX gateways, drop-copy feeds, and analytics dashboards for TCA and market color.

## Question: How do you control for spoofing or layering on an equities desk?
* Interviewer: Mention surveillance logic.
* Interviewee: Real-time monitors look for patterns of large orders canceled rapidly after moving prices, correlate child order placements with trade executions on other venues, enforce messaging throttles, and escalate suspicious behavior to compliance with audit trails and voice logs.

## Question: Why is time synchronization critical in equities trading?
* Interviewer: Think compliance and debugging.
* Interviewee: Accurate timestamps (PTP/IEEE 1588, GPS) ensure sequencing of orders for MiFID RTS 25, enable reconstruction after incidents, support latency measurements, and allow regulators to audit best-ex claims.

## Question: Describe the lifecycle of an order from OMS to settlement.
* Interviewer: Summarize key hops.
* Interviewee: The OMS captures client intent, slices into child orders sent via FIX to EMS/SOR, executes on venues, confirms via drop copies, allocates fills back to accounts, feeds middle office for confirmations/affirmations (CTM), and finally matches in clearing at T+2 (moving to T+1 in US).

## Question: How do equities desks assess venue toxicity?
* Interviewer: Define the term.
* Interviewee: Toxicity refers to adverse selection; desks compute metrics like reversion after fills, markouts, fill-to-reject ratios, or use machine learning to rank venues, throttling those where fills consistently lose money versus less toxic alternative pools.

## Question: What is the role of dark midpoint peg orders?
* Interviewer: Explain pricing logic.
* Interviewee: Midpoint peg orders execute at the mid of NBBO, offering price improvement over displayed quotes, often used for large-in-size or low-urgency flow, but they depend on stable NBBO and can be impacted by flickering markets.

## Question: How do you handle hard-to-borrow stocks during corporate actions?
* Interviewer: Address dividend and split events.
* Interviewee: Lenders may recall shares ahead of record dates or adjust borrow fees, while traders must manage manufactured dividends to lenders and confirm new cusips or conversion ratios to maintain hedges post-event.

## Question: Explain the concept of a synthetic short built with options.
* Interviewer: Why might it be preferable?
* Interviewee: A synthetic short combines a long put and short call at the same strike/expiry to replicate short stock payoff, avoiding borrow constraints but introducing option liquidity, margin, and early assignment considerations.

## Question: What is liquidity fragmentation and how do you mitigate it?
* Interviewer: Relate to technology choices.
* Interviewee: Fragmentation occurs when liquidity is split across dozens of venues; mitigation involves low-latency connectivity, predictive routing, liquidity aggregation, and interlisted arbitrage to ensure best fills.

## Question: How do equities desks price block trades?
* Interviewer: Mention risk transfer and capital charge.
* Interviewee: Sales traders quote a discount/premium to last price reflecting risk of warehousing inventory, volatility, borrow cost, and capital usage, usually referencing statistical models for expected move plus a markup for capital and distribution.

## Question: What metrics feed equities trader dashboards daily?
* Interviewer: Provide examples.
* Interviewee: Dashboards show overnight news, futures indications, sector heatmaps, risk exposures, client axes, IOI interest, intraday volume curves, realized spread, markout, and algo health metrics (latency, reject rates).

## Question: How do you explain factor models to business stakeholders?
* Interviewer: Keep jargon minimal.
* Interviewee: Factor models break returns into exposures to broad characteristics (size, value, momentum); by understanding exposures, traders know whether performance stems from intended bets or unintended tilts, guiding hedging or client messaging.

## Question: Why does settlement shortening to T+1 matter?
* Interviewer: List operational impacts.
* Interviewee: Faster settlement compresses affirmation windows, requires automation for allocations, reduces counterparty risk but increases funding pressure, so systems must accelerate confirmation, stock loan, and FX hedging workflows.

## Question: What is a single-stock circuit breaker?
* Interviewer: Outline triggers and effects.
* Interviewee: Limit Up/Limit Down bands halt trading when prices move outside dynamic thresholds for specified periods, preventing flash-crash behavior; routers must honor limit states and reroute to alternative venues or park orders until trading resumes.

## Question: How do you model transaction cost analysis for equities?
* Interviewer: Mention data inputs.
* Interviewee: TCA ingests trade timestamps, sizes, prices, benchmarks (arrival, VWAP, close), market data (NBBO, volume), and normalizes by volatility to output slippage, impact, and peer comparisons, driving algo tuning and client reports.

## Question: What are ADRs and why would a client trade them instead of local shares?
* Interviewer: Address liquidity and settlement.
* Interviewee: ADRs are US-listed receipts representing foreign shares; clients trade them for USD settlement, US hours, and simpler custody, though pricing must account for ADR ratio, FX, and home-market liquidity.

## Question: Describe how equities desks interact with delta-one and derivatives teams.
* Interviewer: Provide examples.
* Interviewee: Cash traders hedge ETF creations/redemptions or swap desks’ hedges, share borrow color, collaborate on dividend forecasts, and coordinate when options gamma hedging needs immediate cash equity executions.

## Question: How are ETFs created and redeemed?
* Interviewer: Outline AP workflow.
* Interviewee: Authorized participants deliver baskets of underlying securities (or cash) to the ETF sponsor to receive shares (creation) or return shares for the basket (redemption), enabling arbitrage that keeps ETF prices aligned with NAV; trading desks facilitate basket execution and hedging.

## Question: What is internalization in equities trading?
* Interviewer: Explain benefits and risks.
* Interviewee: Internalization matches client orders against the firm’s own inventory or other client flow, reducing market impact and fees, but it requires price improvement, conflicts management, and transparency under regulations like Reg ATS and MiFID.

## Question: How do dark pool conditional orders differ from firm orders?
* Interviewer: Clarify workflow.
* Interviewee: Conditional orders rest indications without committing capital; when a match is found, both sides must firm up quickly, allowing participants to manage information leakage while still sourcing block liquidity.

## Question: Why do equities desks monitor borrow utilization metrics daily?
* Interviewer: Connect to trading constraints.
* Interviewee: High utilization signals scarcity, driving special borrow fees and potential recalls; traders use this data when quoting swaps, shorting, or pricing risk transfers that rely on stable borrow.

## Question: What controls prevent fat-finger errors?
* Interviewer: Mention pre-trade risk.
* Interviewee: Systems enforce price collars, maximum order size, notional and quantity limits, duplicate detection, and trader entitlement checks before releasing orders to venues, often mandated by SEC 15c3-5 Market Access Rule.

## Question: How does MiFID II influence equities transparency?
* Interviewer: Provide concrete obligations.
* Interviewee: MiFID II imposes pre- and post-trade transparency via APA reporting, caps dark pool usage via double volume caps, mandates best-ex policies with RTS 27/28 reporting, and tightens clock synchronization and algo certification.

## Question: What are the main differences between passive and aggressive algos?
* Interviewer: Provide use cases.
* Interviewee: Passive algos rest liquidity to earn spread, suitable for low urgency trades, while aggressive algos cross the spread or sweep liquidity to minimize timing risk, used when urgency outweighs cost concerns.

## Question: How do equities desks support corporate buyback programs?
* Interviewer: Mention regulatory limits.
* Interviewee: Desks execute within safe-harbor rules (e.g., Rule 10b-18 volume and timing limits), manage blackout periods, provide daily execution reports, and may run accelerated share repurchases involving derivatives.

## Question: Explain pair trading in equities.
* Interviewer: Mention signal generation and execution.
* Interviewee: Pair trading identifies correlated stocks, goes long the undervalued leg and short the overvalued leg, hedging market beta; execution stresses synchronized fills and borrow availability while monitoring divergence thresholds.

## Question: Why do traders care about free float versus total shares outstanding?
* Interviewer: Tie to liquidity.
* Interviewee: Free float excludes locked-up or insider-held shares, better reflecting tradable supply; indices and liquidity metrics rely on float to gauge capacity for large trades and to adjust weighting.

## Question: How are ESG considerations integrated into equities trading?
* Interviewer: Provide examples.
* Interviewee: Desks maintain exclusion lists, tag orders with ESG instructions, source green-labeled liquidity pools, and report on portfolio carbon metrics, often integrating alternative data into idea generation while ensuring compliance with client mandates.

