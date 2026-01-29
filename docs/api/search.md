# Search API

Search for companies and securities by various identifiers.

## Methods

### search_symbol

Search for stock symbols matching a query.

```python
results = await client.search_symbol(
    query="AAP",
    limit=10,
    exchange="NASDAQ"
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `query` | `str` | Search query |
| `limit` | `int` | Maximum results to return |
| `exchange` | `str` | Filter by exchange |

---

### search_name

Search for company names matching a query.

```python
results = await client.search_name(
    query="Apple",
    limit=10,
    exchange="NASDAQ"
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `query` | `str` | Company name search query |
| `limit` | `int` | Maximum results to return |
| `exchange` | `str` | Filter by exchange |

---

### search_cik

Search by SEC CIK number.

```python
results = await client.search_cik(cik=320193)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `cik` | `int` | CIK number |

---

### search_cusip

Search by CUSIP number.

```python
results = await client.search_cusip(cusip="037833100")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `cusip` | `str` | CUSIP identifier |

---

### search_isin

Search by ISIN number.

```python
results = await client.search_isin(isin="US0378331005")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `isin` | `str` | ISIN identifier |

---

### search_exchange_variants

Find all exchange variants for a symbol.

```python
variants = await client.search_exchange_variants(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def search_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Find companies with "tech" in the name
        tech_companies = await client.search_name(query="tech", limit=20)

        # Search for specific ticker patterns
        aap_symbols = await client.search_symbol(query="AAP", limit=10)

        # Look up by CUSIP
        apple = await client.search_cusip(cusip="037833100")

asyncio.run(search_examples())
```
