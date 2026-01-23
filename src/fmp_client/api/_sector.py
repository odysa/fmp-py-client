"""Sector and industry performance API endpoints."""

from fmp_client._types import JSONArray


class SectorMixin:
    """Sector and industry performance endpoints."""

    async def sector_performance_snapshot(self) -> JSONArray:
        """Get sector performance snapshot."""
        return await self._request("sector-performance-snapshot")  # type: ignore[attr-defined]

    async def industry_performance_snapshot(self) -> JSONArray:
        """Get industry performance snapshot."""
        return await self._request("industry-performance-snapshot")  # type: ignore[attr-defined]

    async def historical_sector_performance(self) -> JSONArray:
        """Get historical sector performance."""
        return await self._request("historical-sector-performance")  # type: ignore[attr-defined]

    async def historical_industry_performance(self) -> JSONArray:
        """Get historical industry performance."""
        return await self._request("historical-industry-performance")  # type: ignore[attr-defined]

    async def sector_pe_snapshot(self) -> JSONArray:
        """Get sector P/E ratio snapshot."""
        return await self._request("sector-pe-snapshot")  # type: ignore[attr-defined]

    async def industry_pe_snapshot(self) -> JSONArray:
        """Get industry P/E ratio snapshot."""
        return await self._request("industry-pe-snapshot")  # type: ignore[attr-defined]

    async def historical_sector_pe(self) -> JSONArray:
        """Get historical sector P/E ratios."""
        return await self._request("historical-sector-pe")  # type: ignore[attr-defined]

    async def historical_industry_pe(self) -> JSONArray:
        """Get historical industry P/E ratios."""
        return await self._request("historical-industry-pe")  # type: ignore[attr-defined]
