# Exceptions

The FMP Client provides a hierarchy of exception classes for precise error handling.

## Exception Hierarchy

```
FMPError (base)
├── FMPAPIError
│   ├── FMPAuthenticationError (401/403)
│   ├── FMPRateLimitError (429)
│   └── FMPNotFoundError (404)
├── FMPConnectionError
└── FMPTimeoutError
```

## Base Exceptions

### FMPError

Base exception for all FMP client errors.

```python
from fmp_py_client import FMPError

try:
    result = await client.quote(symbol="AAPL")
except FMPError as e:
    print(f"FMP error: {e.message}")
```

**Attributes:**

| Name | Type | Description |
|------|------|-------------|
| `message` | `str` | Error message |

## API Errors

### FMPAPIError

Error returned by the FMP API (non-2xx response).

```python
from fmp_py_client import FMPAPIError

try:
    result = await client.quote(symbol="AAPL")
except FMPAPIError as e:
    print(f"API error {e.status_code}: {e.message}")
    print(f"Response: {e.response_body}")
```

**Attributes:**

| Name | Type | Description |
|------|------|-------------|
| `message` | `str` | Error message |
| `status_code` | `int` | HTTP status code |
| `response_body` | `str \| None` | Raw response body |

---

### FMPAuthenticationError

API key is invalid or missing (HTTP 401/403).

```python
from fmp_py_client import FMPAuthenticationError

try:
    result = await client.quote(symbol="AAPL")
except FMPAuthenticationError as e:
    print("Invalid API key!")
    print(f"Status: {e.status_code}")
```

**Inherits from:** `FMPAPIError`

---

### FMPRateLimitError

Rate limit exceeded (HTTP 429).

```python
import asyncio
from fmp_py_client import FMPRateLimitError

try:
    result = await client.quote(symbol="AAPL")
except FMPRateLimitError as e:
    print(f"Rate limited! Retry after: {e.retry_after} seconds")
    if e.retry_after:
        await asyncio.sleep(e.retry_after)
        # Retry the request
```

**Attributes:**

| Name | Type | Description |
|------|------|-------------|
| `retry_after` | `float \| None` | Seconds to wait before retrying |

**Inherits from:** `FMPAPIError`

---

### FMPNotFoundError

Requested resource not found (HTTP 404).

```python
from fmp_py_client import FMPNotFoundError

try:
    result = await client.quote(symbol="INVALID_SYMBOL")
except FMPNotFoundError as e:
    print(f"Symbol not found: {e.message}")
```

**Inherits from:** `FMPAPIError`

## Network Errors

### FMPConnectionError

Network-level connection error.

```python
from fmp_py_client import FMPConnectionError

try:
    result = await client.quote(symbol="AAPL")
except FMPConnectionError as e:
    print(f"Connection failed: {e.message}")
```

---

### FMPTimeoutError

Request timed out.

```python
from fmp_py_client import FMPTimeoutError

try:
    result = await client.quote(symbol="AAPL")
except FMPTimeoutError as e:
    print(f"Request timed out: {e.message}")
```

## Best Practices

### Catch Specific Exceptions First

```python
from fmp_py_client import (
    AsyncFMPClient,
    FMPAuthenticationError,
    FMPRateLimitError,
    FMPNotFoundError,
    FMPAPIError,
    FMPConnectionError,
    FMPTimeoutError,
    FMPError,
)

async with AsyncFMPClient(api_key) as client:
    try:
        result = await client.quote(symbol="AAPL")
    except FMPAuthenticationError:
        # Handle invalid API key
        print("Check your API key")
    except FMPRateLimitError as e:
        # Handle rate limiting
        print(f"Wait {e.retry_after} seconds")
    except FMPNotFoundError:
        # Handle missing resource
        print("Symbol not found")
    except FMPAPIError as e:
        # Handle other API errors
        print(f"API error: {e.status_code}")
    except FMPConnectionError:
        # Handle network issues
        print("Network connection failed")
    except FMPTimeoutError:
        # Handle timeout
        print("Request timed out")
    except FMPError as e:
        # Catch-all for any FMP error
        print(f"Unexpected error: {e.message}")
```

### Implement Retry Logic

```python
import asyncio
from fmp_py_client import (
    AsyncFMPClient,
    FMPRateLimitError,
    FMPTimeoutError,
    FMPConnectionError,
)

async def fetch_with_retry(client, symbol: str, max_retries: int = 3):
    for attempt in range(max_retries):
        try:
            return await client.quote(symbol=symbol)
        except FMPRateLimitError as e:
            wait_time = e.retry_after or (2 ** attempt)
            print(f"Rate limited, waiting {wait_time}s...")
            await asyncio.sleep(wait_time)
        except (FMPTimeoutError, FMPConnectionError) as e:
            wait_time = 2 ** attempt
            print(f"Network error, retrying in {wait_time}s...")
            await asyncio.sleep(wait_time)
    raise Exception(f"Failed after {max_retries} retries")
```
