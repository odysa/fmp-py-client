# Sector API

Access sector and industry performance data.

## Performance Snapshots

### sector_performance_snapshot

Get sector performance snapshot.

```python
performance = await client.sector_performance_snapshot(date="2024-01-15")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `date` | `str` | Date (YYYY-MM-DD), optional |

---

### industry_performance_snapshot

Get industry performance snapshot.

```python
performance = await client.industry_performance_snapshot(date="2024-01-15")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `date` | `str` | Date (YYYY-MM-DD), optional |

## Historical Performance

### historical_sector_performance

Get historical sector performance.

```python
history = await client.historical_sector_performance(sector="Technology")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `sector` | `str` | Sector name |

---

### historical_industry_performance

Get historical industry performance.

```python
history = await client.historical_industry_performance(industry="Software")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `industry` | `str` | Industry name |

## P/E Ratios

### sector_pe_snapshot

Get sector P/E ratio snapshot.

```python
pe = await client.sector_pe_snapshot(date="2024-01-15")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `date` | `str` | Date (YYYY-MM-DD), optional |

---

### industry_pe_snapshot

Get industry P/E ratio snapshot.

```python
pe = await client.industry_pe_snapshot(date="2024-01-15")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `date` | `str` | Date (YYYY-MM-DD), optional |

---

### historical_sector_pe

Get historical sector P/E ratios.

```python
history = await client.historical_sector_pe(sector="Technology")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `sector` | `str` | Sector name |

---

### historical_industry_pe

Get historical industry P/E ratios.

```python
history = await client.historical_industry_pe(industry="Software")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `industry` | `str` | Industry name |

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def sector_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get sector performance
        sectors = await client.sector_performance_snapshot()
        print("=== Sector Performance ===")
        for s in sorted(sectors, key=lambda x: x.get('changesPercentage', 0), reverse=True):
            change = s.get('changesPercentage', 0)
            print(f"{s['sector']:25} {change:+.2f}%")

        # Get industry performance
        industries = await client.industry_performance_snapshot()
        print(f"\n=== Top 10 Industries ===")
        top_industries = sorted(
            industries,
            key=lambda x: x.get('changesPercentage', 0),
            reverse=True
        )[:10]
        for i in top_industries:
            print(f"{i['industry'][:30]:30} {i.get('changesPercentage', 0):+.2f}%")

        # Get sector P/E ratios
        pe_ratios = await client.sector_pe_snapshot()
        print(f"\n=== Sector P/E Ratios ===")
        for p in sorted(pe_ratios, key=lambda x: x.get('pe', 0)):
            print(f"{p['sector']:25} PE: {p.get('pe', 'N/A'):.1f}")

        # Get historical tech sector performance
        tech_history = await client.historical_sector_performance(sector="Technology")
        print(f"\n=== Technology Sector History ({len(tech_history)} days) ===")
        if tech_history:
            recent = tech_history[:5]
            for day in recent:
                print(f"{day['date']}: {day.get('changesPercentage', 0):+.2f}%")

asyncio.run(sector_examples())
```
