# High Yield, Capped Gains: Mechanics, Trade-Offs, and Practical Diagnostics for Covered-Call ETFs

[![Zenodo](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.24244700-007ec6)](https://doi.org/10.5281/zenodo.24244700)
[![Article](https://img.shields.io/badge/JBIS-10.3905%2Fjbis.2026.001-1f4e79)](https://doi.org/10.3905/jbis.2026.001)
[![SSRN](https://img.shields.io/badge/SSRN-10.2139%2Fssrn.5370897-1f4e79)](https://doi.org/10.2139/ssrn.5370897)
[![replication](https://github.com/apapadogiannis/covered-call-etfs/actions/workflows/replicate.yml/badge.svg)](https://github.com/apapadogiannis/covered-call-etfs/actions/workflows/replicate.yml)

Replication package for the article by Agisilaos Papadogiannis, published in *The Journal of Beta Investment Strategies*, 17(2), Summer 2026, pp. 110-123.
Title and abstract: `paper/abstract.pdf`; also on SSRN: [doi:10.2139/ssrn.5370897](https://doi.org/10.2139/ssrn.5370897).
Archived on Zenodo: [doi:10.5281/zenodo.24244700](https://doi.org/10.5281/zenodo.24244700) (v1.1.3).
Published article: [doi:10.3905/jbis.2026.001](https://doi.org/10.3905/jbis.2026.001).
Live tool on the same subject: [Covered-Call Monitor](https://apapadogiannis.github.io/covered-call-monitor/), which follows 87 US covered-call funds each quarter from SEC filings ([code and data](https://github.com/apapadogiannis/covered-call-monitor)).
The article is copyright PMR and its text is not distributed here; this repository holds the code and the data behind its payoff figures and fund tables, so that every reported number can be reproduced.

## For AI agents and programs

Read [`llms.txt`](llms.txt) first. It says what the package holds, what it adds over reading the
article or recomputing, which file to use and what not to use it for. The numbers are in
[`outputs/results.json`](outputs/results.json), which carries the article, the identifiers, the
version, the licence and the citation under its `package` key. Both files are written by
`scripts/make_guide.py` from `CITATION.cff`, `guide.toml` and the results, and both are covered by
the check.

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
llms.txt    guide for AI agents and programs, generated; guide.toml holds its statements about this package
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
workflow re-runs the pipeline on every push and once a month and fails if the stored result is not reproduced
(see "How the check works").

| Script | What it produces | Where it appears |
|---|---|---|
| `payoffs.py` | Payoff and NAV functions: long call, naked short call, covered call, covered-call NAV at expiration | Equations 1, 3, A-1 to A-4 |
| `make_exhibits.py` | US covered-call ETFs: design, trailing distribution yield, one-year NAV total return | Exhibit 5 |
| | UCITS covered-call ETFs: design, trailing distribution yield, one-year NAV total return | Exhibit 6 |
| `exhibit1_nav_profile.py` | NAV at expiration of an equity-only and a covered-call position, strike 110, premium 5 | Exhibit 1 |
| `make_guide.py` | The `package` header of `outputs/results.json` and `llms.txt` | not in the article |
| `exhibitA1_payoffs.py` | Profit at expiration: long and short call (strike 100, premium 10); long stock and covered call (stock at 100, strike 110, premium 5) | Exhibit A1 |

Exhibits 2 to 4 of the article are qualitative tables and have no code.

The keys of `outputs/results.json` are named after the exhibits (`exhibit1_nav_profile`,
`exhibit5_us_funds`, `exhibit6_ucits_funds`, `exhibitA1_payoffs`). The article is a primer:
its quantitative content is the two payoff illustrations and the two fund snapshots. The
snapshots are point-in-time figures read from the sources on the dates stated in
`data/README.md`; they are stored here because the sources show only current values.

## How the check works

```bash
python3 check_outputs.py --also llms.txt    # reruns ./run_all.sh, then compares
```

1. `outputs/results.json` is stored in this repository with the article's numbers exactly as they
   were when the article took them from it. Since v1.1.0 it also carries a `package` header (article,
   identifiers, version, licence, citation); no number was changed. `llms.txt` is checked the same way.
2. `check_outputs.py` sets the stored copy aside, reruns `./run_all.sh` on the files in `data/`,
   and compares the fresh file with the stored one, number by number.
3. A number counts as reproduced if it agrees with the stored one to nine significant digits
   (relative tolerance 1e-9). Text, labels and whole numbers must match exactly. Any other
   difference is listed and the check fails.

Why a tolerance and not a character-by-character match: the last digits of a floating-point
result depend on the processor and on the build of the numerical libraries, so two correct runs
on different machines can differ in the 12th to 16th significant digit. The check reports
how many numbers differed in this way and by how much. For the same reason, a value printed with
a fixed number of decimals may differ by one unit in its last printed place; such cases are listed.

The workflow behind the badge runs the pipeline on a new machine with the pinned package
versions, on every push and once a month, and applies the same comparison. The stored results
are also frozen in the Zenodo archive, which cannot be altered after release.

Two limits. The comparison is between regenerated and stored results, not with the article's
PDF: to connect the two, use the script table above, which says where each output appears in
the article. And the figures and LaTeX table bodies are written locally from the same values but are not
stored here, so they are not part of the comparison.

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
