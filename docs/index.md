# FMP Client

A fully async Python client for the [Financial Modeling Prep (FMP) API](https://financialmodelingprep.com/).

## Features

- **Fully Async**: Built with `httpx` for high-performance async HTTP requests
- **Type-Safe**: Full type hints and PEP 561 compliance for IDE support
- **Comprehensive**: 180+ API methods covering all FMP endpoints
- **Clean API**: Intuitive method names and parameter handling
- **Error Handling**: Specific exception classes for different error types
- **Context Manager**: Proper resource cleanup with async context manager support

## Quick Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        # Get a stock quote
        quote = await client.quote(symbol="AAPL")
        print(quote)

        # Get income statements
        income = await client.income_statement(symbol="AAPL", period="annual", limit=5)
        print(income)

        # Search for companies
        results = await client.search_name(query="Tesla", limit=10)
        print(results)

asyncio.run(main())
```

## Installation

```bash
pip install fmp-py-client
```

Or with `uv`:

```bash
uv add fmp-py-client
```

## Requirements

- Python 3.12+
- An API key from [Financial Modeling Prep](https://financialmodelingprep.com/developer/docs/)

## API Coverage

The client covers all major FMP API categories:

| Category | Description |
|----------|-------------|
| [Search](api/search.md) | Search by symbol, name, CIK, CUSIP, ISIN |
| [Company](api/company.md) | Company profiles, executives, screener |
| [Financials](api/financials.md) | Income statements, balance sheets, cash flow |
| [Metrics](api/metrics.md) | Key metrics, ratios, financial scores |
| [Quotes](api/quotes.md) | Real-time and batch quotes |
| [Historical](api/historical.md) | Historical prices and charts |
| [Calendar](api/calendar.md) | Dividends, splits, earnings, IPOs |
| [Market](api/market.md) | Stock lists, indexes, constituents |
| [News](api/news.md) | News, analyst estimates, ratings |
| [Sector](api/sector.md) | Sector and industry performance |
| [Movers](api/movers.md) | Gainers, losers, most active |
| [Valuation](api/valuation.md) | DCF and enterprise values |
| [Technical](api/technical.md) | Technical indicators (SMA, EMA, RSI, etc.) |
| [ETF](api/etf.md) | ETF holdings and fund data |
| [Insider](api/insider.md) | Insider and institutional trading |
| [SEC](api/sec.md) | SEC filings and classifications |
| [Economics](api/economics.md) | Treasury rates, economic indicators |
| [Government](api/government.md) | Senate and House trading |
| [ESG](api/esg.md) | ESG ratings and disclosures |
| [Crowdfunding](api/crowdfunding.md) | Crowdfunding and fundraising |
| [Mergers](api/mergers.md) | M&A activity |
| [Bulk](api/bulk.md) | Bulk data downloads |

## License

MIT License
