# The 45 DTE Options Strategy — Summary

A concise reference for the "sell premium at ~45 days to expiration" approach popularized by tastytrade/tastylive research. This is a premium-selling framework, not a directional trading system.

> **Disclaimer:** Educational reference only. Not financial advice. Options involve substantial risk, including losses larger than the premium collected on undefined-risk positions.

## Core idea

Sell options (or option spreads) with roughly **45 days to expiration (DTE)**, collect premium, and close the position early — either at a profit target or at ~21 DTE — rather than holding to expiration.

The edge comes from three properties of option pricing:

1. **Implied volatility overstatement.** Historically, options tend to be priced with implied volatility higher than the volatility that is subsequently realized. Sellers harvest this difference over many occurrences.
2. **The theta/gamma sweet spot.** Around 45 DTE, time decay (theta) is meaningful and accelerating, while gamma (the rate at which your directional exposure changes) is still small. Closer to expiration, theta is faster but gamma risk explodes — small moves in the underlying cause large P/L swings.
3. **Early management avoids the danger zone.** Exiting by ~21 DTE sidesteps the final weeks where gamma risk is highest and the remaining premium is small relative to the risk of holding.

## The standard playbook

### Entry

- **Timing:** Open positions at 40–50 DTE; 45 is the reference point, use the monthly expiration cycle closest to it.
- **Underlying selection:** Liquid products only — tight bid/ask spreads, active options markets (major ETFs, index products, large-cap names).
- **Volatility filter:** Prefer elevated implied volatility — commonly screened via IV Rank (IVR) above ~30. Higher IV means richer premium and more room for volatility contraction to work in your favor.
- **Strike selection:** Typically around the 16-delta strikes for short strangles (~1 standard deviation), or 20–30 delta for spreads, depending on aggressiveness.

### Common structures

| Structure | Risk profile | Typical use |
|---|---|---|
| Short strangle | Undefined risk | High IVR, ample buying power, neutral outlook |
| Iron condor | Defined risk | Smaller accounts, capped-risk mandate |
| Short put / put spread | Undefined / defined | Neutral-to-bullish bias |
| Covered call / short call spread | Covered / defined | Against stock, or bearish lean |

### Management

- **Profit target:** Close at **50% of max profit** (some use 25% for tighter cycles). Taking profits early raises win rate and redeploys capital faster.
- **Time exit:** If the profit target isn't hit, **manage or close at ~21 DTE** regardless of P/L. This is the mechanical rule that removes gamma-heavy final weeks.
- **Defense (tested positions):** Roll the untested side toward the move to collect more credit, or roll the whole position out in time (same strikes, later cycle) for a credit. Avoid rolling for a debit.

### Position sizing

- Keep individual positions small — commonly **1–5% of net liquidating value** in buying-power reduction per position.
- Stay well under ~50% total buying power usage so volatility expansions don't force liquidations.
- The strategy's edge is statistical; it only shows up across **many small, uncorrelated occurrences**. One oversized position defeats the design.

## Why 45 days specifically

- **Theta curve:** Time decay for at-the-money options accelerates as expiration approaches. At 45 DTE you're on the steepening part of the curve while premiums are still substantial.
- **Gamma curve:** Gamma stays low until roughly the last 2–3 weeks. Selling at 45 and exiting by 21 keeps the position in the low-gamma, decent-theta window for its whole life.
- **Cycle mechanics:** 45 in / 21 out gives a ~24-day holding window, letting capital recycle roughly monthly and generating the trade count the statistical edge requires.

## Expected performance profile

- **High win rate, small average winners, occasional large losers.** Selling ~1 SD strangles wins roughly 70–85% of the time when managed early, but the losers can exceed many winners — especially in volatility shocks.
- **P/L smoothness comes from management,** not from prediction. The 50%-profit and 21-DTE rules exist to cut the tail of the P/L distribution, not to improve directional accuracy.
- **Drawdowns cluster in volatility spikes** (e.g., sharp market selloffs). Undefined-risk versions require the discipline and capital to endure these.

## Key risks

1. **Tail risk / volatility shock:** A large gap move can produce losses far beyond collected premium on undefined-risk structures.
2. **Correlation risk:** Multiple short-premium positions across "different" underlyings often behave as one trade when the market drops and IV spikes everywhere.
3. **Assignment risk:** Short in-the-money options, especially near ex-dividend dates, can be assigned early.
4. **Buying-power expansion:** Margin requirements on short options grow exactly when the market is most stressed.
5. **Execution drag:** Wide spreads or illiquid strikes silently erode the small statistical edge.

## The rules on one card

| Rule | Value |
|---|---|
| Entry | ~45 DTE, liquid underlying, IVR > 30 preferred |
| Strikes | ~16Δ strangle / ~1 SD, or 20–30Δ spreads |
| Profit target | Close at 50% of max profit |
| Time management | Manage/close at 21 DTE |
| Size | 1–5% buying power per position; diversify occurrences |
| Defense | Roll untested side or roll out in time, for a credit |
