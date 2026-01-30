"""Quotes and price API endpoints."""

from fmp_py_client.models import (
    AftermarketQuote,
    AftermarketTrade,
    PriceChange,
    ShortQuote,
    StockQuote,
)


class QuotesMixin:
    """Stock quotes and price endpoints."""

    async def quote(self, *, symbol: str | None = None) -> list[StockQuote]:
        """Get real-time stock quote."""
        return await self._request(  # type: ignore[attr-defined]
            "quote",
            params={"symbol": symbol},
        )

    async def quote_short(self, *, symbol: str | None = None) -> list[ShortQuote]:
        """Get short-form stock quote."""
        return await self._request(  # type: ignore[attr-defined]
            "quote-short",
            params={"symbol": symbol},
        )

    async def aftermarket_trade(
        self, *, symbol: str | None = None
    ) -> list[AftermarketTrade]:
        """Get aftermarket trade data."""
        return await self._request(  # type: ignore[attr-defined]
            "aftermarket-trade",
            params={"symbol": symbol},
        )

    async def aftermarket_quote(
        self, *, symbol: str | None = None
    ) -> list[AftermarketQuote]:
        """Get aftermarket quote data."""
        return await self._request(  # type: ignore[attr-defined]
            "aftermarket-quote",
            params={"symbol": symbol},
        )

    async def stock_price_change(
        self, *, symbol: str | None = None
    ) -> list[PriceChange]:
        """Get stock price change data."""
        return await self._request(  # type: ignore[attr-defined]
            "stock-price-change",
            params={"symbol": symbol},
        )

    async def batch_quote(self, *, symbols: str | None = None) -> list[StockQuote]:
        """Get quotes for multiple symbols (comma-separated)."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-quote",
            params={"symbols": symbols},
        )

    async def batch_quote_short(
        self, *, symbols: str | None = None
    ) -> list[ShortQuote]:
        """Get short-form quotes for multiple symbols."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-quote-short",
            params={"symbols": symbols},
        )

    async def batch_aftermarket_trade(
        self, *, symbols: str | None = None
    ) -> list[AftermarketTrade]:
        """Get aftermarket trades for multiple symbols."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-aftermarket-trade",
            params={"symbols": symbols},
        )

    async def batch_aftermarket_quote(
        self, *, symbols: str | None = None
    ) -> list[AftermarketQuote]:
        """Get aftermarket quotes for multiple symbols."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-aftermarket-quote",
            params={"symbols": symbols},
        )

    async def batch_exchange_quote(
        self, *, exchange: str | None = None
    ) -> list[StockQuote]:
        """Get quotes for all symbols on an exchange."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-exchange-quote",
            params={"exchange": exchange},
        )

    async def batch_mutualfund_quotes(self) -> list[StockQuote]:
        """Get mutual fund quotes."""
        return await self._request("batch-mutualfund-quotes")  # type: ignore[attr-defined]

    async def batch_etf_quotes(self) -> list[StockQuote]:
        """Get ETF quotes."""
        return await self._request("batch-etf-quotes")  # type: ignore[attr-defined]

    async def batch_commodity_quotes(self) -> list[StockQuote]:
        """Get commodity quotes."""
        return await self._request("batch-commodity-quotes")  # type: ignore[attr-defined]

    async def batch_crypto_quotes(self) -> list[StockQuote]:
        """Get cryptocurrency quotes."""
        return await self._request("batch-crypto-quotes")  # type: ignore[attr-defined]

    async def batch_forex_quotes(self) -> list[StockQuote]:
        """Get forex quotes."""
        return await self._request("batch-forex-quotes")  # type: ignore[attr-defined]

    async def batch_index_quotes(self) -> list[StockQuote]:
        """Get index quotes."""
        return await self._request("batch-index-quotes")  # type: ignore[attr-defined]
