## Question: Why is the yield curve the core reference for rates trading?
* Interviewer: Put its strategic value in business terms.
* Interviewee: The curve summarises market expectations for funding, inflation, and term premia, so traders use its shape to price everything from swaps to mortgages, set hedge ratios, and signal macro sentiment to sales and clients.

## Question: How do you bootstrap a discount curve from market instruments?
* Interviewer: Walk through the sequence.
* Interviewee: Start with short-dated deposits for the first few tenors, use futures or FRAs to lock in medium points, and extend with swap par rates; each tenor is solved iteratively so that discount factors reproduce observed quotes, often using piecewise-linear or spline interpolation.

## Question: Can you contrast Macaulay duration with DV01 and convexity?
* Interviewer: Explain when each metric is preferable.
* Interviewee: Macaulay/modified duration measures percentage price sensitivity to parallel shifts, DV01 provides dollar impact per basis point for hedging, while convexity captures curvature so large moves or long maturities require convexity adjustments beyond linear duration approximations.

## Question: How do you explain DV01 to a sales colleague?
* Interviewer: Keep it practical.
* Interviewee: DV01 is simply how many dollars the position gains or loses if rates move one basis point; it lets us size hedges quickly by matching DV01s across instruments regardless of price or notional differences.

## Question: What differentiates LIBOR from SOFR?
* Interviewer: Mention risk profile and data sources.
* Interviewee: LIBOR was a panel-based unsecured bank funding rate embedding credit risk, whereas SOFR is a transaction-based secured overnight repo rate backed by Treasury collateral, so SOFR is nearly risk-free and requires adjustments (spreads, compounding) when replacing LIBOR.

## Question: Why do modern desks use multi-curve pricing frameworks?
* Interviewer: Explain the drivers post-crisis.
* Interviewee: After 2008, basis between funding curves exploded, so we discount collateralized trades on OIS curves while projecting forward cashflows on tenor-specific curves (3M, 6M), ensuring pricing reflects actual funding and collateral terms.

## Question: How do you price a plain-vanilla interest rate swap?
* Interviewer: Outline fixed and floating legs.
* Interviewee: Discount each fixed coupon plus notional at maturity using the discount curve, discount expected floating payments derived from forward rates, then set the fixed rate so the PVs match; mid-market PV is zero, while spreads account for credit and funding charges.

## Question: What drives swap spreads versus Treasuries?
* Interviewer: State key factors.
* Interviewee: Swap spreads reflect relative supply/demand for swaps vs bonds, balance-sheet costs, credit risk of banks, and flight-to-quality flows; widening often signals stress or scarcity of high-quality collateral, while narrowing indicates ample balance sheet or heavy Treasury issuance.

## Question: When would you use an FRA instead of a futures contract?
* Interviewer: Give business context.
* Interviewee: FRAs are OTC and tailored to exact start/end dates with credit exposure to a counterparty, useful for bespoke hedges, whereas futures are standardized, exchange-traded with daily margining, offering more liquidity but limited date flexibility.

## Question: Why is OIS discounting considered the standard for collateralized trades?
* Interviewer: Provide economic rationale.
* Interviewee: Under CSA agreements variation margin earns the overnight collateral rate, so discounting future cashflows at OIS ensures PV consistency with actual funding; using LIBOR discounting would misprice trades by ignoring collateral remuneration.

## Question: How do you explain the benefits of central clearing to a client?
* Interviewer: Cover risk and operational angles.
* Interviewee: Clearing novates trades to a CCP, concentrates collateral management, enables multilateral netting, reduces bilateral credit exposure, and satisfies regulatory mandates, though clients must manage margin and default fund contributions.

## Question: Differentiate variation margin from initial margin.
* Interviewer: Why does tech care?
* Interviewee: Variation margin covers current mark-to-market and moves daily, so systems must support frequent settlement and reconciliations; initial margin protects against future exposure and is model-based (e.g., ISDA SIMM), influencing funding and optimization engines.

## Question: How does a CSA's optional collateral currencies influence pricing?
* Interviewer: Mention optionality.
* Interviewee: If a CSA allows multiple collateral currencies, the cheapest-to-deliver currency creates embedded optionality; pricing libraries must model FX basis and apply discounts consistent with expected collateral choice, often via convexity adjustments.

## Question: Why are repo markets vital for rates desks?
* Interviewer: Tie to balance sheet usage.
* Interviewee: Repo provides short-term funding for bond inventories, enables short-selling via borrowing, and sets the collateralized funding benchmark; disruptions in repo translate directly into trading capacity and pricing of specials vs GC.

## Question: Explain the difference between general collateral and special repo.
* Interviewer: Give operational implications.
* Interviewee: GC repos use a basket of acceptable collateral at market rates, while specials involve specific sought-after bonds with lower rates reflecting scarcity; specials influence short squeeze dynamics and hedging costs for on-the-run Treasuries.

## Question: How do central bank policy actions ripple through rates markets?
* Interviewer: Cover QE/QT and rate hikes.
* Interviewee: Policy rates anchor the front-end, asset purchases compress term premia by removing duration, and QT releases collateral causing curve steepening; desks anticipate flows from reserve management, roll risk in futures, and adjust pricing to policy path probabilities.

## Question: Walk me through a US Treasury auction lifecycle.
* Interviewer: Include primary dealers.
* Interviewee: Treasury announces size, dealers submit competitive bids via TAAPS, auction clears with stop-out yield, allocations flow to bidders, when-issued trading transitions to on-the-run once securities settle, and desks manage syndicate positions plus post-auction supply absorption.

## Question: What is the purpose of when-issued trading?
* Interviewer: Describe benefits.
* Interviewee: WI trading allows price discovery and hedging before new Treasuries settle, letting dealers distribute risk, clients lock yields, and futures hedges be fine-tuned; prices converge to auction results at issuance.

## Question: Explain a butterfly trade on the curve.
* Interviewer: Provide intuition.
* Interviewee: A butterfly combines long and short positions at three maturities to bet on curvature; for example, long wings and short belly profits if the middle maturity cheapens relative to wings, often DV01-neutral to focus on local shape changes.

## Question: How do you use key rate duration in risk management?
* Interviewer: Why not rely on parallel DV01 only?
* Interviewee: Key rate durations break exposures into discrete maturity buckets so we can hedge non-parallel shifts; it highlights concentrations (e.g., 5-year bucket) and guides targeted hedges via bonds or swaps at those tenors.

## Question: Describe how you set up a curve steepener trade.
* Interviewer: Explain hedging details.
* Interviewee: A steepener is long long-end duration and short short-end duration, typically balancing DV01 so net exposure is to slope changes; execution might use futures (e.g., long UXY, short FV) or swaps at matched PV01 with stops tied to macro catalysts.

## Question: What are inflation-linked bonds and why do they matter?
* Interviewer: Mention cashflow mechanics.
* Interviewee: Linkers like TIPS adjust principal with CPI, so coupons and redemption scale with inflation; they provide real-yield exposures and hedges for liability-driven investors, affecting breakeven inflation markets and derivative pricing.

## Question: How do you compute breakeven inflation from TIPS and nominals?
* Interviewer: Give the quick formula.
* Interviewee: Subtract the real yield of a TIPS from the nominal Treasury yield of the same maturity; the result approximates market-implied inflation expectations plus risk and liquidity premia.

## Question: How do systems handle negative yields?
* Interviewer: Highlight pitfalls.
* Interviewee: Pricing libraries must avoid assumptions like min(0), allow discount factors above 1, manage log/ln calculations carefully, and ensure risk metrics (DV01, convexity) remain valid, particularly for European or Japanese curves.

## Question: What is the purpose of a cross-currency swap?
* Interviewer: Explain flows.
* Interviewee: Cross-currency swaps exchange principal and interest payments in two currencies, letting borrowers fund in one currency while paying liabilities in another; they hedge FX and interest-rate risk simultaneously, priced off two curves plus FX basis.

## Question: Define basis risk in rates trading.
* Interviewer: Provide an example.
* Interviewee: Basis risk is exposure to the spread between related rates, e.g., 3M vs 6M LIBOR or swap vs Treasury; a hedge may neutralize overall DV01 but still lose money if the spread moves, so desks monitor basis DV01 separately.

## Question: What is CCP basis and why has it grown?
* Interviewer: Discuss clearing fragmentation.
* Interviewee: CCP basis is the pricing difference between swaps cleared at different CCPs (LCH vs CME) due to disjoint default funds and liquidity pools; it reflects balance-sheet preferences and cross-margin benefits, so dealers charge clients when they can't net positions at the same CCP.

## Question: How do caps and floors differ from swaptions?
* Interviewer: Describe payoff structures.
* Interviewee: Caps/floors are series of interest-rate options on individual reset dates (caplets/floorlets) paying when a floating rate exceeds or falls below a strike, while swaptions give the right to enter an entire swap, providing exposure to the entire IRS PV rather than single resets.

## Question: Why is SABR popular for swaption volatility surfaces?
* Interviewer: Mention calibration features.
* Interviewee: SABR captures skew and smile with relatively few parameters, behaves well across strikes/maturities, and can be calibrated to market quotes for pricing exotics; desks manage alpha/beta/rho/nu stability to avoid arbitrage.

## Question: How do you hedge a swaption book's Greeks?
* Interviewer: Discuss delta and vega management.
* Interviewee: Delta hedges use underlying swaps or futures to neutralize rate sensitivity, while vega hedges rely on offsetting swaptions or variance trades; gamma and theta are managed via rolling hedges and adjusting strikes as the surface shifts.

## Question: What makes callable bonds challenging to model?
* Interviewer: Mention embedded options.
* Interviewee: Callable bonds combine fixed cashflows with issuer call optionality, so pricing requires lattice or Monte Carlo models using volatility assumptions; risk includes negative convexity as rates fall, necessitating option-adjusted spread analytics and hedging with swaptions.

## Question: Explain mortgage convexity risk to trading technology.
* Interviewer: Highlight feedback loops.
* Interviewee: As rates fall, mortgage prepayments accelerate, shortening duration and forcing investors to sell duration (negative convexity), while rising rates extend duration; desks must monitor dynamic hedges and ensure analytics refresh quickly with updated prepayment models.

## Question: How does TBA trading work in agency MBS markets?
* Interviewer: Cover settlement.
* Interviewee: TBAs trade generic pools defined by agency, coupon, and settlement month without specific pools until 48-hour day, enabling liquidity; allocations (stipulations) happen later, so systems must manage pool assignment, pair-offs, and dollar-roll funding.

## Question: When do you hedge duration with Treasury futures versus swaps?
* Interviewer: Outline considerations.
* Interviewee: Futures offer liquidity, exchange margining, and standardization but introduce CTD/roll basis risk, while swaps align more closely with liabilities and allow tenor-specific hedging albeit with counterparty and clearing costs; choice depends on balance sheet and precision needed.

## Question: What determines the cheapest-to-deliver bond on a futures contract?
* Interviewer: Explain conversion factors.
* Interviewee: Each eligible bond has a conversion factor to align coupons; the CTD minimizes the implied repo rate given futures price, so traders monitor yields, carry, and delivery options to anticipate which bond is optimal.

## Question: How do you manage roll risk around futures expiry?
* Interviewer: Describe operational steps.
* Interviewee: Desks unwind expiring positions, enter next-contract hedges, manage basis between contracts, and coordinate with clients to avoid delivery, often using calendar spreads and ensuring systems roll analytics and limits automatically.

## Question: Compare liquidity profiles of rates versus credit markets.
* Interviewer: Keep it concise.
* Interviewee: Benchmark rates (UST, Bunds, swaps) trade continuously with deep order books, while credit bonds are more episodic RFQ-driven; this affects technology emphasis—rates need low-latency streaming and curve analytics, credit needs workflow-heavy RFQ tooling.

## Question: What is the workflow for executing swaps on a SEF?
* Interviewer: Provide high-level steps.
* Interviewee: Traders submit RFQs or use order books on SEFs, receive quotes from liquidity providers, select a response, and the trade is captured electronically, reported to SDRs, often followed by straight-through processing to clearing via MarkitWire.

## Question: How do TRACE or SDR reporting rules impact technology builds?
* Interviewer: State requirements.
* Interviewee: Systems must capture regulatory fields (USI/UTI, execution timestamps, notional, product IDs), submit reports within minutes, manage corrections, and ensure clock sync; failure leads to fines, so logging and validations are critical.

## Question: What data inputs are essential for real-time curve building?
* Interviewer: List them.
* Interviewee: Live quotes for deposits, futures, swaps, OIS, basis spreads, plus calendar/day-count data, holiday files, fixing histories, and quality checks; the curve service must handle stale quotes, overrides, and publish deltas to subscribers.

## Question: How do you break down a rates book’s PnL for daily explain?
* Interviewer: Mention drivers.
* Interviewee: Decompose into carry/roll, curve moves, basis changes, volatility effects, credit/funding adjustments, and new trades; linking PnL to risk sensitivities ensures front office can justify moves to controllers and management.

## Question: What stress scenarios matter most for a rates franchise?
* Interviewer: Provide examples.
* Interviewee: Parallel shocks, steepener/flattener shocks, credit spread widening, funding squeeze (repo spike), volatility blowouts, and basis dislocations; scenarios should tie to historical episodes like the taper tantrum or March 2020 liquidity crunch.

## Question: How do funding and capital charges influence trade pricing?
* Interviewer: Tie to business decisions.
* Interviewee: Each trade consumes balance sheet (RWA, leverage ratio) and funding (FVA, MVA), so pricing tools add adjustments reflecting term of funding, collateral usage, and capital return thresholds, often tracked through transfer-pricing grids.

## Question: What is all-to-all trading and why is it growing in rates?
* Interviewer: Give drivers.
* Interviewee: All-to-all platforms let buy-side trade directly without dealers taking balance sheet, increasing transparency and competition, particularly for standardized swaps or Treasuries; regulatory push for electronification accelerates adoption.

## Question: Describe the core technology stack for a rates trading desk.
* Interviewer: Mention components.
* Interviewee: It includes real-time curve builders, pricing/risk libraries, trade capture OMS, electronic execution (RFQ, streaming APIs), integration with clearing, data stores for tick and risk history, plus monitoring for latency and controls.

## Question: How do you ensure pricing models stay synchronized across front and middle office?
* Interviewer: Discuss controls.
* Interviewee: Maintain a single source pricing library with version control, publish calibration sets, automate regression tests, and provide documentation; governance includes sign-offs, model validation, and deployment pipelines to avoid FO/MO breaks.

## Question: What is the interaction model with quantitative research?
* Interviewer: Provide examples.
* Interviewee: Tech collaborates with quants on model requirements, interfaces, performance tuning, and deployment; we translate trading needs into product backlog, backtest changes, and ensure analytics integrate cleanly into GUIs and risk systems.

## Question: Why are holiday calendars and day-count conventions such a big deal in rates systems?
* Interviewer: Explain consequences of errors.
* Interviewee: Misaligned calendars shift accruals, payment dates, and discount factors, leading to PnL breaks or settlement fails; global desks manage dozens of calendars, so central services and automated updates are essential.

## Question: How do you respond when a DV01 limit is breached intraday?
* Interviewer: Outline the escalation.
* Interviewee: Immediately validate the exposure, inform the trader and risk manager, decide whether to hedge or seek approval, document the event, and ensure systems capture remediation steps for audit.

## Question: What coordination is required with operations for settlements in rates?
* Interviewer: Highlight cross-team touchpoints.
* Interviewee: Front office confirms allocations, sends trade details to confirmation platforms, monitors collateral/margin calls, and works with ops on fails, pair-offs, and cash movements, ensuring data flows (FpML/SWIFT) remain in sync to avoid settlement risk.
