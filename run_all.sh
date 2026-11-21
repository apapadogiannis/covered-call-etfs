#!/usr/bin/env bash
# Reproduces the two fund tables (Exhibits 5 and 6) and the payoff figures (Exhibits 1 and A1). Runs in a few seconds.
set -e
cd "$(dirname "$0")/scripts"
for f in make_exhibits exhibit1_nav_profile exhibitA1_payoffs make_guide; do
  echo "== $f"; python3 "$f.py"
done
