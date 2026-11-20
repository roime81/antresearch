# Revised PhD Thesis Blueprint

**Status:** Working research design for supervisory review. Proposed hypotheses are not yet validated.

## 1. Working title

**A Physics-Constrained Probabilistic Ant–Swarm Optimization Framework for Oil and Gas Market Resilience, Resource Longevity, and Long-Term Energy Transition Planning**

This title makes the methodological contribution visible while identifying the empirical domain and three connected application areas.

## 2. Research premise

Oil and gas systems are exposed to interacting geopolitical, economic, geological, operational, logistical, financial, technological and environmental forces. They operate across different spatial and temporal scales. Some relationships are governed by deterministic physical limits; others are uncertain, non-stationary or only partially observable.

This research proposes and evaluates a physics-constrained probabilistic ant–swarm optimization framework that combines:

1. Probabilistic state estimation and forecasting for uncertain market, event, production and transition conditions.
2. Ant Colony Optimization (ACO) to construct discrete structures and pathways, such as asset/route choices, project sequences, technology portfolios and feature structures.
3. Adaptive Particle Swarm Optimization (APSO) to refine continuous decisions, such as production, capacity, investment, storage, flow and hedge allocations.
4. Deterministic physical-feasibility checks for conservation, capacity, operational and engineering constraints.
5. Risk-aware scenario evaluation, including tail risk, chance constraints and robustness.
6. Independent verification and reproducible decision records.

ACO is itself a member of swarm intelligence. The research does not claim ants and swarm intelligence are unrelated inventions. It tests whether a structured hybrid of discrete ant-based construction and adaptive continuous swarm refinement offers measurable benefits over well-tuned component algorithms and established optimization baselines.

## 3. Central research question

**How can a physics-constrained probabilistic ant–swarm optimization framework integrate granular geopolitical, economic, operational and environmental information to improve decision quality in oil and gas price-risk analysis, disruption and resource-longevity assessment, and long-term energy-transition planning?**

The framework must be evaluated separately in each use case. Success in one must not be assumed to transfer to another.

## 4. Research aim

To design, implement and empirically evaluate a physics-constrained probabilistic ant–swarm optimization framework for complex oil and gas systems, and determine whether its hybrid search, uncertainty treatment and feasibility verification improve decision quality, robustness and reliability across three connected use cases.

## 5. Research objectives

- **RO1 — Framework design:** Develop a unified mathematical and computational architecture separating deterministic physical constraints, uncertain states, discrete structures and continuous decisions.
- **RO2 — Price-risk analysis:** Develop a granular event-to-asset-to-physical-flow-to-market representation and evaluate its contribution to crude-price distribution forecasting and risk attribution.
- **RO3 — Disruption and resource longevity:** Model disruption occurrence, duration and recovery alongside field-level production decline, investment, reserves and demand to estimate probabilistic recovery and production-threshold dates.
- **RO4 — Long-term transition planning:** Formulate a multi-objective, scenario-based energy-system planning problem for 2026–2126, including the transitional role and potential repurposing of oil and gas capabilities.
- **RO5 — Algorithm evaluation:** Compare ACO, APSO, hybrid variants and established baselines using equal computational budgets, repeated seeds, ablations and independent test scenarios.
- **RO6 — Validation and reproducibility:** Establish data provenance, point-in-time evaluation, physical-feasibility checks, uncertainty calibration, sensitivity analysis and reproducible artefacts.

## 6. Three empirical use cases

### Use case 1 — Granular oil and gas price formation and risk forecasting

**Research question:** To what extent does representing oil-relevant events through country, asset, route, disrupted-volume, inventory and market-response mechanisms improve explanation and probabilistic forecasting of benchmark and grade/location crude prices compared with price-only and aggregate-risk baselines?

The explanatory chain is:

Event → country/asset/route exposure → disruption probability, severity and duration → lost or delayed physical flow → spare capacity, rerouting and inventory response → market tightness and expectations → benchmark price and grade/location differential.

Factor families:

- Geopolitical: conflict, escalation, sanctions, embargoes, political instability and export restrictions.
- Asset and logistics: fields, pipelines, terminals, ports, chokepoints, shipping routes, insurance, freight and alternatives.
- Physical supply: field output, decline, outages, OPEC+ decisions, spare capacity, production costs, inventories, strategic reserves and refinery throughput.
- Demand and macroeconomics: GDP, industrial production, mobility, aviation, shipping, petrochemicals, inflation, interest rates, FX and recession indicators.
- Market structure: Brent/WTI/Dubai benchmarks, futures curve, spreads, options volatility, positioning, refining margins and storage economics.
- Crude grade and location: API gravity, sulphur, quality differentials, regional basis, freight, refinery compatibility and local scarcity.
- Policy and transition: carbon pricing, methane rules, fuel standards, electrification, alternative fuels and demand substitution.

A delivered crude price can be decomposed into benchmark and explicit grade/location components:

P[g,r,t] = P[benchmark,t] + quality[g,t] + regionalBasis[r,t] + freight[r,t] + insurance[r,t] + taxPolicy[r,t].

**Outputs:** calibrated price distributions at 1-, 3- and 12-month horizons; event and asset exposure maps; conditional tail-risk probabilities; grade/location differentials; and scenario counterfactuals.

**Methodological separation:** predictive feature attribution (for example, SHAP) describes model behaviour and is not, by itself, a causal estimate. Causal claims require a separate identification strategy such as event studies, local projections, synthetic controls or credible instruments. Event timing, confounding, anticipation and data availability must be addressed.

### Use case 2 — Disruption duration, recovery and oil-production/resource longevity

This use case contains two related but distinct time-to-event questions. They must not be collapsed into one target.

**A. Disruption persistence and recovery**

Estimate how long a disruption is likely to persist and when affected production, exports, transport or prices may recover.

Potential methods include survival analysis, hazard models, recurrent-event models and probabilistic state-transition models. Relevant variables include event type, escalation, sanctions, asset exposure, damage severity, repair lead time, alternative routes, spare capacity, inventories, political settlement and historical recovery patterns.

Outputs:
- Probability that a disruption remains active after a specified time.
- Conditional expected duration and duration quantiles.
- Probability and timing of partial and full production/export recovery.
- Time to inventory normalization and price/basis normalization, defined separately.
- Confidence or credible intervals and scenario-conditioned recovery paths.

A geopolitical crisis ending, an asset restarting, exports normalizing and prices reverting are different events. They require different labels and should not be represented by a single recovery date.

**B. Production and resource longevity**

Estimate how regional, field-level and global production capacity evolves under geological decline, investment, discoveries, reserve revisions, technology, costs, policy and demand substitution.

Separate:
1. Geological occurrence.
2. Discovered and classified resources.
3. Technically recoverable resources.
4. Economically recoverable reserves under stated assumptions.
5. Installed production capacity and deliverable output.
6. Market demand and substitution.

For field i and period t, a simplified reserve-state relationship is:

R[i,t+1] = R[i,t] + discoveries[i,t] + revisions[i,t] + recoveryAdditions[i,t] - production[i,t].

Production capacity evolves separately:

K[i,t+1] = K[i,t](1 - decline[i,t]) + sanctionedAdditions[i,t] - decommissionedCapacity[i,t].

These are accounting structures, not complete reservoir models. Reserve classifications, resource categories and production boundaries must follow consistent definitions.

Outputs include distributions of regional/global production peaks; dates when production crosses 75%, 50%, 25% and 10% of an explicitly defined baseline; supply-shortfall probabilities; marginal supply cost; and the distinction between physical depletion, economic stranding and demand-driven decline.

**Research safeguard:** a reserves-to-production ratio is a static indicator, not an exhaustion date. A low-demand scenario is not physical exhaustion. A resource that is uneconomic at one price or policy regime has not thereby ceased to exist geologically.

### Use case 3 — Long-term energy sustainability and transition planning, 2026–2126

**Research question:** How can energy portfolios and oil and gas capabilities evolve across uncertain technology, demand, policy, climate and geopolitical pathways while maintaining reliable and affordable energy services and respecting physical and environmental constraints?

This is a scenario and adaptive-planning problem, not a point forecast of 2126.

Potential system options include efficient oil and gas production during transition; methane abatement; solar, wind, hydro, nuclear and geothermal; storage and grids; hydrogen and low-carbon fuels; sustainable aviation fuel; carbon capture, transport and storage; electrification; efficiency; recycling; and responsible decommissioning.

Potential oil and gas capabilities to evaluate for transition use include subsurface characterisation, reservoir modelling, offshore engineering, project delivery, pipelines, ports, marine operations, process engineering and geological storage. Conversion of existing assets must be validated for engineering suitability, safety, lifecycle emissions and economics; it is not automatically beneficial.

Model the period using 5- or 10-year strategic decision intervals, with shorter operational submodels where needed and rolling-horizon replanning as new information becomes available.

Keep objectives visible rather than hiding policy preferences in a single sustainability score:
- Total system cost and affordability.
- Reliability and unserved-energy risk.
- Lifecycle greenhouse-gas emissions, including methane.
- Energy access and distributional impacts.
- Water, land, materials and critical-mineral use.
- Import dependence and geopolitical exposure.
- Stranded-asset and irreversible lock-in risk.

Use Pareto analysis, scenario regret and sensitivity testing. Explicitly state carbon budgets, discount rates, technology learning assumptions, build-rate limits and policy choices.

## 7. Proposed framework architecture

1. **Data and provenance:** time-stamped, versioned observations with source, unit, geography, frequency, publication date, revision history and quality flags.
2. **State and event:** asset/route exposure, event states, field and infrastructure states, inventories, demand and energy-system capacity.
3. **Probabilistic inference:** price distributions, event-duration/recovery distributions, production/decline distributions and scenario-conditioned technology/demand pathways.
4. **Deterministic physics:** mass and energy balances, capacity, flow, storage, conversion, ramping and engineering bounds.
5. **ACO discrete construction:** selects assets, routes, projects, technology structures, feature groups or project sequences.
6. **APSO continuous refinement:** optimizes allocations, capacities, operating levels, investment, storage, flows and hedge decisions.
7. **Risk and multi-objective evaluation:** expected loss, CVaR, chance constraints, robust or distributionally robust performance, Pareto fronts and scenario regret.
8. **Verification and decision record:** independently checks constraints, records model/data versions, exposes assumptions, reports uncertainty and supports reproducibility.

The forecasting layer estimates uncertain outcomes. The optimizer selects actions under those estimated outcomes. The metaheuristic is not itself presumed to generate predictive information.

## 8. Mathematical problem representation

Represent a decision problem by:
- d: discrete structure, such as selected assets, routes, technologies or projects.
- u: continuous decisions, such as capacity, flow, investment, storage or hedge allocation.
- x[t]: system state, such as inventories, reserves, production capacity and cumulative emissions.
- ξ[t]: uncertain scenario, such as event occurrence, severity, duration, demand, weather, price or technology cost.
- θ: uncertain model parameters and epistemic assumptions.

A generic risk-aware problem is:

min_(d,u) E[L(d,u,ξ;θ)] + λ CVaR_α(L) + transitionRisk(d,u)

subject to deterministic physical constraints:

h(d,u,x,ξ) = 0
g(d,u,x,ξ) <= 0

and, where justified, probabilistic constraints:

P(g[j](d,u,x,ξ) <= 0) >= 1 - ε[j].

The objective, constraints, uncertainty set and risk tolerance must be defined separately for each use case. Do not apply one generic scalar objective indiscriminately to price forecasting, resource estimation and century-scale energy planning.

For safety-critical or physically binding constraints, penalty functions alone are insufficient. Use feasible-first ranking, deterministic validation, projection/repair, conservative bounds or explicit chance/robust constraints.

## 9. Research hypotheses

Each hypothesis is falsifiable and should be preregistered or documented before final test evaluation.

- **H1 — Hybrid search performance:** Under equal objective-evaluation or compute budgets, ACO–APSO improves feasible-solution attainment, solution quality or robustness on defined mixed discrete–continuous O&G optimization problems compared with ACO-only, APSO-only and established baselines.
- **H2 — Regime adaptation:** Regime-conditioned pheromone memory and diversity-aware swarm adaptation improve recovery and decision stability after structural breaks compared with fixed-memory and fixed-parameter variants.
- **H3 — Granular price information:** Event/asset/route/volume and physical-market-response features improve out-of-sample probabilistic price forecast quality or tail-risk calibration compared with price-only and aggregate geopolitical-risk baselines.
- **H4 — Duration and longevity calibration:** Explicit event-duration/recovery and field-level decline/investment models produce better calibrated time-to-event and production-threshold distributions than simpler duration, decline-curve and static R/P baselines.
- **H5 — Long-horizon planning robustness:** Adaptive rolling-horizon portfolios reduce worst-case or distributional scenario regret while meeting stated reliability, emissions and physical constraints compared with deterministic and non-adaptive plans.
- **H6 — Feasibility verification:** Independent deterministic verification and feasible-first constraint handling reduce infeasible proposal rates and constraint violations compared with penalty-only optimization.

A hypothesis may be rejected. H1 must not be declared supported merely because the hybrid beats one baseline on one run or one metric.

## 10. Experimental design and evaluation

### 10.1 Price-risk experiments

Baselines should include naïve/random walk, AR/ARX, VAR where appropriate, GARCH-family volatility models, Bayesian regression and suitable tree/sequence models. Compare at 1-, 3- and 12-month horizons using chronological walk-forward evaluation.

Metrics:
- MAE/RMSE for point forecasts.
- Pinball loss, CRPS and weighted interval score for probabilistic forecasts.
- Interval coverage and width.
- Tail-event calibration and Brier/log scores for event probabilities.
- Directional accuracy only as a secondary metric.

Use point-in-time data and publication calendars to prevent look-ahead and revision leakage. Match feature frequency and timing. Report ablations for aggregate GPR, oil-specific geopolitical risk, event metadata, physical-flow exposure, inventory and market variables.

### 10.2 Disruption-duration experiments

Construct a clearly defined event/asset episode dataset. Define event start, event end, partial restart, full restoration and market normalization separately. Address censoring, recurrent events, competing risks and time-varying covariates where applicable.

Compare Kaplan–Meier or non-parametric survival baselines, Cox or accelerated-failure-time models, flexible survival learners and state-transition alternatives where sample size permits. Evaluate time-dependent Brier score, concordance, calibration, duration error and interval coverage. Use temporal and event-family holdouts.

### 10.3 Resource-longevity experiments

Use field-level or basin-level panel data where accessible and licensed. Validate on held-out fields, regions or historical vintages. Compare decline-curve analysis, cohort models, reserve-life indicators and system-dynamics baselines.

Evaluate production forecast errors, calibration of peak-year and threshold-crossing distributions, sensitivity to price/cost/recovery factors, and scenario consistency. Preserve reserve-category definitions and report data limitations explicitly.

### 10.4 Century-scale planning experiments

Use transparent scenario families from credible energy outlooks as alternative assumptions, not ground-truth forecasts. Model 2026–2126 as adaptive planning with 5- or 10-year strategic intervals. Compare deterministic, stochastic, robust and distributionally robust approaches.

Report cost, emissions, reliability, energy access, resource use, water, land, geopolitical exposure, stranded-asset risk, Pareto fronts and scenario regret separately. Sensitivity-test discount rates, carbon budgets, technology learning, demand, build limits, material constraints and policy regimes.

### 10.5 Algorithm experiments

Compare:
- ACO-only.
- APSO-only.
- Hybrid ACO–APSO.
- Fixed-parameter hybrid.
- Hybrid without pheromone memory.
- Hybrid without adaptive coefficients.
- Hybrid without scenario-based evaluation.
- Hybrid without physics repair/verification.
- Established solver or heuristic baselines, including MILP/MIQP or deterministic engineering solvers on tractable instances.

Use at least 30 independent random seeds for final algorithm comparisons where computationally feasible, equal objective evaluations or transparent compute budgets, held-out scenarios and small-instance reference optima. Report feasibility rate, optimality gap, objective evaluations, wall-clock time, compute energy where measurable, convergence/stagnation, variability and confidence intervals. Account for both scenario-sampling and optimizer-seed uncertainty.

## 11. Preliminary evidence and interpretation

The current repository contains:
- A monthly Brent/GPR pilot with 351 one-month out-of-sample forecasts.
- A synthetic energy-portfolio stress test with 180 training and 5,000 held-out scenarios.
- A transparent reserves-to-production and no-investment decline arithmetic exercise.

The preliminary Brent/GPR experiment found that adding lagged aggregate GPR worsened MAE from 7.49% to 7.72% and directional accuracy from 56.7% to 53.0%. This is evidence against that particular aggregate-index augmentation, not against a more granular event-to-physical-flow model.

The synthetic portfolio experiment found that risk-aware planning improved on a deterministic mean-state plan under the assumed scenarios, but neither risk-aware approach met the illustrative 95% service-reliability target. ACO–APSO improved mean test cost by only about 0.14% over risk-aware PSO and had a slightly higher shortfall-event rate. This does not establish hybrid superiority.

The resource arithmetic shows why static R/P ratios and mechanical decline stresses cannot be presented as exhaustion forecasts.

These findings are retained as pilot evidence and model challenges. They are not final hypothesis tests.

## 12. Scope boundaries and feasibility controls

This is an ambitious interdisciplinary thesis. To keep it doctoral and executable:
- The primary methodological contribution is the constrained probabilistic ACO–APSO framework and its evaluation.
- The three use cases are application/validation settings, not three unrelated theses.
- Price forecasting, survival/duration modelling and long-term energy scenario construction use distinct statistical models where appropriate; they share a decision and optimization architecture rather than forcing one predictive model onto all tasks.
- The price case should start with a defensible benchmark (Brent) and a small number of documented grades/regions before expanding.
- The resource case should begin with a tractable field/basin panel or a transparent regional model if field data access is limited.
- The 100-year case should use scenario families and robust planning, not claim precise probabilities for events a century away.
- Data access, licensing, spatial/temporal resolution and point-in-time availability are research design constraints.
- Real-world operational deployment or safety certification is outside the thesis unless separately scoped and independently validated.

## 13. Proposed thesis chapter structure

1. **Introduction:** context, problem statement, research gap, aim, objectives, questions, hypotheses, scope and contributions.
2. **Literature Review:** oil-market formation, geopolitical risk, event studies, survival and decline modelling, energy transition planning, physical constraints, ACO, PSO, hybrid metaheuristics, robust optimization and research gaps.
3. **Conceptual and Mathematical Framework:** probabilistic–deterministic separation, system ontology, state/decision/scenario definitions, constraints, risk measures and proposed architecture.
4. **Research Methodology:** data provenance, feature engineering, model selection, optimization algorithms, benchmark design, validation, statistics, reproducibility and ethics.
5. **Use Case 1 — Oil and Gas Price Formation:** granular event-to-market model, forecast experiments, attribution and causal analysis.
6. **Use Case 2 — Disruption Duration and Resource Longevity:** survival/recovery models, field decline and reserve/production pathways.
7. **Use Case 3 — Long-Term Energy Sustainability:** scenario design, adaptive portfolio optimization, Pareto and robustness analysis.
8. **Cross-Case Algorithm Evaluation and Discussion:** algorithm comparisons, ablations, generalisability, limitations, threats to validity and implications.
9. **Conclusion and Future Research:** contributions, answers to research questions, limitations and future work.

Chapter 8 may be integrated into Chapters 5–7 if required by university formatting. The three empirical cases should still use a common experimental protocol.

## 14. Expected contributions

Subject to evidence, the thesis may contribute:
1. A typed modelling architecture separating physical invariants, uncertain states, epistemic uncertainty, discrete structures and continuous decisions.
2. A hybrid discrete ACO / adaptive continuous swarm search method with regime-aware memory, diversity control and feasible-first validation.
3. A risk-aware optimization and verification protocol combining probabilistic scenarios with deterministic physical constraints.
4. A reproducible evaluation across price-risk, disruption/resource-longevity and long-term energy-transition problems.
5. Empirical evidence identifying where the hybrid is beneficial, neutral or inferior, including negative results and boundary conditions.

The thesis must not claim novelty merely because ACO and PSO are combined. Novelty must be established through a systematic literature review and a specific algorithmic mechanism that is both new enough and empirically useful.

## 15. Decisions requiring supervisory confirmation

Before freezing the proposal, confirm:
- University thesis structure and word count.
- Whether the principal contribution is expected to be algorithmic, applied or balanced.
- Access to licensed field-level production, reserve and event/asset data.
- Geographic scope for price and longevity studies.
- Operational definition and data source for disruption/recovery events.
- Whether the 2026–2126 planning model should represent a global, regional or selected-country energy system.

Until confirmed, this is the working research design, not a final approved proposal.
