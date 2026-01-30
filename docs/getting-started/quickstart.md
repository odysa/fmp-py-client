# Quick Start

This guide will help you get started with the FMP Client in just a few minutes.

## Basic Usage

The recommended way to use the client is with an async context manager:

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        # Your API calls here
        quote = await client.quote(symbol="AAPL")
        print(quote)

asyncio.run(main())
```

## Get Stock Quotes

```python
async with AsyncFMPClient(api_key) as client:
    # Single stock quote
    quote = await client.quote(symbol="AAPL")

    # Multiple stocks at once
    quotes = await client.batch_quote(symbols="AAPL,GOOGL,MSFT")

    # Short-form quote (less data, faster)
    short_quote = await client.quote_short(symbol="AAPL")
```

## Search for Companies

```python
async with AsyncFMPClient(api_key) as client:
    # Search by company name
    results = await client.search_name(query="Apple", limit=10)

    # Search by ticker symbol
    results = await client.search_symbol(query="AAP", limit=10)

    # Search by CIK number
    results = await client.search_cik(cik=320193)
```

## Get Financial Statements

```python
from fmp_py_client import AsyncFMPClient, Period

async with AsyncFMPClient(api_key) as client:
    # Annual income statements
    income = await client.income_statement(
        symbol="AAPL",
        period=Period.ANNUAL,
        limit=5
    )

    # Quarterly balance sheet
    balance = await client.balance_sheet_statement(
        symbol="AAPL",
        period=Period.QUARTER,
        limit=4
    )

    # Cash flow statement
    cash_flow = await client.cash_flow_statement(
        symbol="AAPL",
        period=Period.ANNUAL,
        limit=5
    )
```

## Get Historical Prices

```python
async with AsyncFMPClient(api_key) as client:
    # End-of-day prices
    prices = await client.historical_price_eod_full(
        "AAPL",
        from_date="2024-01-01",
        to_date="2024-12-31"
    )

    # Intraday charts (1-minute intervals)
    intraday = await client.historical_chart_1min(
        "AAPL",
        from_date="2024-01-15",
        to_date="2024-01-15"
    )
```

## Get Company Information

```python
async with AsyncFMPClient(api_key) as client:
    # Company profile
    profile = await client.profile(symbol="AAPL")

    # Key executives
    executives = await client.key_executives(symbol="AAPL")

    # Stock peers
    peers = await client.stock_peers(symbol="AAPL")
```

## Error Handling

```python
from fmp_py_client import (
    AsyncFMPClient,
    FMPAuthenticationError,
    FMPRateLimitError,
    FMPNotFoundError,
    FMPAPIError,
)

async with AsyncFMPClient(api_key) as client:
    try:
        quote = await client.quote(symbol="AAPL")
    except FMPAuthenticationError:
        print("Invalid API key")
    except FMPRateLimitError as e:
        print(f"Rate limited. Retry after: {e.retry_after} seconds")
    except FMPNotFoundError:
        print("Symbol not found")
    except FMPAPIError as e:
        print(f"API error {e.status_code}: {e.message}")
```

## Next Steps

- Read the [Configuration](configuration.md) guide for advanced options
- Explore the [API Reference](../api/overview.md) for all available methods
- Check out the [Examples](../examples/basic.md) for more use cases
