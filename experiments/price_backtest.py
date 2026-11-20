#!/usr/bin/env python3
"""Rolling one-month Brent return backtest with/without lagged aggregate GPR.

Run from repository root: python experiments/price_backtest.py
Requires numpy and pandas. Uses only checked-in raw snapshots.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)

WINDOW = 120
RIDGE = 0.05


def fit_ridge_predict(x_train, y_train, x_test, ridge=RIDGE):
    x = np.asarray(x_train, dtype=float)
    y = np.asarray(y_train, dtype=float)
    row = np.asarray(x_test, dtype=float)
    gram = x.T @ x
    penalty = np.eye(gram.shape[0]) * ridge
    penalty[0, 0] = 0.0  # Do not penalise intercept.
    beta = np.linalg.solve(gram + penalty, x.T @ y)
    return float(row @ beta)


def metrics(pred, actual):
    pred = np.asarray(pred, dtype=float)
    actual = np.asarray(actual, dtype=float)
    err = pred - actual
    mae = float(np.mean(np.abs(err)))
    rmse = float(np.sqrt(np.mean(err ** 2)))
    denom = float(np.sum((actual - np.mean(actual)) ** 2))
    oos_r2 = float(1 - np.sum(err ** 2) / denom) if denom > 0 else float("nan")
    direction = float(np.mean(np.sign(pred) == np.sign(actual)))
    return {
        "n": int(len(actual)),
        "mae_pct_log_return": mae * 100,
        "rmse_pct_log_return": rmse * 100,
        "directional_accuracy_pct": direction * 100,
        "oos_r2_vs_mean": oos_r2,
    }


def rolling_model(returns, gpr, with_gpr=False, window=WINDOW):
    preds, actuals, dates = [], [], []
    log_gpr = np.log1p(gpr)
    for t in range(window + 1, len(returns)):
        x_train, y_train = [], []
        for i in range(t - window, t):
            if not (np.isfinite(returns[i]) and np.isfinite(returns[i - 1])):
                continue
            row = [1.0, returns[i - 1]]
            if with_gpr:
                if i < 2 or not (np.isfinite(log_gpr[i - 1]) and np.isfinite(log_gpr[i - 2])):
                    continue
                row.extend([log_gpr[i - 1], log_gpr[i - 1] - log_gpr[i - 2]])
            x_train.append(row)
            y_train.append(returns[i])

        if not np.isfinite(returns[t - 1]):
            continue
        x_test = [1.0, returns[t - 1]]
        if with_gpr:
            if t < 2 or not (np.isfinite(log_gpr[t - 1]) and np.isfinite(log_gpr[t - 2])):
                continue
            x_test.extend([log_gpr[t - 1], log_gpr[t - 1] - log_gpr[t - 2]])

        pred = fit_ridge_predict(x_train, y_train, x_test)
        preds.append(pred)
        actuals.append(float(returns[t]))
        dates.append(str(t))

    return metrics(preds, actuals), {"prediction": preds, "actual": actuals, "index": dates}


def main():
    brent = pd.read_csv(DATA / "brent_monthly.csv")
    gpr = pd.read_csv(DATA / "gpr_caldara_iacoviello_monthly.csv")

    brent["month"] = pd.to_datetime(brent["Date"]).dt.to_period("M")
    gpr["month"] = pd.to_datetime(gpr["date"]).dt.to_period("M")
    gpr["GPR"] = pd.to_numeric(gpr["GPR"], errors="coerce")
    joined = (
        brent[["month", "Price"]]
        .merge(gpr[["month", "GPR"]], on="month", how="inner")
        .dropna(subset=["Price", "GPR"])
        .sort_values("month")
        .reset_index(drop=True)
    )

    price = joined["Price"].to_numpy(dtype=float)
    gpr_values = joined["GPR"].to_numpy(dtype=float)
    returns = np.diff(np.log(price), prepend=np.nan)

    same_month_corr = float(np.corrcoef(gpr_values[1:], returns[1:])[0, 1])
    prior_gpr_corr = float(np.corrcoef(gpr_values[:-1], returns[1:])[0, 1])

    ar_metrics, ar_predictions = rolling_model(returns, gpr_values, with_gpr=False)
    gpr_metrics, gpr_predictions = rolling_model(returns, gpr_values, with_gpr=True)

    result = {
        "data": {
            "brent_rows": int(len(brent)),
            "gpr_rows": int(len(gpr)),
            "joined_rows": int(len(joined)),
            "first_month": str(joined["month"].iloc[0]),
            "last_month": str(joined["month"].iloc[-1]),
            "brent_min_usd_per_bbl": float(brent["Price"].min()),
            "brent_max_usd_per_bbl": float(brent["Price"].max()),
        },
        "method": {
            "forecast_horizon_months": 1,
            "rolling_training_window_months": WINDOW,
            "ridge_penalty": RIDGE,
            "target": "monthly Brent log return",
            "gpr_features": "prior-month log1p(GPR) level and one-month change",
            "note": "This is a simple predictive baseline, not a causal event-impact model.",
        },
        "correlation": {
            "same_month_gpr_vs_same_month_return": same_month_corr,
            "prior_month_gpr_vs_next_month_return": prior_gpr_corr,
        },
        "price_only_ar1": ar_metrics,
        "ar1_plus_lagged_gpr": gpr_metrics,
    }

    (OUT / "price_backtest.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    pd.DataFrame({
        "price_only_prediction": ar_predictions["prediction"],
        "price_only_actual": ar_predictions["actual"],
        "ar1_gpr_prediction": gpr_predictions["prediction"],
        "ar1_gpr_actual": gpr_predictions["actual"],
    }).to_csv(OUT / "price_backtest_forecasts.csv", index=False)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
