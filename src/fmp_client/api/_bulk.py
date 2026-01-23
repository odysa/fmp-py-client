"""Bulk data API endpoints."""

from fmp_client._types import JSONArray, Period


class BulkMixin:
    """Bulk data download endpoints."""

    async def profile_bulk(self) -> JSONArray:
        """Get bulk company profiles."""
        return await self._request("profile-bulk")  # type: ignore[attr-defined]

    async def rating_bulk(self) -> JSONArray:
        """Get bulk ratings."""
        return await self._request("rating-bulk")  # type: ignore[attr-defined]

    async def dcf_bulk(self) -> JSONArray:
        """Get bulk DCF valuations."""
        return await self._request("dcf-bulk")  # type: ignore[attr-defined]

    async def scores_bulk(self) -> JSONArray:
        """Get bulk financial scores."""
        return await self._request("scores-bulk")  # type: ignore[attr-defined]

    async def price_target_summary_bulk(self) -> JSONArray:
        """Get bulk price target summaries."""
        return await self._request("price-target-summary-bulk")  # type: ignore[attr-defined]

    async def etf_holder_bulk(self) -> JSONArray:
        """Get bulk ETF holder data."""
        return await self._request("etf-holder-bulk")  # type: ignore[attr-defined]

    async def upgrades_downgrades_consensus_bulk(self) -> JSONArray:
        """Get bulk upgrades/downgrades consensus."""
        return await self._request("upgrades-downgrades-consensus-bulk")  # type: ignore[attr-defined]

    async def key_metrics_ttm_bulk(
        self,
        *,
        year: int | None = None,
        period: Period = Period.ANNUAL,
    ) -> JSONArray:
        """Get bulk TTM key metrics."""
        return await self._request(  # type: ignore[attr-defined]
            "key-metrics-ttm-bulk",
            params={"year": year, "period": period},
        )

    async def ratios_ttm_bulk(
        self,
        *,
        year: int | None = None,
        period: Period = Period.ANNUAL,
    ) -> JSONArray:
        """Get bulk TTM ratios."""
        return await self._request(  # type: ignore[attr-defined]
            "ratios-ttm-bulk",
            params={"year": year, "period": period},
        )

    async def peers_bulk(self) -> JSONArray:
        """Get bulk peer comparisons."""
        return await self._request("peers-bulk")  # type: ignore[attr-defined]

    async def earnings_surprises_bulk(self) -> JSONArray:
        """Get bulk earnings surprises."""
        return await self._request("earnings-surprises-bulk")  # type: ignore[attr-defined]

    async def eod_bulk(self, date: str) -> JSONArray:
        """Get bulk end-of-day data for a specific date (YYYY-MM-DD)."""
        return await self._request(  # type: ignore[attr-defined]
            "eod-bulk",
            params={"date": date},
        )

    async def shares_float(self, symbol: str) -> JSONArray:
        """Get shares float data."""
        return await self._request(  # type: ignore[attr-defined]
            "shares-float",
            params={"symbol": symbol},
        )

    async def shares_float_all(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> JSONArray:
        """Get all shares float data."""
        return await self._request(  # type: ignore[attr-defined]
            "shares-float-all",
            params={"page": page, "limit": limit},
        )

    async def executive_compensation_benchmark(
        self,
        symbol: str,
    ) -> JSONArray:
        """Get executive compensation benchmark."""
        return await self._request(  # type: ignore[attr-defined]
            "executive-compensation-benchmark",
            params={"symbol": symbol},
        )
