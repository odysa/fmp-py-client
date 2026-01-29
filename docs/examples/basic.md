# Basic Usage Examples

This page demonstrates common use cases for the FMP Client.

## Getting Stock Quotes

### Single Quote

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        quote = await client.quote(symbol="AAPL")
        if quote:
            q = quote[0]
            print(f"Symbol: {q['symbol']}")
            print(f"Price: ${q['price']:.2f}")
            print(f"Change: {q['changesPercentage']:+.2f}%")
            print(f"Volume: {q['volume']:,}")
            print(f"Market Cap: ${q['marketCap']:,.0f}")

asyncio.run(main())
```

### Multiple Quotes

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        # Get multiple quotes in one request
        quotes = await client.batch_quote(symbols="AAPL,GOOGL,MSFT,AMZN")

        print("Symbol      Price       Change      Volume")
        print("-" * 50)
        for q in quotes:
            print(f"{q['symbol']:8} ${q['price']:>10.2f} {q['changesPercentage']:>+8.2f}% {q['volume']:>12,}")

asyncio.run(main())
```

## Searching for Companies

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        # Search by company name
        results = await client.search_name(query="electric vehicle", limit=10)

        print("EV-related companies:")
        for r in results:
            print(f"  {r['symbol']:8} {r['name'][:40]}")

        # Search by ticker pattern
        results = await client.search_symbol(query="TSL", limit=10)

        print("\nSymbols matching 'TSL':")
        for r in results:
            print(f"  {r['symbol']:8} {r['name'][:40]}")

asyncio.run(main())
```

## Getting Company Profiles

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        profile = await client.profile(symbol="AAPL")

        if profile:
            p = profile[0]
            print(f"Company: {p['companyName']}")
            print(f"Industry: {p['industry']}")
            print(f"Sector: {p['sector']}")
            print(f"CEO: {p['ceo']}")
            print(f"Employees: {p['fullTimeEmployees']:,}")
            print(f"Description: {p['description'][:200]}...")

asyncio.run(main())
```

## Working with Financial Statements

```python
import asyncio
from fmp_py_client import AsyncFMPClient, Period

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        symbol = "AAPL"

        # Get annual income statements
        income = await client.income_statement(
            symbol=symbol,
            period=Period.ANNUAL,
            limit=3
        )

        print(f"Income Statements for {symbol}")
        print("-" * 60)
        for stmt in income:
            print(f"\n{stmt['date']}:")
            print(f"  Revenue:      ${stmt['revenue']:>15,.0f}")
            print(f"  Gross Profit: ${stmt['grossProfit']:>15,.0f}")
            print(f"  Net Income:   ${stmt['netIncome']:>15,.0f}")
            print(f"  EPS:          ${stmt['eps']:>15.2f}")

asyncio.run(main())
```

## Historical Price Data

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        # Get daily prices for 2024
        prices = await client.historical_price_eod_full(
            "AAPL",
            from_date="2024-01-01",
            to_date="2024-12-31"
        )

        if prices:
            # Calculate statistics
            closes = [p['close'] for p in prices]
            high = max(closes)
            low = min(closes)
            avg = sum(closes) / len(closes)

            print(f"AAPL 2024 Statistics")
            print(f"  Trading days: {len(prices)}")
            print(f"  High:         ${high:.2f}")
            print(f"  Low:          ${low:.2f}")
            print(f"  Average:      ${avg:.2f}")
            print(f"  YTD Return:   {(prices[0]['close'] - prices[-1]['close']) / prices[-1]['close'] * 100:.1f}%")

asyncio.run(main())
```

## Concurrent Requests

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def main():
    symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "META", "NVDA", "TSLA"]

    async with AsyncFMPClient("your-api-key") as client:
        # Fetch profiles for all symbols concurrently
        tasks = [client.profile(symbol=s) for s in symbols]
        results = await asyncio.gather(*tasks)

        print("Company Profiles")
        print("-" * 70)
        for profile in results:
            if profile:
                p = profile[0]
                print(f"{p['symbol']:6} {p['companyName'][:30]:30} {p['sector']}")

asyncio.run(main())
```

## Error Handling

```python
import asyncio
from fmp_py_client import (
    AsyncFMPClient,
    FMPAuthenticationError,
    FMPRateLimitError,
    FMPNotFoundError,
    FMPAPIError,
)

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        try:
            quote = await client.quote(symbol="INVALID_SYMBOL_12345")
        except FMPAuthenticationError:
            print("Error: Invalid API key")
        except FMPRateLimitError as e:
            print(f"Error: Rate limited. Retry after {e.retry_after}s")
        except FMPNotFoundError:
            print("Error: Symbol not found")
        except FMPAPIError as e:
            print(f"Error: API returned {e.status_code}")

asyncio.run(main())
```

## Using Environment Variables

```python
import asyncio
import os
from fmp_py_client import AsyncFMPClient

async def main():
    api_key = os.environ.get("FMP_API_KEY")
    if not api_key:
        raise ValueError("FMP_API_KEY environment variable required")

    async with AsyncFMPClient(api_key) as client:
        quote = await client.quote(symbol="AAPL")
        print(f"AAPL: ${quote[0]['price']:.2f}")

asyncio.run(main())
```
