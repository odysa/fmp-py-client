# Configuration

## Client Initialization

The `AsyncFMPClient` accepts several configuration options:

```python
from fmp_py_client import AsyncFMPClient
import httpx

client = AsyncFMPClient(
    api_key="your-api-key",
    base_url="https://financialmodelingprep.com",  # Default
    timeout=30.0,  # Request timeout in seconds
    httpx_client=None,  # Optional custom httpx client
)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api_key` | `str` | Required | Your FMP API key |
| `base_url` | `str` | `https://financialmodelingprep.com` | API base URL |
| `timeout` | `float` | `30.0` | Request timeout in seconds |
| `httpx_client` | `httpx.AsyncClient \| None` | `None` | Custom httpx client |

## Context Manager Usage

The recommended way to use the client is with an async context manager:

```python
async with AsyncFMPClient("your-api-key") as client:
    # Client is automatically closed when exiting the context
    quote = await client.quote(symbol="AAPL")
```

## Manual Lifecycle Management

If you need more control, you can manage the client lifecycle manually:

```python
client = AsyncFMPClient("your-api-key")
try:
    quote = await client.quote(symbol="AAPL")
finally:
    await client.aclose()
```

## Custom httpx Client

For advanced use cases, you can provide your own httpx client:

```python
import httpx
from fmp_py_client import AsyncFMPClient

# Custom client with specific configuration
custom_client = httpx.AsyncClient(
    timeout=httpx.Timeout(60.0),
    limits=httpx.Limits(max_connections=100),
    headers={"User-Agent": "MyApp/1.0"},
)

async with AsyncFMPClient(
    api_key="your-api-key",
    httpx_client=custom_client,
) as client:
    quote = await client.quote(symbol="AAPL")

# Note: When providing a custom client, you're responsible for closing it
await custom_client.aclose()
```

## Timeout Configuration

Set a custom timeout for slow networks or large requests:

```python
# 60-second timeout
client = AsyncFMPClient("your-api-key", timeout=60.0)
```

## Base URL Override

Override the base URL for testing or alternative endpoints:

```python
client = AsyncFMPClient(
    api_key="your-api-key",
    base_url="https://api.example.com",
)
```

## Environment Variable Configuration

Best practice is to use environment variables for sensitive configuration:

```python
import os
from fmp_py_client import AsyncFMPClient

API_KEY = os.environ.get("FMP_API_KEY")
if not API_KEY:
    raise ValueError("FMP_API_KEY environment variable is required")

async with AsyncFMPClient(API_KEY) as client:
    quote = await client.quote(symbol="AAPL")
```

## Concurrent Requests

The async design allows efficient concurrent requests:

```python
import asyncio
from fmp_py_client import AsyncFMPClient

async def get_multiple_quotes(symbols: list[str]):
    async with AsyncFMPClient("your-api-key") as client:
        tasks = [client.quote(symbol=s) for s in symbols]
        results = await asyncio.gather(*tasks)
        return dict(zip(symbols, results))

# Get quotes for multiple symbols concurrently
quotes = asyncio.run(get_multiple_quotes(["AAPL", "GOOGL", "MSFT", "AMZN"]))
```

## Connection Pooling

The default httpx client includes connection pooling. For high-throughput applications, you can tune the connection limits:

```python
import httpx
from fmp_py_client import AsyncFMPClient

custom_client = httpx.AsyncClient(
    limits=httpx.Limits(
        max_connections=100,
        max_keepalive_connections=20,
    ),
)

async with AsyncFMPClient("your-api-key", httpx_client=custom_client) as client:
    # High-throughput operations
    pass
```
