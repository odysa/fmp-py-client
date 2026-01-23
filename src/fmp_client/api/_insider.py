"""Insider and institutional trading API endpoints."""

from fmp_client._types import JSONArray


class InsiderMixin:
    """Insider and institutional trading endpoints."""

    async def insider_trading_latest(
        self,
        *,
        symbol: str | None = None,
        limit: int | None = None,
    ) -> JSONArray:
        """Get latest insider trades."""
        return await self._request(  # type: ignore[attr-defined]
            "insider-trading/latest",
            params={"symbol": symbol, "limit": limit},
        )

    async def insider_trading_search(
        self,
        *,
        symbol: str | None = None,
        name: str | None = None,
        officer_title: str | None = None,
        limit: int | None = None,
    ) -> JSONArray:
        """Search insider trades."""
        return await self._request(  # type: ignore[attr-defined]
            "insider-trading/search",
            params={
                "symbol": symbol,
                "name": name,
                "officerTitle": officer_title,
                "limit": limit,
            },
        )

    async def insider_trading_reporting_name(
        self,
        reporting_name: str,
        *,
        limit: int | None = None,
    ) -> JSONArray:
        """Get insider trades by reporting name."""
        return await self._request(  # type: ignore[attr-defined]
            "insider-trading/reporting-name",
            params={"reportingName": reporting_name, "limit": limit},
        )

    async def insider_trading_transaction_type(
        self,
        symbol: str,
    ) -> JSONArray:
        """Get insider trading transaction types."""
        return await self._request(  # type: ignore[attr-defined]
            "insider-trading-transaction-type",
            params={"symbol": symbol},
        )

    async def insider_trading_statistics(self, symbol: str) -> JSONArray:
        """Get insider trading statistics."""
        return await self._request(  # type: ignore[attr-defined]
            "insider-trading/statistics",
            params={"symbol": symbol},
        )

    async def acquisition_of_beneficial_ownership(
        self,
        symbol: str,
    ) -> JSONArray:
        """Get acquisition of beneficial ownership data."""
        return await self._request(  # type: ignore[attr-defined]
            "acquisition-of-beneficial-ownership",
            params={"symbol": symbol},
        )

    async def institutional_ownership_latest(self, symbol: str) -> JSONArray:
        """Get latest institutional ownership."""
        return await self._request(  # type: ignore[attr-defined]
            "institutional-ownership/latest",
            params={"symbol": symbol},
        )

    async def institutional_ownership_extract(
        self,
        symbol: str,
        *,
        date: str | None = None,
    ) -> JSONArray:
        """Get institutional ownership extract."""
        return await self._request(  # type: ignore[attr-defined]
            "institutional-ownership/extract",
            params={"symbol": symbol, "date": date},
        )

    async def institutional_ownership_dates(self, symbol: str) -> JSONArray:
        """Get institutional ownership data dates."""
        return await self._request(  # type: ignore[attr-defined]
            "institutional-ownership/dates",
            params={"symbol": symbol},
        )

    async def institutional_ownership_holder_analytics(
        self,
        *,
        symbol: str | None = None,
        cik: str | None = None,
    ) -> JSONArray:
        """Get institutional holder analytics."""
        return await self._request(  # type: ignore[attr-defined]
            "institutional-ownership/extract-analytics/holder",
            params={"symbol": symbol, "cik": cik},
        )

    async def institutional_ownership_holder_performance_summary(
        self,
        *,
        symbol: str | None = None,
        cik: str | None = None,
    ) -> JSONArray:
        """Get institutional holder performance summary."""
        return await self._request(  # type: ignore[attr-defined]
            "institutional-ownership/holder-performance-summary",
            params={"symbol": symbol, "cik": cik},
        )

    async def institutional_ownership_holder_industry_breakdown(
        self,
        *,
        symbol: str | None = None,
        cik: str | None = None,
    ) -> JSONArray:
        """Get institutional holder industry breakdown."""
        return await self._request(  # type: ignore[attr-defined]
            "institutional-ownership/holder-industry-breakdown",
            params={"symbol": symbol, "cik": cik},
        )

    async def institutional_ownership_symbol_positions_summary(
        self,
        symbol: str,
    ) -> JSONArray:
        """Get institutional symbol positions summary."""
        return await self._request(  # type: ignore[attr-defined]
            "institutional-ownership/symbol-positions-summary",
            params={"symbol": symbol},
        )
