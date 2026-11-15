# Data

Every file used by the scripts, with its source, as-of date and the terms stated by the
source. Third-party data remain the property of their sources and are redistributed here
for replication only, with attribution.

| File | Content | Source | As of | Terms |
|---|---|---|---|---|
| `us_funds.csv` | Four US-listed covered-call ETFs (QYLD, JEPI, XYLD, RYLD), USD share classes: trailing distribution yield (%) and one-year NAV total return (%), with index focus, overlay method and reset/moneyness | Charles Schwab & Co., Inc., Schwab Exchange Traded Funds Report Cards, https://www.schwab.com. Yield is Schwab's "Distribution Yield"; return is Schwab's "Standardized Quarterly Total Return" (NAV) | Yield: close of December 19, 2025. Return: September 30, 2025. Accessed December 22, 2025 | Site terms apply; no open license. Eight figures transcribed by hand from the report cards |
| `ucits_funds.csv` | Four UCITS covered-call ETFs (JEPG, JEPQ, JEPI, QYLD UCITS), EUR share classes, with ISIN: trailing distribution yield (%) and one-year NAV total return (%), with index focus, overlay method and reset/moneyness | justETF, fund profile pages (returns overview and current dividend yield), https://www.justetf.com | November 2025 | Site terms apply; no open license. Eight figures transcribed by hand from the profile pages |

Overlay method, moneyness and reset cadence in both files are descriptive and come from
issuer materials: Global X ETFs (https://www.globalxetfs.com, https://globalxetfs.eu) and
J.P. Morgan Asset Management (https://am.jpmorgan.com).

## Constants entered in the code

The payoff illustrations use round numbers chosen for exposition, not market data:

- Exhibit 1: strike 110, premium 5.
- Exhibit A1, Panel A: strike 100, premium 10.
- Exhibit A1, Panel B: stock bought at 100, strike 110, premium 5.

## Notes

- Returns assume distributions reinvested. US figures are in USD and UCITS figures in EUR;
  the EUR share classes are unhedged and hold largely USD assets, so their returns include
  the USD/EUR move over the window.
- The yield and return dates of the US funds differ (December 19 and September 30, 2025),
  as the source reports total return at quarter end.
- The two files are snapshots. The sources show current values only, so the figures cannot
  be downloaded again for the same dates.
