# Crowdfunding API

Access crowdfunding offerings, fundraising data, and IPO prospectus information.

## Crowdfunding Offerings

### crowdfunding_offerings_latest

Get latest crowdfunding offerings.

```python
offerings = await client.crowdfunding_offerings_latest(page=0, limit=100)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

---

### crowdfunding_offerings_search

Search crowdfunding offerings by name.

```python
offerings = await client.crowdfunding_offerings_search(name="tech")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` | Company name to search |

---

### crowdfunding_offerings

Get crowdfunding offerings by CIK.

```python
offerings = await client.crowdfunding_offerings(cik=12345)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `cik` | `int` | CIK number |

## Fundraising

### fundraising_latest

Get latest fundraising data.

```python
fundraising = await client.fundraising_latest(page=0, limit=100)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

---

### fundraising_search

Search fundraising data by name.

```python
fundraising = await client.fundraising_search(name="biotech")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` | Company name to search |

---

### fundraising

Get fundraising data by CIK.

```python
fundraising = await client.fundraising(cik=12345)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `cik` | `int` | CIK number |

## IPO Prospectus

### ipos_prospectus

Get IPO prospectus data.

```python
prospectus = await client.ipos_prospectus()
```

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def crowdfunding_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get latest crowdfunding offerings
        offerings = await client.crowdfunding_offerings_latest(limit=20)
        print(f"=== Latest Crowdfunding Offerings ({len(offerings)}) ===")
        for o in offerings[:10]:
            print(f"{o.get('name', 'Unknown')[:30]:30} - ${o.get('amountRaised', 0):>12,.0f}")

        # Search for tech-related crowdfunding
        tech_offerings = await client.crowdfunding_offerings_search(name="tech")
        print(f"\n=== Tech Crowdfunding Offerings ({len(tech_offerings)}) ===")
        for o in tech_offerings[:5]:
            print(f"{o.get('name', 'Unknown')[:40]}")

        # Get latest fundraising rounds
        fundraising = await client.fundraising_latest(limit=20)
        print(f"\n=== Latest Fundraising ({len(fundraising)}) ===")
        for f in fundraising[:10]:
            amount = f.get('totalOfferingAmount', 0)
            print(f"{f.get('name', 'Unknown')[:30]:30} - ${amount:>15,.0f}")

        # Get IPO prospectus data
        prospectus = await client.ipos_prospectus()
        print(f"\n=== IPO Prospectus ({len(prospectus)}) ===")
        for p in prospectus[:10]:
            print(f"{p.get('symbol', 'N/A'):8} {p.get('company', 'Unknown')[:30]}")

asyncio.run(crowdfunding_examples())
```
