# ESG API

Access Environmental, Social, and Governance (ESG) data and Commitment of Traders (COT) reports.

## ESG Data

### esg_disclosures

Get ESG disclosures for a company.

```python
disclosures = await client.esg_disclosures(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### esg_ratings

Get ESG ratings for a company.

```python
ratings = await client.esg_ratings(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

**Returns:** ESG scores including:

- Environmental score
- Social score
- Governance score
- Total ESG score

---

### esg_benchmark

Get ESG benchmark comparison data.

```python
benchmark = await client.esg_benchmark()
```

## Commitment of Traders (COT)

### commitment_of_traders_report

Get Commitment of Traders report.

```python
cot = await client.commitment_of_traders_report()
```

---

### commitment_of_traders_analysis

Get COT analysis by dates.

```python
analysis = await client.commitment_of_traders_analysis()
```

---

### commitment_of_traders_list

Get list of Commitment of Traders symbols.

```python
symbols = await client.commitment_of_traders_list()
```

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def esg_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get ESG ratings for Apple
        ratings = await client.esg_ratings(symbol="AAPL")
        if ratings:
            r = ratings[0]
            print("=== Apple ESG Ratings ===")
            print(f"Environmental: {r.get('environmentalScore', 'N/A')}")
            print(f"Social: {r.get('socialScore', 'N/A')}")
            print(f"Governance: {r.get('governanceScore', 'N/A')}")
            print(f"Total ESG: {r.get('esgScore', 'N/A')}")

        # Get ESG disclosures
        disclosures = await client.esg_disclosures(symbol="AAPL")
        print(f"\n=== Apple ESG Disclosures ({len(disclosures)} entries) ===")
        for d in disclosures[:5]:
            print(f"{d.get('date', 'N/A')}: {d.get('formType', 'N/A')}")

        # Compare ESG scores across companies
        print("\n=== ESG Score Comparison ===")
        symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]
        for symbol in symbols:
            ratings = await client.esg_ratings(symbol=symbol)
            if ratings:
                r = ratings[0]
                score = r.get('esgScore', 'N/A')
                print(f"{symbol:6} ESG Score: {score}")

        # Get ESG benchmark
        benchmark = await client.esg_benchmark()
        print(f"\n=== ESG Benchmark Data ({len(benchmark)} companies) ===")
        # Sort by ESG score
        sorted_bench = sorted(
            [b for b in benchmark if b.get('esgScore')],
            key=lambda x: x.get('esgScore', 0),
            reverse=True
        )
        print("Top 10 ESG Companies:")
        for b in sorted_bench[:10]:
            print(f"{b.get('symbol', 'N/A'):8} {b.get('esgScore', 0):.1f}")

        # Get COT data
        cot_symbols = await client.commitment_of_traders_list()
        print(f"\n=== COT Symbols ({len(cot_symbols)} available) ===")
        for c in cot_symbols[:10]:
            print(f"  {c.get('short_name', 'N/A')}")

asyncio.run(esg_examples())
```
