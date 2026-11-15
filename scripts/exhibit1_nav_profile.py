"""Exhibit 1: NAV at expiration of an equity-only position (dashed) and a covered-call
position (solid), strike K = 110, premium 5."""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from payoffs import covered_call_nav

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": "serif", "font.serif": ["Latin Modern Roman", "DejaVu Serif"],
                     "mathtext.fontset": "cm", "font.size": 10})

K, C = 110.0, 5.0
s = np.linspace(80, 140, 601)

fig, ax = plt.subplots(figsize=(6.3, 3.6))
ax.plot(s[s <= 130], s[s <= 130], color="0.45", lw=1.2, ls=(0, (4, 3)), label="Equity-only NAV")
ax.plot(s, covered_call_nav(s, K, C), color="#1f3fbf", lw=1.6, label="Covered-call NAV")
ax.axvline(K, color="#c0392b", lw=0.9, ls=(0, (3, 3)))
ax.axhline(K + C, color="0.6", lw=0.8, ls=(0, (1, 3)))
ax.set_xlim(80, 140); ax.set_ylim(80, 130)
ax.set_xticks([80, 100, 110, 120, 140]); ax.set_yticks(range(80, 131, 10))
ax.set_xlabel(r"Asset price at expiration ($S_T$)"); ax.set_ylabel("Covered-call ETF NAV")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=2, frameon=True, fontsize=9)
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "exhibit1_nav_profile.pdf"))
fig.savefig(os.path.join(OUT, "exhibit1_nav_profile.png"), dpi=150)
