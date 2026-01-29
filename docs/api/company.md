# Company API

Get company profiles, executives, and use the stock screener.

## Methods

### profile

Get company profile data.

```python
profile = await client.profile(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### profile_cik

Get company profile by CIK number.

```python
profile = await client.profile_cik(cik=320193)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `cik` | `int` | CIK number |

---

### company_notes

Get company notes.

```python
notes = await client.company_notes(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### stock_peers

Get stock peer comparison.

```python
peers = await client.stock_peers(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### company_screener

Screen companies by various criteria.

```python
results = await client.company_screener(
    market_cap_more_than=1_000_000_000,
    market_cap_less_than=10_000_000_000,
    sector="Technology",
    exchange="NASDAQ",
    is_actively_trading=True,
    limit=50
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `market_cap_more_than` | `float` | Minimum market cap |
| `market_cap_less_than` | `float` | Maximum market cap |
| `price_more_than` | `float` | Minimum stock price |
| `price_less_than` | `float` | Maximum stock price |
| `beta_more_than` | `float` | Minimum beta |
| `beta_less_than` | `float` | Maximum beta |
| `volume_more_than` | `int` | Minimum trading volume |
| `volume_less_than` | `int` | Maximum trading volume |
| `dividend_more_than` | `float` | Minimum dividend yield |
| `dividend_less_than` | `float` | Maximum dividend yield |
| `sector` | `str` | Filter by sector |
| `industry` | `str` | Filter by industry |
| `exchange` | `str` | Filter by exchange |
| `country` | `str` | Filter by country |
| `is_etf` | `bool` | Filter ETFs only |
| `is_fund` | `bool` | Filter funds only |
| `is_actively_trading` | `bool` | Filter actively trading only |
| `limit` | `int` | Maximum results |

---

### key_executives

Get key executives for a company.

```python
executives = await client.key_executives(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### executive_compensation

Get executive compensation data.

```python
compensation = await client.executive_compensation(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### executive_compensation_benchmark

Get executive compensation benchmark data.

```python
benchmark = await client.executive_compensation_benchmark()
```

---

### employee_count

Get current employee count.

```python
count = await client.employee_count(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### historical_employee_count

Get historical employee count.

```python
history = await client.historical_employee_count(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### market_capitalization

Get current market capitalization.

```python
market_cap = await client.market_capitalization(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### market_capitalization_batch

Get market capitalization for multiple symbols.

```python
market_caps = await client.market_capitalization_batch(symbols="AAPL,GOOGL,MSFT")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbols` | `str` | Comma-separated symbols |

---

### historical_market_capitalization

Get historical market capitalization.

```python
history = await client.historical_market_capitalization(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### shares_float

Get shares float data.

```python
float_data = await client.shares_float(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### shares_float_all

Get all shares float data.

```python
all_float = await client.shares_float_all(page=0, limit=100)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def company_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get company profile
        profile = await client.profile(symbol="AAPL")
        print(f"Company: {profile[0]['companyName']}")
        print(f"Industry: {profile[0]['industry']}")

        # Screen for mid-cap tech stocks
        mid_cap_tech = await client.company_screener(
            market_cap_more_than=2_000_000_000,
            market_cap_less_than=10_000_000_000,
            sector="Technology",
            is_actively_trading=True,
            limit=20
        )
        print(f"Found {len(mid_cap_tech)} mid-cap tech stocks")

        # Get executive info
        executives = await client.key_executives(symbol="AAPL")
        for exec in executives[:3]:
            print(f"{exec['name']}: {exec['title']}")

asyncio.run(company_examples())
```
