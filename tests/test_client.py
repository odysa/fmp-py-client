"""Tests for the AsyncFMPClient."""

import pytest
import httpx

from fmp_client import AsyncFMPClient
from fmp_client._base import BASE_URL


class TestAsyncFMPClient:
    """Tests for AsyncFMPClient class."""

    def test_init_with_defaults(self, api_key):
        """Test initialization with default values."""
        client = AsyncFMPClient(api_key)

        assert client._api_key == api_key
        assert client._base_url == BASE_URL
        assert client._timeout == 30.0
        assert client._owns_client is True

    def test_init_with_custom_values(self, api_key, base_url):
        """Test initialization with custom values."""
        client = AsyncFMPClient(
            api_key,
            base_url=base_url,
            timeout=60.0,
        )

        assert client._api_key == api_key
        assert client._base_url == base_url
        assert client._timeout == 60.0

    def test_init_with_custom_httpx_client(self, api_key):
        """Test initialization with custom httpx client."""
        custom_client = httpx.AsyncClient()
        client = AsyncFMPClient(api_key, httpx_client=custom_client)

        assert client._client is custom_client
        assert client._owns_client is False

    @pytest.mark.asyncio
    async def test_context_manager(self, api_key):
        """Test async context manager."""
        async with AsyncFMPClient(api_key) as client:
            assert isinstance(client, AsyncFMPClient)
            assert not client._client.is_closed

    @pytest.mark.asyncio
    async def test_has_search_methods(self, api_key):
        """Test that client has search mixin methods."""
        async with AsyncFMPClient(api_key) as client:
            assert hasattr(client, "search_symbol")
            assert hasattr(client, "search_name")
            assert hasattr(client, "search_cik")
            assert hasattr(client, "search_cusip")
            assert hasattr(client, "search_isin")

    @pytest.mark.asyncio
    async def test_has_company_methods(self, api_key):
        """Test that client has company mixin methods."""
        async with AsyncFMPClient(api_key) as client:
            assert hasattr(client, "profile")
            assert hasattr(client, "company_screener")
            assert hasattr(client, "key_executives")
            assert hasattr(client, "employee_count")

    @pytest.mark.asyncio
    async def test_has_quotes_methods(self, api_key):
        """Test that client has quotes mixin methods."""
        async with AsyncFMPClient(api_key) as client:
            assert hasattr(client, "quote")
            assert hasattr(client, "quote_short")
            assert hasattr(client, "batch_quote")

    @pytest.mark.asyncio
    async def test_has_financial_methods(self, api_key):
        """Test that client has financial mixin methods."""
        async with AsyncFMPClient(api_key) as client:
            assert hasattr(client, "income_statement")
            assert hasattr(client, "balance_sheet_statement")
            assert hasattr(client, "cash_flow_statement")

    @pytest.mark.asyncio
    async def test_has_historical_methods(self, api_key):
        """Test that client has historical mixin methods."""
        async with AsyncFMPClient(api_key) as client:
            assert hasattr(client, "historical_price_eod_light")
            assert hasattr(client, "historical_chart_1min")

    @pytest.mark.asyncio
    async def test_quote_request(self, api_key, mock_transport):
        """Test quote request integration."""
        expected_data = [{"symbol": "AAPL", "price": 150.0}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "quote" in str(request.url)
            assert "symbol=AAPL" in str(request.url)
            return httpx.Response(200, json=expected_data)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.quote(symbol="AAPL")

        assert result == expected_data

    @pytest.mark.asyncio
    async def test_search_symbol_request(self, api_key, mock_transport):
        """Test search_symbol request integration."""
        expected_data = [{"symbol": "AAPL", "name": "Apple Inc"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "search-symbol" in str(request.url)
            return httpx.Response(200, json=expected_data)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.search_symbol(query="AAPL", limit=10)

        assert result == expected_data

    @pytest.mark.asyncio
    async def test_profile_request(self, api_key, mock_transport):
        """Test profile request integration."""
        expected_data = [{"symbol": "AAPL", "companyName": "Apple Inc"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "profile" in str(request.url)
            return httpx.Response(200, json=expected_data)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.profile(symbol="AAPL")

        assert result == expected_data

    @pytest.mark.asyncio
    async def test_company_screener_request(self, api_key, mock_transport):
        """Test company_screener request integration."""
        expected_data = [{"symbol": "AAPL"}, {"symbol": "MSFT"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "company-screener" in str(request.url)
            return httpx.Response(200, json=expected_data)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.company_screener(
                market_cap_more_than=1000000000,
                sector="Technology",
                limit=10,
            )

        assert result == expected_data
