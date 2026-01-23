"""Financial metrics and ratios API endpoints."""

from fmp_client._types import JSONArray, Period


class MetricsMixin:
    """Financial metrics and ratios endpoints."""

    async def key_metrics(
        self,
        symbol: str,
        *,
        period: Period = Period.ANNUAL,
        limit: int | None = None,
    ) -> JSONArray:
        """Get key financial metrics."""
        return await self._request(  # type: ignore[attr-defined]
            "key-metrics",
            params={"symbol": symbol, "period": period, "limit": limit},
        )

    async def ratios(
        self,
        symbol: str,
        *,
        period: Period = Period.ANNUAL,
        limit: int | None = None,
    ) -> JSONArray:
        """Get financial ratios."""
        return await self._request(  # type: ignore[attr-defined]
            "ratios",
            params={"symbol": symbol, "period": period, "limit": limit},
        )

    async def key_metrics_ttm(self, symbol: str) -> JSONArray:
        """Get trailing twelve months key metrics."""
        return await self._request(  # type: ignore[attr-defined]
            "key-metrics-ttm",
            params={"symbol": symbol},
        )

    async def ratios_ttm(self, symbol: str) -> JSONArray:
        """Get trailing twelve months financial ratios."""
        return await self._request(  # type: ignore[attr-defined]
            "ratios-ttm",
            params={"symbol": symbol},
        )

    async def financial_scores(self, symbol: str) -> JSONArray:
        """Get financial scores (Altman Z-Score, Piotroski, etc.)."""
        return await self._request(  # type: ignore[attr-defined]
            "financial-scores",
            params={"symbol": symbol},
        )

    async def owner_earnings(self, symbol: str) -> JSONArray:
        """Get owner earnings."""
        return await self._request(  # type: ignore[attr-defined]
            "owner-earnings",
            params={"symbol": symbol},
        )
