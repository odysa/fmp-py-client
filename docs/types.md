# Types

The FMP Client provides type aliases and enumerations for type-safe development.

## Type Aliases

### JSONObject

A dictionary representing a JSON object.

```python
from typing import Any

type JSONObject = dict[str, Any]
```

Used as the return type for methods that return a single object.

---

### JSONArray

A list of JSON objects.

```python
from typing import Any

type JSONArray = list[dict[str, Any]]
```

Used as the return type for most API methods that return collections.

## Enumerations

### Period

Financial reporting period.

```python
from fmp_py_client import Period

# Annual financial statements
income = await client.income_statement(
    symbol="AAPL",
    period=Period.ANNUAL,
    limit=5
)

# Quarterly financial statements
income = await client.income_statement(
    symbol="AAPL",
    period=Period.QUARTER,
    limit=4
)
```

**Values:**

| Value | String | Description |
|-------|--------|-------------|
| `Period.ANNUAL` | `"annual"` | Annual reporting period |
| `Period.QUARTER` | `"quarter"` | Quarterly reporting period |

---

### Timeframe

Technical indicator timeframe.

```python
from fmp_py_client import Timeframe

# Daily SMA
sma = await client.sma(
    symbol="AAPL",
    period_length=20,
    timeframe=Timeframe.ONE_DAY
)

# 15-minute RSI
rsi = await client.rsi(
    symbol="AAPL",
    period_length=14,
    timeframe=Timeframe.FIFTEEN_MIN
)
```

**Values:**

| Value | String | Description |
|-------|--------|-------------|
| `Timeframe.ONE_MIN` | `"1min"` | 1-minute intervals |
| `Timeframe.FIVE_MIN` | `"5min"` | 5-minute intervals |
| `Timeframe.FIFTEEN_MIN` | `"15min"` | 15-minute intervals |
| `Timeframe.THIRTY_MIN` | `"30min"` | 30-minute intervals |
| `Timeframe.ONE_HOUR` | `"1hour"` | 1-hour intervals |
| `Timeframe.FOUR_HOUR` | `"4hour"` | 4-hour intervals |
| `Timeframe.ONE_DAY` | `"1day"` | Daily intervals |

## Using Enums as Strings

Since both enums inherit from `StrEnum`, you can use them interchangeably with strings:

```python
from fmp_py_client import Period, Timeframe

# Using enum values
income = await client.income_statement(symbol="AAPL", period=Period.ANNUAL)

# Using string values (also valid)
income = await client.income_statement(symbol="AAPL", period="annual")
```

## Type Hints in Your Code

For full IDE support, use the types in your own code:

```python
from fmp_py_client import AsyncFMPClient, Period
from fmp_py_client._types import JSONArray, JSONObject

async def get_financials(
    client: AsyncFMPClient,
    symbol: str,
    period: Period = Period.ANNUAL,
) -> JSONArray:
    """Get income statement with full type hints."""
    return await client.income_statement(
        symbol=symbol,
        period=period,
        limit=5
    )

async def get_profile(
    client: AsyncFMPClient,
    symbol: str,
) -> JSONObject | None:
    """Get company profile with type hints."""
    result = await client.profile(symbol=symbol)
    return result[0] if result else None
```

## PEP 561 Support

The package includes a `py.typed` marker file, indicating full type hint support. This enables:

- IDE autocompletion
- Type checking with mypy, pyright, etc.
- Inline documentation in editors

```bash
# Type check your code using the fmp-py-client types
mypy your_script.py
```
