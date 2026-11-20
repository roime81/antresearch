#!/usr/bin/env python3
"""Transparent R/P and natural-decline arithmetic; not an exhaustion forecast."""
import json

# OPEC ASB-2026: year-end 2025 proven crude reserves and 2025 crude production.
opec_reserves_bn_bbl = 1572.0
opec_crude_production_mbpd = 74.85
opec_static_rp_years = (
    opec_reserves_bn_bbl * 1000
    / (opec_crude_production_mbpd * 365)
)

# Eni World Energy Review 2026 reports its own oil scope and R/P.
eni_reported_reserves_bn_bbl = 1790.0  # "exceeded" this value
eni_reported_production_mbpd = 100.4
eni_reported_rp_years = 48.9

# IEA 2025 no-investment natural decline stress: around 8% annually on average.
# Apply it mechanically to a rounded baseline only to illustrate compounding.
baseline_mbpd = 100.4
annual_decline = 0.08
years = 10
no_investment_2035_mbpd = baseline_mbpd * (1 - annual_decline) ** years

result = {
    "opec_crude_scope": {
        "proven_reserves_end_2025_bn_bbl": opec_reserves_bn_bbl,
        "world_crude_production_2025_mbpd": opec_crude_production_mbpd,
        "static_rp_years_calculated": opec_static_rp_years,
    },
    "eni_oil_scope": {
        "proven_reserves_end_2025_bn_bbl_lower_bound": eni_reported_reserves_bn_bbl,
        "production_2025_mbpd": eni_reported_production_mbpd,
        "reported_rp_years": eni_reported_rp_years,
    },
    "no_investment_decline_illustration": {
        "baseline_mbpd": baseline_mbpd,
        "annual_compound_decline": annual_decline,
        "years": years,
        "mechanical_2035_mbpd": no_investment_2035_mbpd,
        "warning": "Illustrative stress arithmetic, not a forecast or date of geological exhaustion.",
    },
    "interpretation": (
        "R/P is a static ratio. Reserve classifications and production boundaries differ "
        "between sources. Field decline, investment, reserve additions, technology, "
        "economics and demand determine actual production pathways."
    ),
}
print(json.dumps(result, indent=2))
