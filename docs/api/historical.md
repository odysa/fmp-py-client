# Historical API

Get historical end-of-day prices and intraday chart data.

## End-of-Day Prices

### historical_price_eod_light

Get light historical end-of-day prices (OHLCV only).

```python
prices = await client.historical_price_eod_light(
    "AAPL",
    from_date="2024-01-01",
    to_date="2024-12-31"
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol (positional) |
| `from_date` | `str` | Start date (YYYY-MM-DD) |
| `to_date` | `str` | End date (YYYY-MM-DD) |

---

### historical_price_eod_full

Get full historical end-of-day prices with additional data.

```python
prices = await client.historical_price_eod_full(
    "AAPL",
    from_date="2024-01-01",
    to_date="2024-12-31"
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol (positional) |
| `from_date` | `str` | Start date (YYYY-MM-DD) |
| `to_date` | `str` | End date (YYYY-MM-DD) |

---

### historical_price_eod_non_split_adjusted

Get non-split-adjusted historical prices.

```python
prices = await client.historical_price_eod_non_split_adjusted(
    "AAPL",
    from_date="2024-01-01",
    to_date="2024-12-31"
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol (positional) |
| `from_date` | `str` | Start date (YYYY-MM-DD) |
| `to_date` | `str` | End date (YYYY-MM-DD) |

---

### historical_price_eod_dividend_adjusted

Get dividend-adjusted historical prices.

```python
prices = await client.historical_price_eod_dividend_adjusted(
    "AAPL",
    from_date="2024-01-01",
    to_date="2024-12-31"
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol (positional) |
| `from_date` | `str` | Start date (YYYY-MM-DD) |
| `to_date` | `str` | End date (YYYY-MM-DD) |

## Intraday Charts

### historical_chart_1min

Get 1-minute interval chart data.

```python
chart = await client.historical_chart_1min(
    "AAPL",
    from_date="2024-01-15",
    to_date="2024-01-15"
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol (positional) |
| `from_date` | `str` | Start date (YYYY-MM-DD) |
| `to_date` | `str` | End date (YYYY-MM-DD) |

---

### historical_chart_5min

Get 5-minute interval chart data.

```python
chart = await client.historical_chart_5min(
    "AAPL",
    from_date="2024-01-15",
    to_date="2024-01-15"
)
```

---

### historical_chart_15min

Get 15-minute interval chart data.

```python
chart = await client.historical_chart_15min(
    "AAPL",
    from_date="2024-01-15",
    to_date="2024-01-15"
)
```

---

### historical_chart_30min

Get 30-minute interval chart data.

```python
chart = await client.historical_chart_30min(
    "AAPL",
    from_date="2024-01-15",
    to_date="2024-01-15"
)
```

---

### historical_chart_1hour

Get 1-hour interval chart data.

```python
chart = await client.historical_chart_1hour(
    "AAPL",
    from_date="2024-01-15",
    to_date="2024-01-19"
)
```

---

### historical_chart_4hour

Get 4-hour interval chart data.

```python
chart = await client.historical_chart_4hour(
    "AAPL",
    from_date="2024-01-01",
    to_date="2024-01-31"
)
```

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def historical_examples():
    async with AsyncFMPClient("your-api-key") as client:
        symbol = "AAPL"

        # Get daily prices for 2024
        daily = await client.historical_price_eod_full(
            symbol,
            from_date="2024-01-01",
            to_date="2024-12-31"
        )

        print(f"=== {symbol} Daily Prices (2024) ===")
        print(f"Total trading days: {len(daily)}")

        if daily:
            latest = daily[0]
            oldest = daily[-1]
            print(f"Latest: {latest['date']} - ${latest['close']:.2f}")
            print(f"Oldest: {oldest['date']} - ${oldest['close']:.2f}")

            # Calculate YTD return
            ytd_return = (latest['close'] - oldest['close']) / oldest['close'] * 100
            print(f"YTD Return: {ytd_return:+.1f}%")

        # Get intraday data for a specific day
        intraday = await client.historical_chart_5min(
            symbol,
            from_date="2024-01-15",
            to_date="2024-01-15"
        )

        print(f"\n=== Intraday 5-min bars (Jan 15, 2024) ===")
        print(f"Total bars: {len(intraday)}")

        if intraday:
            # Find high and low of day
            high = max(bar['high'] for bar in intraday)
            low = min(bar['low'] for bar in intraday)
            print(f"Day High: ${high:.2f}")
            print(f"Day Low: ${low:.2f}")
            print(f"Day Range: ${high - low:.2f}")

asyncio.run(historical_examples())
```
