# API Reference Overview

The `AsyncFMPClient` provides access to all Financial Modeling Prep API endpoints through organized method groups.

## Client Class

```python
from fmp_py_client import AsyncFMPClient

async with AsyncFMPClient(api_key="your-key") as client:
    # All API methods available on client
    pass
```

## API Categories

The client methods are organized into the following categories:

### Market Data

| Category | Methods | Description |
|----------|---------|-------------|
| [Quotes](quotes.md) | 16 | Real-time and batch stock quotes |
| [Historical](historical.md) | 10 | Historical prices and chart data |
| [Movers](movers.md) | 3 | Gainers, losers, most active |
| [Market](market.md) | 18 | Stock lists, indexes, constituents |

### Fundamentals

| Category | Methods | Description |
|----------|---------|-------------|
| [Financials](financials.md) | 28 | Income, balance sheet, cash flow statements |
| [Metrics](metrics.md) | 6 | Key metrics, ratios, scores |
| [Valuation](valuation.md) | 5 | DCF and enterprise values |

### Company Information

| Category | Methods | Description |
|----------|---------|-------------|
| [Company](company.md) | 15 | Profiles, executives, screener |
| [Search](search.md) | 6 | Search by symbol, name, CIK, etc. |

### Analysis

| Category | Methods | Description |
|----------|---------|-------------|
| [News](news.md) | 18 | News, analyst estimates, ratings |
| [Technical](technical.md) | 9 | Technical indicators (SMA, EMA, RSI) |
| [Sector](sector.md) | 8 | Sector and industry performance |

### Events & Calendar

| Category | Methods | Description |
|----------|---------|-------------|
| [Calendar](calendar.md) | 12 | Dividends, splits, earnings, IPOs |

### Alternative Data

| Category | Methods | Description |
|----------|---------|-------------|
| [ETF](etf.md) | 9 | ETF holdings and fund data |
| [Insider](insider.md) | 14 | Insider and institutional trading |
| [SEC](sec.md) | 12 | SEC filings and classifications |
| [Economics](economics.md) | 10 | Treasury rates, economic indicators |
| [Government](government.md) | 6 | Senate and House trading |
| [ESG](esg.md) | 6 | ESG ratings and disclosures |
| [Crowdfunding](crowdfunding.md) | 7 | Crowdfunding campaigns |
| [Mergers](mergers.md) | 2 | M&A activity |
| [Bulk](bulk.md) | 12 | Bulk data downloads |

## Common Parameters

Many methods share common parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| `symbol` | `str` | Stock ticker symbol (e.g., "AAPL") |
| `symbols` | `str` | Comma-separated symbols (e.g., "AAPL,GOOGL") |
| `period` | `Period` | Financial period: `"annual"` or `"quarter"` |
| `limit` | `int` | Maximum number of results |
| `page` | `int` | Page number for pagination |
| `from_date` | `str` | Start date (YYYY-MM-DD format) |
| `to_date` | `str` | End date (YYYY-MM-DD format) |

## Return Types

All methods return one of:

- `JSONArray` - `list[dict[str, Any]]` - List of objects
- `JSONObject` - `dict[str, Any]` - Single object

## Error Handling

All methods may raise:

- `FMPAuthenticationError` - Invalid API key (401/403)
- `FMPRateLimitError` - Rate limit exceeded (429)
- `FMPNotFoundError` - Resource not found (404)
- `FMPAPIError` - Other API errors
- `FMPConnectionError` - Network connection issues
- `FMPTimeoutError` - Request timeout

See [Exceptions](../exceptions.md) for details.
