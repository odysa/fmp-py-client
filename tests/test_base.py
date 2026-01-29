"""Tests for the base client module."""

import pytest
import httpx

from fmp_client._base import BaseClient, AsyncBaseClient, BASE_URL, API_PREFIX
from fmp_client._exceptions import (
    FMPAPIError,
    FMPAuthenticationError,
    FMPConnectionError,
    FMPNotFoundError,
    FMPRateLimitError,
    FMPTimeoutError,
)


class TestBaseClient:
    """Tests for BaseClient class."""

    def test_init_with_defaults(self, api_key):
        """Test initialization with default values."""
        client = BaseClient(api_key)

        assert client._api_key == api_key
        assert client._base_url == BASE_URL
        assert client._timeout == 30.0

    def test_init_with_custom_values(self, api_key, base_url):
        """Test initialization with custom values."""
        client = BaseClient(api_key, base_url=base_url, timeout=60.0)

        assert client._api_key == api_key
        assert client._base_url == base_url
        assert client._timeout == 60.0

    def test_init_strips_trailing_slash(self, api_key):
        """Test that trailing slashes are stripped from base_url."""
        client = BaseClient(api_key, base_url="https://example.com/")

        assert client._base_url == "https://example.com"

    def test_build_url(self, api_key):
        """Test URL building."""
        client = BaseClient(api_key)
        url = client._build_url("quote")

        assert url == f"{BASE_URL}{API_PREFIX}/quote"

    def test_build_url_with_leading_slash(self, api_key):
        """Test URL building with leading slash in path."""
        client = BaseClient(api_key)
        url = client._build_url("/quote")

        assert url == f"{BASE_URL}{API_PREFIX}/quote"

    def test_build_url_with_custom_base(self, api_key, base_url):
        """Test URL building with custom base URL."""
        client = BaseClient(api_key, base_url=base_url)
        url = client._build_url("profile")

        assert url == f"{base_url}{API_PREFIX}/profile"

    def test_prepare_params_adds_api_key(self, api_key):
        """Test that API key is added to params."""
        client = BaseClient(api_key)
        params = client._prepare_params({})

        assert params == {"apikey": api_key}

    def test_prepare_params_keeps_values(self, api_key):
        """Test that existing params are preserved."""
        client = BaseClient(api_key)
        params = client._prepare_params({"symbol": "AAPL", "limit": 10})

        assert params == {"symbol": "AAPL", "limit": 10, "apikey": api_key}

    def test_prepare_params_removes_none_values(self, api_key):
        """Test that None values are removed from params."""
        client = BaseClient(api_key)
        params = client._prepare_params({"symbol": "AAPL", "limit": None})

        assert params == {"symbol": "AAPL", "apikey": api_key}

    def test_prepare_params_removes_all_none_values(self, api_key):
        """Test that all None values are removed."""
        client = BaseClient(api_key)
        params = client._prepare_params({"a": None, "b": None, "c": "value"})

        assert params == {"c": "value", "apikey": api_key}

    def test_prepare_params_keeps_falsy_non_none_values(self, api_key):
        """Test that falsy non-None values (0, False, '') are preserved."""
        client = BaseClient(api_key)
        params = client._prepare_params({"zero": 0, "false": False, "empty": ""})

        assert params == {"zero": 0, "false": False, "empty": "", "apikey": api_key}


class TestAsyncBaseClient:
    """Tests for AsyncBaseClient class."""

    def test_init_with_defaults(self, api_key):
        """Test initialization with default values."""
        client = AsyncBaseClient(api_key)

        assert client._api_key == api_key
        assert client._base_url == BASE_URL
        assert client._timeout == 30.0
        assert client._owns_client is True
        assert isinstance(client._client, httpx.AsyncClient)

    def test_init_with_custom_httpx_client(self, api_key):
        """Test initialization with custom httpx client."""
        custom_client = httpx.AsyncClient()
        client = AsyncBaseClient(api_key, httpx_client=custom_client)

        assert client._client is custom_client
        assert client._owns_client is False

    @pytest.mark.asyncio
    async def test_context_manager(self, api_key):
        """Test async context manager."""
        async with AsyncBaseClient(api_key) as client:
            assert isinstance(client, AsyncBaseClient)
            assert not client._client.is_closed

    @pytest.mark.asyncio
    async def test_aclose_owned_client(self, api_key):
        """Test closing owned client."""
        client = AsyncBaseClient(api_key)
        await client.aclose()

        assert client._client.is_closed

    @pytest.mark.asyncio
    async def test_aclose_external_client(self, api_key):
        """Test that external client is not closed."""
        custom_client = httpx.AsyncClient()
        client = AsyncBaseClient(api_key, httpx_client=custom_client)
        await client.aclose()

        assert not custom_client.is_closed
        await custom_client.aclose()

    @pytest.mark.asyncio
    async def test_request_success(self, api_key, mock_transport):
        """Test successful request."""
        expected_data = [{"symbol": "AAPL", "price": 150.0}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "apikey" in str(request.url)
            return httpx.Response(200, json=expected_data)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncBaseClient(api_key, httpx_client=http_client)
            result = await client._request("quote", {"symbol": "AAPL"})

        assert result == expected_data

    @pytest.mark.asyncio
    async def test_request_with_no_params(self, api_key, mock_transport):
        """Test request with no params."""
        expected_data = [{"data": "test"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "apikey" in str(request.url)
            return httpx.Response(200, json=expected_data)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncBaseClient(api_key, httpx_client=http_client)
            result = await client._request("some-endpoint")

        assert result == expected_data

    @pytest.mark.asyncio
    async def test_request_authentication_error_401(self, api_key, mock_transport):
        """Test authentication error on 401."""

        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(401, text="Unauthorized")

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncBaseClient(api_key, httpx_client=http_client)

            with pytest.raises(FMPAuthenticationError) as exc_info:
                await client._request("quote")

            assert exc_info.value.status_code == 401
            assert exc_info.value.response_body == "Unauthorized"
            assert "Invalid or missing API key" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_request_authentication_error_403(self, api_key, mock_transport):
        """Test authentication error on 403."""

        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(403, text="Forbidden")

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncBaseClient(api_key, httpx_client=http_client)

            with pytest.raises(FMPAuthenticationError) as exc_info:
                await client._request("quote")

            assert exc_info.value.status_code == 403

    @pytest.mark.asyncio
    async def test_request_rate_limit_error(self, api_key, mock_transport):
        """Test rate limit error on 429."""

        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(
                429,
                text="Rate limit exceeded",
                headers={"Retry-After": "60"},
            )

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncBaseClient(api_key, httpx_client=http_client)

            with pytest.raises(FMPRateLimitError) as exc_info:
                await client._request("quote")

            assert exc_info.value.retry_after == 60.0
            assert exc_info.value.response_body == "Rate limit exceeded"

    @pytest.mark.asyncio
    async def test_request_rate_limit_no_retry_after(self, api_key, mock_transport):
        """Test rate limit error without Retry-After header."""

        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(429, text="Rate limit exceeded")

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncBaseClient(api_key, httpx_client=http_client)

            with pytest.raises(FMPRateLimitError) as exc_info:
                await client._request("quote")

            assert exc_info.value.retry_after is None

    @pytest.mark.asyncio
    async def test_request_not_found_error(self, api_key, mock_transport):
        """Test not found error on 404."""

        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(404, text="Not found")

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncBaseClient(api_key, httpx_client=http_client)

            with pytest.raises(FMPNotFoundError) as exc_info:
                await client._request("nonexistent")

            assert exc_info.value.status_code == 404
            assert "nonexistent" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_request_generic_api_error(self, api_key, mock_transport):
        """Test generic API error on other 4xx/5xx status codes."""

        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(500, text="Internal Server Error")

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncBaseClient(api_key, httpx_client=http_client)

            with pytest.raises(FMPAPIError) as exc_info:
                await client._request("quote")

            assert exc_info.value.status_code == 500
            assert "500" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_request_timeout_error(self, api_key, mock_transport):
        """Test timeout error."""

        def handler(request: httpx.Request) -> httpx.Response:
            raise httpx.TimeoutException("Request timed out")

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncBaseClient(api_key, httpx_client=http_client)

            with pytest.raises(FMPTimeoutError) as exc_info:
                await client._request("quote")

            assert "timed out" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_request_connection_error(self, api_key, mock_transport):
        """Test connection error."""

        def handler(request: httpx.Request) -> httpx.Response:
            raise httpx.ConnectError("Connection refused")

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncBaseClient(api_key, httpx_client=http_client)

            with pytest.raises(FMPConnectionError) as exc_info:
                await client._request("quote")

            assert "Failed to connect" in str(exc_info.value)
