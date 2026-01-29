"""Additional tests for API mixin modules to improve coverage."""

import pytest
import httpx

from fmp_client import AsyncFMPClient


class TestCalendarMixin:
    """Tests for calendar API endpoints."""

    @pytest.mark.asyncio
    async def test_dividends(self, api_key, mock_transport):
        """Test dividends endpoint."""
        expected = [{"date": "2024-01-15", "dividend": 0.24}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/dividends" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.dividends(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_dividends_calendar(self, api_key, mock_transport):
        """Test dividends_calendar endpoint."""
        expected = [{"symbol": "AAPL", "date": "2024-01-15"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/dividends-calendar" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.dividends_calendar()

        assert result == expected

    @pytest.mark.asyncio
    async def test_splits(self, api_key, mock_transport):
        """Test splits endpoint."""
        expected = [{"date": "2020-08-31", "ratio": "4:1"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/splits" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.splits(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_splits_calendar(self, api_key, mock_transport):
        """Test splits_calendar endpoint."""
        expected = [{"symbol": "XYZ", "date": "2024-02-01"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/splits-calendar" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.splits_calendar()

        assert result == expected

    @pytest.mark.asyncio
    async def test_earnings(self, api_key, mock_transport):
        """Test earnings endpoint."""
        expected = [{"date": "2024-01-25", "eps": 2.18}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/earnings" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.earnings(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_earnings_calendar(self, api_key, mock_transport):
        """Test earnings_calendar endpoint."""
        expected = [{"symbol": "AAPL", "date": "2024-01-25"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/earnings-calendar" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.earnings_calendar()

        assert result == expected

    @pytest.mark.asyncio
    async def test_earning_call_transcript(self, api_key, mock_transport):
        """Test earning_call_transcript endpoint."""
        expected = [{"symbol": "AAPL", "content": "..."}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/earning-call-transcript" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.earning_call_transcript(
                symbol="AAPL", quarter=1, year=2024
            )

        assert result == expected

    @pytest.mark.asyncio
    async def test_earning_call_transcript_latest(self, api_key, mock_transport):
        """Test earning_call_transcript_latest endpoint."""
        expected = [{"symbol": "AAPL", "content": "latest..."}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/earning-call-transcript-latest" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.earning_call_transcript_latest()

        assert result == expected

    @pytest.mark.asyncio
    async def test_earning_call_transcript_dates(self, api_key, mock_transport):
        """Test earning_call_transcript_dates endpoint."""
        expected = [{"date": "2024-01-25", "quarter": 1}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/earning-call-transcript-dates" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.earning_call_transcript_dates(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_earnings_transcript_list(self, api_key, mock_transport):
        """Test earnings_transcript_list endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/earnings-transcript-list" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.earnings_transcript_list()

        assert result == expected

    @pytest.mark.asyncio
    async def test_ipos_calendar(self, api_key, mock_transport):
        """Test ipos_calendar endpoint."""
        expected = [{"symbol": "XYZ", "date": "2024-02-01"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/ipos-calendar" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.ipos_calendar()

        assert result == expected

    @pytest.mark.asyncio
    async def test_ipos_disclosure(self, api_key, mock_transport):
        """Test ipos_disclosure endpoint."""
        expected = [{"symbol": "XYZ", "disclosure": "..."}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/ipos-disclosure" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.ipos_disclosure()

        assert result == expected


class TestMarketMixin:
    """Tests for market API endpoints."""

    @pytest.mark.asyncio
    async def test_stock_list(self, api_key, mock_transport):
        """Test stock_list endpoint."""
        expected = [{"symbol": "AAPL"}, {"symbol": "MSFT"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/stock-list" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.stock_list()

        assert result == expected

    @pytest.mark.asyncio
    async def test_financial_statement_symbol_list(self, api_key, mock_transport):
        """Test financial_statement_symbol_list endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/financial-statement-symbol-list" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.financial_statement_symbol_list()

        assert result == expected

    @pytest.mark.asyncio
    async def test_cik_list(self, api_key, mock_transport):
        """Test cik_list endpoint."""
        expected = [{"cik": 320193, "symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/cik-list" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.cik_list(page=0, limit=10)

        assert result == expected

    @pytest.mark.asyncio
    async def test_symbol_change(self, api_key, mock_transport):
        """Test symbol_change endpoint."""
        expected = [{"oldSymbol": "FB", "newSymbol": "META"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/symbol-change" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.symbol_change()

        assert result == expected

    @pytest.mark.asyncio
    async def test_etf_list(self, api_key, mock_transport):
        """Test etf_list endpoint."""
        expected = [{"symbol": "SPY"}, {"symbol": "QQQ"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/etf-list" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.etf_list()

        assert result == expected

    @pytest.mark.asyncio
    async def test_actively_trading_list(self, api_key, mock_transport):
        """Test actively_trading_list endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/actively-trading-list" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.actively_trading_list()

        assert result == expected

    @pytest.mark.asyncio
    async def test_delisted_companies(self, api_key, mock_transport):
        """Test delisted_companies endpoint."""
        expected = [{"symbol": "XYZ", "delistedDate": "2023-01-01"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/delisted-companies" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.delisted_companies(page=0, limit=10)

        assert result == expected

    @pytest.mark.asyncio
    async def test_available_exchanges(self, api_key, mock_transport):
        """Test available_exchanges endpoint."""
        expected = [{"exchange": "NASDAQ"}, {"exchange": "NYSE"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/available-exchanges" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.available_exchanges()

        assert result == expected

    @pytest.mark.asyncio
    async def test_available_sectors(self, api_key, mock_transport):
        """Test available_sectors endpoint."""
        expected = [{"sector": "Technology"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/available-sectors" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.available_sectors()

        assert result == expected

    @pytest.mark.asyncio
    async def test_available_industries(self, api_key, mock_transport):
        """Test available_industries endpoint."""
        expected = [{"industry": "Software"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/available-industries" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.available_industries()

        assert result == expected

    @pytest.mark.asyncio
    async def test_available_countries(self, api_key, mock_transport):
        """Test available_countries endpoint."""
        expected = [{"country": "US"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/available-countries" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.available_countries()

        assert result == expected

    @pytest.mark.asyncio
    async def test_index_list(self, api_key, mock_transport):
        """Test index_list endpoint."""
        expected = [{"symbol": "^GSPC"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/index-list" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.index_list()

        assert result == expected

    @pytest.mark.asyncio
    async def test_sp500_constituent(self, api_key, mock_transport):
        """Test sp500_constituent endpoint."""
        expected = [{"symbol": "AAPL"}, {"symbol": "MSFT"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/sp500-constituent" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.sp500_constituent()

        assert result == expected

    @pytest.mark.asyncio
    async def test_nasdaq_constituent(self, api_key, mock_transport):
        """Test nasdaq_constituent endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/nasdaq-constituent" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.nasdaq_constituent()

        assert result == expected

    @pytest.mark.asyncio
    async def test_dowjones_constituent(self, api_key, mock_transport):
        """Test dowjones_constituent endpoint."""
        expected = [{"symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/dowjones-constituent" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.dowjones_constituent()

        assert result == expected

    @pytest.mark.asyncio
    async def test_historical_sp500_constituent(self, api_key, mock_transport):
        """Test historical_sp500_constituent endpoint."""
        expected = [{"date": "2023-01-01", "symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-sp500-constituent" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_sp500_constituent()

        assert result == expected

    @pytest.mark.asyncio
    async def test_historical_nasdaq_constituent(self, api_key, mock_transport):
        """Test historical_nasdaq_constituent endpoint."""
        expected = [{"date": "2023-01-01", "symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-nasdaq-constituent" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_nasdaq_constituent()

        assert result == expected

    @pytest.mark.asyncio
    async def test_historical_dowjones_constituent(self, api_key, mock_transport):
        """Test historical_dowjones_constituent endpoint."""
        expected = [{"date": "2023-01-01", "symbol": "AAPL"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/historical-dowjones-constituent" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.historical_dowjones_constituent()

        assert result == expected


class TestNewsMixin:
    """Tests for news API endpoints."""

    @pytest.mark.asyncio
    async def test_fmp_articles(self, api_key, mock_transport):
        """Test fmp_articles endpoint."""
        expected = [{"title": "Article", "content": "..."}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/fmp-articles" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.fmp_articles(page=0, limit=10)

        assert result == expected

    @pytest.mark.asyncio
    async def test_news_general_latest(self, api_key, mock_transport):
        """Test news_general_latest endpoint."""
        expected = [{"title": "News", "content": "..."}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/news/general-latest" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.news_general_latest(page=0, limit=10)

        assert result == expected

    @pytest.mark.asyncio
    async def test_news_press_releases_latest(self, api_key, mock_transport):
        """Test news_press_releases_latest endpoint."""
        expected = [{"title": "Press Release"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/news/press-releases-latest" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.news_press_releases_latest(page=0, limit=10)

        assert result == expected

    @pytest.mark.asyncio
    async def test_news_stock_latest(self, api_key, mock_transport):
        """Test news_stock_latest endpoint."""
        expected = [{"title": "Stock News"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/news/stock-latest" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.news_stock_latest(page=0, limit=10)

        assert result == expected

    @pytest.mark.asyncio
    async def test_news_crypto_latest(self, api_key, mock_transport):
        """Test news_crypto_latest endpoint."""
        expected = [{"title": "Crypto News"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/news/crypto-latest" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.news_crypto_latest(page=0, limit=10)

        assert result == expected

    @pytest.mark.asyncio
    async def test_news_forex_latest(self, api_key, mock_transport):
        """Test news_forex_latest endpoint."""
        expected = [{"title": "Forex News"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/news/forex-latest" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.news_forex_latest(page=0, limit=10)

        assert result == expected

    @pytest.mark.asyncio
    async def test_news_press_releases(self, api_key, mock_transport):
        """Test news_press_releases endpoint."""
        expected = [{"title": "AAPL Press Release"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/news/press-releases" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.news_press_releases(symbols="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_news_stock(self, api_key, mock_transport):
        """Test news_stock endpoint."""
        expected = [{"title": "AAPL News"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/news/stock" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.news_stock(symbols="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_news_crypto(self, api_key, mock_transport):
        """Test news_crypto endpoint."""
        expected = [{"title": "BTC News"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/news/crypto" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.news_crypto(symbols="BTCUSD")

        assert result == expected

    @pytest.mark.asyncio
    async def test_news_forex(self, api_key, mock_transport):
        """Test news_forex endpoint."""
        expected = [{"title": "EUR/USD News"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/news/forex" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.news_forex(symbols="EURUSD")

        assert result == expected

    @pytest.mark.asyncio
    async def test_analyst_estimates(self, api_key, mock_transport):
        """Test analyst_estimates endpoint."""
        expected = [{"symbol": "AAPL", "estimatedEps": 2.50}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/analyst-estimates" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.analyst_estimates(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_ratings_snapshot(self, api_key, mock_transport):
        """Test ratings_snapshot endpoint."""
        expected = [{"symbol": "AAPL", "rating": "Buy"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/ratings-snapshot" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.ratings_snapshot(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_ratings_historical(self, api_key, mock_transport):
        """Test ratings_historical endpoint."""
        expected = [{"date": "2024-01-01", "rating": "Buy"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/ratings-historical" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.ratings_historical(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_price_target_summary(self, api_key, mock_transport):
        """Test price_target_summary endpoint."""
        expected = [{"symbol": "AAPL", "avgPriceTarget": 200}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/price-target-summary" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.price_target_summary(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_price_target_consensus(self, api_key, mock_transport):
        """Test price_target_consensus endpoint."""
        expected = [{"symbol": "AAPL", "consensus": 200}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/price-target-consensus" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.price_target_consensus(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_grades(self, api_key, mock_transport):
        """Test grades endpoint."""
        expected = [{"symbol": "AAPL", "grade": "Buy"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/grades" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.grades(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_grades_historical(self, api_key, mock_transport):
        """Test grades_historical endpoint."""
        expected = [{"date": "2024-01-01", "grade": "Buy"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/grades-historical" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.grades_historical(symbol="AAPL")

        assert result == expected

    @pytest.mark.asyncio
    async def test_grades_consensus(self, api_key, mock_transport):
        """Test grades_consensus endpoint."""
        expected = [{"symbol": "AAPL", "consensus": "Buy"}]

        def handler(request: httpx.Request) -> httpx.Response:
            assert "/stable/grades-consensus" in str(request.url)
            return httpx.Response(200, json=expected)

        async with httpx.AsyncClient(transport=mock_transport(handler)) as http_client:
            client = AsyncFMPClient(api_key, httpx_client=http_client)
            result = await client.grades_consensus(symbol="AAPL")

        assert result == expected
