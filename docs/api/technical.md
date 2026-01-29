# Technical API

Access technical indicators including moving averages, RSI, and more.

## Moving Averages

### sma

Get Simple Moving Average (SMA).

```python
from fmp_py_client import Timeframe

sma = await client.sma(
    symbol="AAPL",
    period_length=20,
    timeframe=Timeframe.ONE_DAY
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |
| `period_length` | `int` | Number of periods |
| `timeframe` | `Timeframe` | Time interval |

---

### ema

Get Exponential Moving Average (EMA).

```python
ema = await client.ema(
    symbol="AAPL",
    period_length=20,
    timeframe=Timeframe.ONE_DAY
)
```

---

### wma

Get Weighted Moving Average (WMA).

```python
wma = await client.wma(
    symbol="AAPL",
    period_length=20,
    timeframe=Timeframe.ONE_DAY
)
```

---

### dema

Get Double Exponential Moving Average (DEMA).

```python
dema = await client.dema(
    symbol="AAPL",
    period_length=20,
    timeframe=Timeframe.ONE_DAY
)
```

---

### tema

Get Triple Exponential Moving Average (TEMA).

```python
tema = await client.tema(
    symbol="AAPL",
    period_length=20,
    timeframe=Timeframe.ONE_DAY
)
```

## Oscillators

### rsi

Get Relative Strength Index (RSI).

```python
rsi = await client.rsi(
    symbol="AAPL",
    period_length=14,
    timeframe=Timeframe.ONE_DAY
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |
| `period_length` | `int` | RSI period (typically 14) |
| `timeframe` | `Timeframe` | Time interval |

**RSI Interpretation:**

- RSI > 70: Overbought
- RSI < 30: Oversold

---

### williams

Get Williams %R indicator.

```python
williams = await client.williams(
    symbol="AAPL",
    period_length=14,
    timeframe=Timeframe.ONE_DAY
)
```

## Trend Indicators

### adx

Get Average Directional Index (ADX).

```python
adx = await client.adx(
    symbol="AAPL",
    period_length=14,
    timeframe=Timeframe.ONE_DAY
)
```

**ADX Interpretation:**

- ADX > 25: Strong trend
- ADX < 20: Weak trend or ranging

## Volatility

### standard_deviation

Get Standard Deviation indicator.

```python
std = await client.standard_deviation(
    symbol="AAPL",
    period_length=20,
    timeframe=Timeframe.ONE_DAY
)
```

## Timeframe Options

The `Timeframe` enum supports:

| Value | Description |
|-------|-------------|
| `Timeframe.ONE_MIN` | 1-minute intervals |
| `Timeframe.FIVE_MIN` | 5-minute intervals |
| `Timeframe.FIFTEEN_MIN` | 15-minute intervals |
| `Timeframe.THIRTY_MIN` | 30-minute intervals |
| `Timeframe.ONE_HOUR` | 1-hour intervals |
| `Timeframe.FOUR_HOUR` | 4-hour intervals |
| `Timeframe.ONE_DAY` | Daily intervals |

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient, Timeframe

async def technical_examples():
    async with AsyncFMPClient("your-api-key") as client:
        symbol = "AAPL"

        # Get multiple moving averages for trend analysis
        sma_20 = await client.sma(
            symbol=symbol,
            period_length=20,
            timeframe=Timeframe.ONE_DAY
        )
        sma_50 = await client.sma(
            symbol=symbol,
            period_length=50,
            timeframe=Timeframe.ONE_DAY
        )
        sma_200 = await client.sma(
            symbol=symbol,
            period_length=200,
            timeframe=Timeframe.ONE_DAY
        )

        print(f"=== {symbol} Moving Averages ===")
        if sma_20:
            print(f"SMA 20: ${sma_20[0].get('sma', 0):.2f}")
        if sma_50:
            print(f"SMA 50: ${sma_50[0].get('sma', 0):.2f}")
        if sma_200:
            print(f"SMA 200: ${sma_200[0].get('sma', 0):.2f}")

        # Get RSI for overbought/oversold analysis
        rsi = await client.rsi(
            symbol=symbol,
            period_length=14,
            timeframe=Timeframe.ONE_DAY
        )

        print(f"\n=== {symbol} RSI (14) ===")
        if rsi:
            rsi_value = rsi[0].get('rsi', 0)
            print(f"RSI: {rsi_value:.2f}")
            if rsi_value > 70:
                print("Signal: OVERBOUGHT")
            elif rsi_value < 30:
                print("Signal: OVERSOLD")
            else:
                print("Signal: NEUTRAL")

        # Get ADX for trend strength
        adx = await client.adx(
            symbol=symbol,
            period_length=14,
            timeframe=Timeframe.ONE_DAY
        )

        print(f"\n=== {symbol} ADX (14) ===")
        if adx:
            adx_value = adx[0].get('adx', 0)
            print(f"ADX: {adx_value:.2f}")
            if adx_value > 25:
                print("Trend: STRONG")
            else:
                print("Trend: WEAK/RANGING")

        # Intraday analysis with 15-minute timeframe
        rsi_15m = await client.rsi(
            symbol=symbol,
            period_length=14,
            timeframe=Timeframe.FIFTEEN_MIN
        )

        print(f"\n=== {symbol} Intraday RSI (15min) ===")
        if rsi_15m:
            print(f"RSI: {rsi_15m[0].get('rsi', 0):.2f}")

asyncio.run(technical_examples())
```
