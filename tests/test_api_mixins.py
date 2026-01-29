"""Tests for API mixin modules."""

import pytest
import httpx

from fmp_client import AsyncFMPClient, Period


class TestQuotesMixin:
    """Tests for quotes API endpoints."""

    @pytest.mark.asyncio
    async def test_quote(self, api_key, mock_transport):
        """Test quote endpoint."""
        expected = [{"symbol": "AAPL", "price": 150.0}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/quote" in str(request.url)
            assert "symbol=AAPL" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.quote(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_quote_short(self, api_key, mock_transport):
        """Test quote_short endpoint."""
        expected = [{"symbol": "AAPL", "price": 150.0}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/quote-short" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.quote_short(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_batch_quote(self, api_key, mock_transport):
        """Test batch_quote endpoint."""
        expected = [{"symbol": "AAPL"}, {"symbol": "MSFT"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/batch-quote" in str(request.url)
            assert "symbols=AAPL%2CMSFT" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.batch_quote(symbols="AAPL,MSFT")

        assert result == expected

    @pytest.mark.asyncio
    async def test_aftermarket_trade(self, api_key, mock_transport):
        """Test aftermarket_trade endpoint."""
        expected = [{"symbol": "AAPL", "price": 151.0}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/aftermarket-trade" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.aftermarket_trade(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_batch_mutualfund_quotes(self, api_key, mock_transport):
        """Test batch_mutualfund_quotes endpoint (no params)."""
        expected = [{"symbol": "VTSAX"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/batch-mutualfund-quotes" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.batch_mutualfund_quotes()

        assert result == expected


class TestSearchMixin:
    """Tests for search API endpoints."""

    @pytest.mark.asyncio
    async def test_search_symbol(self, api_key, mock_transport):
        """Test search_symbol endpoint."""
        expected = [{"symbol": "AAPL", "name": "Apple Inc"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/search-symbol" in str(request.url)
            assert "query=apple" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.search_symbol(query="apple", limit=10)

        assert result == expected

    @pytest.mark.asyncio
    async def test_search_name(self, api_key, mock_transport):
        """Test search_name endpoint."""
        expected = [{"symbol": "AAPL", "name": "Apple Inc"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/search-name" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.search_name(query="Apple", exchange="NASDAQ")

        assert result == expected

    @pytest.mark.asyncio
    async def test_search_cik(self, api_key, mock_transport):
        """Test search_cik endpoint."""
        expected = [{"symbol": "AAPL", "cik": 320193}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/search-cik" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.search_cik(cik=320193)

        assert result == expected

    @pytest.mark.asyncio
    async def test_search_cusip(self, api_key, mock_transport):
        """Test search_cusip endpoint."""
        expected = [{"symbol": "AAPL", "cusip": "037833100"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/search-cusip" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.search_cusip(cusip="037833100")

        assert result == expected


class TestCompanyMixin:
    """Tests for company API endpoints."""

    @pytest.mark.asyncio
    async def test_profile(self, api_key, mock_transport):
        """Test profile endpoint."""
        expected = [{"symbol": "AAPL", "companyName": "Apple Inc"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/profile" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.profile(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_company_screener(self, api_key, mock_transport):
        """Test company_screener endpoint with multiple params."""
        expected = [{"symbol": "AAPL"}, {"symbol": "MSFT"}]

        def handler(request: httpx.Request) -> httpx.Response:
            url_str = str(request.url)
            assert "/stable/company-screener" in url_str
            assert "sector=Technology" in url_str
            assert "marketCapMoreThan=1000000000" in url_str
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.company_screener(
                market_cap_more_than=1000000000,
                sector="Technology",
                limit=10,
            )

        assert result == expected

    @pytest.mark.asyncio
    async def test_key_executives(self, api_key, mock_transport):
        """Test key_executives endpoint."""
        expected = [{"name": "Tim Cook", "title": "CEO"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/key-executives" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.key_executives(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_market_capitalization(self, api_key, mock_transport):
        """Test market_capitalization endpoint."""
        expected = [{"symbol": "AAPL", "marketCap": 3000000000000}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/market-capitalization" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.market_capitalization(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_executive_compensation_benchmark(self, api_key, mock_transport):
        """Test executive_compensation_benchmark endpoint (no params)."""
        expected = [{"industry": "Technology", "avgCompensation": 15000000}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/executive-compensation-benchmark" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.executive_compensation_benchmark()

        assert result == expected


class TestFinancialsMixin:
    """Tests for financial statements API endpoints."""

    @pytest.mark.asyncio
    async def test_income_statement(self, api_key, mock_transport):
        """Test income_statement endpoint."""
        expected = [{"symbol": "AAPL", "revenue": 400000000000}]

        def handler(request: httpx.Request) -> httpx.Response:
            url_str = str(request.url)
            assert "/stable/income-statement" in url_str
            assert "period=annual" in url_str
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.income_statement(
                symbol="AAPL", period=Period.ANNUAL, limit=5
            )

        assert result == expected

    @pytest.mark.asyncio
    async def test_balance_sheet_statement(self, api_key, mock_transport):
        """Test balance_sheet_statement endpoint."""
        expected = [{"symbol": "AAPL", "totalAssets": 350000000000}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/balance-sheet-statement" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.balance_sheet_statement(
                symbol="AAPL", period=Period.QUARTER
            )

        assert result == expected

    @pytest.mark.asyncio
    async def test_cash_flow_statement(self, api_key, mock_transport):
        """Test cash_flow_statement endpoint."""
        expected = [{"symbol": "AAPL", "operatingCashFlow": 100000000000}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/cash-flow-statement" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.cash_flow_statement(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_income_statement_ttm(self, api_key, mock_transport):
        """Test income_statement_ttm endpoint."""
        expected = [{"symbol": "AAPL", "revenueTTM": 400000000000}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/income-statement-ttm" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.income_statement_ttm(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_financial_growth(self, api_key, mock_transport):
        """Test financial_growth endpoint."""
        expected = [{"symbol": "AAPL", "revenueGrowth": 0.08}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/financial-growth" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.financial_growth(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_income_statement_bulk(self, api_key, mock_transport):
        """Test income_statement_bulk endpoint."""
        expected = [{"symbol": "AAPL"}, {"symbol": "MSFT"}]

        def handler(request: httpx.Request) -> httpx.Response:
            url_str = str(request.url)
            assert "/stable/income-statement-bulk" in url_str
            assert "year=2023" in url_str
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.income_statement_bulk(year=2023, period=Period.ANNUAL)

        assert result == expected


class TestHistoricalMixin:
    """Tests for historical price API endpoints."""

    @pytest.mark.asyncio
    async def test_historical_price_eod_light(self, api_key, mock_transport):
        """Test historical_price_eod_light endpoint."""
        expected = [{"date": "2024-01-01", "close": 150.0}]

        def handler(request: httpx.Request) -> httpx.Response:
            url_str = str(request.url)
            assert "/stable/historical-price-eod/light" in url_str
            assert "symbol=AAPL" in url_str
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_price_eod_light(
                "AAPL", from_date="2024-01-01", to_date="2024-01-31"
            )

        assert result == expected

    @pytest.mark.asyncio
    async def test_historical_price_eod_full(self, api_key, mock_transport):
        """Test historical_price_eod_full endpoint."""
        expected = [{"date": "2024-01-01", "open": 149.0, "close": 150.0}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-price-eod/full" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_price_eod_full("AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_historical_chart_1min(self, api_key, mock_transport):
        """Test historical_chart_1min endpoint."""
        expected = [{"date": "2024-01-01 09:30:00", "close": 150.0}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-chart/1min" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_chart_1min("AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_historical_chart_4hour(self, api_key, mock_transport):
        """Test historical_chart_4hour endpoint."""
        expected = [{"date": "2024-01-01 12:00:00", "close": 151.0}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-chart/4hour" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_chart_4hour("AAPL")

        assert result == expected


class TestModuleImports:
    """Tests for module imports and exports."""

    def test_main_module_exports(self):
        """Test that main module exports expected items."""
        from fmp_client import (
            AsyncFMPClient,
            FMPAPIError,
            FMPAuthenticationError,
            FMPConnectionError,
            FMPError,
            FMPNotFoundError,
            FMPRateLimitError,
            FMPTimeoutError,
            Period,
            Timeframe,
        )

        assert AsyncFMPClient is not None
        assert FMPError is not None
        assert FMPAPIError is not None
        assert FMPAuthenticationError is not None
        assert FMPConnectionError is not None
        assert FMPNotFoundError is not None
        assert FMPRateLimitError is not None
        assert FMPTimeoutError is not None
        assert Period is not None
        assert Timeframe is not None

    def test_all_exports_match(self):
        """Test that __all__ contains the expected exports."""
        import fmp_client

        expected_exports = {
            "AsyncFMPClient",
            "FMPAPIError",
            "FMPAuthenticationError",
            "FMPConnectionError",
            "FMPError",
            "FMPNotFoundError",
            "FMPRateLimitError",
            "FMPTimeoutError",
            "Period",
            "Timeframe",
        }

        assert set(fmp_client.__all__) == expected_exports
