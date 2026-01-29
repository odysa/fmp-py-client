# Valuation API

Access discounted cash flow valuations and enterprise values.

## Methods

### discounted_cash_flow

Get discounted cash flow (DCF) valuation.

```python
dcf = await client.discounted_cash_flow(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

**Returns:** DCF valuation including intrinsic value estimate.

---

### levered_discounted_cash_flow

Get levered discounted cash flow valuation.

```python
dcf = await client.levered_discounted_cash_flow(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### custom_discounted_cash_flow

Get custom DCF valuation with adjustable parameters.

```python
dcf = await client.custom_discounted_cash_flow(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### custom_levered_discounted_cash_flow

Get custom levered DCF valuation.

```python
dcf = await client.custom_levered_discounted_cash_flow(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### enterprise_values

Get enterprise values over time.

```python
ev = await client.enterprise_values(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

**Returns:** Historical enterprise value data including:

- Market capitalization
- Total debt
- Cash and equivalents
- Enterprise value

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def valuation_examples():
    async with AsyncFMPClient("your-api-key") as client:
        symbol = "AAPL"

        # Get DCF valuation
        dcf = await client.discounted_cash_flow(symbol=symbol)
        if dcf:
            d = dcf[0]
            print(f"=== {symbol} DCF Valuation ===")
            print(f"Current Price: ${d.get('price', 0):.2f}")
            print(f"DCF Value: ${d.get('dcf', 0):.2f}")

            price = d.get('price', 0)
            dcf_value = d.get('dcf', 0)
            if price and dcf_value:
                upside = (dcf_value - price) / price * 100
                print(f"Upside/Downside: {upside:+.1f}%")

        # Get levered DCF
        levered = await client.levered_discounted_cash_flow(symbol=symbol)
        if levered:
            print(f"\nLevered DCF: ${levered[0].get('dcf', 0):.2f}")

        # Get enterprise values
        ev = await client.enterprise_values(symbol=symbol)
        print(f"\n=== {symbol} Enterprise Values ===")
        for e in ev[:5]:
            print(f"{e['date']}: EV ${e.get('enterpriseValue', 0):,.0f}")

        # Compare multiple stocks
        print("\n=== DCF Comparison ===")
        symbols = ["AAPL", "GOOGL", "MSFT", "AMZN"]

        for s in symbols:
            dcf = await client.discounted_cash_flow(symbol=s)
            if dcf:
                d = dcf[0]
                price = d.get('price', 0)
                dcf_val = d.get('dcf', 0)
                upside = (dcf_val - price) / price * 100 if price else 0
                print(f"{s}: Price ${price:.2f}, DCF ${dcf_val:.2f} ({upside:+.1f}%)")

asyncio.run(valuation_examples())
```
