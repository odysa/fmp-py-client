"""Quotes and price API endpoints."""

from fmp_client._types import JSONArray


class QuotesMixin:
    """Stock quotes and price endpoints."""

    async def quote(self, symbol: str) -> JSONArray:
        """Get real-time stock quote."""
        return await self._request(  # type: ignore[attr-defined]
            "quote",
            params={"symbol": symbol},
        )

    async def quote_short(self, symbol: str) -> JSONArray:
        """Get short-form stock quote."""
        return await self._request(  # type: ignore[attr-defined]
            "quote-short",
            params={"symbol": symbol},
        )

    async def aftermarket_trade(self, symbol: str) -> JSONArray:
        """Get aftermarket trade data."""
        return await self._request(  # type: ignore[attr-defined]
            "aftermarket-trade",
            params={"symbol": symbol},
        )

    async def aftermarket_quote(self, symbol: str) -> JSONArray:
        """Get aftermarket quote data."""
        return await self._request(  # type: ignore[attr-defined]
            "aftermarket-quote",
            params={"symbol": symbol},
        )

    async def stock_price_change(self, symbol: str) -> JSONArray:
        """Get stock price change data."""
        return await self._request(  # type: ignore[attr-defined]
            "stock-price-change",
            params={"symbol": symbol},
        )

    async def batch_quote(self, symbols: str) -> JSONArray:
        """Get quotes for multiple symbols (comma-separated)."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-quote",
            params={"symbols": symbols},
        )

    async def batch_quote_short(self, symbols: str) -> JSONArray:
        """Get short-form quotes for multiple symbols."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-quote-short",
            params={"symbols": symbols},
        )

    async def batch_aftermarket_trade(self, symbols: str) -> JSONArray:
        """Get aftermarket trades for multiple symbols."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-aftermarket-trade",
            params={"symbols": symbols},
        )

    async def batch_aftermarket_quote(self, symbols: str) -> JSONArray:
        """Get aftermarket quotes for multiple symbols."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-aftermarket-quote",
            params={"symbols": symbols},
        )

    async def batch_exchange_quote(self, exchange: str) -> JSONArray:
        """Get quotes for all symbols on an exchange."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-exchange-quote",
            params={"exchange": exchange},
        )

    async def batch_mutualfund_quotes(self, symbols: str) -> JSONArray:
        """Get mutual fund quotes for multiple symbols."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-mutualfund-quotes",
            params={"symbols": symbols},
        )

    async def batch_etf_quotes(self, symbols: str) -> JSONArray:
        """Get ETF quotes for multiple symbols."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-etf-quotes",
            params={"symbols": symbols},
        )

    async def batch_commodity_quotes(self, symbols: str) -> JSONArray:
        """Get commodity quotes for multiple symbols."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-commodity-quotes",
            params={"symbols": symbols},
        )

    async def batch_crypto_quotes(self, symbols: str) -> JSONArray:
        """Get cryptocurrency quotes for multiple symbols."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-crypto-quotes",
            params={"symbols": symbols},
        )

    async def batch_forex_quotes(self, symbols: str) -> JSONArray:
        """Get forex quotes for multiple pairs."""
        return await self._request(  # type: ignore[attr-defined]
            "batch-forex-quotes",
            params={"symbols": symbols},
        )
