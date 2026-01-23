"""Government trading API endpoints."""

from fmp_client._types import JSONArray


class GovernmentMixin:
    """Government trading (Senate/House) endpoints."""

    async def senate_latest(
        self,
        *,
        limit: int | None = None,
    ) -> JSONArray:
        """Get latest Senate trading activity."""
        return await self._request(  # type: ignore[attr-defined]
            "senate-latest",
            params={"limit": limit},
        )

    async def house_latest(
        self,
        *,
        limit: int | None = None,
    ) -> JSONArray:
        """Get latest House trading activity."""
        return await self._request(  # type: ignore[attr-defined]
            "house-latest",
            params={"limit": limit},
        )

    async def senate_trades(
        self,
        symbol: str,
        *,
        limit: int | None = None,
    ) -> JSONArray:
        """Get Senate trades for a symbol."""
        return await self._request(  # type: ignore[attr-defined]
            "senate-trades",
            params={"symbol": symbol, "limit": limit},
        )

    async def senate_trades_by_name(
        self,
        name: str,
        *,
        limit: int | None = None,
    ) -> JSONArray:
        """Get Senate trades by official name."""
        return await self._request(  # type: ignore[attr-defined]
            "senate-trades-by-name",
            params={"name": name, "limit": limit},
        )
