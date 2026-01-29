# Economics API

Access treasury rates, economic indicators, and market timing data.

## Treasury and Rates

### treasury_rates

Get US treasury rates.

```python
rates = await client.treasury_rates()
```

**Returns:** Treasury yields across different maturities (1M, 2M, 3M, 6M, 1Y, 2Y, 5Y, 10Y, 30Y).

---

### market_risk_premium

Get market risk premium by country.

```python
premiums = await client.market_risk_premium()
```

## Economic Indicators

### economic_indicators

Get economic indicators by name.

```python
gdp = await client.economic_indicators(name="GDP")
cpi = await client.economic_indicators(name="CPI")
unemployment = await client.economic_indicators(name="unemployment")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `name` | `str` | Indicator name (GDP, CPI, unemployment, etc.) |

---

### economic_calendar

Get economic data releases calendar.

```python
calendar = await client.economic_calendar(
    from_date="2024-01-01",
    to_date="2024-01-31"
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `from_date` | `str` | Start date (YYYY-MM-DD) |
| `to_date` | `str` | End date (YYYY-MM-DD) |

## Asset Lists

### commodities_list

Get list of available commodities.

```python
commodities = await client.commodities_list()
```

---

### forex_list

Get list of available forex pairs.

```python
forex = await client.forex_list()
```

---

### cryptocurrency_list

Get list of available cryptocurrencies.

```python
crypto = await client.cryptocurrency_list()
```

## Exchange Information

### exchange_market_hours

Get market hours for an exchange.

```python
hours = await client.exchange_market_hours(exchange="NYSE")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `exchange` | `str` | Exchange name |

---

### all_exchange_market_hours

Get market hours for all exchanges.

```python
all_hours = await client.all_exchange_market_hours()
```

---

### holidays_by_exchange

Get holidays for an exchange.

```python
holidays = await client.holidays_by_exchange(exchange="NYSE")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `exchange` | `str` | Exchange name |

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def economics_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get treasury rates
        rates = await client.treasury_rates()
        print("=== US Treasury Rates ===")
        if rates:
            r = rates[0]
            print(f"Date: {r.get('date')}")
            print(f"3-Month: {r.get('month3', 0):.2f}%")
            print(f"2-Year: {r.get('year2', 0):.2f}%")
            print(f"5-Year: {r.get('year5', 0):.2f}%")
            print(f"10-Year: {r.get('year10', 0):.2f}%")
            print(f"30-Year: {r.get('year30', 0):.2f}%")

            # Calculate yield curve slope
            slope = r.get('year10', 0) - r.get('year2', 0)
            print(f"\n10Y-2Y Spread: {slope:.2f}% ", end="")
            if slope < 0:
                print("(INVERTED)")
            else:
                print("(NORMAL)")

        # Get GDP data
        gdp = await client.economic_indicators(name="GDP")
        print(f"\n=== GDP Data ({len(gdp)} periods) ===")
        for g in gdp[:5]:
            print(f"{g.get('date')}: ${g.get('value', 0):,.0f}B")

        # Get economic calendar
        calendar = await client.economic_calendar(
            from_date="2024-01-01",
            to_date="2024-01-07"
        )
        print(f"\n=== Economic Calendar ===")
        for event in calendar[:10]:
            print(f"{event.get('date'):12} {event.get('event', 'N/A')[:40]}")

        # Get market hours for NYSE
        hours = await client.exchange_market_hours(exchange="NYSE")
        print(f"\n=== NYSE Market Hours ===")
        if hours:
            h = hours[0]
            print(f"Open: {h.get('openingHour')}")
            print(f"Close: {h.get('closingHour')}")

        # Get NYSE holidays
        holidays = await client.holidays_by_exchange(exchange="NYSE")
        print(f"\n=== NYSE Holidays ({len(holidays)}) ===")
        for hol in holidays[:5]:
            print(f"{hol.get('date')}: {hol.get('name', 'Unknown')}")

        # Get available forex pairs
        forex = await client.forex_list()
        print(f"\n=== Forex Pairs ({len(forex)} available) ===")
        for pair in forex[:10]:
            print(f"  {pair.get('symbol')}: {pair.get('name', 'N/A')}")

asyncio.run(economics_examples())
```
