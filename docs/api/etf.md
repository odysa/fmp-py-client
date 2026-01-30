# ETF API

Access ETF holdings, weightings, and fund disclosure data.

## ETF Information

### etf_info

Get ETF information.

```python
info = await client.etf_info(symbol="SPY")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | ETF symbol |

---

### etf_holdings

Get ETF holdings (constituent stocks).

```python
holdings = await client.etf_holdings(symbol="SPY")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | ETF symbol |

## Weightings

### etf_sector_weightings

Get ETF sector weightings.

```python
sectors = await client.etf_sector_weightings(symbol="SPY")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | ETF symbol |

---

### etf_country_weightings

Get ETF country weightings.

```python
countries = await client.etf_country_weightings(symbol="VEU")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | ETF symbol |

---

### etf_asset_exposure

Get ETF asset class exposure.

```python
exposure = await client.etf_asset_exposure(symbol="SPY")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | ETF symbol |

## Fund Disclosures

### funds_disclosure_holders_latest

Get latest fund disclosure holders.

```python
holders = await client.funds_disclosure_holders_latest(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol to find fund holders |

---

### funds_disclosure

Get fund disclosure data for a specific period.

```python
disclosure = await client.funds_disclosure(
    symbol="AAPL",
    year=2024,
    quarter=1
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |
| `year` | `int` | Year |
| `quarter` | `int` | Quarter (1-4) |

---

### funds_disclosure_holders_search

Search fund disclosure holders by name.

```python
holders = await client.funds_disclosure_holders_search(name="Vanguard")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` | Fund name to search |

---

### funds_disclosure_dates

Get available fund disclosure dates.

```python
dates = await client.funds_disclosure_dates(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def etf_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get SPY ETF info
        info = await client.etf_info(symbol="SPY")
        if info:
            print("=== SPY ETF Info ===")
            i = info[0]
            print(f"Name: {i.get('name', 'N/A')}")
            print(f"Expense Ratio: {i.get('expenseRatio', 'N/A')}%")
            print(f"AUM: ${i.get('aum', 0):,.0f}")

        # Get top holdings
        holdings = await client.etf_holdings(symbol="SPY")
        print(f"\n=== SPY Top 10 Holdings ===")
        for h in holdings[:10]:
            weight = h.get('weightPercentage', 0)
            print(f"{h['asset']:6} {weight:5.2f}% - {h.get('name', 'N/A')[:30]}")

        # Get sector breakdown
        sectors = await client.etf_sector_weightings(symbol="SPY")
        print(f"\n=== SPY Sector Breakdown ===")
        for s in sectors:
            weight = s.get('weightPercentage', 0)
            print(f"{s['sector']:25} {weight:5.2f}%")

        # Get country exposure for international ETF
        countries = await client.etf_country_weightings(symbol="VEU")
        print(f"\n=== VEU Top Countries ===")
        for c in countries[:10]:
            weight = c.get('weightPercentage', 0)
            print(f"{c['country']:20} {weight:5.2f}%")

        # Find which funds hold AAPL
        apple_holders = await client.funds_disclosure_holders_latest(symbol="AAPL")
        print(f"\n=== Funds Holding AAPL ({len(apple_holders)} funds) ===")
        for h in apple_holders[:5]:
            print(f"{h.get('holder', 'Unknown')}: {h.get('shares', 0):,} shares")

asyncio.run(etf_examples())
```
