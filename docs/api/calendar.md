# Calendar API

Access dividends, splits, earnings, and IPO calendar data.

## Dividends

### dividends

Get dividend history for a company.

```python
dividends = await client.dividends(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### dividends_calendar

Get upcoming dividend calendar.

```python
calendar = await client.dividends_calendar()
```

## Stock Splits

### splits

Get stock split history.

```python
splits = await client.splits(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### splits_calendar

Get upcoming stock splits calendar.

```python
calendar = await client.splits_calendar()
```

## Earnings

### earnings

Get earnings data for a company.

```python
earnings = await client.earnings(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### earnings_calendar

Get upcoming earnings calendar.

```python
calendar = await client.earnings_calendar()
```

## Earnings Transcripts

### earning_call_transcript_latest

Get latest earnings call transcript.

```python
transcript = await client.earning_call_transcript_latest()
```

---

### earning_call_transcript

Get earnings call transcript for a specific period.

```python
transcript = await client.earning_call_transcript(
    symbol="AAPL",
    quarter=1,
    year=2024
)
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |
| `quarter` | `int` | Quarter (1-4) |
| `year` | `int` | Year |

---

### earning_call_transcript_dates

Get available earnings call transcript dates.

```python
dates = await client.earning_call_transcript_dates(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### earnings_transcript_list

Get list of available earnings transcripts.

```python
transcripts = await client.earnings_transcript_list()
```

## IPOs

### ipos_calendar

Get IPO calendar.

```python
ipos = await client.ipos_calendar()
```

---

### ipos_disclosure

Get IPO disclosure data.

```python
disclosure = await client.ipos_disclosure()
```

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def calendar_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get upcoming earnings
        earnings = await client.earnings_calendar()
        print(f"=== Upcoming Earnings ({len(earnings)} companies) ===")
        for e in earnings[:5]:
            print(f"{e['symbol']}: {e['date']} - Est. EPS: {e.get('epsEstimated', 'N/A')}")

        # Get Apple's dividend history
        dividends = await client.dividends(symbol="AAPL")
        print(f"\n=== AAPL Dividend History ===")
        for d in dividends[:5]:
            print(f"{d['date']}: ${d['dividend']:.4f}")

        # Get stock splits
        splits = await client.splits(symbol="AAPL")
        print(f"\n=== AAPL Stock Splits ===")
        for s in splits:
            print(f"{s['date']}: {s['numerator']}-for-{s['denominator']}")

        # Get upcoming IPOs
        ipos = await client.ipos_calendar()
        print(f"\n=== Upcoming IPOs ({len(ipos)}) ===")
        for ipo in ipos[:5]:
            print(f"{ipo.get('symbol', 'TBD')}: {ipo.get('date', 'TBD')} - {ipo.get('company', 'Unknown')}")

asyncio.run(calendar_examples())
```
