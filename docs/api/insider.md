# Insider API

Access insider trading and institutional ownership data.

## Insider Trading

### insider_trading_latest

Get latest insider trades.

```python
trades = await client.insider_trading_latest(page=0, limit=100)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

---

### insider_trading_search

Search insider trades.

```python
trades = await client.insider_trading_search(page=0, limit=100)
```

---

### insider_trading_reporting_name

Get insider trades by reporting name.

```python
trades = await client.insider_trading_reporting_name(name="Tim Cook")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` | Insider name |

---

### insider_trading_transaction_type

Get list of insider trading transaction types.

```python
types = await client.insider_trading_transaction_type()
```

---

### insider_trading_statistics

Get insider trading statistics for a symbol.

```python
stats = await client.insider_trading_statistics(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### acquisition_of_beneficial_ownership

Get acquisition of beneficial ownership data.

```python
ownership = await client.acquisition_of_beneficial_ownership(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

## Institutional Ownership

### institutional_ownership_latest

Get latest institutional ownership data.

```python
ownership = await client.institutional_ownership_latest(page=0, limit=100)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

---

### institutional_ownership_extract

Get institutional ownership extract.

```python
ownership = await client.institutional_ownership_extract(
    cik=102909,
    year=2024,
    quarter=1
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `cik` | `int` | Institution CIK number |
| `year` | `int` | Year |
| `quarter` | `int` | Quarter (1-4) |

---

### institutional_ownership_dates

Get institutional ownership data dates.

```python
dates = await client.institutional_ownership_dates(cik=102909)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `cik` | `int` | Institution CIK number |

---

### institutional_ownership_holder_analytics

Get institutional holder analytics.

```python
analytics = await client.institutional_ownership_holder_analytics(
    symbol="AAPL",
    year=2024,
    quarter=1,
    page=0,
    limit=100
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |
| `year` | `int` | Year |
| `quarter` | `int` | Quarter (1-4) |
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

---

### institutional_ownership_holder_performance_summary

Get institutional holder performance summary.

```python
summary = await client.institutional_ownership_holder_performance_summary(
    cik=102909,
    page=0
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `cik` | `int` | Institution CIK number |
| `page` | `int` | Page number |

---

### institutional_ownership_holder_industry_breakdown

Get institutional holder industry breakdown.

```python
breakdown = await client.institutional_ownership_holder_industry_breakdown(
    cik=102909,
    year=2024,
    quarter=1
)
```

---

### institutional_ownership_symbol_positions_summary

Get institutional symbol positions summary.

```python
summary = await client.institutional_ownership_symbol_positions_summary(
    symbol="AAPL",
    year=2024,
    quarter=1
)
```

---

### institutional_ownership_industry_summary

Get institutional ownership industry summary.

```python
summary = await client.institutional_ownership_industry_summary(
    year=2024,
    quarter=1
)
```

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def insider_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get latest insider trades
        trades = await client.insider_trading_latest(limit=20)
        print("=== Latest Insider Trades ===")
        for t in trades[:10]:
            action = "BUY" if t.get('acquistionOrDisposition') == 'A' else "SELL"
            print(f"{t['symbol']:6} {action:4} {t.get('securitiesTransacted', 0):>10,} shares by {t.get('reportingName', 'Unknown')[:20]}")

        # Get insider trading stats for Apple
        stats = await client.insider_trading_statistics(symbol="AAPL")
        if stats:
            s = stats[0]
            print(f"\n=== AAPL Insider Trading Stats ===")
            print(f"Total Buys: {s.get('totalBought', 0):,}")
            print(f"Total Sells: {s.get('totalSold', 0):,}")

        # Get institutional ownership for Apple
        analytics = await client.institutional_ownership_holder_analytics(
            symbol="AAPL",
            year=2024,
            quarter=1,
            limit=10
        )
        print(f"\n=== AAPL Top Institutional Holders ===")
        for a in analytics[:10]:
            print(f"{a.get('investorName', 'Unknown')[:30]:30} {a.get('shares', 0):>15,} shares")

        # Get industry summary
        industry = await client.institutional_ownership_industry_summary(
            year=2024,
            quarter=1
        )
        print(f"\n=== Institutional Ownership by Industry ===")
        for i in industry[:10]:
            print(f"{i.get('industry', 'Unknown')[:25]:25} {i.get('totalInvestment', 0):>15,.0f}")

asyncio.run(insider_examples())
```
