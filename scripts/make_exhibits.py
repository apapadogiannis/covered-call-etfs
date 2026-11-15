"""Builds outputs/results.json: the fund figures of Exhibits 5 and 6 and the key values of
the payoff illustrations in Exhibits 1 and A1. Also writes the LaTeX bodies of the two tables."""
import json
import os

import pandas as pd

from payoffs import covered_call, covered_call_nav, long_call, naked_short_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "outputs")
os.makedirs(OUT, exist_ok=True)

us = pd.read_csv(os.path.join(DATA, "us_funds.csv"), dtype=str)
uc = pd.read_csv(os.path.join(DATA, "ucits_funds.csv"), dtype=str)


def rows(df, cols):
    out = []
    for _, r in df.iterrows():
        d = {c: r[c] for c in cols}
        d["distribution_yield_pct"] = float(r["distribution_yield_pct"])
        d["tr_1y_nav_pct"] = float(r["tr_1y_nav_pct"])
        out.append(d)
    return out


def grid(f, points):
    return {str(p): round(float(f(p)), 2) for p in points}


# Exhibit 1: NAV at expiration, strike 110, premium 5.
K1, C1 = 110.0, 5.0
# Exhibit A1, Panel A: long and short call, strike 100, premium 10.
KA, CA = 100.0, 10.0
# Exhibit A1, Panel B: covered call, stock bought at 100, strike 110, premium 5.
P0, KB, CB = 100.0, 110.0, 5.0

results = {
    "exhibit1_nav_profile": {
        "strike": K1,
        "premium": C1,
        "nav_cap": K1 + C1,
        "equity_only_nav": grid(lambda s: s, [80, 100, 110, 120, 140]),
        "covered_call_nav": grid(lambda s: covered_call_nav(s, K1, C1), [80, 100, 110, 120, 140]),
    },
    "exhibit5_us_funds": {
        "currency": "USD",
        "distribution_yield_as_of": us["yield_as_of"].iloc[0],
        "total_return_as_of": us["tr_as_of"].iloc[0],
        "funds": rows(us, ["ticker", "index_focus", "overlay_method", "reset_moneyness"]),
    },
    "exhibit6_ucits_funds": {
        "currency": "EUR",
        "as_of": uc["as_of"].iloc[0],
        "funds": rows(uc, ["ticker", "isin", "index_focus", "overlay_method", "reset_moneyness"]),
    },
    "exhibitA1_payoffs": {
        "panel_a": {
            "strike": KA,
            "premium": CA,
            "breakeven": KA + CA,
            "long_call_profit": grid(lambda s: long_call(s, KA, CA), [50, 100, 110, 150]),
            "short_call_profit": grid(lambda s: naked_short_call(s, KA, CA), [50, 100, 110, 150]),
        },
        "panel_b": {
            "purchase_price": P0,
            "strike": KB,
            "premium": CB,
            "breakeven": P0 - CB,
            "max_profit": KB - P0 + CB,
            "long_stock_profit": grid(lambda s: s - P0, [50, 95, 100, 110, 150]),
            "covered_call_profit": grid(lambda s: covered_call(s, P0, KB, CB), [50, 95, 100, 110, 150]),
        },
    },
}

with open(os.path.join(OUT, "results.json"), "w") as f:
    json.dump(results, f, indent=2)
    f.write("\n")


def pct(x, d):
    s = f"{abs(x):.{d}f}\\%"
    return ("$-$" + s) if x < 0 else s


def table(df, name, d_tr):
    lines = []
    for _, r in df.iterrows():
        focus = r["index_focus"].replace("&", "\\&")
        lines.append(" & ".join([
            f"{r['ticker']} ({focus})", r["overlay_method"], r["reset_moneyness"],
            pct(float(r["distribution_yield_pct"]), 2), pct(float(r["tr_1y_nav_pct"]), d_tr),
        ]) + " \\\\")
    with open(os.path.join(OUT, name), "w") as f:
        f.write("\n".join(lines) + "\n")


table(us, "exhibit5.tex", 1)
table(uc, "exhibit6.tex", 2)

for label, df in (("Exhibit 5 (US, USD)", us), ("Exhibit 6 (UCITS, EUR)", uc)):
    print(label)
    for _, r in df.iterrows():
        print(f"  {r['ticker']:<11} yield {float(r['distribution_yield_pct']):6.2f}%   1Y TR (NAV) {float(r['tr_1y_nav_pct']):6.2f}%")
