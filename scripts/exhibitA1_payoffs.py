"""Exhibit A1: profit at expiration. Panel A: long and short call, strike 100, premium 10.
Panel B: long stock and covered call, stock bought at 100, strike 110, premium 5."""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from payoffs import covered_call, long_call, long_stock, naked_short_call

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": "serif", "font.serif": ["Latin Modern Roman", "DejaVu Serif"],
                     "mathtext.fontset": "cm", "font.size": 10})

s = np.linspace(50, 150, 1001)
fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.3), sharey=True)

ax = axes[0]
K, C = 100.0, 10.0
ax.plot(s, long_call(s, K, C), color="#1f3fbf", lw=1.6, label="Long call (net)")
ax.plot(s, naked_short_call(s, K, C), color="#c0392b", lw=1.6, label="Short call (net)")
ax.set_title(r"Panel A: long vs. short call, $K=100$, $C=10$", fontsize=9.5)

ax = axes[1]
P0, K, C = 100.0, 110.0, 5.0
ax.plot(s, long_stock(s, P0), color="0.45", lw=1.2, ls=(0, (4, 3)), label="Long stock only")
ax.plot(s, covered_call(s, P0, K, C), color="#1f3fbf", lw=1.6, label="Covered call (net)")
ax.set_title(r"Panel B: covered call, $P_0=100$, $K=110$, $C=5$", fontsize=9.5)

for ax, k in zip(axes, (100.0, 110.0)):
    ax.axhline(0, color="0.2", lw=0.7)
    ax.axvline(k, color="0.6", lw=0.8, ls=(0, (3, 3)))
    ax.set_xlim(50, 150); ax.set_ylim(-55, 55)
    ax.set_xticks([50, 100, 150]); ax.set_yticks([-50, -20, 0, 20, 50])
    ax.set_xlabel(r"$S_T$ (expiration price)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.24), ncol=2, frameon=False, fontsize=9)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
axes[0].set_ylabel("Profit/loss")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "exhibitA1_payoffs.pdf"))
fig.savefig(os.path.join(OUT, "exhibitA1_payoffs.png"), dpi=150)
