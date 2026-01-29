# Portfolio Tracking Examples

Examples for building portfolio tracking and monitoring applications.

## Portfolio Value Tracker

```python
import asyncio
from dataclasses import dataclass
from fmp_py_client import AsyncFMPClient

@dataclass
class Position:
    symbol: str
    shares: float
    cost_basis: float

async def track_portfolio(client: AsyncFMPClient, positions: list[Position]):
    """Track portfolio value and performance."""

    symbols = ",".join(p.symbol for p in positions)
    quotes = await client.batch_quote(symbols=symbols)

    quote_map = {q['symbol']: q for q in quotes}

    print(f"\n{'='*80}")
    print("PORTFOLIO SUMMARY")
    print(f"{'='*80}")

    print(f"\n{'Symbol':<8} {'Shares':>10} {'Price':>10} {'Value':>12} {'Cost':>12} {'P/L':>12} {'%':>8}")
    print("-" * 82)

    total_value = 0
    total_cost = 0
    total_pl = 0

    for pos in positions:
        q = quote_map.get(pos.symbol)
        if not q:
            continue

        price = q['price']
        value = pos.shares * price
        cost = pos.shares * pos.cost_basis
        pl = value - cost
        pl_pct = pl / cost * 100 if cost else 0

        total_value += value
        total_cost += cost
        total_pl += pl

        print(f"{pos.symbol:<8} {pos.shares:>10.2f} ${price:>9.2f} ${value:>11,.2f} ${cost:>11,.2f} ${pl:>+11,.2f} {pl_pct:>+7.1f}%")

    total_pl_pct = total_pl / total_cost * 100 if total_cost else 0

    print("-" * 82)
    print(f"{'TOTAL':<8} {'':<10} {'':<10} ${total_value:>11,.2f} ${total_cost:>11,.2f} ${total_pl:>+11,.2f} {total_pl_pct:>+7.1f}%")

async def main():
    portfolio = [
        Position("AAPL", 100, 150.00),
        Position("GOOGL", 50, 120.00),
        Position("MSFT", 75, 300.00),
        Position("AMZN", 30, 130.00),
        Position("NVDA", 25, 450.00),
    ]

    async with AsyncFMPClient("your-api-key") as client:
        await track_portfolio(client, portfolio)

asyncio.run(main())
```

## Portfolio Diversification Analysis

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def analyze_diversification(client: AsyncFMPClient, symbols: list[str], weights: list[float]):
    """Analyze portfolio diversification by sector and industry."""

    tasks = [client.profile(symbol=s) for s in symbols]
    profiles = await asyncio.gather(*tasks)

    print(f"\n{'='*60}")
    print("DIVERSIFICATION ANALYSIS")
    print(f"{'='*60}")

    # Group by sector
    sectors = {}
    industries = {}

    for symbol, weight, profile in zip(symbols, weights, profiles):
        if profile:
            p = profile[0]
            sector = p.get('sector', 'Unknown')
            industry = p.get('industry', 'Unknown')

            sectors[sector] = sectors.get(sector, 0) + weight
            industries[industry] = industries.get(industry, 0) + weight

    print(f"\nSector Allocation:")
    for sector, weight in sorted(sectors.items(), key=lambda x: -x[1]):
        bar = "#" * int(weight * 50)
        print(f"  {sector:25} {weight:5.1%} {bar}")

    print(f"\nTop Industries:")
    for industry, weight in sorted(industries.items(), key=lambda x: -x[1])[:5]:
        print(f"  {industry:30} {weight:5.1%}")

    # Concentration warnings
    print(f"\nConcentration Analysis:")
    max_sector = max(sectors.values())
    if max_sector > 0.4:
        print(f"  WARNING: High sector concentration ({max_sector:.0%})")
    else:
        print(f"  OK: Sector concentration within limits")

    top_position = max(weights)
    if top_position > 0.25:
        print(f"  WARNING: Large single position ({top_position:.0%})")
    else:
        print(f"  OK: Position sizes within limits")

async def main():
    symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "NVDA", "JPM", "JNJ", "PG"]
    weights = [0.15, 0.15, 0.15, 0.10, 0.15, 0.10, 0.10, 0.10]

    async with AsyncFMPClient("your-api-key") as client:
        await analyze_diversification(client, symbols, weights)

asyncio.run(main())
```

## Watchlist Monitor

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def monitor_watchlist(client: AsyncFMPClient, symbols: list[str]):
    """Monitor a watchlist with key metrics and alerts."""

    # Fetch quotes and metrics concurrently
    quote_task = client.batch_quote(symbols=",".join(symbols))
    metric_tasks = [client.key_metrics_ttm(symbol=s) for s in symbols]

    quotes, *metrics = await asyncio.gather(quote_task, *metric_tasks)

    quote_map = {q['symbol']: q for q in quotes}

    print(f"\n{'='*100}")
    print("WATCHLIST MONITOR")
    print(f"{'='*100}")

    print(f"\n{'Symbol':<8} {'Price':>10} {'Change':>10} {'Volume':>12} {'P/E':>8} {'RSI':>8} {'Alerts'}")
    print("-" * 100)

    for symbol, metric_data in zip(symbols, metrics):
        q = quote_map.get(symbol, {})
        m = metric_data[0] if metric_data else {}

        price = q.get('price', 0)
        change = q.get('changesPercentage', 0)
        volume = q.get('volume', 0)
        avg_volume = q.get('avgVolume', 1)
        pe = m.get('peRatioTTM', 0)

        # Generate alerts
        alerts = []
        if abs(change) > 5:
            alerts.append(f"BIG MOVE {change:+.1f}%")
        if volume > avg_volume * 2:
            alerts.append("HIGH VOLUME")
        if pe and pe < 15:
            alerts.append("LOW P/E")
        if pe and pe > 50:
            alerts.append("HIGH P/E")

        alert_str = ", ".join(alerts) if alerts else "-"
        print(f"{symbol:<8} ${price:>9.2f} {change:>+9.2f}% {volume:>11,} {pe:>8.1f} {'-':>8} {alert_str}")

async def main():
    watchlist = ["AAPL", "GOOGL", "MSFT", "AMZN", "NVDA", "TSLA", "META", "AMD"]

    async with AsyncFMPClient("your-api-key") as client:
        await monitor_watchlist(client, watchlist)

asyncio.run(main())
```

## Daily Market Summary

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def market_summary(client: AsyncFMPClient):
    """Generate daily market summary."""

    # Fetch market data concurrently
    gainers, losers, actives, sectors, indexes = await asyncio.gather(
        client.biggest_gainers(),
        client.biggest_losers(),
        client.most_actives(),
        client.sector_performance_snapshot(),
        client.batch_index_quotes(),
    )

    print(f"\n{'='*70}")
    print("DAILY MARKET SUMMARY")
    print(f"{'='*70}")

    # Major indexes
    print(f"\nMAJOR INDEXES:")
    target_indexes = ["^GSPC", "^DJI", "^IXIC", "^RUT"]
    index_map = {i['symbol']: i for i in indexes}
    for idx in target_indexes:
        if idx in index_map:
            i = index_map[idx]
            print(f"  {i.get('name', idx)[:20]:20} {i.get('price', 0):>12,.2f} {i.get('changesPercentage', 0):>+8.2f}%")

    # Sector performance
    print(f"\nSECTOR PERFORMANCE:")
    for s in sorted(sectors, key=lambda x: x.get('changesPercentage', 0), reverse=True)[:5]:
        change = s.get('changesPercentage', 0)
        bar = "+" * int(abs(change) * 5) if change > 0 else "-" * int(abs(change) * 5)
        print(f"  {s['sector']:25} {change:>+6.2f}% {bar}")

    # Top gainers
    print(f"\nTOP GAINERS:")
    for g in gainers[:5]:
        print(f"  {g['symbol']:8} ${g['price']:>8.2f} {g['changesPercentage']:>+8.2f}%")

    # Top losers
    print(f"\nTOP LOSERS:")
    for l in losers[:5]:
        print(f"  {l['symbol']:8} ${l['price']:>8.2f} {l['changesPercentage']:>+8.2f}%")

    # Most active
    print(f"\nMOST ACTIVE:")
    for a in actives[:5]:
        print(f"  {a['symbol']:8} ${a['price']:>8.2f} Vol: {a.get('volume', 0):>15,}")

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        await market_summary(client)

asyncio.run(main())
```

## Earnings Calendar Tracker

```python
import asyncio
from datetime import datetime, timedelta
from fmp_py_client import AsyncFMPClient

async def earnings_calendar(client: AsyncFMPClient, symbols: list[str]):
    """Track upcoming earnings for portfolio holdings."""

    calendar = await client.earnings_calendar()

    # Filter for our symbols
    symbol_set = set(symbols)
    relevant = [e for e in calendar if e.get('symbol') in symbol_set]

    print(f"\n{'='*70}")
    print("UPCOMING EARNINGS FOR PORTFOLIO")
    print(f"{'='*70}")

    if not relevant:
        print("\nNo upcoming earnings in the next period")
        return

    print(f"\n{'Date':<12} {'Symbol':<8} {'Time':>10} {'EPS Est':>10} {'Revenue Est':>15}")
    print("-" * 65)

    for e in sorted(relevant, key=lambda x: x.get('date', ''))[:20]:
        date = e.get('date', 'N/A')
        symbol = e.get('symbol', 'N/A')
        time = e.get('time', 'N/A')
        eps_est = e.get('epsEstimated', 'N/A')
        rev_est = e.get('revenueEstimated', 0)

        eps_str = f"${eps_est:.2f}" if isinstance(eps_est, (int, float)) else eps_est
        rev_str = f"${rev_est/1e9:.1f}B" if rev_est else "N/A"

        print(f"{date:<12} {symbol:<8} {time:>10} {eps_str:>10} {rev_str:>15}")

async def main():
    portfolio = ["AAPL", "GOOGL", "MSFT", "AMZN", "NVDA", "META", "TSLA", "AMD"]

    async with AsyncFMPClient("your-api-key") as client:
        await earnings_calendar(client, portfolio)

asyncio.run(main())
```
