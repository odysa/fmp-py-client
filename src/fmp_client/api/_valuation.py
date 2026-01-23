"""Valuation and DCF API endpoints."""

from fmp_client._types import JSONArray, Period


class ValuationMixin:
    """Valuation and discounted cash flow endpoints."""

    async def discounted_cash_flow(self, symbol: str) -> JSONArray:
        """Get discounted cash flow valuation."""
        return await self._request(  # type: ignore[attr-defined]
            "discounted-cash-flow",
            params={"symbol": symbol},
        )

    async def levered_discounted_cash_flow(self, symbol: str) -> JSONArray:
        """Get levered discounted cash flow valuation."""
        return await self._request(  # type: ignore[attr-defined]
            "levered-discounted-cash-flow",
            params={"symbol": symbol},
        )

    async def custom_discounted_cash_flow(
        self,
        symbol: str,
        *,
        year: int | None = None,
        period: Period = Period.ANNUAL,
    ) -> JSONArray:
        """Get custom DCF with specific parameters."""
        return await self._request(  # type: ignore[attr-defined]
            "custom-discounted-cash-flow",
            params={"symbol": symbol, "year": year, "period": period},
        )

    async def custom_levered_discounted_cash_flow(
        self,
        symbol: str,
        *,
        year: int | None = None,
        period: Period = Period.ANNUAL,
    ) -> JSONArray:
        """Get custom levered DCF with specific parameters."""
        return await self._request(  # type: ignore[attr-defined]
            "custom-levered-discounted-cash-flow",
            params={"symbol": symbol, "year": year, "period": period},
        )

    async def enterprise_values(
        self,
        symbol: str,
        *,
        period: Period = Period.ANNUAL,
        limit: int | None = None,
    ) -> JSONArray:
        """Get enterprise values."""
        return await self._request(  # type: ignore[attr-defined]
            "enterprise-values",
            params={"symbol": symbol, "period": period, "limit": limit},
        )
