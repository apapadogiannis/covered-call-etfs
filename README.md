# High Yield, Capped Gains: Mechanics, Trade-Offs, and Practical Diagnostics for Covered-Call ETFs

[![SSRN](https://img.shields.io/badge/SSRN-10.2139%2Fssrn.5370897-1f4e79)](https://doi.org/10.2139/ssrn.5370897)
[![replication](https://github.com/apapadogiannis/covered-call-etfs/actions/workflows/replicate.yml/badge.svg)](https://github.com/apapadogiannis/covered-call-etfs/actions/workflows/replicate.yml)

Replication package for the article by Agisilaos Papadogiannis, published in *The Journal of Beta Investment Strategies*, 17(2), Summer 2026, pp. 110-123.
Title and abstract: `paper/abstract.pdf`; also on SSRN: [doi:10.2139/ssrn.5370897](https://doi.org/10.2139/ssrn.5370897).
Published article: [The Journal of Beta Investment Strategies, Volume 17, Issue 2](https://www.pm-research.com/content/iijindinv/17/2).
The article is copyright PMR and its text is not distributed here; this repository holds the code and the data behind its payoff figures and fund tables, so that every reported number can be reproduced.

## What this is

Covered-call exchange-traded funds (ETFs) convert part of equity upside into option-premium
cash distributions by systematically writing call options against an equity portfolio. This
article is a high-level primer and due-diligence guide for investors and allocators evaluating
covered-call ETFs. We explain the mechanics with a payoff view and a mark-to-market net
asset value (NAV) decomposition that helps interpret distribution yield and NAV dynamics in
the presence of a short-call liability. We then summarize the dominant exposures and the
market environments in which covered-call strategies tend to help or hurt. We contrast US
products with European UCITS (Undertakings for Collective Investment in Transferable
Securities) variants to show how design choices, including moneyness, reset cadence, listed
options versus equity-linked note (ELN) implementation, and currency exposure, affect
realized outcomes. The guidance is practical: treat covered-call ETFs as satellite
complements, not core growth anchors. Evaluate them on total return and distribution
sustainability rather than headline yield, and monitor return of capital (ROC) and implied
volatility (IV).

## Layout

```
scripts/    the code (see below)
data/       the fund figures of Exhibits 5 and 6, with sources and terms in data/README.md
outputs/    results.json: every number in Exhibits 5 and 6 and the key values of Exhibits 1 and A1
paper/      title and abstract of the article (PDF and LaTeX source); the full text is not included
```

## Reproducing

Requirements: Python 3.11+, `pip install -r requirements.txt` (numpy, pandas, matplotlib).
`requirements-lock.txt` lists the exact versions under which `outputs/results.json` was
generated.

```bash
git clone https://github.com/apapadogiannis/covered-call-etfs
cd covered-call-etfs
pip install -r requirements.txt
./run_all.sh    # a few seconds
```

The scripts are deterministic. Re-running them reproduces `outputs/results.json` and
writes the LaTeX table bodies (`outputs/exhibit5.tex`, `outputs/exhibit6.tex`) and the two
figures (`figures/`), which are generated locally and not tracked. A GitHub Actions
workflow re-runs the pipeline on every push and fails if `results.json` differs from the
committed file.

| Script | What it produces | Where it appears |
|---|---|---|
| `payoffs.py` | Payoff and NAV functions: long call, naked short call, covered call, covered-call NAV at expiration | Equations 1, 3, A-1 to A-4 |
| `make_exhibits.py` | US covered-call ETFs: design, trailing distribution yield, one-year NAV total return | Exhibit 5 |
| | UCITS covered-call ETFs: design, trailing distribution yield, one-year NAV total return | Exhibit 6 |
| `exhibit1_nav_profile.py` | NAV at expiration of an equity-only and a covered-call position, strike 110, premium 5 | Exhibit 1 |
| `exhibitA1_payoffs.py` | Profit at expiration: long and short call (strike 100, premium 10); long stock and covered call (stock at 100, strike 110, premium 5) | Exhibit A1 |

Exhibits 2 to 4 of the article are qualitative tables and have no code.

The keys of `outputs/results.json` are named after the exhibits (`exhibit1_nav_profile`,
`exhibit5_us_funds`, `exhibit6_ucits_funds`, `exhibitA1_payoffs`). The article is a primer:
its quantitative content is the two payoff illustrations and the two fund snapshots. The
snapshots are point-in-time figures read from the sources on the dates stated in
`data/README.md`; they are stored here because the sources show only current values.

## Data and licensing

All input files are in `data/`; `data/README.md` lists, for each file, the source, the
as-of date and the terms under which the source makes it available. In short:

- US funds (QYLD, JEPI, XYLD, RYLD): Charles Schwab ETF report cards.
- UCITS funds (JEPG, JEPQ, JEPI, QYLD UCITS): justETF fund profiles.
- Overlay method, moneyness and reset cadence: issuer materials (Global X, J.P. Morgan Asset Management).

Third-party data remain the property of their sources and are included for replication
only, with attribution; they are not covered by the license of this repository.
Code: MIT License. `outputs/results.json`: CC BY 4.0, cite the article.

## Citation

> Papadogiannis, A. (2026). "High yield, capped gains: Mechanics, trade-offs, and practical
> diagnostics for covered-call ETFs." *The Journal of Beta Investment Strategies*, 17(2), 110-123.
> SSRN: https://doi.org/10.2139/ssrn.5370897

## Disclaimer

Independent research; no funding, no institutional position. Not investment advice.
