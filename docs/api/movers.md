# Movers API

Get biggest gainers, losers, and most actively traded stocks.

## Methods

### biggest_gainers

Get biggest gaining stocks of the day.

```python
gainers = await client.biggest_gainers()
```

**Returns:** List of stocks with the highest percentage gains.

---

### biggest_losers

Get biggest losing stocks of the day.

```python
losers = await client.biggest_losers()
```

**Returns:** List of stocks with the largest percentage losses.

---

### most_actives

Get most actively traded stocks.

```python
actives = await client.most_actives()
```

**Returns:** List of stocks with the highest trading volume.

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def movers_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get biggest gainers
        gainers = await client.biggest_gainers()
        print("=== Top 10 Gainers ===")
        for g in gainers[:10]:
            print(f"{g['symbol']:8} ${g['price']:8.2f}  {g['changesPercentage']:+6.2f}%")

        # Get biggest losers
        losers = await client.biggest_losers()
        print("\n=== Top 10 Losers ===")
        for l in losers[:10]:
            print(f"{l['symbol']:8} ${l['price']:8.2f}  {l['changesPercentage']:+6.2f}%")

        # Get most active
        actives = await client.most_actives()
        print("\n=== Most Active ===")
        for a in actives[:10]:
            volume = a.get('volume', 0)
            print(f"{a['symbol']:8} ${a['price']:8.2f}  Vol: {volume:,}")

asyncio.run(movers_examples())
```
