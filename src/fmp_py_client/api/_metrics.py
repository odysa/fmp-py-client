"""Financial metrics and ratios API endpoints."""

from fmp_py_client.models import (
    FinancialRatios,
    FinancialScores,
    KeyMetrics,
    OwnerEarnings,
)


class MetricsMixin:
    """Financial metrics and ratios endpoints."""

    async def key_metrics(self, *, symbol: str | None = None) -> list[KeyMetrics]:
        """Get key financial metrics."""
        return await self._request(  # type: ignore[attr-defined]
            "key-metrics",
            params={"symbol": symbol},
        )

    async def ratios(self, *, symbol: str | None = None) -> list[FinancialRatios]:
        """Get financial ratios."""
        return await self._request(  # type: ignore[attr-defined]
            "ratios",
            params={"symbol": symbol},
        )

    async def key_metrics_ttm(self, *, symbol: str | None = None) -> list[KeyMetrics]:
        """Get trailing twelve months key metrics."""
        return await self._request(  # type: ignore[attr-defined]
            "key-metrics-ttm",
            params={"symbol": symbol},
        )

    async def ratios_ttm(self, *, symbol: str | None = None) -> list[FinancialRatios]:
        """Get trailing twelve months financial ratios."""
        return await self._request(  # type: ignore[attr-defined]
            "ratios-ttm",
            params={"symbol": symbol},
        )

    async def financial_scores(
        self, *, symbol: str | None = None
    ) -> list[FinancialScores]:
        """Get financial scores (Altman Z-Score, Piotroski, etc.)."""
        return await self._request(  # type: ignore[attr-defined]
            "financial-scores",
            params={"symbol": symbol},
        )

    async def owner_earnings(self, *, symbol: str | None = None) -> list[OwnerEarnings]:
        """Get owner earnings."""
        return await self._request(  # type: ignore[attr-defined]
            "owner-earnings",
            params={"symbol": symbol},
        )
