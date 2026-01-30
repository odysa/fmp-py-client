"""Market info and list response types."""

from typing import NotRequired, TypedDict


class StockListEntry(TypedDict):
    """Stock list entry."""

    symbol: str
    name: str
    price: NotRequired[float]
    exchange: NotRequired[str]
    exchangeShortName: NotRequired[str]
    type: NotRequired[str]


class CIKEntry(TypedDict):
    """CIK list entry."""

    cik: str
    name: str


class SymbolChange(TypedDict):
    """Symbol change record."""

    date: str
    name: str
    oldSymbol: str
    newSymbol: str


class DelistedCompany(TypedDict):
    """Delisted company info."""

    symbol: str
    companyName: str
    exchange: NotRequired[str]
    ipoDate: NotRequired[str]
    delistedDate: str


class IndexInfo(TypedDict):
    """Market index info."""

    symbol: str
    name: str
    currency: NotRequired[str]
    stockExchange: NotRequired[str]
    exchangeShortName: NotRequired[str]


class IndexConstituent(TypedDict):
    """Index constituent (S&P 500, Nasdaq, Dow Jones)."""

    symbol: str
    name: str
    sector: NotRequired[str]
    subSector: NotRequired[str]
    headQuarter: NotRequired[str]
    dateFirstAdded: NotRequired[str]
    cik: NotRequired[str]
    founded: NotRequired[str]


class HistoricalIndexConstituent(TypedDict):
    """Historical index constituent change."""

    dateAdded: NotRequired[str]
    addedSecurity: NotRequired[str]
    removedTicker: NotRequired[str]
    removedSecurity: NotRequired[str]
    date: NotRequired[str]
    symbol: NotRequired[str]
    reason: NotRequired[str]
