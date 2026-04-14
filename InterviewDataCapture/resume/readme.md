# Equities Lead Developer Interview Study Notes

This file distills preparation material for a director-level interview in an Equities Stock Borrow Loan (SBL) technology team. It combines resume-linked keywords with deeper study topics, so you can map personal experience to the business domain.

## 1. Finance-Facing Keywords From The Resume
The interviewer is likely to probe anything on the resume that intersects with financial markets or trading controls. Be ready to describe the business motivation, technical implementation, and impact for each of the following:

| Resume Keyword / Phrase | Why It Matters In Equity Trading Conversations |
| --- | --- |
| **Crypto exchange order matching & position management** | Demonstrates understanding of crossing engines, priority rules, and how holdings are updated for spot vs. perpetual instruments. Tie it back to equity central limit order books (CLOBs). |
| **Cross-collateral & liquidation risk tooling** | Shows experience with credit risk mitigation and margin logic that parallels equity short-selling and prime brokerage risk. |
| **FIX protocol, Drop Copy, hot–cold session management** | Core connectivity pattern for equities (client order flow, market data, regulatory drop copies). Expect questions about sequence gaps, session recovery, and certification. |
| **OMS performance tuning (active/live orders)** | Directly maps to cash-equity order state stores and borrow/locate management components. Discuss latency, pagination, and idempotency strategies. |
| **Commodities e-Trading, SEDA/FPG architecture** | Highlights ability to design event-driven trading stacks—a pattern also used in cash-equity algo desks and inventory systems. |
| **TWAP-based hedging & spread management** | Illustrates familiarity with execution algos and how credit tiers or internal borrow costs change quoted spreads. |
| **LME / CME connectivity & market data failover** | Equity directors value engineers who understand exchange-specific nuances, kill switches, and handshakes. |
| **Drop-Copy feeds for clients** | Mirrors equities prime brokers giving clients post-trade confirmations; you can speak about entitlement controls and FIX tags (35=AE, 75, 55…). |
| **Rates e-Trading platform / intra-day risk** | Demonstrates pricing, valuation, and greeks computation skill—transferable to equity delta/gamma hedging. |
| **Total Return Swap (TRS) support** | Equities desks use TRS for synthetic exposure; explain funding legs, resets, and hedging with physical borrow. |
| **Basel II/III, RWA, limit management** | Directors may test knowledge of capital usage, stress scenarios, and how tech enforces concentration or single-name borrow limits. |
| **Credit risk & limit management systems** | Relevant for ensuring short availability, borrow caps, and counterparty exposure in SBL. |
| **MongoDB/Kdb regulatory & desk reporting** | Shows ability to serve regulators (e.g., Reg SHO, CAT) and internal surveillance, which is critical for equities financing workflows. |
| **Triage / RCA leadership** | Expect situational questions on handling exchange outages, fail-to-deliver spikes, or corporate-action driven recalls. |

## 2. Stock Borrow Loan (SBL) Business Primer
Stock borrow loan (a.k.a. securities lending) enables short selling, hedging, and collateral upgrades. Be fluent in the following lifecycle:

1. **Locate & inventory management**: The locate desk checks internal inventory, rehypothecated positions, and external lending pools (agent lenders, other primes) to determine availability and borrow costs. The system must respect beneficial owner restrictions and regulatory limits (e.g., Reg SHO in the U.S.).
2. **Borrow negotiation**: Once quantity is secured, terms are locked—loan rate (fee or rebate), currency, acceptable collateral (cash vs. non-cash), haircuts, and any rights on recalls. Specials (hard-to-borrow names) carry high fees and intraday rate volatility.
3. **Settlement & booking**: The loan settles like a delivery-vs-payment (DVP) trade. Title transfers to the borrower, who owes manufactured dividends/interest back to the lender plus borrow fees accrued daily.
4. **Lifecycle events**: Systems monitor collateral calls, rate re-fixes, borrower substitutions, recalls, corporate actions (dividends, splits, mergers), and marks for fails. Equity financing tech must automatically recall or re-route borrows around record dates and tender offers.
5. **Return / buy-in**: Loans end via borrower return (delivering shares back) or lender recall. Regulation SHO and local market rules can trigger mandatory buy-ins if the borrower cannot source shares.

### Key metrics & controls
- **Availability & GC vs. Special books**: Distinguish general collateral (low-fee liquid names) and specials (tight supply) to explain pricing logic.
- **Utilization & concentration**: Track how much of a security’s lendable inventory is deployed; align with VaR/ES limits and client concentration caps.
- **Funding spreads**: Borrow rate relative to benchmark (Fed Funds, SOFR) impacts desk P&L; negative rebate trades vs. fee trades have different accounting.
- **Operational risk**: Recall management, settlement fails, manufactured dividend accuracy, and collateral margining (daily mark-to-market).

> **Deep dives**: [SIFMA Securities Lending Primer](https://www.sifma.org/resources/general/securities-lending-primer/), [ISLA Securities Lending Overview](https://www.islaemea.org/securities-lending/), [DTCC CNS Stock Borrow Program](https://www.dtcc.com/clearing-services/equities-clearing-services/cns-stock-borrow). 

## 3. Greeks & Risk Sensitivities Relevant To Equities Financing
Even in loan-centric roles, directors expect precise risk language:

- **Delta (∂P/∂S)**: Measures price sensitivity of synthetic or hedged positions (e.g., TRS, options overlays). SBL teams hedge short exposure by buying shares equal to net delta. 
- **Gamma (∂Δ/∂S)**: Important when supporting delta-one vs. options desks; high gamma near the money requires intraday rebalancing, impacting borrow needs.
- **Theta**: Time decay affects option writers and structured equity trades that may drive borrow demand when they roll hedges.
- **Vega**: Volatility changes feed into securities finance funding (e.g., structured notes hedged with options may need more borrow when vega spikes).
- **Rho / Carry (∂P/∂r)**: Rate moves change financing costs, borrow rebates, and TRS funding legs.
- **Stock loan-specific metrics**: Borrow cost (b), negative rebate, and **Funding Value Adjustment (FVA)** for collateral usage.

Be ready to map how technology surfaces these metrics to trading, risk, and collateral teams (e.g., streaming greeks from quant libraries, caching in Kdb, distributing via Solace/Kafka).

> **References**: [Cboe Options Greeks Guide](https://www.cboe.com/learncenter/options-strategies/options-greeks/), [CME Delta Hedging Primer](https://www.cmegroup.com/education/courses/introduction-to-options/delta-hedging.html), [ISDA Margin & Funding Adjustments](https://www.isda.org/a/pmiEE/isda-margin-survey.pdf).

## 4. Hedging Logic Used Around Stock Loans
Discuss the multi-layered hedging stack that a lead developer must enable:

1. **Locate vs. borrow vs. synthetic**: Describe when the desk borrows physical shares, uses internal inventory, or executes synthetic substitutes (TRS, single-stock futures, ETFs) to cover shorts.
2. **Delta hedging for structured products**: Use TWAP/VWAP algos to source borrow gradually and minimize market impact; show awareness of execution algo parameters (slice size, child order urgency, throttles).
3. **Basis & pair trades**: Hedge convertibles, ADR/local pairs, and ETF creations by borrowing components; highlight how hedging logic manages correlation breakdowns and recall risk.
4. **Inventory optimization**: Algorithms choose which lending pool to tap (internal, external GC, agent lenders) based on rate, utilization, and settlement risk; mention scoring models and ML features (age of borrow, counterparty reliability).
5. **Regulatory kill switches**: Systems enforce client-level or security-level stop logic if borrow availability drops below threshold, or if regulatory halts (short sale restrictions) kick in.

> **References**: [Morgan Stanley Prime Brokerage Stock Loan Overview](https://www.morganstanley.com/articles/what-is-prime-brokerage), [ECB Shadow Banking Securities Lending Study](https://www.ecb.europa.eu/pub/financial-stability/macroprudential-bulletin/html/ecb.mpbu202204_02~07dc9b3e1a.en.html), [CFA Institute Short-Selling Guide](https://www.cfainstitute.org/-/media/documents/support/programs/investment-foundations/cfa-short-selling.pdf).

## 5. Margin Trading & Collateral Mechanics
Key talking points connecting borrow activity with margin platforms:

- **Initial vs. maintenance margin**: Explain Reg T (U.S.) or local equivalents, and how portfolio margin frameworks lower requirements for hedged books. 
- **Variation margin & collateral substitution**: Systems recalc exposure intraday (mark-to-market). Discuss workflows for accepting cash vs. securities, FX haircuts, and rehypothecation.
- **Risk-based margin (SPAN, TIMS)**: For prime services, describe how margin engines consume greeks and scenario shocks to set requirements for delta-one funding clients.
- **Margin calls & liquidation**: Tie back to crypto experience (auto-liquidation) but highlight differences in equities (manual notices, buy-ins, fail cures).
- **Client tiers & credit ratings**: Similar to quoting TWAP spreads, margin engines tier clients by ratings which drive borrow pricing and allowed leverage.

> **References**: [FINRA Margin Disclosure Statement](https://www.finra.org/investors/learn-to-invest/advanced-investing/margin-statistics/margin-disclosure-statement), [OCC Portfolio Margin Overview](https://www.theocc.com/about/publications/portfolio-margining), [BIS Basel III Margin Requirements](https://www.bis.org/publ/bcbs280.htm).

## 6. Cash Equities Flow & Supporting Topics
Being conversant in the straight-through-processing (STP) chain strengthens credibility with an equities director:

1. **Order lifecycle**: Client order → algo/OMS → exchange (CLOB, dark pool, SI) → confirmation (FIX drop copy) → booking.
2. **Post-trade & settlement**: Affirmation (Omgeo CTM), clearing (NSCC/DTCC), Continuous Net Settlement (CNS) stock borrow program, and move toward T+1 in the U.S. (impact on recall & collateral timetables).
3. **Fails management**: Reg SHO close-outs, buy-in desks, use of CNS Stock Borrow to cover same-day fails.
4. **Corporate actions & tax**: How systems track manufactured dividends, withholding tax on loaned shares, and special processing for tender offers or spinoffs.
5. **Regulatory reporting**: CAT, SEC 13f-2 short sale reporting (U.S.), SFTR (EU/UK) for securities finance transactions—tie to data tooling (MongoDB/Kdb) on the resume.
6. **Controls & monitoring**: Real-time market data checks, price collars, self-match prevention, locates logs, surveillance alerts routed through Datadog/Kafka/Solace pipelines.

> **References**: [DTCC Equities Clearing Overview](https://www.dtcc.com/clearing-services/equities-clearing-services), [SEC Reg SHO FAQ](https://www.sec.gov/divisions/marketreg/mrfaqregsho1204.htm), [FIA Post-Trade Processing Guide](https://www.fia.org/resources/post-trade-processing-primer).

## 7. Bringing It Together For The Interview
- Frame each resume keyword with a **business problem → technical action → measurable outcome** narrative that resonates with equities financing (availability, risk, regulatory control, latency).
- For each domain topic above, prepare 2–3 short customer-impact stories (e.g., “how we prevented a fail chain during a special dividend recall”).
- Keep handy diagrams of system architecture (FIX gateways, borrow inventory service, margin engine) and note where the greeks feed or margin data sits—directors appreciate system thinking.
- Cross-reference the external reading links for deeper dives and cite them when discussing best practices.

Good luck! Use this document as a checklist before the interview and update with additional notes/examples after each study session.
