# Ant Algorithm Optimization & Adaptive Swarm Intelligence for O&G Systems

Research repository for the doctoral thesis:

**A Physics-Constrained Probabilistic Ant–Swarm Optimization Framework for Oil and Gas Market Resilience, Resource Longevity, and Long-Term Energy Transition Planning**

The revised thesis blueprint and experimental roadmap are available in [docs/REVISED_THESIS_BLUEPRINT.md](docs/REVISED_THESIS_BLUEPRINT.md) and [docs/REVISED_EXPERIMENTAL_ROADMAP.md](docs/REVISED_EXPERIMENTAL_ROADMAP.md). The original research direction and preliminary experiments are retained as the foundation and audit trail.\n\nThis repository operationalises three oil-and-gas (O&G) research use cases:

1. **Oil-price formation and forecasting:** explain benchmark and grade/location prices through granular geopolitical, supply, demand, macro-financial, logistics, crude-quality and policy drivers.
2. **Resource longevity and production decline:** distinguish geological resources, technically recoverable resources, economically recoverable reserves, production capacity and market demand; estimate probabilistic production thresholds rather than a single “run-out” date.
3. **Energy sustainability (2026–2126):** explore adaptive, multi-decade energy portfolios under energy-security, affordability, reliability, physical-resource, emissions and technology constraints.

## Research stance

Ant Colony Optimization (ACO) is already a member of the swarm-intelligence family. The proposed research is therefore **not** that ACO and swarm intelligence are unrelated inventions. It tests a hybrid in which:

- ACO constructs discrete structures and investment/route/asset choices through probabilistic search and pheromone memory.
- An adaptive continuous swarm (e.g. adaptive PSO) tunes operating and investment variables.
- A deterministic physics layer enforces balances, capacities, equipment bounds and safety constraints.
- A probabilistic layer represents demand, price, geopolitical events, outages, weather, policy and model uncertainty.
- A structured “deep reasoning” cycle decomposes a problem, proposes alternatives, challenges them with scenarios, checks feasibility, compares risk and revises the solution.

The algorithms are hypotheses to test, not presumed winners. Prediction models (econometrics/ML) estimate outcomes; ACO/ASI search and optimize decisions, model structures and policies. Metaheuristics do not automatically create predictive information.

## Reproducibility and current evidence

The repository contains public monthly historical data snapshots and scripts. The preliminary price experiment uses EIA-sourced monthly Brent data and the Caldara–Iacoviello monthly geopolitical-risk index. It compares a price-only autoregressive benchmark with a version augmented by lagged aggregate GPR.

Preliminary results (one-month rolling forecasts, 120-month training window, 351 out-of-sample forecasts):

| Model | MAE (% log-return) | RMSE (% log-return) | Direction accuracy | OOS R² |
|---|---:|---:|---:|---:|
| Price-only AR(1) | 7.49 | 10.53 | 56.7% | -0.022 |
| AR(1) + lagged GPR level/change | 7.72 | 10.81 | 53.0% | -0.077 |

The aggregate GPR feature **worsened** this preliminary test. This is evidence against a simplistic “geopolitical index → price” model, not evidence against modelling specific event-to-asset-to-volume-to-inventory pathways.

A separate stylized energy-portfolio simulation is a synthetic stress test, not real plant data. It showed risk-aware search reduced shortage versus a deterministic mean-state plan, but the ACO–PSO hybrid did not materially outperform PSO and neither met the assumed reliability target. The result is deliberately retained as a model challenge.

See [docs/REVISED_THESIS_BLUEPRINT.md](docs/REVISED_THESIS_BLUEPRINT.md), [docs/REVISED_EXPERIMENTAL_ROADMAP.md](docs/REVISED_EXPERIMENTAL_ROADMAP.md), [docs/RESEARCH_DESIGN.md](docs/RESEARCH_DESIGN.md), [docs/EMPIRICAL_FINDINGS.md](docs/EMPIRICAL_FINDINGS.md), and [data/README.md](data/README.md).

## Quick start

Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

python experiments/price_backtest.py
python experiments/resource_longevity.py
python experiments/portfolio_stress_test.py
```

The price backtest uses the checked-in snapshots. For live refreshes, use the source URLs in `data/README.md` and retain the download date and file hash. Do not silently overwrite a vintage used in a published result.

## Repository layout

- `data/`: raw source snapshots and provenance.
- `experiments/`: reproducible analysis and simulation scripts.
- `docs/`: research design, empirical findings and model challenges.
- `results/`: machine-readable preliminary outputs.

## Critical limitations

- The Brent/GPR backtest is a univariate price-lag baseline plus one aggregate geopolitical proxy. It does not yet include the complete factor set or estimate causal effects.
- Historical revised data can create vintage/look-ahead bias. Final experiments must use point-in-time data vintages and release calendars.
- GPR is news coverage intensity, not a direct measure of barrels disrupted, asset exposure, event duration or physical export loss.
- The portfolio simulation uses assumed engineering parameters and synthetic scenarios. It must not be interpreted as a forecast for a real country, company or grid.
- A 100-year horizon is a scenario/robust-planning problem, not a conventional point forecast.
- Any safety-critical deployment requires independent engineering validation, feasible-first constraint handling, deterministic interlocks and human governance.

## Citation and data use

See the data provenance, licensing and citation notes in [data/README.md](data/README.md). Cite original data providers and papers, not only the mirrors used to obtain snapshots.
