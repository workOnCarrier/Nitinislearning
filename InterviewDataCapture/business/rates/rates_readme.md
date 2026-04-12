# Rates Front-Office Interview Concepts

Key fixed-income and interest-rate topics technologists and leaders should command before a trading interview. Each section includes representative learning sources.

## 1. Rate Instruments & Products
- Government bonds, bills, notes; agencies, supranationals, covered bonds, inflation-linked issues.
- Interest rate swaps (IRS), OIS, basis swaps, cross-currency swaps, futures (ED/ERM), FRAs, caps/floors, swaptions.
- Structured notes (CMS, range accruals), callable/putable bonds, mortgage-backed securities (MBS) and TBAs.
- **Sources:** Fabozzi, "Fixed Income Analysis"; ISDA product primers; CME interest rate futures guides.

## 2. Yield Curve Construction & Term Structure
- Bootstrapping spot curves from deposits, futures, swaps; spline or monotone convex interpolation.
- Curve smoothing (Nelson-Siegel, Svensson), multi-curve frameworks (OIS discounting vs LIBOR/EURIBOR forwarding).
- Key rate durations, DV01 ladders, scenario curve shifts (parallel, steepener, flattener).
- **Sources:** Henrard, "Interest Rate Modelling"; BIS Working Papers on multi-curve; QuantLib documentation.

## 3. Pricing & Risk Analytics
- Present value, discount factors, accrual conventions (30/360, ACT/360), day count adjustments.
- Duration, convexity, PV01, bucketed delta, gamma/delta for swaptions, vega for volatility products.
- SABR/LMM volatility surface modeling, smile management, multi-factor HJM models.
- **Sources:** Brigo & Mercurio, "Interest Rate Models"; Bloomberg FI courseware; ISDA SIMM methodology notes.

## 4. Funding, Collateral, and Clearing
- CSA terms, margining (variation vs initial), collateral optimization, discounting choices.
- Central clearing via LCH, CME, Eurex; default fund structure, trade compression, CCP basis.
- Repo markets (GC vs special), securities lending for HQLA, balance-sheet constraints (SLR, NSFR).
- **Sources:** ISDA collateral management papers; LCH/CME rulebooks; ICMA repo market best practices.

## 5. Trading Strategies & Workflows
- Cash vs derivatives desks, relative value (butterfly, box trades), curve trades, basis trades, inflation hedging.
- Execution styles (voice risk transfer, dealer RFQ, streaming APIs, CLOBs like BrokerTec, MarketAxess).
- Primary auctions, when-issued trading, taps, buybacks, central bank operations (QE, QT).
- **Sources:** Citi and JPM rates strategy primers; MarketAxess all-to-all trading guides; UST primary dealer handbooks.

## 6. Market Structure & Regulation
- SEFs (swap execution facilities) vs D2D interdealer brokers vs D2C platforms; MiFID II transparency (APA reporting) for bonds and derivatives.
- Dodd-Frank clearing/execution mandates, TRACE/EMIR reporting, CFTC swap data repositories.
- Benchmark reforms (LIBOR cessation, SOFR/ESTR/SONIA adoption) and fallback language.
- **Sources:** CFTC SEF rules; ARRC/ISDA LIBOR transition documentation; ESMA/MiFID RTS for bonds.

## 7. Risk & PnL Control
- Intraday PnL explained by carry, curve, basis, vol; linking risk reports with FO pricing.
- Stress testing (rate shocks, basis blowouts, liquidity droughts) and scenario libraries.
- Limits on DV01, gamma, vega, basis tenor exposures; hedging with futures, swaps, options.
- **Sources:** Basel FRTB IMA/SA papers; bank treasury risk policy docs; MSCI RiskMetrics for rates.

## 8. Technology & Data Considerations
- Real-time curve services, pricing libraries (QuantLib, in-house), scenario engines offloading to grids.
- Low-latency streaming quotes for US Treasuries, STIR futures, OTC quoting via FIX/FPML.
- Reference data (ISIN/CUSIP, coupon schedules, day-count, holiday calendars), event handling for coupon payments and schedule changes.
- **Sources:** QuickFIX/FPML specs; Refinitiv/Bloomberg FI data dictionaries; open-source risk engines (OpenGamma, fincad docs).

## 9. Client & Sales Workflow
- Risk runs to clients (axes, inventory), distribution of liquidity via chat, API, or voice.
- Pricing structures for corporates vs asset managers, balance-sheet charges, capital add-ons for large trades.
- Post-trade: affirmation (MarkitWire), confirmation (SWIFT, FpML), settlement (Fedwire, Euroclear, CLS for swaps).
- **Sources:** MarkitSERV user guides; DTCC derivatives services; AFME client clearing primers.

## Suggested Study Plan
1. Refresh core fixed-income math (discounting, duration) via Fabozzi or CFA Level II FI readings.
2. Study derivatives microstructure and regulation via ISDA/ARRC resources.
3. Practice articulating technology implications (curve services, risk engines, connectivity) with business value narratives.
4. Create flashcards from each section, capturing formulas (DV01, convexity) and workflow steps (SEF trade lifecycle).
