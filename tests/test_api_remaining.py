"""Tests for remaining API mixin modules to achieve 80%+ coverage."""

import pytest
import httpx

from fmp_py_client import AsyncFMPClient


class TestCompanyMixinRemaining:
    """Tests for remaining company API endpoints."""

    @pytest.mark.asyncio
    async def test_profile_cik(self, api_key, mock_transport):
        """Test profile_cik endpoint."""
        expected = [{"symbol": "AAPL", "cik": 320193}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/profile-cik" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.profile_cik(cik=320193)

        assert result == expected

    @pytest.mark.asyncio
    async def test_company_notes(self, api_key, mock_transport):
        """Test company_notes endpoint."""
        expected = [{"symbol": "AAPL", "notes": "..."}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/company-notes" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.company_notes(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_stock_peers(self, api_key, mock_transport):
        """Test stock_peers endpoint."""
        expected = [{"symbol": "AAPL", "peers": ["MSFT", "GOOG"]}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/stock-peers" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.stock_peers(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_executive_compensation(self, api_key, mock_transport):
        """Test executive_compensation endpoint."""
        expected = [{"name": "Tim Cook", "compensation": 99000000}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/governance-executive-compensation" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.executive_compensation(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_employee_count(self, api_key, mock_transport):
        """Test employee_count endpoint."""
        expected = [{"symbol": "AAPL", "employeeCount": 164000}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/employee-count" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.employee_count(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_historical_employee_count(self, api_key, mock_transport):
        """Test historical_employee_count endpoint."""
        expected = [{"date": "2023-09-30", "employeeCount": 161000}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-employee-count" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_employee_count(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_market_capitalization_batch(self, api_key, mock_transport):
        """Test market_capitalization_batch endpoint."""
        expected = [{"symbol": "AAPL"}, {"symbol": "MSFT"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/market-capitalization-batch" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.market_capitalization_batch(symbols="AAPL,MSFT")

        assert result == expected

    @pytest.mark.asyncio
    async def test_historical_market_capitalization(self, api_key, mock_transport):
        """Test historical_market_capitalization endpoint."""
        expected = [{"date": "2024-01-01", "marketCap": 2800000000000}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-market-capitalization" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_market_capitalization(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_shares_float(self, api_key, mock_transport):
        """Test shares_float endpoint."""
        expected = [{"symbol": "AAPL", "floatShares": 15500000000}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/shares-float" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.shares_float(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_shares_float_all(self, api_key, mock_transport):
        """Test shares_float_all endpoint."""
        expected = [{"symbol": "AAPL"}, {"symbol": "MSFT"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/shares-float-all" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.shares_float_all(page=0, limit=10)

        assert result == expected


class TestQuotesMixinRemaining:
    """Tests for remaining quotes API endpoints."""

    @pytest.mark.asyncio
    async def test_aftermarket_quote(self, api_key, mock_transport):
        """Test aftermarket_quote endpoint."""
        expected = [{"symbol": "AAPL", "price": 151.50}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/aftermarket-quote" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.aftermarket_quote(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_stock_price_change(self, api_key, mock_transport):
        """Test stock_price_change endpoint."""
        expected = [{"symbol": "AAPL", "change1D": 1.5}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/stock-price-change" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.stock_price_change(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_batch_quote_short(self, api_key, mock_transport):
        """Test batch_quote_short endpoint."""
        expected = [{"symbol": "AAPL"}, {"symbol": "MSFT"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/batch-quote-short" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.batch_quote_short(symbols="AAPL,MSFT")

        assert result == expected

    @pytest.mark.asyncio
    async def test_batch_aftermarket_trade(self, api_key, mock_transport):
        """Test batch_aftermarket_trade endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/batch-aftermarket-trade" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.batch_aftermarket_trade(symbols="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_batch_aftermarket_quote(self, api_key, mock_transport):
        """Test batch_aftermarket_quote endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/batch-aftermarket-quote" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.batch_aftermarket_quote(symbols="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_batch_exchange_quote(self, api_key, mock_transport):
        """Test batch_exchange_quote endpoint."""
        expected = [{"symbol": "AAPL"}, {"symbol": "MSFT"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/batch-exchange-quote" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.batch_exchange_quote(exchange="NASDAQ")

        assert result == expected

    @pytest.mark.asyncio
    async def test_batch_etf_quotes(self, api_key, mock_transport):
        """Test batch_etf_quotes endpoint."""
        expected = [{"symbol": "SPY"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/batch-etf-quotes" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.batch_etf_quotes()

        assert result == expected

    @pytest.mark.asyncio
    async def test_batch_commodity_quotes(self, api_key, mock_transport):
        """Test batch_commodity_quotes endpoint."""
        expected = [{"symbol": "GCUSD"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/batch-commodity-quotes" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.batch_commodity_quotes()

        assert result == expected

    @pytest.mark.asyncio
    async def test_batch_crypto_quotes(self, api_key, mock_transport):
        """Test batch_crypto_quotes endpoint."""
        expected = [{"symbol": "BTCUSD"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/batch-crypto-quotes" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.batch_crypto_quotes()

        assert result == expected

    @pytest.mark.asyncio
    async def test_batch_forex_quotes(self, api_key, mock_transport):
        """Test batch_forex_quotes endpoint."""
        expected = [{"symbol": "EURUSD"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/batch-forex-quotes" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.batch_forex_quotes()

        assert result == expected

    @pytest.mark.asyncio
    async def test_batch_index_quotes(self, api_key, mock_transport):
        """Test batch_index_quotes endpoint."""
        expected = [{"symbol": "^GSPC"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/batch-index-quotes" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.batch_index_quotes()

        assert result == expected


class TestSearchMixinRemaining:
    """Tests for remaining search API endpoints."""

    @pytest.mark.asyncio
    async def test_search_isin(self, api_key, mock_transport):
        """Test search_isin endpoint."""
        expected = [{"symbol": "AAPL", "isin": "US0378331005"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/search-isin" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.search_isin(isin="US0378331005")

        assert result == expected

    @pytest.mark.asyncio
    async def test_search_exchange_variants(self, api_key, mock_transport):
        """Test search_exchange_variants endpoint."""
        expected = [{"symbol": "AAPL.US"}, {"symbol": "AAPL.DE"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/search-exchange-variants" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.search_exchange_variants(symbol="AAPL")

        assert result == expected


class TestHistoricalMixinRemaining:
    """Tests for remaining historical API endpoints."""

    @pytest.mark.asyncio
    async def test_historical_price_eod_non_split_adjusted(
        self, api_key, mock_transport
    ):
        """Test historical_price_eod_non_split_adjusted endpoint."""
        expected = [{"date": "2024-01-01", "close": 150.0}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-price-eod/non-split-adjusted" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_price_eod_non_split_adjusted("AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_historical_price_eod_dividend_adjusted(
        self, api_key, mock_transport
    ):
        """Test historical_price_eod_dividend_adjusted endpoint."""
        expected = [{"date": "2024-01-01", "close": 149.5}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-price-eod/dividend-adjusted" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_price_eod_dividend_adjusted("AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_historical_chart_5min(self, api_key, mock_transport):
        """Test historical_chart_5min endpoint."""
        expected = [{"date": "2024-01-01 09:35:00", "close": 150.0}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-chart/5min" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_chart_5min("AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_historical_chart_15min(self, api_key, mock_transport):
        """Test historical_chart_15min endpoint."""
        expected = [{"date": "2024-01-01 09:45:00", "close": 150.5}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-chart/15min" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_chart_15min("AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_historical_chart_30min(self, api_key, mock_transport):
        """Test historical_chart_30min endpoint."""
        expected = [{"date": "2024-01-01 10:00:00", "close": 151.0}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-chart/30min" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_chart_30min("AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_historical_chart_1hour(self, api_key, mock_transport):
        """Test historical_chart_1hour endpoint."""
        expected = [{"date": "2024-01-01 10:30:00", "close": 151.5}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-chart/1hour" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_chart_1hour("AAPL")

        assert result == expected


class TestFinancialsMixinRemaining:
    """Tests for remaining financials API endpoints."""

    @pytest.mark.asyncio
    async def test_balance_sheet_statement_ttm(self, api_key, mock_transport):
        """Test balance_sheet_statement_ttm endpoint."""
        expected = [{"symbol": "AAPL", "totalAssetsTTM": 350000000000}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/balance-sheet-statement-ttm" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.balance_sheet_statement_ttm(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_cash_flow_statement_ttm(self, api_key, mock_transport):
        """Test cash_flow_statement_ttm endpoint."""
        expected = [{"symbol": "AAPL", "operatingCashFlowTTM": 100000000000}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/cash-flow-statement-ttm" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.cash_flow_statement_ttm(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_latest_financial_statements(self, api_key, mock_transport):
        """Test latest_financial_statements endpoint."""
        expected = [{"symbol": "AAPL"}, {"symbol": "MSFT"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/latest-financial-statements" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.latest_financial_statements(page=0, limit=10)

        assert result == expected

    @pytest.mark.asyncio
    async def test_income_statement_growth(self, api_key, mock_transport):
        """Test income_statement_growth endpoint."""
        expected = [{"symbol": "AAPL", "revenueGrowth": 0.08}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/income-statement-growth" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.income_statement_growth(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_balance_sheet_statement_growth(self, api_key, mock_transport):
        """Test balance_sheet_statement_growth endpoint."""
        expected = [{"symbol": "AAPL", "totalAssetsGrowth": 0.05}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/balance-sheet-statement-growth" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.balance_sheet_statement_growth(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_cash_flow_statement_growth(self, api_key, mock_transport):
        """Test cash_flow_statement_growth endpoint."""
        expected = [{"symbol": "AAPL", "operatingCashFlowGrowth": 0.10}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/cash-flow-statement-growth" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.cash_flow_statement_growth(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_income_statement_as_reported(self, api_key, mock_transport):
        """Test income_statement_as_reported endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/income-statement-as-reported" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.income_statement_as_reported(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_balance_sheet_statement_as_reported(self, api_key, mock_transport):
        """Test balance_sheet_statement_as_reported endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/balance-sheet-statement-as-reported" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.balance_sheet_statement_as_reported(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_cash_flow_statement_as_reported(self, api_key, mock_transport):
        """Test cash_flow_statement_as_reported endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/cash-flow-statement-as-reported" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.cash_flow_statement_as_reported(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_financial_statement_full_as_reported(self, api_key, mock_transport):
        """Test financial_statement_full_as_reported endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/financial-statement-full-as-reported" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.financial_statement_full_as_reported(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_financial_reports_dates(self, api_key, mock_transport):
        """Test financial_reports_dates endpoint."""
        expected = [{"date": "2024-01-01"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/financial-reports-dates" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.financial_reports_dates(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_financial_reports_json(self, api_key, mock_transport):
        """Test financial_reports_json endpoint."""
        expected = {"symbol": "AAPL", "data": {}}

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/financial-reports-json" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.financial_reports_json(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_revenue_product_segmentation(self, api_key, mock_transport):
        """Test revenue_product_segmentation endpoint."""
        expected = [{"symbol": "AAPL", "product": "iPhone"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/revenue-product-segmentation" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.revenue_product_segmentation(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_revenue_geographic_segmentation(self, api_key, mock_transport):
        """Test revenue_geographic_segmentation endpoint."""
        expected = [{"symbol": "AAPL", "region": "Americas"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/revenue-geographic-segmentation" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.revenue_geographic_segmentation(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_balance_sheet_statement_bulk(self, api_key, mock_transport):
        """Test balance_sheet_statement_bulk endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/balance-sheet-statement-bulk" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.balance_sheet_statement_bulk(year=2023)

        assert result == expected

    @pytest.mark.asyncio
    async def test_cash_flow_statement_bulk(self, api_key, mock_transport):
        """Test cash_flow_statement_bulk endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/cash-flow-statement-bulk" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.cash_flow_statement_bulk(year=2023)

        assert result == expected

    @pytest.mark.asyncio
    async def test_financial_reports_xlsx(self, api_key, mock_transport):
        """Test financial_reports_xlsx endpoint."""
        expected = {"data": "xlsx_content"}

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/financial-reports-xlsx" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.financial_reports_xlsx(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_income_statement_growth_bulk(self, api_key, mock_transport):
        """Test income_statement_growth_bulk endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/income-statement-growth-bulk" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.income_statement_growth_bulk(year=2023)

        assert result == expected

    @pytest.mark.asyncio
    async def test_balance_sheet_statement_growth_bulk(self, api_key, mock_transport):
        """Test balance_sheet_statement_growth_bulk endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/balance-sheet-statement-growth-bulk" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.balance_sheet_statement_growth_bulk(year=2023)

        assert result == expected

    @pytest.mark.asyncio
    async def test_cash_flow_statement_growth_bulk(self, api_key, mock_transport):
        """Test cash_flow_statement_growth_bulk endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/cash-flow-statement-growth-bulk" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.cash_flow_statement_growth_bulk(year=2023)

        assert result == expected
