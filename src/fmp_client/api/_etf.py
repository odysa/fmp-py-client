"""ETF and fund API endpoints."""

from fmp_client._types import JSONArray


class ETFMixin:
    """ETF and fund endpoints."""

    async def etf_holdings(self, symbol: str) -> JSONArray:
        """Get ETF holdings."""
        return await self._request(  # type: ignore[attr-defined]
            "etf/holdings",
            params={"symbol": symbol},
        )

    async def etf_info(self, symbol: str) -> JSONArray:
        """Get ETF information."""
        return await self._request(  # type: ignore[attr-defined]
            "etf/info",
            params={"symbol": symbol},
        )

    async def etf_country_weightings(self, symbol: str) -> JSONArray:
        """Get ETF country weightings."""
        return await self._request(  # type: ignore[attr-defined]
            "etf/country-weightings",
            params={"symbol": symbol},
        )

    async def etf_asset_exposure(self, symbol: str) -> JSONArray:
        """Get ETF asset class exposure."""
        return await self._request(  # type: ignore[attr-defined]
            "etf/asset-exposure",
            params={"symbol": symbol},
        )

    async def etf_sector_weightings(self, symbol: str) -> JSONArray:
        """Get ETF sector weightings."""
        return await self._request(  # type: ignore[attr-defined]
            "etf/sector-weightings",
            params={"symbol": symbol},
        )

    async def funds_disclosure_holders_latest(self, symbol: str) -> JSONArray:
        """Get latest fund disclosure holders."""
        return await self._request(  # type: ignore[attr-defined]
            "funds/disclosure-holders-latest",
            params={"symbol": symbol},
        )

    async def funds_disclosure(self, symbol: str) -> JSONArray:
        """Get fund disclosure data."""
        return await self._request(  # type: ignore[attr-defined]
            "funds/disclosure",
            params={"symbol": symbol},
        )

    async def funds_disclosure_holders_search(
        self,
        *,
        symbol: str | None = None,
        cik: str | None = None,
    ) -> JSONArray:
        """Search fund disclosure holders."""
        return await self._request(  # type: ignore[attr-defined]
            "funds/disclosure-holders-search",
            params={"symbol": symbol, "cik": cik},
        )

    async def funds_disclosure_dates(self, symbol: str) -> JSONArray:
        """Get fund disclosure dates."""
        return await self._request(  # type: ignore[attr-defined]
            "funds/disclosure-dates",
            params={"symbol": symbol},
        )
