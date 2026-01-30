# News API

Access news, press releases, analyst estimates, and ratings.

## FMP Articles

### fmp_articles

Get FMP articles.

```python
articles = await client.fmp_articles(page=0, limit=20)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

## Latest News

### news_general_latest

Get latest general news.

```python
news = await client.news_general_latest(page=0, limit=20)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

---

### news_stock_latest

Get latest stock news.

```python
news = await client.news_stock_latest(page=0, limit=20)
```

---

### news_crypto_latest

Get latest crypto news.

```python
news = await client.news_crypto_latest(page=0, limit=20)
```

---

### news_forex_latest

Get latest forex news.

```python
news = await client.news_forex_latest(page=0, limit=20)
```

---

### news_press_releases_latest

Get latest press releases.

```python
releases = await client.news_press_releases_latest(page=0, limit=20)
```

## Symbol-Specific News

### news_stock

Get stock news for specific symbols.

```python
news = await client.news_stock(symbols="AAPL,GOOGL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbols` | `str` | Comma-separated symbols |

---

### news_crypto

Get crypto news for specific symbols.

```python
news = await client.news_crypto(symbols="BTCUSD")
```

---

### news_forex

Get forex news for specific pairs.

```python
news = await client.news_forex(symbols="EURUSD")
```

---

### news_press_releases

Get press releases for a symbol.

```python
releases = await client.news_press_releases(symbols="AAPL")
```

## Analyst Estimates

### analyst_estimates

Get analyst estimates.

```python
estimates = await client.analyst_estimates(
    symbol="AAPL",
    period="annual",
    page=0,
    limit=10
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |
| `period` | `str` | `"annual"` or `"quarter"` |
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

## Ratings

### ratings_snapshot

Get ratings snapshot.

```python
ratings = await client.ratings_snapshot(symbol="AAPL")
```

---

### ratings_historical

Get historical ratings.

```python
ratings = await client.ratings_historical(symbol="AAPL")
```

## Price Targets

### price_target_summary

Get price target summary.

```python
summary = await client.price_target_summary(symbol="AAPL")
```

---

### price_target_consensus

Get price target consensus.

```python
consensus = await client.price_target_consensus(symbol="AAPL")
```

## Analyst Grades

### grades

Get analyst grades.

```python
grades = await client.grades(symbol="AAPL")
```

---

### grades_historical

Get historical analyst grades.

```python
grades = await client.grades_historical(symbol="AAPL")
```

---

### grades_consensus

Get analyst grades consensus.

```python
consensus = await client.grades_consensus(symbol="AAPL")
```

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def news_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get latest stock news
        news = await client.news_stock_latest(limit=10)
        print("=== Latest Stock News ===")
        for article in news[:5]:
            print(f"- {article['title'][:60]}...")
            print(f"  Source: {article.get('site', 'Unknown')}")
            print()

        # Get news for specific stocks
        apple_news = await client.news_stock(symbols="AAPL")
        print(f"=== Apple News ({len(apple_news)} articles) ===")
        for article in apple_news[:3]:
            print(f"- {article['title'][:60]}...")

        # Get analyst estimates
        estimates = await client.analyst_estimates(symbol="AAPL", period="annual")
        print(f"\n=== AAPL Analyst Estimates ===")
        if estimates:
            e = estimates[0]
            print(f"Date: {e.get('date')}")
            print(f"Revenue Est: ${e.get('estimatedRevenueAvg', 0):,.0f}")
            print(f"EPS Est: ${e.get('estimatedEpsAvg', 0):.2f}")

        # Get price target consensus
        target = await client.price_target_consensus(symbol="AAPL")
        print(f"\n=== AAPL Price Target Consensus ===")
        if target:
            t = target[0]
            print(f"Target High: ${t.get('targetHigh', 0):.2f}")
            print(f"Target Low: ${t.get('targetLow', 0):.2f}")
            print(f"Target Median: ${t.get('targetMedian', 0):.2f}")
            print(f"Target Consensus: ${t.get('targetConsensus', 0):.2f}")

        # Get analyst grades
        grades = await client.grades_consensus(symbol="AAPL")
        print(f"\n=== AAPL Analyst Grades ===")
        if grades:
            g = grades[0]
            print(f"Strong Buy: {g.get('strongBuy', 0)}")
            print(f"Buy: {g.get('buy', 0)}")
            print(f"Hold: {g.get('hold', 0)}")
            print(f"Sell: {g.get('sell', 0)}")
            print(f"Strong Sell: {g.get('strongSell', 0)}")

asyncio.run(news_examples())
```
