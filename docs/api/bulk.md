# Bulk API

Access bulk data downloads for efficient large-scale data retrieval.

## Methods

### profile_bulk

Get bulk company profiles.

```python
profiles = await client.profile_bulk(part=0)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `part` | `int` | Data partition number |

---

### rating_bulk

Get bulk ratings data.

```python
ratings = await client.rating_bulk()
```

---

### dcf_bulk

Get bulk DCF valuations.

```python
dcf = await client.dcf_bulk()
```

---

### scores_bulk

Get bulk financial scores.

```python
scores = await client.scores_bulk()
```

---

### price_target_summary_bulk

Get bulk price target summaries.

```python
targets = await client.price_target_summary_bulk()
```

---

### etf_holder_bulk

Get bulk ETF holder data.

```python
holders = await client.etf_holder_bulk(part=0)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `part` | `int` | Data partition number |

---

### upgrades_downgrades_consensus_bulk

Get bulk upgrades/downgrades consensus.

```python
consensus = await client.upgrades_downgrades_consensus_bulk()
```

---

### key_metrics_ttm_bulk

Get bulk TTM key metrics.

```python
metrics = await client.key_metrics_ttm_bulk()
```

---

### ratios_ttm_bulk

Get bulk TTM ratios.

```python
ratios = await client.ratios_ttm_bulk()
```

---

### peers_bulk

Get bulk peer comparisons.

```python
peers = await client.peers_bulk()
```

---

### earnings_surprises_bulk

Get bulk earnings surprises.

```python
surprises = await client.earnings_surprises_bulk(year=2024)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `year` | `int` | Year for earnings data |

---

### eod_bulk

Get bulk end-of-day data for a specific date.

```python
eod = await client.eod_bulk(date="2024-01-15")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `date` | `str` | Date (YYYY-MM-DD) |

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def bulk_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get bulk DCF valuations for all stocks
        dcf_all = await client.dcf_bulk()
        print(f"=== Bulk DCF Data ({len(dcf_all)} companies) ===")

        # Find undervalued stocks (DCF > price)
        undervalued = []
        for d in dcf_all:
            price = d.get('price', 0)
            dcf = d.get('dcf', 0)
            if price and dcf and dcf > price * 1.2:  # 20% margin
                upside = (dcf - price) / price * 100
                undervalued.append({
                    'symbol': d.get('symbol'),
                    'price': price,
                    'dcf': dcf,
                    'upside': upside
                })

        print(f"\nUndervalued stocks (DCF > 20% above price): {len(undervalued)}")
        undervalued.sort(key=lambda x: -x['upside'])
        for stock in undervalued[:10]:
            print(f"{stock['symbol']:8} Price: ${stock['price']:8.2f} DCF: ${stock['dcf']:8.2f} ({stock['upside']:+.1f}%)")

        # Get bulk financial scores
        scores = await client.scores_bulk()
        print(f"\n=== Bulk Financial Scores ({len(scores)}) ===")

        # Find financially strong companies
        strong = [s for s in scores if s.get('piotroskiScore', 0) >= 8]
        print(f"Strong Piotroski scores (8+): {len(strong)}")
        for s in strong[:10]:
            print(f"{s.get('symbol', 'N/A'):8} Piotroski: {s.get('piotroskiScore')} Altman Z: {s.get('altmanZScore', 0):.2f}")

        # Get bulk TTM metrics
        metrics = await client.key_metrics_ttm_bulk()
        print(f"\n=== Bulk TTM Metrics ({len(metrics)}) ===")

        # Find high ROE companies
        high_roe = [m for m in metrics if m.get('roeTTM', 0) > 0.25]
        high_roe.sort(key=lambda x: -x.get('roeTTM', 0))
        print(f"High ROE companies (>25%): {len(high_roe)}")
        for m in high_roe[:10]:
            print(f"{m.get('symbol', 'N/A'):8} ROE: {m.get('roeTTM', 0) * 100:.1f}%")

        # Get EOD data for specific date
        eod = await client.eod_bulk(date="2024-01-15")
        print(f"\n=== EOD Data for 2024-01-15 ({len(eod)} stocks) ===")

        # Calculate market statistics
        total_volume = sum(e.get('volume', 0) for e in eod)
        avg_change = sum(e.get('changePercent', 0) for e in eod) / len(eod) if eod else 0
        print(f"Total volume: {total_volume:,.0f}")
        print(f"Average change: {avg_change:.2f}%")

asyncio.run(bulk_examples())
```
