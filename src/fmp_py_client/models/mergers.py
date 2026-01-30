"""Mergers and acquisitions response types."""

from typing import NotRequired, TypedDict


class MergerAcquisition(TypedDict):
    """Merger and acquisition data."""

    symbol: str
    companyName: str
    cik: NotRequired[str]
    targetedCompanyName: str
    targetedCik: NotRequired[str]
    targetedSymbol: NotRequired[str]
    transactionDate: str
    acceptedDate: NotRequired[str]
    link: NotRequired[str]
