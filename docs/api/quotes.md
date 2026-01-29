# Quotes API

Get real-time and batch stock quotes.

## Single Quotes

### quote

Get real-time stock quote with full details.

```python
quote = await client.quote(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

**Returns:** Full quote data including price, volume, market cap, PE ratio, etc.

---

### quote_short

Get short-form stock quote (faster, less data).

```python
quote = await client.quote_short(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### aftermarket_trade

Get aftermarket trade data.

```python
aftermarket = await client.aftermarket_trade(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### aftermarket_quote

Get aftermarket quote data.

```python
aftermarket = await client.aftermarket_quote(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

---

### stock_price_change

Get stock price change data.

```python
change = await client.stock_price_change(symbol="AAPL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbol` | `str` | Stock symbol |

## Batch Quotes

### batch_quote

Get quotes for multiple symbols.

```python
quotes = await client.batch_quote(symbols="AAPL,GOOGL,MSFT")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbols` | `str` | Comma-separated symbols |

---

### batch_quote_short

Get short-form quotes for multiple symbols.

```python
quotes = await client.batch_quote_short(symbols="AAPL,GOOGL,MSFT")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbols` | `str` | Comma-separated symbols |

---

### batch_aftermarket_trade

Get aftermarket trades for multiple symbols.

```python
trades = await client.batch_aftermarket_trade(symbols="AAPL,GOOGL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbols` | `str` | Comma-separated symbols |

---

### batch_aftermarket_quote

Get aftermarket quotes for multiple symbols.

```python
quotes = await client.batch_aftermarket_quote(symbols="AAPL,GOOGL")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `symbols` | `str` | Comma-separated symbols |

---

### batch_exchange_quote

Get quotes for all symbols on an exchange.

```python
quotes = await client.batch_exchange_quote(exchange="NASDAQ")
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `exchange` | `str` | Exchange name |

## Asset Class Quotes

### batch_mutualfund_quotes

Get all mutual fund quotes.

```python
quotes = await client.batch_mutualfund_quotes()
```

---

### batch_etf_quotes

Get all ETF quotes.

```python
quotes = await client.batch_etf_quotes()
```

---

### batch_commodity_quotes

Get all commodity quotes.

```python
quotes = await client.batch_commodity_quotes()
```

---

### batch_crypto_quotes

Get all cryptocurrency quotes.

```python
quotes = await client.batch_crypto_quotes()
```

---

### batch_forex_quotes

Get all forex pair quotes.

```python
quotes = await client.batch_forex_quotes()
```

---

### batch_index_quotes

Get all index quotes.

```python
quotes = await client.batch_index_quotes()
```

## Example

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def quote_examples():
    async with AsyncFMPClient("your-api-key") as client:
        # Get single quote
        quote = await client.quote(symbol="AAPL")
        q = quote[0]
        print(f"AAPL: ${q['price']:.2f} ({q['changesPercentage']:+.2f}%)")

        # Get multiple quotes at once
        symbols = "AAPL,GOOGL,MSFT,AMZN,META"
        quotes = await client.batch_quote(symbols=symbols)

        print("\n=== FAANG+ Quotes ===")
        for q in quotes:
            print(f"{q['symbol']}: ${q['price']:.2f} ({q['changesPercentage']:+.2f}%)")

        # Get aftermarket data
        aftermarket = await client.aftermarket_quote(symbol="AAPL")
        if aftermarket:
            print(f"\nAAPL After Hours: ${aftermarket[0].get('price', 'N/A')}")

        # Get all crypto quotes
        crypto = await client.batch_crypto_quotes()
        print(f"\nTotal cryptocurrencies: {len(crypto)}")

asyncio.run(quote_examples())
```
