# High Yield, Capped Gains: Mechanics, Trade-Offs, and Practical Diagnostics for Covered-Call ETFs

[![Zenodo](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.24244700-007ec6)](https://doi.org/10.5281/zenodo.24244700)
[![SSRN](https://img.shields.io/badge/SSRN-10.2139%2Fssrn.5370897-1f4e79)](https://doi.org/10.2139/ssrn.5370897)
[![replication](https://github.com/apapadogiannis/covered-call-etfs/actions/workflows/replicate.yml/badge.svg)](https://github.com/apapadogiannis/covered-call-etfs/actions/workflows/replicate.yml)

Replication package for the article by Agisilaos Papadogiannis, published in *The Journal of Beta Investment Strategies*, 17(2), Summer 2026, pp. 110-123.
Title and abstract: `paper/abstract.pdf`; also on SSRN: [doi:10.2139/ssrn.5370897](https://doi.org/10.2139/ssrn.5370897).
Archived on Zenodo: [doi:10.5281/zenodo.24244700](https://doi.org/10.5281/zenodo.24244700) (v1.0.1).
Published article: [doi:10.3905/jbis.2026.001](https://doi.org/10.3905/jbis.2026.001).
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
workflow re-runs the pipeline on every push and once a month and fails if `results.json` differs from the
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

## How the check works

1. `outputs/results.json` is stored in this repository exactly as it was when the
   article's numbers were taken from it.
2. `./run_all.sh` reruns every script on the files in `data/` and overwrites that file with
   a freshly computed one.
3. `git diff --exit-code -- outputs/results.json` then compares the fresh file with the
   stored version, character by character. If nothing is printed, it is identical; any
   difference is listed and counts as a failure.

The workflow behind the badge does exactly these three steps on a new machine with the pinned
package versions, on every push and once a month, so a green badge means the stored
file still follows from the data and code. The stored file is also frozen in the Zenodo
archive, which cannot be altered after release.

Two limits. The comparison is between the regenerated and the stored file, not with the article's
PDF: to connect the two, use the script table above, which says where each output appears in
the article. And the figures and LaTeX table bodies are written locally from the same values but are
not stored here, so they are not part of the comparison.

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
> https://doi.org/10.3905/jbis.2026.001
> SSRN: https://doi.org/10.2139/ssrn.5370897

Code and data:

> Papadogiannis, A. (2026). "High yield, capped gains: Mechanics, trade-offs, and practical diagnostics for covered-call ETFs. Replication package." Zenodo.
> https://doi.org/10.5281/zenodo.24244700

## Disclaimer

Independent research; no funding, no institutional position. Not investment advice.
