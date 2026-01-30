# Financials API

Access income statements, balance sheets, cash flow statements, and growth metrics.

## Core Financial Statements

### income_statement

Get income statements.

```python
from fmp_py_client import Period

income = await client.income_statement(
    symbol="AAPL",
    period=Period.ANNUAL,
    limit=5
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |
| `period` | `Period` | `"annual"` or `"quarter"` |
| `limit` | `int` | Number of periods |

---

### balance_sheet_statement

Get balance sheet statements.

```python
balance = await client.balance_sheet_statement(
    symbol="AAPL",
    period=Period.QUARTER,
    limit=4
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |
| `period` | `Period` | `"annual"` or `"quarter"` |
| `limit` | `int` | Number of periods |

---

### cash_flow_statement

Get cash flow statements.

```python
cash_flow = await client.cash_flow_statement(
    symbol="AAPL",
    period=Period.ANNUAL,
    limit=5
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |
| `period` | `Period` | `"annual"` or `"quarter"` |
| `limit` | `int` | Number of periods |

## TTM (Trailing Twelve Months)

### income_statement_ttm

Get trailing twelve months income statement.

```python
ttm = await client.income_statement_ttm(symbol="AAPL")
```

---

### balance_sheet_statement_ttm

Get trailing twelve months balance sheet.

```python
ttm = await client.balance_sheet_statement_ttm(symbol="AAPL")
```

---

### cash_flow_statement_ttm

Get trailing twelve months cash flow statement.

```python
ttm = await client.cash_flow_statement_ttm(symbol="AAPL")
```

## Growth Metrics

### income_statement_growth

Get income statement growth metrics.

```python
growth = await client.income_statement_growth(
    symbol="AAPL",
    period=Period.ANNUAL,
    limit=5
)
```

---

### balance_sheet_statement_growth

Get balance sheet growth metrics.

```python
growth = await client.balance_sheet_statement_growth(
    symbol="AAPL",
    period=Period.ANNUAL,
    limit=5
)
```

---

### cash_flow_statement_growth

Get cash flow statement growth metrics.

```python
growth = await client.cash_flow_statement_growth(
    symbol="AAPL",
    period=Period.ANNUAL,
    limit=5
)
```

---

### financial_growth

Get overall financial growth metrics.

```python
growth = await client.financial_growth(
    symbol="AAPL",
    period=Period.ANNUAL,
    limit=5
)
```

## As-Reported Statements

### income_statement_as_reported

Get income statement as reported to SEC.

```python
as_reported = await client.income_statement_as_reported(symbol="AAPL")
```

---

### balance_sheet_statement_as_reported

Get balance sheet as reported to SEC.

```python
as_reported = await client.balance_sheet_statement_as_reported(symbol="AAPL")
```

---

### cash_flow_statement_as_reported

Get cash flow statement as reported to SEC.

```python
as_reported = await client.cash_flow_statement_as_reported(symbol="AAPL")
```

---

### financial_statement_full_as_reported

Get full financial statement as reported.

```python
full = await client.financial_statement_full_as_reported(symbol="AAPL")
```

## Reports and Segmentation

### latest_financial_statements

Get latest financial statements across all companies.

```python
latest = await client.latest_financial_statements(page=0, limit=100)
```

---

### financial_reports_dates

Get available financial report dates.

```python
dates = await client.financial_reports_dates(symbol="AAPL")
```

---

### financial_reports_json

Get financial reports in JSON format.

```python
reports = await client.financial_reports_json(symbol="AAPL")
```

---

### financial_reports_xlsx

Get financial reports in XLSX format.

```python
xlsx = await client.financial_reports_xlsx(symbol="AAPL")
```

---

### revenue_product_segmentation

Get revenue breakdown by product.

```python
segments = await client.revenue_product_segmentation(symbol="AAPL")
```

---

### revenue_geographic_segmentation

Get revenue breakdown by geography.

```python
segments = await client.revenue_geographic_segmentation(symbol="AAPL")
```

## Bulk Operations

### income_statement_bulk

Get bulk income statements.

```python
bulk = await client.income_statement_bulk(year=2023, period=Period.ANNUAL)
```

---

### balance_sheet_statement_bulk

Get bulk balance sheet statements.

```python
bulk = await client.balance_sheet_statement_bulk(year=2023, period=Period.ANNUAL)
```

---

### cash_flow_statement_bulk

Get bulk cash flow statements.

```python
bulk = await client.cash_flow_statement_bulk(year=2023, period=Period.ANNUAL)
```

---

### income_statement_growth_bulk

Get bulk income statement growth data.

```python
bulk = await client.income_statement_growth_bulk(year=2023, period=Period.ANNUAL)
```

---

### balance_sheet_statement_growth_bulk

Get bulk balance sheet growth data.

```python
bulk = await client.balance_sheet_statement_growth_bulk(year=2023, period=Period.ANNUAL)
```

---

### cash_flow_statement_growth_bulk

Get bulk cash flow statement growth data.

```python
bulk = await client.cash_flow_statement_growth_bulk(year=2023, period=Period.ANNUAL)
```

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient, Period

async def financial_analysis():
    async with AsyncFMPClient("your-api-key") as client:
        symbol = "AAPL"

        # Get 5 years of annual income statements
        income = await client.income_statement(
            symbol=symbol,
            period=Period.ANNUAL,
            limit=5
        )

        # Calculate revenue growth
        for i, stmt in enumerate(income[:-1]):
            prev = income[i + 1]
            growth = (stmt["revenue"] - prev["revenue"]) / prev["revenue"] * 100
            print(f"{stmt['date']}: Revenue ${stmt['revenue']:,.0f} ({growth:+.1f}%)")

        # Get TTM metrics for current snapshot
        ttm = await client.income_statement_ttm(symbol=symbol)
        print(f"\nTTM Revenue: ${ttm[0]['revenue']:,.0f}")
        print(f"TTM Net Income: ${ttm[0]['netIncome']:,.0f}")

        # Get revenue segmentation
        geo = await client.revenue_geographic_segmentation(symbol=symbol)
        product = await client.revenue_product_segmentation(symbol=symbol)

asyncio.run(financial_analysis())
```
