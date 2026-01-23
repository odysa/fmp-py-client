"""Crowdfunding and fundraising API endpoints."""

from fmp_client._types import JSONArray


class CrowdfundingMixin:
    """Crowdfunding and fundraising endpoints."""

    async def crowdfunding_offerings_latest(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> JSONArray:
        """Get latest crowdfunding offerings."""
        return await self._request(  # type: ignore[attr-defined]
            "crowdfunding-offerings-latest",
            params={"page": page, "limit": limit},
        )

    async def crowdfunding_offerings_search(
        self,
        search_term: str,
    ) -> JSONArray:
        """Search crowdfunding offerings."""
        return await self._request(  # type: ignore[attr-defined]
            "crowdfunding-offerings-search",
            params={"search_term": search_term},
        )

    async def crowdfunding_offerings(self) -> JSONArray:
        """Get all crowdfunding offerings."""
        return await self._request("crowdfunding-offerings")  # type: ignore[attr-defined]

    async def fundraising_latest(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> JSONArray:
        """Get latest fundraising data."""
        return await self._request(  # type: ignore[attr-defined]
            "fundraising-latest",
            params={"page": page, "limit": limit},
        )

    async def fundraising_search(self, search_term: str) -> JSONArray:
        """Search fundraising data."""
        return await self._request(  # type: ignore[attr-defined]
            "fundraising-search",
            params={"search_term": search_term},
        )

    async def fundraising(self) -> JSONArray:
        """Get all fundraising data."""
        return await self._request("fundraising")  # type: ignore[attr-defined]

    async def ipos_prospectus(
        self,
        *,
        symbol: str | None = None,
    ) -> JSONArray:
        """Get IPO prospectus data."""
        return await self._request(  # type: ignore[attr-defined]
            "ipos-prospectus",
            params={"symbol": symbol},
        )
