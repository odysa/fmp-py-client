# Market API

Access stock lists, indexes, and market constituents.

## Stock Lists

### stock_list

Get list of all stock symbols.

```python
stocks = await client.stock_list()
```

---

### financial_statement_symbol_list

Get list of symbols with financial statements available.

```python
symbols = await client.financial_statement_symbol_list()
```

---

### actively_trading_list

Get list of actively trading symbols.

```python
active = await client.actively_trading_list()
```

---

### etf_list

Get list of ETF symbols.

```python
etfs = await client.etf_list()
```

---

### delisted_companies

Get list of delisted companies.

```python
delisted = await client.delisted_companies(page=0, limit=100)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

## CIK and Symbol Changes

### cik_list

Get list of CIK numbers.

```python
ciks = await client.cik_list(page=0, limit=100)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

---

### symbol_change

Get list of symbol changes.

```python
changes = await client.symbol_change()
```

## Available Options

### available_exchanges

Get list of available exchanges.

```python
exchanges = await client.available_exchanges()
```

---

### available_sectors

Get list of available sectors.

```python
sectors = await client.available_sectors()
```

---

### available_industries

Get list of available industries.

```python
industries = await client.available_industries()
```

---

### available_countries

Get list of available countries.

```python
countries = await client.available_countries()
```

## Index Information

### index_list

Get list of market indexes.

```python
indexes = await client.index_list()
```

---

### sp500_constituent

Get S&P 500 constituents.

```python
sp500 = await client.sp500_constituent()
```

---

### nasdaq_constituent

Get Nasdaq constituents.

```python
nasdaq = await client.nasdaq_constituent()
```

---

### dowjones_constituent

Get Dow Jones constituents.

```python
dow = await client.dowjones_constituent()
```

## Historical Constituents

### historical_sp500_constituent

Get historical S&P 500 constituents (additions/removals).

```python
history = await client.historical_sp500_constituent()
```

---

### historical_nasdaq_constituent

Get historical Nasdaq constituents.

```python
history = await client.historical_nasdaq_constituent()
```

---

### historical_dowjones_constituent

Get historical Dow Jones constituents.

```python
history = await client.historical_dowjones_constituent()
```

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def market_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get all available exchanges
        exchanges = await client.available_exchanges()
        print(f"=== Available Exchanges ({len(exchanges)}) ===")
        for ex in exchanges[:10]:
            print(f"  {ex}")

        # Get all sectors
        sectors = await client.available_sectors()
        print(f"\n=== Available Sectors ({len(sectors)}) ===")
        for s in sectors:
            print(f"  {s}")

        # Get S&P 500 constituents
        sp500 = await client.sp500_constituent()
        print(f"\n=== S&P 500 Constituents ({len(sp500)}) ===")

        # Group by sector
        sectors = {}
        for stock in sp500:
            sector = stock.get('sector', 'Unknown')
            sectors[sector] = sectors.get(sector, 0) + 1

        for sector, count in sorted(sectors.items(), key=lambda x: -x[1]):
            print(f"  {sector}: {count} companies")

        # Get Dow Jones constituents
        dow = await client.dowjones_constituent()
        print(f"\n=== Dow Jones 30 ===")
        for stock in dow:
            print(f"  {stock['symbol']}: {stock['name']}")

        # Get recent symbol changes
        changes = await client.symbol_change()
        print(f"\n=== Recent Symbol Changes ({len(changes)}) ===")
        for c in changes[:5]:
            print(f"  {c.get('oldSymbol')} -> {c.get('newSymbol')}: {c.get('date')}")

asyncio.run(market_examples())
```
