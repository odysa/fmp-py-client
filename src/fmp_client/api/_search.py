"""Search API endpoints."""

from fmp_client._types import JSONArray


class SearchMixin:
    """Search-related API endpoints."""

    async def search_symbol(
        self,
        query: str,
        *,
        limit: int | None = None,
        exchange: str | None = None,
    ) -> JSONArray:
        """Search for stock symbols matching a query."""
        return await self._request(  # type: ignore[attr-defined]
            "search-symbol",
            params={"query": query, "limit": limit, "exchange": exchange},
        )

    async def search_name(
        self,
        query: str,
        *,
        limit: int | None = None,
        exchange: str | None = None,
    ) -> JSONArray:
        """Search for company names matching a query."""
        return await self._request(  # type: ignore[attr-defined]
            "search-name",
            params={"query": query, "limit": limit, "exchange": exchange},
        )

    async def search_cik(self, cik: int) -> JSONArray:
        """Search by CIK number."""
        return await self._request(  # type: ignore[attr-defined]
            "search-cik",
            params={"cik": cik},
        )

    async def search_cusip(self, cusip: str) -> JSONArray:
        """Search by CUSIP number."""
        return await self._request(  # type: ignore[attr-defined]
            "search-cusip",
            params={"cusip": cusip},
        )

    async def search_isin(self, isin: str) -> JSONArray:
        """Search by ISIN number."""
        return await self._request(  # type: ignore[attr-defined]
            "search-isin",
            params={"isin": isin},
        )

    async def search_exchange_variants(self, symbol: str) -> JSONArray:
        """Search for exchange variants of a symbol."""
        return await self._request(  # type: ignore[attr-defined]
            "search-exchange-variants",
            params={"symbol": symbol},
        )
