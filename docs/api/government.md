# Government API

Access Senate and House trading data.

## Senate Trading

### senate_latest

Get latest Senate trading activity.

```python
trades = await client.senate_latest(page=0, limit=100)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

---

### senate_trades

Get Senate trades for a specific stock symbol.

```python
trades = await client.senate_trades(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### senate_trades_by_name

Get Senate trades by official name.

```python
trades = await client.senate_trades_by_name(name="Nancy Pelosi")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` | Senator name |

## House Trading

### house_latest

Get latest House trading activity.

```python
trades = await client.house_latest(page=0, limit=100)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

---

### house_trades

Get House trades for a specific stock symbol.

```python
trades = await client.house_trades(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### house_trades_by_name

Get House trades by official name.

```python
trades = await client.house_trades_by_name(name="Nancy Pelosi")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` | Representative name |

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def government_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get latest Senate trades
        senate = await client.senate_latest(limit=20)
        print("=== Latest Senate Trades ===")
        for t in senate[:10]:
            action = t.get('type', 'Unknown')
            print(f"{t.get('transactionDate', 'N/A'):12} {t.get('senator', 'Unknown')[:20]:20} {action:10} {t.get('ticker', 'N/A'):6}")

        # Get latest House trades
        house = await client.house_latest(limit=20)
        print("\n=== Latest House Trades ===")
        for t in house[:10]:
            action = t.get('type', 'Unknown')
            print(f"{t.get('transactionDate', 'N/A'):12} {t.get('representative', 'Unknown')[:20]:20} {action:10} {t.get('ticker', 'N/A'):6}")

        # Get trades for a specific stock
        apple_senate = await client.senate_trades(symbol="AAPL")
        print(f"\n=== Senate Trades in AAPL ({len(apple_senate)}) ===")
        for t in apple_senate[:5]:
            print(f"{t.get('transactionDate')}: {t.get('senator', 'Unknown')} - {t.get('type')}")

        apple_house = await client.house_trades(symbol="AAPL")
        print(f"\n=== House Trades in AAPL ({len(apple_house)}) ===")
        for t in apple_house[:5]:
            print(f"{t.get('transactionDate')}: {t.get('representative', 'Unknown')} - {t.get('type')}")

        # Analyze most traded stocks by Congress
        all_senate = await client.senate_latest(limit=500)
        stock_counts = {}
        for t in all_senate:
            ticker = t.get('ticker')
            if ticker:
                stock_counts[ticker] = stock_counts.get(ticker, 0) + 1

        print("\n=== Most Traded Stocks by Senate ===")
        sorted_stocks = sorted(stock_counts.items(), key=lambda x: -x[1])
        for stock, count in sorted_stocks[:10]:
            print(f"{stock:8} {count:3} trades")

asyncio.run(government_examples())
```
