"""Valuation and DCF API endpoints."""

from fmp_py_client.models import CustomDCF, DCFValuation, EnterpriseValue


class ValuationMixin:
    """Valuation and discounted cash flow endpoints."""

    async def discounted_cash_flow(
        self, *, symbol: str | None = None
    ) -> list[DCFValuation]:
        """Get discounted cash flow valuation."""
        return await self._request(  # type: ignore[attr-defined]
            "discounted-cash-flow",
            params={"symbol": symbol},
        )

    async def levered_discounted_cash_flow(
        self, *, symbol: str | None = None
    ) -> list[DCFValuation]:
        """Get levered discounted cash flow valuation."""
        return await self._request(  # type: ignore[attr-defined]
            "levered-discounted-cash-flow",
            params={"symbol": symbol},
        )

    async def custom_discounted_cash_flow(
        self, *, symbol: str | None = None
    ) -> list[CustomDCF]:
        """Get custom DCF valuation."""
        return await self._request(  # type: ignore[attr-defined]
            "custom-discounted-cash-flow",
            params={"symbol": symbol},
        )

    async def custom_levered_discounted_cash_flow(
        self, *, symbol: str | None = None
    ) -> list[CustomDCF]:
        """Get custom levered DCF valuation."""
        return await self._request(  # type: ignore[attr-defined]
            "custom-levered-discounted-cash-flow",
            params={"symbol": symbol},
        )

    async def enterprise_values(
        self, *, symbol: str | None = None
    ) -> list[EnterpriseValue]:
        """Get enterprise values."""
        return await self._request(  # type: ignore[attr-defined]
            "enterprise-values",
            params={"symbol": symbol},
        )
