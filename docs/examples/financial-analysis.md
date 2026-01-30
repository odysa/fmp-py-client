# Financial Analysis Examples

Advanced examples for financial analysis and research.

## Company Valuation Analysis

```python
import asyncio
from fmp_py_client import AsyncFMPClient, Period

async def analyze_valuation(client: AsyncFMPClient, symbol: str):
    """Comprehensive valuation analysis for a stock."""

    # Fetch all required data
    profile, dcf, metrics, ratios = await asyncio.gather(
        client.profile(symbol=symbol),
        client.discounted_cash_flow(symbol=symbol),
        client.key_metrics_ttm(symbol=symbol),
        client.ratios_ttm(symbol=symbol),
    )

    print(f"\n{'='*60}")
    print(f"VALUATION ANALYSIS: {symbol}")
    print(f"{'='*60}")

    if profile:
        p = profile[0]
        print(f"\nCompany: {p['companyName']}")
        print(f"Sector: {p['sector']}")
        print(f"Industry: {p['industry']}")
        print(f"Current Price: ${p['price']:.2f}")
        print(f"Market Cap: ${p['mktCap']:,.0f}")

    if dcf:
        d = dcf[0]
        price = d.get('price', 0)
        dcf_value = d.get('dcf', 0)
        upside = (dcf_value - price) / price * 100 if price else 0

        print(f"\nDCF Analysis:")
        print(f"  Intrinsic Value: ${dcf_value:.2f}")
        print(f"  Upside/Downside: {upside:+.1f}%")
        if upside > 20:
            print(f"  Signal: UNDERVALUED")
        elif upside < -20:
            print(f"  Signal: OVERVALUED")
        else:
            print(f"  Signal: FAIRLY VALUED")

    if metrics:
        m = metrics[0]
        print(f"\nKey Metrics (TTM):")
        print(f"  P/E Ratio: {m.get('peRatioTTM', 'N/A'):.2f}")
        print(f"  P/B Ratio: {m.get('pbRatioTTM', 'N/A'):.2f}")
        print(f"  P/S Ratio: {m.get('priceToSalesRatioTTM', 'N/A'):.2f}")
        print(f"  EV/EBITDA: {m.get('enterpriseValueOverEBITDATTM', 'N/A'):.2f}")

    if ratios:
        r = ratios[0]
        print(f"\nProfitability (TTM):")
        print(f"  Gross Margin: {r.get('grossProfitMarginTTM', 0) * 100:.1f}%")
        print(f"  Operating Margin: {r.get('operatingProfitMarginTTM', 0) * 100:.1f}%")
        print(f"  Net Margin: {r.get('netProfitMarginTTM', 0) * 100:.1f}%")
        print(f"  ROE: {r.get('returnOnEquityTTM', 0) * 100:.1f}%")
        print(f"  ROA: {r.get('returnOnAssetsTTM', 0) * 100:.1f}%")

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        await analyze_valuation(client, "AAPL")
        await analyze_valuation(client, "MSFT")

asyncio.run(main())
```

## Financial Health Assessment

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def assess_financial_health(client: AsyncFMPClient, symbol: str):
    """Assess company financial health using multiple metrics."""

    scores, ratios, balance = await asyncio.gather(
        client.financial_scores(symbol=symbol),
        client.ratios_ttm(symbol=symbol),
        client.balance_sheet_statement(symbol=symbol, limit=1),
    )

    print(f"\n{'='*60}")
    print(f"FINANCIAL HEALTH: {symbol}")
    print(f"{'='*60}")

    if scores:
        s = scores[0]
        piotroski = s.get('piotroskiScore', 0)
        altman = s.get('altmanZScore', 0)

        print(f"\nFinancial Scores:")
        print(f"  Piotroski F-Score: {piotroski}/9", end=" ")
        if piotroski >= 8:
            print("(STRONG)")
        elif piotroski <= 2:
            print("(WEAK)")
        else:
            print("(MODERATE)")

        print(f"  Altman Z-Score: {altman:.2f}", end=" ")
        if altman > 2.99:
            print("(SAFE ZONE)")
        elif altman < 1.81:
            print("(DISTRESS ZONE)")
        else:
            print("(GREY ZONE)")

    if ratios:
        r = ratios[0]
        print(f"\nLiquidity Ratios:")
        current = r.get('currentRatioTTM', 0)
        quick = r.get('quickRatioTTM', 0)
        print(f"  Current Ratio: {current:.2f}", end=" ")
        print("(GOOD)" if current > 1.5 else "(CONCERN)" if current < 1 else "(OK)")
        print(f"  Quick Ratio: {quick:.2f}", end=" ")
        print("(GOOD)" if quick > 1 else "(CONCERN)")

        print(f"\nLeverage Ratios:")
        de = r.get('debtEquityRatioTTM', 0)
        print(f"  Debt/Equity: {de:.2f}", end=" ")
        print("(LOW)" if de < 0.5 else "(HIGH)" if de > 2 else "(MODERATE)")

    if balance:
        b = balance[0]
        cash = b.get('cashAndCashEquivalents', 0)
        debt = b.get('totalDebt', 0)
        net_debt = debt - cash

        print(f"\nBalance Sheet Highlights:")
        print(f"  Cash: ${cash:,.0f}")
        print(f"  Total Debt: ${debt:,.0f}")
        print(f"  Net Debt: ${net_debt:,.0f}")

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        await assess_financial_health(client, "AAPL")

asyncio.run(main())
```

## Growth Analysis

```python
import asyncio
from fmp_py_client import AsyncFMPClient, Period

async def analyze_growth(client: AsyncFMPClient, symbol: str, years: int = 5):
    """Analyze revenue and earnings growth trends."""

    income = await client.income_statement(
        symbol=symbol,
        period=Period.ANNUAL,
        limit=years + 1
    )

    if not income or len(income) < 2:
        print(f"Insufficient data for {symbol}")
        return

    print(f"\n{'='*60}")
    print(f"GROWTH ANALYSIS: {symbol} ({years} Years)")
    print(f"{'='*60}")

    # Calculate YoY growth rates
    print(f"\n{'Year':<12} {'Revenue':>15} {'YoY %':>10} {'Net Income':>15} {'YoY %':>10}")
    print("-" * 62)

    revenue_growth = []
    earnings_growth = []

    for i, stmt in enumerate(income[:-1]):
        prev = income[i + 1]

        rev = stmt['revenue']
        prev_rev = prev['revenue']
        rev_growth = (rev - prev_rev) / prev_rev * 100 if prev_rev else 0

        ni = stmt['netIncome']
        prev_ni = prev['netIncome']
        ni_growth = (ni - prev_ni) / abs(prev_ni) * 100 if prev_ni else 0

        revenue_growth.append(rev_growth)
        earnings_growth.append(ni_growth)

        print(f"{stmt['date']:<12} ${rev:>14,.0f} {rev_growth:>+9.1f}% ${ni:>14,.0f} {ni_growth:>+9.1f}%")

    # Calculate CAGR
    if len(income) >= 2:
        first_rev = income[-1]['revenue']
        last_rev = income[0]['revenue']
        cagr = ((last_rev / first_rev) ** (1 / years) - 1) * 100 if first_rev > 0 else 0

        print(f"\nSummary:")
        print(f"  Revenue CAGR: {cagr:.1f}%")
        print(f"  Avg Revenue Growth: {sum(revenue_growth) / len(revenue_growth):.1f}%")
        print(f"  Avg Earnings Growth: {sum(earnings_growth) / len(earnings_growth):.1f}%")

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        await analyze_growth(client, "AAPL", years=5)
        await analyze_growth(client, "NVDA", years=5)

asyncio.run(main())
```

## Peer Comparison

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def compare_peers(client: AsyncFMPClient, symbol: str):
    """Compare a stock with its peers."""

    # Get peers
    peers_data = await client.stock_peers(symbol=symbol)
    if not peers_data:
        print(f"No peers found for {symbol}")
        return

    peers = [symbol] + peers_data[0].get('peersList', [])[:5]

    # Fetch metrics for all peers
    tasks = [client.key_metrics_ttm(symbol=s) for s in peers]
    results = await asyncio.gather(*tasks)

    print(f"\n{'='*80}")
    print(f"PEER COMPARISON: {symbol}")
    print(f"{'='*80}")

    print(f"\n{'Symbol':<8} {'P/E':>10} {'P/B':>10} {'ROE':>10} {'Margin':>10} {'D/E':>10}")
    print("-" * 68)

    for peer, metrics in zip(peers, results):
        if metrics:
            m = metrics[0]
            pe = m.get('peRatioTTM', 0)
            pb = m.get('pbRatioTTM', 0)
            roe = m.get('roeTTM', 0) * 100
            margin = m.get('netProfitMarginTTM', 0) * 100
            de = m.get('debtToEquityTTM', 0)

            marker = " *" if peer == symbol else ""
            print(f"{peer:<8} {pe:>10.2f} {pb:>10.2f} {roe:>9.1f}% {margin:>9.1f}% {de:>10.2f}{marker}")

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        await compare_peers(client, "AAPL")

asyncio.run(main())
```

## Dividend Analysis

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def analyze_dividends(client: AsyncFMPClient, symbol: str):
    """Analyze dividend history and yield."""

    profile, dividends = await asyncio.gather(
        client.profile(symbol=symbol),
        client.dividends(symbol=symbol),
    )

    print(f"\n{'='*60}")
    print(f"DIVIDEND ANALYSIS: {symbol}")
    print(f"{'='*60}")

    if profile:
        p = profile[0]
        div_yield = p.get('lastDiv', 0) / p.get('price', 1) * 100 * 4  # Annualized
        print(f"\nCurrent:")
        print(f"  Price: ${p.get('price', 0):.2f}")
        print(f"  Last Dividend: ${p.get('lastDiv', 0):.4f}")
        print(f"  Yield (Est.): {div_yield:.2f}%")

    if dividends:
        print(f"\nDividend History (Last 10):")
        print(f"{'Date':<12} {'Amount':>10} {'Yield':>10}")
        print("-" * 32)

        for d in dividends[:10]:
            print(f"{d['date']:<12} ${d['dividend']:>9.4f}")

        # Calculate dividend growth
        if len(dividends) >= 5:
            recent = sum(d['dividend'] for d in dividends[:4])
            older = sum(d['dividend'] for d in dividends[4:8])
            growth = (recent - older) / older * 100 if older else 0
            print(f"\n  YoY Dividend Growth: {growth:+.1f}%")

async def main():
    async with AsyncFMPClient("your-api-key") as client:
        await analyze_dividends(client, "AAPL")

asyncio.run(main())
```
