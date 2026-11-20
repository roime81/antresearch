#!/usr/bin/env python3
"""Synthetic O&G energy-portfolio stress test: ACO + adaptive PSO vs PSO.

The scenario parameters are illustrative assumptions, not measured project or grid data.
Run from repository root: python experiments/portfolio_stress_test.py
"""
from pathlib import Path
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)

TECH = [
    dict(name="Legacy oil & gas + methane controls", capex=13., yld=14., opex=2.4, ef=.45, base=.97, geo=.50, shockp=.15),
    dict(name="LNG import/export diversification", capex=19., yld=13., opex=3., ef=.34, base=.96, geo=.36, shockp=.12),
    dict(name="Renewables + storage", capex=22., yld=13., opex=.55, ef=.03, base=.58, geo=0., shockp=0.),
    dict(name="Nuclear", capex=29., yld=13., opex=1.55, ef=.015, base=.93, geo=0., shockp=.025),
    dict(name="Geothermal", capex=24., yld=10., opex=1.20, ef=.02, base=.96, geo=0., shockp=.03),
    dict(name="Gas + carbon capture", capex=21., yld=14., opex=2.2, ef=.11, base=.95, geo=.32, shockp=.13),
]
CAPEX = np.array([x["capex"] for x in TECH])
YIELD = np.array([x["yld"] for x in TECH])
OPEX = np.array([x["opex"] for x in TECH])
EF = np.array([x["ef"] for x in TECH])
BASE = np.array([x["base"] for x in TECH])
GEO_SEV = np.array([x["geo"] for x in TECH])
SHOCKP = np.array([x["shockp"] for x in TECH])


def make_scenarios(n, seed):
    rng = np.random.default_rng(seed)
    geop = rng.random(n) < .15
    weather = rng.random(n) < .12
    demand = 60 + 5 * rng.normal(size=n) + (rng.random(n) < .08) * 12
    availability = np.tile(BASE, (n, 1)) + .04 * rng.normal(size=(n, 6))
    availability[:, [0, 1, 5]] -= (
        geop[:, None] * GEO_SEV[[0, 1, 5]][None, :]
        * (.7 + .6 * rng.random((n, 3)))
    )
    availability[:, 2] -= weather * (.18 + .12 * rng.random(n))
    availability[:, 3] -= (rng.random(n) < SHOCKP[3]) * .5
    availability[:, 4] -= (rng.random(n) < SHOCKP[4]) * .5
    return {"demand": demand, "av": np.clip(availability, .05, 1.05)}


def evaluate(weights, selected, usage, scenarios, robust=True):
    weights = np.asarray(weights, dtype=float)
    selected = np.asarray(selected, dtype=int)
    spend = np.zeros(6)
    spend[selected] = weights * 100 * usage
    capacity = spend / CAPEX
    supply_by_tech = capacity[None, :] * YIELD[None, :] * scenarios["av"]
    total_supply = supply_by_tech.sum(axis=1)
    operating = (supply_by_tech * OPEX[None, :]).sum(axis=1)
    emissions = (supply_by_tech * EF[None, :]).sum(axis=1)
    shortfall = np.maximum(0, scenarios["demand"] - total_supply)
    costs = (
        .085 * (100 * usage)
        + operating
        + 7 * emissions
        + 250 * shortfall
        + 60 * np.maximum(0, emissions - 24)
    )
    sorted_shortfall = np.sort(shortfall)[::-1]
    tail_n = max(1, int(math.ceil(.05 * len(shortfall))))
    cvar95 = float(sorted_shortfall[:tail_n].mean())
    carbon_violation = float(np.mean(emissions > 24))
    score = float(costs.mean())
    if robust:
        score += 4.5 * cvar95 + 60 * carbon_violation
    return {
        "score": score,
        "mean_cost": float(costs.mean()),
        "mean_shortfall": float(shortfall.mean()),
        "cvar95_shortfall": cvar95,
        "shortfall_event_rate": float(np.mean(shortfall > .02 * scenarios["demand"])),
        "mean_emissions": float(emissions.mean()),
        "carbon_violation_probability": carbon_violation,
        "investment": float(spend.sum()),
        "weights": weights.tolist(),
    }


def softmax(x):
    z = np.exp(x - np.max(x))
    return z / z.sum()


def pso(selected, scenarios, robust, seed, particles=10, iters=22):
    rng = np.random.default_rng(seed)
    k = len(selected)
    dim = k + 1
    positions = rng.uniform(-1.5, 1.5, (particles, dim))
    velocities = rng.uniform(-.25, .25, (particles, dim))

    def decode(z):
        weights = softmax(z[:k])
        usage = .6 + .4 * ((np.tanh(z[-1]) + 1) / 2)
        return weights, usage

    pbest = positions.copy()
    pbest_scores = np.empty(particles)
    for i in range(particles):
        weights, usage = decode(positions[i])
        pbest_scores[i] = evaluate(weights, selected, usage, scenarios, robust)["score"]

    best_idx = int(np.argmin(pbest_scores))
    global_pos = pbest[best_idx].copy()
    global_score = float(pbest_scores[best_idx])

    for iteration in range(iters):
        inertia = .82 - .42 * iteration / max(1, iters - 1)
        diversity = float(np.mean(np.var(positions, axis=0)))
        for i in range(particles):
            velocities[i] = (
                inertia * velocities[i]
                + 1.35 * rng.random(dim) * (pbest[i] - positions[i])
                + 1.45 * rng.random(dim) * (global_pos - positions[i])
            )
            if diversity < .18 and rng.random() < .18:
                velocities[i] += rng.normal(0, .6, dim)
            positions[i] = np.clip(positions[i] + velocities[i], -3.5, 3.5)
            weights, usage = decode(positions[i])
            score = evaluate(weights, selected, usage, scenarios, robust)["score"]
            if score < pbest_scores[i]:
                pbest_scores[i] = score
                pbest[i] = positions[i].copy()
                if score < global_score:
                    global_score = float(score)
                    global_pos = positions[i].copy()

    weights, usage = decode(global_pos)
    return {
        **evaluate(weights, selected, usage, scenarios, robust),
        "selected": list(selected),
        "usage": float(usage),
    }


def choose_weighted(pheromone, selected, rng):
    candidates = [i for i in range(6) if i not in selected]
    heuristic = np.sqrt(YIELD[candidates] / CAPEX[candidates])
    score = (pheromone[candidates] ** 1.2) * heuristic
    return int(rng.choice(candidates, p=score / score.sum()))


def aco_pso(scenarios, seed):
    rng = np.random.default_rng(seed)
    pheromone = np.ones(6)
    best = None
    best_score = math.inf
    history = []
    for iteration in range(8):
        ants = []
        for ant_no in range(10):
            selected = []
            while len(selected) < 3:
                selected.append(choose_weighted(pheromone, selected, rng))
            candidate = pso(
                selected, scenarios, True,
                seed + iteration * 113 + ant_no * 17,
                particles=8, iters=16
            )
            ants.append(candidate)
            if candidate["score"] < best_score:
                best_score = candidate["score"]
                best = candidate
        ants.sort(key=lambda item: item["score"])
        pheromone *= .78
        for rank, ant in enumerate(ants[:4]):
            deposit = 1 / (1 + ant["score"] / 100)
            for index in ant["selected"]:
                pheromone[index] += deposit / (rank + 1)
        history.append({
            "iteration": iteration + 1,
            "best_training_score": float(ants[0]["score"]),
            "selected": [TECH[i]["name"] for i in ants[0]["selected"]],
        })
    return {**best, "history": history}


def scenario_vectors(plan, scenarios):
    weights = np.asarray(plan["weights"])
    selected = np.asarray(plan["selected"], dtype=int)
    spend = np.zeros(6)
    spend[selected] = weights * 100 * plan["usage"]
    capacity = spend / CAPEX
    supply = capacity[None, :] * YIELD[None, :] * scenarios["av"]
    total = supply.sum(axis=1)
    operating = (supply * OPEX[None, :]).sum(axis=1)
    emissions = (supply * EF[None, :]).sum(axis=1)
    shortfall = np.maximum(0, scenarios["demand"] - total)
    costs = (
        .085 * (100 * plan["usage"])
        + operating + 7 * emissions + 250 * shortfall
        + 60 * np.maximum(0, emissions - 24)
    )
    return costs, shortfall, emissions


def main():
    train = make_scenarios(180, 99123)
    test = make_scenarios(5000, 44109)
    mean_state = {"demand": np.array([60.0]), "av": BASE.reshape(1, -1)}

    deterministic = pso(list(range(6)), mean_state, False, 601, particles=14, iters=35)
    risk_pso = pso(list(range(6)), train, True, 602, particles=14, iters=35)
    hybrid = aco_pso(train, 603)

    plans = [
        ("Deterministic mean-state PSO", deterministic),
        ("Risk-aware PSO", risk_pso),
        ("ACO + adaptive PSO", hybrid),
    ]
    result_rows = []
    for name, plan in plans:
        test_metrics = evaluate(plan["weights"], plan["selected"], plan["usage"], test, robust=True)
        result_rows.append({
            "model": name,
            "selected_technologies": [TECH[i]["name"] for i in plan["selected"]],
            "test": test_metrics,
        })

    cost_pso, short_pso, _ = scenario_vectors(risk_pso, test)
    cost_hybrid, short_hybrid, _ = scenario_vectors(hybrid, test)
    delta = cost_hybrid - cost_pso
    rng_boot = np.random.default_rng(20261120)
    bootstrap = np.array([
        rng_boot.choice(delta, size=len(delta), replace=True).mean()
        for _ in range(3000)
    ])

    # Exploratory random feasibility screen: not a proof that no feasible plan exists.
    rng_screen = np.random.default_rng(777)
    n_portfolios, n_scenarios = 20000, 1000
    weights = rng_screen.dirichlet(np.ones(6) * .8, size=n_portfolios)
    usage = rng_screen.uniform(.6, 1, size=n_portfolios)
    capacities = weights * (100 * usage[:, None]) / CAPEX[None, :]
    supply_coeff = capacities * YIELD[None, :]
    supply = supply_coeff @ test["av"][:n_scenarios].T
    shortfall = np.maximum(0, test["demand"][:n_scenarios][None, :] - supply)
    event_rate = (shortfall > .02 * test["demand"][:n_scenarios][None, :]).mean(axis=1)
    emission_coeff = capacities * YIELD[None, :] * EF[None, :]
    emissions = emission_coeff @ test["av"][:n_scenarios].T
    carbon_probability = (emissions > 24).mean(axis=1)
    best = int(np.argmin(event_rate))

    output = {
        "type": "synthetic_stress_test_not_real_asset_data",
        "seeds": {"train": 99123, "test": 44109, "deterministic": 601, "risk_pso": 602, "aco_pso": 603},
        "training_scenarios": 180,
        "heldout_test_scenarios": 5000,
        "capital_budget_arbitrary_units": 100,
        "mean_demand_arbitrary_units": 60,
        "carbon_threshold_arbitrary_emission_units": 24,
        "shortfall_event_definition": "unserved energy > 2% of scenario demand",
        "results": result_rows,
        "paired_hybrid_minus_pso_test_cost": {
            "mean_difference": float(delta.mean()),
            "conditional_scenario_bootstrap_95pct_ci": np.quantile(bootstrap, [.025, .975]).tolist(),
            "share_of_test_scenarios_hybrid_cost_lower": float(np.mean(delta < 0)),
            "shortfall_event_rate_difference_percentage_points": float(
                100 * ((short_hybrid > .02 * test["demand"]).mean()
                       - (short_pso > .02 * test["demand"]).mean())
            ),
            "warning": "Conditional on two fitted plans; does not include optimizer-seed uncertainty.",
        },
        "random_feasibility_screen": {
            "candidate_portfolios": n_portfolios,
            "test_scenarios": n_scenarios,
            "best_shortfall_event_rate": float(event_rate[best]),
            "best_capital_shares": (weights[best] * usage[best] * 100).tolist(),
            "carbon_violation_probability_for_that_candidate": float(carbon_probability[best]),
            "meets_95pct_reliability": bool(event_rate[best] <= .05),
            "warning": "Random search is not proof of infeasibility.",
        },
        "model_challenge": [
            "The hybrid did not establish practical superiority over adaptive PSO.",
            "Neither risk-aware plan met a 95% supply-reliability requirement.",
            "Current penalties do not guarantee hard chance constraints.",
            "A real study needs repeated seeds, compute-matched baselines and calibrated asset-level scenarios.",
        ],
    }
    (OUT / "portfolio_stress_test.json").write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
