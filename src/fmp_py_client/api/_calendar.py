"""Dividends, splits, earnings, and IPO calendar API endpoints."""

from fmp_py_client.models import (
    Dividend,
    EarningsReport,
    EarningsTranscript,
    EarningsTranscriptDate,
    IPOCalendar,
    IPOProspectus,
    StockSplit,
)


class CalendarMixin:
    """Dividends, splits, earnings, and IPO endpoints."""

    async def dividends(self, *, symbol: str | None = None) -> list[Dividend]:
        """Get dividend history for a company."""
        return await self._request(  # type: ignore[attr-defined]
            "dividends",
            params={"symbol": symbol},
        )

    async def dividends_calendar(self) -> list[Dividend]:
        """Get upcoming dividend calendar."""
        return await self._request("dividends-calendar")  # type: ignore[attr-defined]

    async def splits(self, *, symbol: str | None = None) -> list[StockSplit]:
        """Get stock split history."""
        return await self._request(  # type: ignore[attr-defined]
            "splits",
            params={"symbol": symbol},
        )

    async def splits_calendar(self) -> list[StockSplit]:
        """Get upcoming stock splits calendar."""
        return await self._request("splits-calendar")  # type: ignore[attr-defined]

    async def earnings(self, *, symbol: str | None = None) -> list[EarningsReport]:
        """Get earnings data for a company."""
        return await self._request(  # type: ignore[attr-defined]
            "earnings",
            params={"symbol": symbol},
        )

    async def earnings_calendar(self) -> list[EarningsReport]:
        """Get upcoming earnings calendar."""
        return await self._request("earnings-calendar")  # type: ignore[attr-defined]

    async def earning_call_transcript_latest(self) -> list[EarningsTranscript]:
        """Get latest earnings call transcript."""
        return await self._request("earning-call-transcript-latest")  # type: ignore[attr-defined]

    async def earning_call_transcript(
        self,
        *,
        symbol: str | None = None,
        quarter: int | None = None,
        year: int | None = None,
    ) -> list[EarningsTranscript]:
        """Get earnings call transcript for a specific period."""
        return await self._request(  # type: ignore[attr-defined]
            "earning-call-transcript",
            params={"symbol": symbol, "quarter": quarter, "year": year},
        )

    async def earning_call_transcript_dates(
        self, *, symbol: str | None = None
    ) -> list[EarningsTranscriptDate]:
        """Get available earnings call transcript dates."""
        return await self._request(  # type: ignore[attr-defined]
            "earning-call-transcript-dates",
            params={"symbol": symbol},
        )

    async def earnings_transcript_list(self) -> list[EarningsTranscriptDate]:
        """Get list of available earnings transcripts."""
        return await self._request(  # type: ignore[attr-defined]
            "earnings-transcript-list",
        )

    async def ipos_calendar(self) -> list[IPOCalendar]:
        """Get IPO calendar."""
        return await self._request("ipos-calendar")  # type: ignore[attr-defined]

    async def ipos_disclosure(self) -> list[IPOProspectus]:
        """Get IPO disclosure data."""
        return await self._request("ipos-disclosure")  # type: ignore[attr-defined]
