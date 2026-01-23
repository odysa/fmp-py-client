"""Company profile and data API endpoints."""

from fmp_client._types import JSONArray


class CompanyMixin:
    """Company profile and data endpoints."""

    async def profile(self, symbol: str) -> JSONArray:
        """Get company profile data."""
        return await self._request(  # type: ignore[attr-defined]
            "profile",
            params={"symbol": symbol},
        )

    async def profile_cik(self, cik: int) -> JSONArray:
        """Get company profile by CIK number."""
        return await self._request(  # type: ignore[attr-defined]
            "profile-cik",
            params={"cik": cik},
        )

    async def company_notes(self, symbol: str) -> JSONArray:
        """Get company notes."""
        return await self._request(  # type: ignore[attr-defined]
            "company-notes",
            params={"symbol": symbol},
        )

    async def stock_peers(self, symbol: str) -> JSONArray:
        """Get stock peer comparison."""
        return await self._request(  # type: ignore[attr-defined]
            "stock-peers",
            params={"symbol": symbol},
        )

    async def company_screener(
        self,
        *,
        market_cap_more_than: int | None = None,
        market_cap_lower_than: int | None = None,
        sector: str | None = None,
        industry: str | None = None,
        country: str | None = None,
        exchange: str | None = None,
        limit: int | None = None,
    ) -> JSONArray:
        """Screen companies by various criteria."""
        return await self._request(  # type: ignore[attr-defined]
            "company-screener",
            params={
                "marketCapMoreThan": market_cap_more_than,
                "marketCapLowerThan": market_cap_lower_than,
                "sector": sector,
                "industry": industry,
                "country": country,
                "exchange": exchange,
                "limit": limit,
            },
        )

    async def key_executives(self, symbol: str) -> JSONArray:
        """Get key executives for a company."""
        return await self._request(  # type: ignore[attr-defined]
            "key-executives",
            params={"symbol": symbol},
        )

    async def executive_compensation(self, symbol: str) -> JSONArray:
        """Get executive compensation data."""
        return await self._request(  # type: ignore[attr-defined]
            "governance-executive-compensation",
            params={"symbol": symbol},
        )
