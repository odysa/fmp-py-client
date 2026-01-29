# SEC API

Access SEC filings, company searches, and industry classifications.

## SEC Filings

### sec_filings_8k

Get SEC 8-K filings (current reports).

```python
filings = await client.sec_filings_8k(
    from_date="2024-01-01",
    to_date="2024-01-31",
    page=0,
    limit=100
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `from_date` | `str` | Start date (YYYY-MM-DD) |
| `to_date` | `str` | End date (YYYY-MM-DD) |
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

---

### sec_filings_financials

Get SEC financial filings (10-K, 10-Q).

```python
filings = await client.sec_filings_financials(
    from_date="2024-01-01",
    to_date="2024-03-31",
    page=0,
    limit=100
)
```

---

### sec_filings_search_form_type

Search SEC filings by form type.

```python
filings = await client.sec_filings_search_form_type(
    form_type="10-K",
    from_date="2024-01-01",
    to_date="2024-12-31",
    page=0,
    limit=100
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `form_type` | `str` | SEC form type (e.g., "10-K", "10-Q", "8-K") |
| `from_date` | `str` | Start date |
| `to_date` | `str` | End date |
| `page` | `int` | Page number |
| `limit` | `int` | Results per page |

---

### sec_filings_search_symbol

Search SEC filings by stock symbol.

```python
filings = await client.sec_filings_search_symbol(
    symbol="AAPL",
    from_date="2024-01-01",
    to_date="2024-12-31",
    page=0,
    limit=100
)
```

---

### sec_filings_search_cik

Search SEC filings by CIK number.

```python
filings = await client.sec_filings_search_cik(
    cik=320193,
    from_date="2024-01-01",
    to_date="2024-12-31",
    page=0,
    limit=100
)
```

## Company Search

### sec_filings_company_search_name

Search SEC companies by name.

```python
companies = await client.sec_filings_company_search_name(company="Apple")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `company` | `str` | Company name search query |

---

### sec_filings_company_search_symbol

Search SEC companies by symbol.

```python
companies = await client.sec_filings_company_search_symbol(symbol="AAPL")
```

---

### sec_filings_company_search_cik

Search SEC companies by CIK.

```python
companies = await client.sec_filings_company_search_cik(cik=320193)
```

## SEC Profile

### sec_profile

Get SEC profile for a company.

```python
profile = await client.sec_profile(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

## Industry Classifications

### standard_industrial_classification_list

Get SIC codes list.

```python
sic_list = await client.standard_industrial_classification_list()
```

---

### industry_classification_search

Search industry classifications.

```python
classifications = await client.industry_classification_search()
```

---

### all_industry_classification

Get all industry classifications.

```python
classifications = await client.all_industry_classification()
```

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def sec_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get Apple's SEC filings
        apple_filings = await client.sec_filings_search_symbol(
            symbol="AAPL",
            from_date="2024-01-01",
            to_date="2024-12-31",
            limit=20
        )
        print("=== Apple SEC Filings (2024) ===")
        for f in apple_filings[:10]:
            print(f"{f['filedDate']:12} {f['form']:8} {f.get('description', 'N/A')[:40]}")

        # Get recent 10-K filings
        annual_reports = await client.sec_filings_search_form_type(
            form_type="10-K",
            from_date="2024-01-01",
            to_date="2024-03-31",
            limit=20
        )
        print(f"\n=== Recent 10-K Filings ({len(annual_reports)}) ===")
        for f in annual_reports[:10]:
            print(f"{f['symbol']:8} {f['filedDate']}")

        # Get SEC profile
        profile = await client.sec_profile(symbol="AAPL")
        if profile:
            p = profile[0]
            print(f"\n=== Apple SEC Profile ===")
            print(f"CIK: {p.get('cik')}")
            print(f"SIC: {p.get('sic')} - {p.get('sicDescription', 'N/A')}")
            print(f"Fiscal Year End: {p.get('fiscalYearEnd')}")

        # Get SIC codes
        sic_codes = await client.standard_industrial_classification_list()
        print(f"\n=== SIC Codes ({len(sic_codes)} total) ===")
        for sic in sic_codes[:10]:
            print(f"{sic.get('sicCode', 'N/A'):6} {sic.get('industryTitle', 'N/A')[:50]}")

asyncio.run(sec_examples())
```
