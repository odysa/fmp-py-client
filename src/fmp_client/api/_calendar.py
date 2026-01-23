"""Dividends, splits, earnings, and IPO calendar API endpoints."""

from fmp_client._types import JSONArray


class CalendarMixin:
    """Dividends, splits, earnings, and IPO endpoints."""

    async def dividends(self, symbol: str) -> JSONArray:
        """Get dividend history for a company."""
        return await self._request(  # type: ignore[attr-defined]
            "dividends",
            params={"symbol": symbol},
        )

    async def dividends_calendar(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
    ) -> JSONArray:
        """Get upcoming dividend calendar."""
        return await self._request(  # type: ignore[attr-defined]
            "dividends-calendar",
            params={"from": from_date, "to": to_date},
        )

    async def splits(self, symbol: str) -> JSONArray:
        """Get stock split history."""
        return await self._request(  # type: ignore[attr-defined]
            "splits",
            params={"symbol": symbol},
        )

    async def splits_calendar(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
    ) -> JSONArray:
        """Get upcoming stock splits calendar."""
        return await self._request(  # type: ignore[attr-defined]
            "splits-calendar",
            params={"from": from_date, "to": to_date},
        )

    async def earnings(self, symbol: str) -> JSONArray:
        """Get earnings data for a company."""
        return await self._request(  # type: ignore[attr-defined]
            "earnings",
            params={"symbol": symbol},
        )

    async def earnings_calendar(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
    ) -> JSONArray:
        """Get upcoming earnings calendar."""
        return await self._request(  # type: ignore[attr-defined]
            "earnings-calendar",
            params={"from": from_date, "to": to_date},
        )

    async def earning_call_transcript_latest(self, symbol: str) -> JSONArray:
        """Get latest earnings call transcript."""
        return await self._request(  # type: ignore[attr-defined]
            "earning-call-transcript-latest",
            params={"symbol": symbol},
        )

    async def earning_call_transcript(
        self,
        symbol: str,
        *,
        quarter: int | None = None,
        year: int | None = None,
    ) -> JSONArray:
        """Get earnings call transcript for a specific period."""
        return await self._request(  # type: ignore[attr-defined]
            "earning-call-transcript",
            params={"symbol": symbol, "quarter": quarter, "year": year},
        )

    async def earning_call_transcript_dates(self, symbol: str) -> JSONArray:
        """Get available earnings call transcript dates."""
        return await self._request(  # type: ignore[attr-defined]
            "earning-call-transcript-dates",
            params={"symbol": symbol},
        )

    async def earnings_transcript_list(self) -> JSONArray:
        """Get list of available earnings transcripts."""
        return await self._request(  # type: ignore[attr-defined]
            "earnings-transcript-list",
        )

    async def ipos_calendar(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
    ) -> JSONArray:
        """Get IPO calendar."""
        return await self._request(  # type: ignore[attr-defined]
            "ipos-calendar",
            params={"from": from_date, "to": to_date},
        )

    async def ipos_disclosure(
        self,
        *,
        from_date: str | None = None,
        to_date: str | None = None,
    ) -> JSONArray:
        """Get IPO disclosure data."""
        return await self._request(  # type: ignore[attr-defined]
            "ipos-disclosure",
            params={"from": from_date, "to": to_date},
        )
