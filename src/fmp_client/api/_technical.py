"""Technical indicators API endpoints."""

from fmp_client._types import JSONArray, Interval


class TechnicalMixin:
    """Technical indicators endpoints."""

    async def sma(
        self,
        symbol: str,
        *,
        period: int = 20,
        interval: Interval = Interval.ONE_HOUR,
    ) -> JSONArray:
        """Get Simple Moving Average (SMA)."""
        return await self._request(  # type: ignore[attr-defined]
            "technical-indicators/sma",
            params={"symbol": symbol, "period": period, "interval": interval},
        )

    async def ema(
        self,
        symbol: str,
        *,
        period: int = 20,
        interval: Interval = Interval.ONE_HOUR,
    ) -> JSONArray:
        """Get Exponential Moving Average (EMA)."""
        return await self._request(  # type: ignore[attr-defined]
            "technical-indicators/ema",
            params={"symbol": symbol, "period": period, "interval": interval},
        )

    async def wma(
        self,
        symbol: str,
        *,
        period: int = 20,
        interval: Interval = Interval.ONE_HOUR,
    ) -> JSONArray:
        """Get Weighted Moving Average (WMA)."""
        return await self._request(  # type: ignore[attr-defined]
            "technical-indicators/wma",
            params={"symbol": symbol, "period": period, "interval": interval},
        )

    async def dema(
        self,
        symbol: str,
        *,
        period: int = 20,
        interval: Interval = Interval.ONE_HOUR,
    ) -> JSONArray:
        """Get Double Exponential Moving Average (DEMA)."""
        return await self._request(  # type: ignore[attr-defined]
            "technical-indicators/dema",
            params={"symbol": symbol, "period": period, "interval": interval},
        )

    async def tema(
        self,
        symbol: str,
        *,
        period: int = 20,
        interval: Interval = Interval.ONE_HOUR,
    ) -> JSONArray:
        """Get Triple Exponential Moving Average (TEMA)."""
        return await self._request(  # type: ignore[attr-defined]
            "technical-indicators/tema",
            params={"symbol": symbol, "period": period, "interval": interval},
        )

    async def rsi(
        self,
        symbol: str,
        *,
        period: int = 14,
        interval: Interval = Interval.ONE_HOUR,
    ) -> JSONArray:
        """Get Relative Strength Index (RSI)."""
        return await self._request(  # type: ignore[attr-defined]
            "technical-indicators/rsi",
            params={"symbol": symbol, "period": period, "interval": interval},
        )

    async def standard_deviation(
        self,
        symbol: str,
        *,
        period: int = 20,
        interval: Interval = Interval.ONE_HOUR,
    ) -> JSONArray:
        """Get Standard Deviation."""
        return await self._request(  # type: ignore[attr-defined]
            "technical-indicators/standarddeviation",
            params={"symbol": symbol, "period": period, "interval": interval},
        )

    async def williams(
        self,
        symbol: str,
        *,
        period: int = 14,
        interval: Interval = Interval.ONE_HOUR,
    ) -> JSONArray:
        """Get Williams %R."""
        return await self._request(  # type: ignore[attr-defined]
            "technical-indicators/williams",
            params={"symbol": symbol, "period": period, "interval": interval},
        )
