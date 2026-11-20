# Data provenance and usage

## 1. Monthly Brent and WTI spot prices

- Snapshot files: `brent_monthly.csv`, `wti_monthly.csv`.
- Original provider: U.S. Energy Information Administration (EIA), Europe Brent spot price and Cushing, OK WTI spot price, monthly series.
- Snapshot mirror: [datasets/oil-prices](https://github.com/datasets/oil-prices).
- Original EIA series pages: [Brent](https://www.eia.gov/dnav/pet/hist/RBRTEd.htm), [WTI](https://www.eia.gov/dnav/pet/hist/RWTCD.htm).
- Frequency: monthly; dates are month labels (the 15th in the mirror).
- Brent snapshot covers 1987-05 through 2026-10 (474 monthly rows); WTI starts 1986-01 and runs through 2026-10.
- EIA data are US government data; retain attribution to EIA and note that the GitHub repository is a mirror, not the data origin.

## 2. Geopolitical Risk (GPR)

- Snapshot file: `gpr_caldara_iacoviello_monthly.csv`.
- Original authors: Dario Caldara and Matteo Iacoviello.
- Paper: Caldara, D. & Iacoviello, M. (2022). “Measuring Geopolitical Risk.” *American Economic Review*, 112(4), 1194–1225. https://doi.org/10.1257/aer.20191823
- Official data/methodology page: https://www.matteoiacoviello.com/gpr.htm
- Download mirror used for this snapshot: [kvasilopoulos/econdata](https://github.com/kvasilopoulos/econdata/blob/master/docs/data/ci2022.csv).
- Frequency: monthly; columns include GPR, threat/act subindices and country-specific measures.
- Recent GPR index begins in 1985; historical series begin in 1900. This file contains 1985–2026 recent GPR observations plus historical fields.
- The GPR measure is derived from newspaper coverage. It is not a direct physical measure of oil-export disruption and does not establish causal impact on Brent.
- Cite the original authors and official site; record the repository snapshot date when refreshing.

## 3. Oil VAR reference data

- Snapshot file: `oil_var_kilian_lutkepohl.csv`.
- The mirror labels it as the Kilian and Lütkepohl (2017) textbook oil VAR dataset.
- Mirror: [kvasilopoulos/econdata](https://github.com/kvasilopoulos/econdata/blob/master/docs/data/oil.csv).
- Variables: quarterly real oil price growth, inflation and real GDP growth; 1973-Q1 to 2013-Q2.
- Use it as a separate textbook replication/benchmark. Do not merge its US quarterly macro measures naively with monthly nominal Brent or claim it is a global causal model.

## 4. Planned sources for full O&G studies

| Domain | Recommended primary source | Use |
|---|---|---|
| Global supply/demand/inventories | EIA, IEA, OPEC statistical bulletins | Balance, stocks, production, exports, refining |
| Field decline | IEA, *The Implications of Oil and Gas Field Decline Rates* (2025) | Field-level decline rates and natural decline |
| Reserves/resources | OPEC ASB, national regulators, SPE-PRMS-aligned reports | Proven/probable/possible and resource definitions |
| Geopolitical exposure | Caldara–Iacoviello GPR; AI-GPR; GDELT; OFAC/UN sanctions | Events, threats/acts, sanctions and country/asset exposure |
| Macro | World Bank, IMF, FRED, national statistical agencies | GDP, industrial production, inflation, FX, rates |
| Futures/market positioning | ICE, CME, CFTC Commitments of Traders | Term structure, positioning, options/volatility |
| Shipping/logistics | AIS vendors, port authorities, UNCTAD, public chokepoint data | Route capacity, freight, port and insurance exposure |
| Energy transition | IEA WEO, IPCC, OWID, national energy plans | Technology pathways, demand, emissions, affordability |

Some sources require API keys or paid licences. Never scrape or redistribute licensed data contrary to their terms. Record units, scope, publication date, data vintage, license, missingness and transformations in a data dictionary.

## 5. Reproducibility rules

1. Preserve raw snapshots unchanged.
2. Store retrieval date, source URL, provider, file hash and license.
3. Keep separate frequencies and currencies until explicitly transformed.
4. Use information available at the prediction timestamp only.
5. Do not treat imputed data as observed.
6. Keep causal inference separate from predictive feature attribution.
