# Mergers API

Access mergers and acquisitions (M&A) data.

## Methods

### mergers_acquisitions_latest

Get latest M&A activity.

```python
deals = await client.mergers_acquisitions_latest(page=0, limit=100)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

---

### mergers_acquisitions_search

Search M&A activity by company name.

```python
deals = await client.mergers_acquisitions_search(name="Microsoft")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` | Company name to search |

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def mergers_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get latest M&A deals
        deals = await client.mergers_acquisitions_latest(limit=20)
        print(f"=== Latest M&A Activity ({len(deals)}) ===")
        for d in deals[:10]:
            acquirer = d.get('acquirerName', 'Unknown')[:20]
            target = d.get('targetName', 'Unknown')[:20]
            value = d.get('transactionValue', 0)
            print(f"{acquirer:20} acquiring {target:20} - ${value:,.0f}M")

        # Search for specific company M&A
        microsoft_deals = await client.mergers_acquisitions_search(name="Microsoft")
        print(f"\n=== Microsoft M&A ({len(microsoft_deals)}) ===")
        for d in microsoft_deals[:5]:
            target = d.get('targetName', 'Unknown')
            date = d.get('acceptanceTime', 'N/A')
            print(f"{date[:10] if date else 'N/A'}: {target}")

        # Analyze M&A by sector
        all_deals = await client.mergers_acquisitions_latest(limit=500)
        sectors = {}
        for d in all_deals:
            sector = d.get('targetSector', 'Unknown')
            sectors[sector] = sectors.get(sector, 0) + 1

        print("\n=== M&A by Sector ===")
        for sector, count in sorted(sectors.items(), key=lambda x: -x[1])[:10]:
            print(f"{sector:30} {count:3} deals")

asyncio.run(mergers_examples())
```
