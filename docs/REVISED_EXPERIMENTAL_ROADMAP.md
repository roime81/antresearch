# Revised Experimental Roadmap

**Repository:** roime81/antresearch  
**Working branch:** research/revised-thesis-framework  
**Purpose:** Convert the revised thesis blueprint into a staged, reproducible research programme.

## Guiding rules

1. Preserve all existing pilot datasets, scripts, results and negative findings.
2. Never overwrite a data vintage used in a reported experiment; store source URL, retrieval date, hash, publication date and revision notes.
3. Separate forecasting, causal estimation, survival analysis and optimization. Do not use one as evidence for another.
4. Separate training, validation and final test scenarios chronologically or by event/asset/region as appropriate.
5. Freeze evaluation metrics and acceptance gates before opening final test results.
6. Treat physical constraints as hard constraints where engineering meaning requires it. Penalty terms alone do not guarantee feasibility.
7. Compare algorithms with equal evaluation/compute budgets and independent random seeds.
8. Do not claim 100-year point prediction. Evaluate scenario robustness and adaptive planning.

## Phase 0 — Research design lock

**Deliverables**
- Approved thesis title, aim, objectives, research questions and hypotheses.
- Operational definitions for event start/end, partial/full recovery, price normalization, field production peak and threshold crossing.
- Data dictionary and data-source register.
- Written scope and data-access assessment.

**Exit gate**
- Each research question has a target variable, unit, geography, frequency, horizon, dataset plan, baseline and evaluation metric.
- The three use cases share a specified optimization architecture but retain their appropriate statistical models.

## Phase 1 — Reproducibility and data foundation

**Work**
- Add a data manifest with source, licence, retrieval timestamp, hash, units, geographic coverage, frequency, release lag and revision policy.
- Add schema and range validation for every input.
- Add explicit timezone/date and frequency alignment.
- Implement point-in-time joins and publication-calendar checks.
- Add immutable raw/vintage directories and derived-data lineage.
- Add an environment lockfile and deterministic run configuration.

**Exit gate**
- A clean environment reproduces all current pilot outputs.
- No feature is used before its real-world publication/availability time.
- Missingness, revisions, outliers and unit conversions are documented.

## Phase 2 — Use case 1: price formation

**Minimum viable scope**
- Brent monthly baseline, preserving current experiment.
- Add WTI as a secondary benchmark after schema and vintage checks.
- Add oil-specific geopolitical risk, event metadata, sanctions, supply/demand balances, inventories, spare capacity, futures structure, freight/FX and macro variables only where reliable time-aligned data exist.
- Add selected grade/location differentials only when quality, location and pricing basis are comparable.

**Experiments**
1. Reproduce price-only AR and aggregate-GPR augmented baseline.
2. Add oil-specific GPR and event metadata.
3. Add event-to-country/asset/route exposure and disrupted-volume proxies.
4. Add inventory, spare-capacity, supply/demand and market-structure features.
5. Compare point and probabilistic forecast baselines at 1-, 3- and 12-month horizons.
6. Conduct separate event-study/local-projection work for causal impact questions.
7. Run feature-family ablations and stress periods.

**Exit gate**
- Chronological walk-forward results with point-in-time availability controls.
- Probabilistic calibration and forecast skill reported against simple baselines.
- Causal claims supported by a separate identification strategy.
- No unsupported claim that a SHAP value is a causal contribution.

## Phase 3 — Use case 2A: disruption duration and recovery

**Work**
- Build event/asset episode schema.
- Record event type, start, censoring, escalation, affected assets/routes, volume exposure, partial restart and full restoration.
- Distinguish physical restoration, export normalization, inventory normalization and price normalization.
- Identify competing risks and recurrent episodes.
- Start with interpretable survival baselines before flexible models.

**Experiments**
- Kaplan–Meier and parametric survival baselines.
- Cox/AFT or suitable time-varying survival models.
- Calibration by time horizon and event class.
- Hold out later periods, event families or asset groups.
- Compare duration and recovery quantiles with naive historical and domain baselines.

**Exit gate**
- Definitions and censoring rules are auditable.
- Time-dependent calibration and discrimination are reported.
- Sample size and event coverage support the complexity of the selected model.

## Phase 4 — Use case 2B: resource and production longevity

**Work**
- Start with a clearly bounded basin, country or field cohort.
- Harmonize reserve/resource categories and production scope.
- Build field-level production, decline, investment, discovery/revision and decommissioning panels where available.
- Represent price/cost/economic cutoff, technology and demand as scenarios.

**Experiments**
- Static R/P comparator.
- Decline-curve and cohort baselines.
- Probabilistic field/basin production model.
- Threshold-crossing and peak-year distributions.
- Sensitivity to capex, recovery factor, reserve revisions, price, policy and demand.

**Exit gate**
- No reserve-category mixing.
- Held-out field/region or vintage validation.
- Production peak and threshold-crossing distributions are calibrated and conditional assumptions are explicit.

## Phase 5 — Use case 3: 2026–2126 energy planning

**Work**
- Define system boundary (global, regional or country).
- Establish 5-/10-year strategic periods and shorter operational constraints where required.
- Define demand-service trajectories and technology families.
- Define carbon budget, reliability, affordability, materials, water, land, workforce, grid and build-rate constraints.
- Build divergent scenario families and document assumptions.

**Experiments**
- Deterministic baseline.
- Stochastic scenario planning.
- Robust and distributionally robust planning.
- Rolling-horizon adaptive planning.
- Pareto front, scenario regret and stress-case analysis.
- Sensitivity to discount rate, technology learning, demand, policy and carbon budgets.

**Exit gate**
- All scenarios are transparent and reproducible.
- No unsupported century-scale probability claims.
- Trade-offs are reported as separate metrics and Pareto alternatives.
- Feasibility is checked independently.

## Phase 6 — Algorithm development and benchmark protocol

**Algorithm variants**
- ACO-only.
- APSO-only.
- Hybrid ACO–APSO.
- Fixed-parameter hybrid.
- No pheromone memory.
- No adaptive swarm coefficients.
- No scenario/risk layer.
- No physical repair/verification.
- Established solver or heuristic baselines.
- Exact MILP/MIQP or deterministic engineering solver on small reference instances.

**Protocol**
- Equal objective evaluations or explicitly justified compute budget.
- At least 30 independent optimizer seeds for final comparisons where feasible.
- Independent held-out scenario sets.
- Report objective, feasibility, constraint violations, optimality gap, runtime, energy, convergence, stability and confidence intervals.
- Include optimizer-seed uncertainty and scenario-sampling uncertainty.
- Use paired tests and multiplicity-aware interpretation when testing multiple variants/metrics.

**Exit gate**
- Hybrid superiority is claimed only if predeclared primary metric and statistical/practical significance criteria are met.
- If the hybrid is not better, report where and why; the thesis can still contribute a rigorous boundary-condition result and a validated framework.

## Phase 7 — Cross-case synthesis and thesis writing

**Deliverables**
- One consistent architecture and notation.
- Three empirical chapters with separate datasets, baselines and validity threats.
- Cross-case analysis of the common optimizer and feasibility layer.
- Reproducibility appendix and model/data cards.
- Limitations and negative results.
- Supervisory review package.

## Proposed repository structure

~~~text
antresearch/
  data/
    raw/
    vintages/
    processed/
    manifests/
  docs/
    REVISED_THESIS_BLUEPRINT.md
    REVISED_EXPERIMENTAL_ROADMAP.md
    RESEARCH_DESIGN.md
    EMPIRICAL_FINDINGS.md
    DATA_DICTIONARY.md
    THREAT_MODEL_AND_VALIDITY.md
  src/
    data/
    features/
    forecasting/
    survival/
    resource/
    physics/
    optimization/
      aco/
      apso/
      hybrid/
    planning/
    evaluation/
  experiments/
    price/
    disruption/
    longevity/
    sustainability/
    optimizer_benchmarks/
  configs/
  results/
    pilot/
    final/
  tests/
  requirements.txt
  README.md
~~~

This is a target structure, not a claim that all modules already exist. Move current scripts incrementally and preserve reproducible entry points during refactoring.

## Immediate next implementation tasks

1. Add the revised thesis blueprint and experimental roadmap.
2. Update README to point to the revised thesis direction while retaining the original research history and pilot evidence.
3. Add a machine-readable research configuration and data manifest.
4. Refactor the existing price experiment into a baseline module without changing its reported results.
5. Add test coverage for data joins, point-in-time feature availability and physical constraint validation.
6. Design the event-duration dataset before implementing a complex survival model.
7. Define a small reference optimization problem with known feasible solutions before expanding the ACO–APSO algorithm.
