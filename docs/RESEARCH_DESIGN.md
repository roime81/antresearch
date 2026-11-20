# Research design: three O&G use cases

## 1. Research proposition

The thesis investigates whether an adaptive ant-based and swarm-based search architecture can improve decision quality in complex systems where discrete structural choices, continuous operating variables, deterministic physical constraints, uncertain external conditions and finite resources interact.

Oil and gas (O&G) is a demanding empirical domain because it connects geological depletion, production engineering, logistics, refining, commodity markets, geopolitics, finance, energy security and climate policy.

The three use cases are deliberately coupled but not conflated:

1. **Price formation and prediction:** how do global events and physical market mechanisms influence benchmark and grade/location prices?
2. **Resource longevity:** how long can economically recoverable oil sustain production under field decline, reinvestment, discovery, technology, cost and demand uncertainty?
3. **Energy sustainability, 2026–2126:** how can an O&G-centred energy system evolve toward reliable, affordable and lower-emission energy services over a century?

## 2. The probabilistic–deterministic mismatch

The research distinguishes three classes.

- **Deterministic invariants:** mass balance, energy balance, maximum field and pipeline throughput, refinery capacity, pressure/temperature operating envelopes, equipment limits, reserve stocks, well constraints and binding safety limits.
- **Aleatory uncertainty:** demand, weather, equipment outages, conflict occurrence, event duration, freight rates, market prices and renewable availability.
- **Epistemic uncertainty:** incomplete reserves data, uncertain recovery factors, disputed resource definitions, model misspecification, uncertain decline curves and unknown future technology costs.

A model must not turn a conservation equation into a probability distribution simply because operating inputs are uncertain. Conversely, it must not treat uncertain future demand, geopolitical events or technological adoption as deterministic constants.

## 3. Use case 1 — Granular oil-price formation and forecasting

### 3.1 Research question

Can a model represent the chain from geopolitical/economic event to exposed asset, physical flow disruption, inventory response, market tightness and the delivered price of a defined crude grade?

A single global geopolitical-risk index is not a physical oil-supply variable. A conflict only has a material oil-price effect when its location, timing, assets, routes, affected volumes, inventories, spare capacity, substitution options and demand context produce a market consequence.

### 3.2 Factor ontology

**Geopolitical and political**
- War, military escalation, civil unrest, political instability, regime transition and state fragility.
- Sanctions, embargoes, export restrictions, tariffs, asset seizures and changes to production-sharing or fiscal terms.
- Country exposure, event type, start/end time, escalation probability, duration distribution, affected basin, operator and ownership.
- Exposure of producing fields, gathering systems, pipelines, processing facilities, terminals, ports, straits and maritime routes.
- Insurance availability, war-risk premiums, shipping diversions and security costs.

**Physical supply**
- Field-level production, decline phase, base decline, water cut, recovery factor, workovers, artificial lift and enhanced recovery.
- OPEC+ quotas and compliance; non-OPEC production; spare capacity; rig counts; drilled-but-uncompleted wells; capex and project sanctioning.
- Planned/unplanned outages, maintenance, weather disruption, pipeline/terminal throughput, storage, strategic reserves and inventories.
- Crude and product exports/imports; refinery runs; refinery utilisation; product yields and maintenance turnarounds.

**Demand and economic activity**
- Global/regional GDP, industrial production, purchasing-manager surveys, trade, construction and manufacturing.
- Road freight, passenger mobility, aviation, shipping, petrochemical feedstock, agriculture and heating/cooling demand.
- Population, urbanisation, income, vehicle fleet, fuel efficiency, electrification and seasonal/weather effects.
- Recessions, inflation, interest rates, financial stress and currency exchange rates.

**Financial and market structure**
- Brent, WTI, Dubai/Oman and regional benchmarks; futures curve; calendar spreads; options implied volatility and skew.
- CFTC positioning, open interest, hedging flows, speculative positioning and risk premia.
- Refining margins, crack spreads, storage economics, convenience yield and inventory-to-consumption ratios.

**Crude grade and location**
- API gravity, sulphur, viscosity, metals, acidity, contaminants and product-yield characteristics.
- Refinery configuration and crude compatibility; light/sweet versus heavy/sour differentials.
- Basin/field origin, quality differential, regional basis, pipeline access, freight, insurance, port charges and local scarcity.

**Policy and transition**
- Carbon pricing, methane regulation, flaring rules, fuel standards, subsidies, strategic-stock policy, biofuel mandates, EV policy and renewable deployment.
- Expected demand substitution by efficiency, electrification, hydrogen, biofuels and alternative feedstocks.

### 3.3 Price construction

For grade g, delivery region r and time t:

```
P[g,r,t] = P[benchmark,t]
         + quality_differential[g,t]
         + regional_basis[r,t]
         + freight[r,t]
         + insurance[r,t]
         + tax_and_policy[r,t]
```

The benchmark return model should represent interactions among inventory tightness, expected supply-demand imbalance, spare capacity, FX, macro activity, futures structure, GPR, sanctions, weather, disruptions and policy regime.

A causal mechanism should be represented explicitly:

```
Event
  -> country / asset / route exposure
  -> affected probability and duration
  -> disrupted production or export volume
  -> alternative routes and spare capacity
  -> inventory and refinery response
  -> benchmark risk premium and regional/grade basis
  -> delivered price distribution
```

Use Shapley values or other feature attribution only to describe model behaviour, not to claim causal contributions. Causal claims require a separate design such as event studies, local projections, synthetic controls or credible instruments, with event timestamps and point-in-time data.

### 3.4 Role of the ant–swarm method

- ACO explores discrete event-to-asset-to-route causal pathways, asset exposure sets, feature groups, crude-grade pathways and alternative trading/hedging or supply-response structures.
- The adaptive continuous swarm tunes model parameters, exposure weights, scenario response variables, inventory/production decisions and hedge allocations.
- Deterministic physical balances cap the volume that can be lost, rerouted, stored, produced or refined.
- Probabilistic scenarios represent event probability, event duration, demand, outage severity, freight and inventory uncertainty.
- A separate probabilistic forecast model produces price distributions; the metaheuristic searches model structures and decisions rather than magically “predicting” price.

### 3.5 Forecast horizons and outputs

- Daily/weekly: event impact, logistics and disruption nowcasts.
- 1–12 months: benchmark and grade/location price distributions.
- 1–5 years: scenario-conditioned balance, investment and price-risk paths.
- Outputs: median, P10/P50/P90 or quantile forecasts; probability of tail price events; event contribution ranges; asset/route exposure; and decision counterfactuals.

## 4. Use case 2 — When will oil last?

### 4.1 The question must be decomposed

“Oil lasts until year X” is not a scientifically well-defined output. The study must separate:

1. Geological occurrence.
2. Discovered and classified resources.
3. Technically recoverable resources.
4. Economically recoverable reserves under specified price/cost/regulatory assumptions.
5. Installed production capacity after decline, investment and outages.
6. Market demand and substitution.
7. Strategic relevance of oil as a feedstock, transport fuel or energy carrier.

A reserves-to-production (R/P) ratio is a static indicator, not an exhaustion forecast.

### 4.2 State and flow model

For field i and year t:

```
R[i,t+1] = R[i,t]
         + discoveries[i,t]
         + reserve_revisions[i,t]
         + recovery_factor_additions[i,t]
         - production[i,t]
```

```
K[i,t+1] = K[i,t] * (1 - decline[i,t])
         + sanctioned_capacity_additions[i,t]
         - decommissioned_capacity[i,t]
```

Production is bounded by field capacity, operating constraints, available investment, transport, processing capacity and demand. The decline parameter is field-specific and changes with field age, reservoir properties, water/gas handling, technology and capital expenditure.

Resource classification and reserve booking must follow a consistent standard (for example, SPE-PRMS-aligned definitions where applicable). Proven, probable, possible, contingent and undiscovered resources must not be mixed without an explicit uncertainty model.

### 4.3 Inputs

- Field discovery/first-oil/peak dates, production histories, decline curves and shut-in/restart history.
- Proven/probable/possible reserves; contingent and undiscovered resources; recovery factors and reserve revisions.
- Operating cost, lifting cost, capex, fiscal terms, carbon cost, technology and project lead time.
- Water handling, pressure support, enhanced oil recovery, reservoir complexity and energy intensity.
- Geopolitical exposure, fiscal stability, sanctions, logistics and infrastructure access.
- Demand trajectories by sector, electrification and substitute feedstocks.
- Oil-price and financing scenarios.

### 4.4 Outputs

- Probability distribution of global and regional production peak years.
- Distribution for production falling below 75%, 50%, 25% and 10% of a clearly defined baseline.
- Reserve/resource distributions by classification and economic-price threshold.
- Probability of supply shortfall by region and time.
- Marginal supply cost and energy-return-on-investment (EROI) ranges.
- Explicit separation between geological scarcity, economic stranding and demand-side obsolescence.

The model should never describe a low-demand future as physical exhaustion, or a high-cost resource as non-existent.

## 5. Use case 3 — O&G contribution to energy sustainability, 2026–2126

### 5.1 Problem definition

The target is sustainable energy services, not the indefinite preservation of oil production. A 100-year horizon must be a scenario and adaptive-planning exercise, not a deterministic forecast of 2126.

The portfolio may include:
- Efficient and lower-methane oil and gas production during the transition.
- Solar, wind, hydro and sustainable bioenergy.
- Nuclear and geothermal as potential firm low-carbon sources.
- Grid, transmission, interconnection, demand response and storage.
- Hydrogen, low-carbon fuels, sustainable aviation fuel and industrial feedstocks.
- Carbon capture, transport, storage, monitoring and responsible decommissioning.
- Efficiency, electrification, recycling, circularity and demand reduction.

O&G capabilities with potential transition value include subsurface characterisation, reservoir modelling, offshore engineering, project delivery, pipelines, ports, marine operations, materials, process engineering and geological storage. Any conversion of existing assets must be assessed on engineering suitability, lifecycle emissions, economics and safety; it is not automatically beneficial.

### 5.2 Dynamic portfolio problem

Use 5- or 10-year decision periods between 2026 and 2126, with rolling-horizon replanning as technology, demand, policy and physical constraints evolve.

State variables:
- Energy service demand by sector and region.
- Generation and production capacity by technology and age.
- Asset decline, construction lead time and decommissioning schedule.
- Storage, grid, transmission and fuel-network capacity.
- Cumulative greenhouse-gas emissions and methane leakage.
- Water, land, materials, critical minerals and ecosystem constraints.
- Investment capital, cost of finance, technology learning and workforce capability.

Decision variables:
- New asset construction, retrofit, retirement and life extension.
- Fuel mix, dispatch, storage, demand response and infrastructure routing.
- Investments in methane abatement, electrification, CCS, hydrogen, geothermal, renewable energy and firm low-carbon supply.
- Research/technology investment and geographic diversification.

### 5.3 Objectives and constraints

The problem is naturally multi-objective. Avoid hiding policy choices inside one arbitrary “sustainability score.”

```
Minimise / Pareto-optimise:
  affordability and total system cost
  unserved energy and reliability risk
  lifecycle CO2e and methane emissions
  resource, water and land pressure
  energy-import and geopolitical exposure
  irreversible lock-in and stranded-asset risk
  inequity in access and transition costs
```

Subject to:
- Energy supply-demand balance in every time slice.
- Firm capacity, ramping, grid, storage and reserve-margin limits.
- Technology build rates, lead times, material and workforce constraints.
- Lifecycle emissions pathways and cumulative carbon budget.
- Water, land, safety and ecological constraints.
- Financing and capital availability.
- Robustness to alternative demand, technology, climate and geopolitical scenarios.

Use Pareto fronts and scenario regret rather than a single opaque weighted score. Policy weights should be explicit, documented and sensitivity-tested.

## 6. Proposed adaptive ant–swarm architecture

### 6.1 Decision decomposition

Represent each candidate as:
- Discrete structure d: asset, route, technology, project sequence, feature group or policy selection.
- Continuous variables u: capacities, flows, setpoints, investment shares, hedge amounts and control parameters.
- State x: reserves, inventories, equipment state, capacity, storage, field pressure proxies and cumulative emissions.
- Scenario ξ: events, demand, weather, price, outage, technology cost, policy and model uncertainty.

### 6.2 Objective and constraints

A generic risk-aware formulation is:

```
min_(d,u)  E_P[L(d,u,ξ)] + λ CVaR_α(L) + μ transition_penalty
```

subject to deterministic equalities and inequalities for physical conservation, capacity, equipment, mass/energy quality and safety, and separately stated probabilistic or distributionally robust constraints:

```
P(g_j(d,u,ξ) <= 0) >= 1 - ε_j
```

For material/safety-critical constraints, use feasible-first ranking, projection/repair, exact checks or conservative robust bounds. A penalty term alone is not a safety mechanism.

When the scenario distribution is uncertain, use an ambiguity set P ∈ 𝒫 and test distributionally robust objectives/constraints. Do not assume historical frequencies are stationary over a century.

### 6.3 Search roles

**ACO**
- Constructs discrete paths and project/asset/route structures.
- Uses pheromone memory and heuristic information.
- Uses regime-conditioned memory, aging/evaporation and diversity safeguards to avoid retaining obsolete pathways after structural market changes.
- Deposits pheromone only for feasible or explicitly least-violating solutions; infeasible solutions must not silently dominate.

**Adaptive continuous swarm**
- Refines continuous allocations and operating variables.
- Adapts inertia, cognitive/social coefficients and restart/mutation behaviour using diversity, feasibility rate, progress and regime-shift indicators.
- Projects or repairs solutions to satisfy deterministic physical bounds.
- Tracks convergence and stagnation and can re-seed sub-swarms.

**Reasoning and verification cycle**
1. Decompose the problem into typed variables and constraints.
2. Generate a diverse set of discrete and continuous candidates.
3. Challenge candidates with adversarial and tail scenarios.
4. Apply deterministic physical validators.
5. Evaluate predictive distributions, CVaR and distribution shift.
6. Compare non-dominated alternatives and counterfactuals.
7. Explain the decision pathway and residual uncertainty.
8. Replan when new information changes the state or regime.

This defines “deep thinking” as an observable algorithmic workflow; it does not require access to or claims about a language model’s private chain-of-thought.

## 7. Research hypotheses

- **H1 — Hybrid search:** on mixed discrete–continuous O&G optimization problems, ACO plus adaptive swarm will improve feasible-solution attainment or optimality gap versus ACO-only, adaptive-PSO-only and established mathematical/heuristic baselines under equal computational budgets.
- **H2 — Regime adaptation:** regime-conditioned pheromone memory and diversity-aware swarm adaptation will improve recovery after shocks or structural breaks versus fixed-parameter variants.
- **H3 — Event-to-physics price model:** granular event/asset/route/volume and inventory features will produce better calibrated price distributions than price lags plus an aggregate GPR index alone.
- **H4 — Resource longevity:** field-level decline, investment, reserve reclassification and economics will produce better calibrated production-threshold distributions than a static R/P ratio.
- **H5 — 100-year robust planning:** adaptive rolling-horizon portfolios will reduce worst-case regret and transition risk while respecting reliability, physical-resource and emissions constraints across competing scenarios.
- **H6 — Reasoning/verification:** explicit scenario challenge and independent feasibility validation will reduce infeasible proposal rates and decision instability versus a search algorithm without the reasoning/verification cycle.

All six hypotheses are falsifiable. H1 in particular must be rejected if the hybrid does not outperform the best component or a tuned baseline under equal compute and repeated seeds.

## 8. Experimental protocol

### Price case
- Use chronological train/validation/test splits and expanding/rolling walk-forward tests.
- Compare naïve/random-walk, AR/ARX, VAR, GARCH, Bayesian models, gradient-boosted trees and sequence models.
- Forecast 1-, 3- and 12-month horizons.
- Use MAE/RMSE for point errors, pinball loss/CRPS/weighted interval score for distributions, directional accuracy only as a secondary measure, and tail-event calibration.
- Use event-study/local-projection designs separately for causal contributions.
- Record point-in-time availability and revisions for all source features.

### Longevity case
- Use field-level production panels where licences and data access permit.
- Fit decline curves and reserve/production state transitions; validate on held-out fields/regions and historical vintages.
- Evaluate calibration of peak-year and threshold-crossing distributions.
- Compare against decline-curve, cohort, reserve-life and system-dynamics baselines.
- Stress price, capex, recovery factor, sanctioning lead time and demand scenarios.

### 100-year sustainability case
- Use transparent scenario families (for example, IEA CPS/STEPS/NZE and OPEC outlooks) as divergent assumptions, not truth labels.
- Use decadal rolling horizons with annual/shorter operational submodels where necessary.
- Compare deterministic, stochastic, robust and distributionally robust planning.
- Report cost, emissions, reliability, access, material use, water, land, risk and scenario regret as separate metrics.
- Perform sensitivity analysis across discount rate, carbon budget, technology learning, demand growth, build limits and policy regimes.

### Algorithm comparison
- ACO-only, adaptive swarm-only, hybrid ACO–swarm, fixed-parameter hybrid, no-pheromone ablation, no-adaptation ablation, no-scenario ablation and no-physics-repair ablation.
- Use equal objective evaluations or wall-clock/energy budgets.
- At least 30 random seeds for final algorithm comparisons.
- Report feasibility rate, constraint violation, best-known gap, runtime, compute energy, stability and statistical confidence intervals.
- Use exact solvers/MILP/MIQP or deterministic engineering solvers on small instances as reference optima where possible.

## 9. Main scientific risks

1. The hybrid may add complexity without improving results.
2. Aggregate event indices may not add predictive value.
3. Historical geopolitical distributions are non-stationary and revised.
4. Supply, demand and price features may be endogenous.
5. Reserve categories and production boundaries may be incomparable.
6. 100-year probability distributions may be unidentifiable; use scenario robustness and sensitivity instead.
7. Metaheuristics may find low-cost infeasible solutions if constraints are penalty-only.
8. Pareto trade-offs cannot be collapsed into a neutral “sustainability” score without normative choices.

## 10. What would constitute a contribution

The contribution is not “using ants for oil prices” or “combining ACO and PSO.” Those are applications/known algorithm families. A credible novel contribution would be the validated design of:
- physically typed decision/search spaces,
- discrete ant construction and adaptive continuous refinement,
- scenario- and regime-conditioned collective memory,
- feasible-first deterministic and probabilistic constraint handling,
- uncertainty-calibrated iterative challenge and revision,
- and cross-horizon validation on price, resource-longevity and energy-transition O&G problems.
