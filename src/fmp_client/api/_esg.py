"""ESG and sustainability API endpoints."""

from fmp_client._types import JSONArray


class ESGMixin:
    """ESG and sustainability endpoints."""

    async def esg_disclosures(self, symbol: str) -> JSONArray:
        """Get ESG disclosures for a company."""
        return await self._request(  # type: ignore[attr-defined]
            "esg-disclosures",
            params={"symbol": symbol},
        )

    async def esg_ratings(self, symbol: str) -> JSONArray:
        """Get ESG ratings for a company."""
        return await self._request(  # type: ignore[attr-defined]
            "esg-ratings",
            params={"symbol": symbol},
        )

    async def esg_benchmark(self) -> JSONArray:
        """Get ESG benchmark comparison."""
        return await self._request("esg-benchmark")  # type: ignore[attr-defined]

    async def commitment_of_traders_report(self) -> JSONArray:
        """Get Commitment of Traders (COT) report."""
        return await self._request("commitment-of-traders-report")  # type: ignore[attr-defined]

    async def commitment_of_traders_analysis(self) -> JSONArray:
        """Get COT analysis by dates."""
        return await self._request("commitment-of-traders-analysis")  # type: ignore[attr-defined]
