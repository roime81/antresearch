# Preliminary empirical findings and model challenges

**Status:** pilot empirical analysis and synthetic simulation, not a completed validation of the thesis hypotheses.

## 1. Dataset snapshots and coverage

### Monthly price data
The checked-in Brent snapshot contains 474 monthly observations from May 1987 through October 2026. It is an EIA-sourced monthly spot-price mirror. The observed price range in this snapshot is USD 9.82–132.72 per barrel; October 2026 is USD 123.93 per barrel. The WTI snapshot begins in January 1986 and also runs through October 2026.

### Geopolitical risk data
The checked-in Caldara–Iacoviello monthly file contains 500 recent-GPR observations from January 1985 through August 2026. It contains the global GPR, threat/act subindices and country-specific indices. The price/GPR overlap has 472 monthly observations from May 1987 through August 2026.

Caldara and Iacoviello (2022) construct GPR from newspaper article shares; the recent index uses ten newspapers and starts in 1985. GPR is a news-coverage measure, not a direct measure of oil barrels removed from the market, asset exposure or event duration.

## 2. Price/GPR baseline experiment

### Question

Does one aggregate lagged geopolitical-risk index improve one-month Brent return forecasts beyond a simple price-lag model?

### Protocol

- Target: monthly log return of Brent spot price.
- Sample: common monthly Brent/GPR observations, May 1987–August 2026.
- Forecast: one month ahead.
- Walk-forward: rolling 120-month training window.
- Benchmark: AR(1) on the preceding monthly log return.
- Augmented model: same AR(1) plus the log level of prior-month GPR and its one-month change.
- Linear ridge fit, small fixed regularisation; no test-period refitting.
- Out-of-sample forecast count: 351.

### Results

| Metric | Price-only AR(1) | AR(1) + lagged GPR level/change |
|---|---:|---:|
| MAE (% log-return) | 7.49 | 7.72 |
| RMSE (% log-return) | 10.53 | 10.81 |
| Directional accuracy | 56.7% | 53.0% |
| Out-of-sample R² | -0.022 | -0.077 |

The contemporaneous correlation between monthly GPR level and same-month Brent log return is approximately -0.010. The correlation between prior-month GPR level and the following month's Brent log return is approximately -0.086.

### Interpretation

The augmented model performs worse on all four reported metrics in this pilot. Both negative out-of-sample R² values indicate performance below the historical-mean benchmark under this scoring definition. This falsifies the simplistic hypothesis that adding a global GPR level/change automatically improves short-horizon Brent returns.

It does **not** falsify the more precise hypothesis that asset-specific, oil-relevant geopolitical exposures and physical flow consequences can improve a price-distribution model. The global GPR is too aggregated to represent:
- affected country and asset,
- export share and pipeline/terminal/chokepoint,
- barrels per day at risk,
- probability and duration,
- spare capacity and alternative routes,
- inventory buffers,
- crude quality and grade/location basis,
- market expectations and demand response.

Examples of high-GPR months show both positive and negative same-month Brent returns: August 1990 about +45.9%, October 2001 about -22.1%, March 2022 about +18.8%, and March 2026 about +37.5%. These examples are descriptive and are not causal event-effect estimates.

### Limitations

- No GDP/industrial-production, supply, demand, inventory, futures, FX, shipping, sanctions or crude-grade variables are in this pilot.
- GPR history can be revised; the final study needs source publication calendars and vintage-aware features.
- Monthly data cannot resolve intramonth event timing.
- The simple model is not a complete structural oil-market model.
- The pilot does not implement ACO/ASI as a forecasting model; ACO/ASI should search structures, features and decisions while a separately validated forecasting model estimates conditional distributions.

## 3. Resource-longevity arithmetic and decline challenge

OPEC ASB-2026 reports 1,572 billion barrels of world proven crude oil reserves at end-2025 and 74.85 million barrels/day of world crude oil production for 2025. A crude-on-crude static ratio is:

```
R/P = 1,572,000 million barrels
      / (74.85 million barrels/day × 365)
    ≈ 57.5 years
```

Eni's World Energy Review 2026 reports more than 1,790 billion barrels of proven oil reserves, 100.4 million barrels/day of production under its oil scope, and an R/P ratio of 48.9 years. The measures have different definitions and production boundaries. They must not be blended as if they were the same numerator and denominator.

IEA's 2025 field-decline study draws on roughly 15,000 fields and reports a 5.6% average observed post-peak decline for conventional oil; rates vary widely by field type and location. The IEA separately estimates that without investment in new or existing projects, global oil production would fall by around 8% annually on average through 2035.

Applying 8% compound decline to a rounded 100.4 mb/d baseline for ten years gives:

```
100.4 × (1 - 0.08)^10 ≈ 43.6 mb/d
```

This is an illustrative application of the IEA's no-investment decline stress, not a forecast of 2035 production and not an estimate of reserve exhaustion. New projects, workovers, recovery technology, reserve reclassification, demand and prices change the path.

**Finding:** a static R/P ratio cannot answer “when will oil last?” A field/asset/country-system model must separately project capacity decline, reserve additions/revisions, economic cutoffs, investment, demand and substitution, with distributions and scenario assumptions.

## 4. Synthetic O&G energy-portfolio stress test

### Purpose

Test whether a deterministic mean-state portfolio can fail when demand, geopolitics, weather and asset availability vary, and whether a hybrid ACO + adaptive-PSO search shows a distinct benefit over PSO alone.

### Scenario assumptions

This is an illustrative synthetic system, not measured data from a real country, company, grid or offshore asset.

- Investment budget: 100 arbitrary capital units.
- Mean demand: 60 arbitrary energy units per time period.
- Technologies: legacy oil/gas with methane controls; LNG diversification; renewables plus storage; nuclear; geothermal; gas with carbon capture.
- Random scenarios: 180 training and 5,000 independent test scenarios.
- Stressors: demand variation, common geopolitical events affecting exposed hydrocarbon routes/assets, renewable-weather dips and independent nuclear/geothermal outage events.
- Objective: annualised capital cost, operating cost, emissions cost, energy-shortage penalty and CVaR95 shortage risk.
- A scenario is marked as a shortfall event if unmet energy exceeds 2% of demand.
- Illustrative carbon-budget threshold: 24 emissions units.

### Held-out test results

| Metric | Deterministic mean-state PSO | Risk-aware PSO | ACO + adaptive PSO |
|---|---:|---:|---:|
| Mean cost (arbitrary units) | 1,496.26 | 892.20 | 890.97 |
| Mean unserved energy | 5.289 | 2.299 | 2.305 |
| CVaR95 unserved energy | 26.695 | 23.840 | 23.806 |
| Shortfall-event rate | 53.12% | 14.88% | 15.16% |
| Mean emissions units | 6.31 | 20.61 | 20.58 |
| Probability emissions exceed 24 | 0.00% | 0.02% | 0.02% |

The risk-aware models materially improve test performance against the mean-state plan under this stylized shock model. However:
- Neither risk-aware plan meets a hypothetical 95% service-reliability requirement; the observed shortfall-event rate remains around 15%.
- The ACO–PSO hybrid reduces mean cost by only about 1.23 units (approximately 0.14%) versus risk-aware PSO.
- In the paired 5,000-scenario comparison, the conditional test-scenario bootstrap 95% interval for hybrid-minus-PSO mean cost is approximately [-2.31, -0.09] units. This is conditional on the fitted plans, does not include algorithm-seed uncertainty, and does not establish a general algorithmic advantage.
- Hybrid shortfall-event rate is about 0.28 percentage points worse than PSO in this run.
- A random feasibility screen of 20,000 portfolios over 1,000 test scenarios did not find a portfolio meeting both a 95% service-reliability target and the carbon budget. The most reliable sampled portfolio still had a 12.5% shortage-event rate and an 86.5% carbon-violation rate; this is not proof of mathematical infeasibility, but a warning that the assumed budget/technology/scenario envelope may not permit the stated requirements.

### What the experiment says about the thesis

1. Probabilistic stress testing matters: the deterministic mean-state plan was brittle under common shocks.
2. The hybrid has not yet demonstrated practical superiority over an adaptive swarm alone.
3. A multi-objective decision should show the reliability/emissions trade-off, not hide it in one scalar.
4. The current search objective uses soft penalties for shortage and carbon breaches. It does not guarantee a hard chance constraint. A final safety-critical formulation must use feasible-first ranking, repair/projection, explicit chance constraints or robust bounds.
5. The benchmark needs multiple algorithm seeds, compute-matched baselines, exact/OR benchmarks on smaller instances and better calibrated scenario distributions.

## 5. Hypotheses challenged

| Hypothesis | Preliminary evidence | Status |
|---|---|---|
| Aggregate GPR improves Brent return prediction | Augmented rolling model was worse | Not supported in pilot |
| Probabilistic scenario modelling improves decisions over mean-state planning | Shortage and mean cost improved on synthetic stress test | Tentative support, synthetic only |
| ACO + adaptive swarm beats adaptive PSO | Very small cost difference; shortfall incidence slightly worse | Not demonstrated |
| The framework guarantees physical/service feasibility | Current penalty-based test missed 95% service reliability | Rejected for current prototype |
| Static R/P predicts the date oil runs out | Definitions and decline/investment effects invalidate that interpretation | Rejected |

## 6. Required next experiments

1. Add oil-specific GPR/AI-GPR, sanctions, conflict-event metadata, country/asset/route exposure and event durations.
2. Join physical supply loss, inventories, spare capacity, freight, refinery utilisation, futures structure, FX, macro and demand data at valid frequencies.
3. Conduct a point-in-time, vintage-safe walk-forward forecast with event studies for causal claims.
4. Obtain field-level production/decline histories and consistent reserve classifications for the resource-longevity case.
5. Turn the portfolio stress test into a constrained benchmark with explicit 95% reliability and carbon-budget chance constraints; first test whether the feasible region is non-empty.
6. Run at least 30 seeds per optimizer, equalise objective evaluations, add ablations and compare to exact/established solvers.
7. Extend the energy transition problem with transparent IEA, OPEC, IPCC and national scenario families. Treat 2050 as a scenario anchor and 2050–2126 as adaptive robust planning, not a point forecast.
