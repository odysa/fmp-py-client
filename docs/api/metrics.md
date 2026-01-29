# Metrics API

Access key financial metrics, ratios, and scores.

## Methods

### key_metrics

Get key financial metrics.

```python
metrics = await client.key_metrics(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

**Returns key metrics including:**

- Revenue per share
- Net income per share
- Operating cash flow per share
- Free cash flow per share
- Book value per share
- PE ratio, PB ratio, PS ratio
- Enterprise value metrics
- ROE, ROA, ROIC
- And many more

---

### key_metrics_ttm

Get trailing twelve months key metrics.

```python
ttm_metrics = await client.key_metrics_ttm(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### ratios

Get financial ratios.

```python
ratios = await client.ratios(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

**Returns ratios including:**

- Liquidity ratios (current, quick, cash)
- Profitability ratios (gross margin, operating margin, net margin)
- Leverage ratios (debt/equity, debt/assets)
- Efficiency ratios (asset turnover, inventory turnover)
- Valuation ratios (PE, PB, PS, PEG)

---

### ratios_ttm

Get trailing twelve months financial ratios.

```python
ttm_ratios = await client.ratios_ttm(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### financial_scores

Get financial scores including Altman Z-Score, Piotroski F-Score, and more.

```python
scores = await client.financial_scores(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

**Returns:**

- **Altman Z-Score**: Bankruptcy prediction score
  - > 2.99: Safe zone
  - 1.81 - 2.99: Grey zone
  - < 1.81: Distress zone
- **Piotroski F-Score**: Financial strength (0-9)
  - 8-9: Strong
  - 0-2: Weak

---

### owner_earnings

Get owner earnings (Buffett's preferred metric).

```python
owner = await client.owner_earnings(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def analyze_metrics():
    async with AsyncFMPClient("your-api-key") as client:
        symbol = "AAPL"

        # Get current TTM metrics
        metrics = await client.key_metrics_ttm(symbol=symbol)
        m = metrics[0]

        print(f"=== {symbol} Key Metrics (TTM) ===")
        print(f"PE Ratio: {m.get('peRatioTTM', 'N/A'):.2f}")
        print(f"PB Ratio: {m.get('pbRatioTTM', 'N/A'):.2f}")
        print(f"ROE: {m.get('roeTTM', 0) * 100:.1f}%")
        print(f"ROA: {m.get('roaTTM', 0) * 100:.1f}%")
        print(f"Debt/Equity: {m.get('debtToEquityTTM', 'N/A'):.2f}")

        # Get financial ratios
        ratios = await client.ratios_ttm(symbol=symbol)
        r = ratios[0]

        print(f"\n=== Financial Ratios (TTM) ===")
        print(f"Current Ratio: {r.get('currentRatioTTM', 'N/A'):.2f}")
        print(f"Quick Ratio: {r.get('quickRatioTTM', 'N/A'):.2f}")
        print(f"Gross Margin: {r.get('grossProfitMarginTTM', 0) * 100:.1f}%")
        print(f"Operating Margin: {r.get('operatingProfitMarginTTM', 0) * 100:.1f}%")
        print(f"Net Margin: {r.get('netProfitMarginTTM', 0) * 100:.1f}%")

        # Get financial scores
        scores = await client.financial_scores(symbol=symbol)
        if scores:
            s = scores[0]
            print(f"\n=== Financial Scores ===")
            print(f"Altman Z-Score: {s.get('altmanZScore', 'N/A')}")
            print(f"Piotroski Score: {s.get('piotroskiScore', 'N/A')}")

asyncio.run(analyze_metrics())
```
