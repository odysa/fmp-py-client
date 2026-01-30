"""Search response types."""

from typing import NotRequired, TypedDict


class SearchResult(TypedDict):
    """Symbol/name search result."""

    symbol: str
    name: str
    currency: NotRequired[str]
    stockExchange: NotRequired[str]
    exchangeShortName: NotRequired[str]


class CIKSearchResult(TypedDict):
    """CIK search result."""

    cik: str
    name: str
    ticker: NotRequired[str]


class ExchangeVariant(TypedDict):
    """Exchange variant of a symbol."""

    symbol: str
    exchange: str
    name: NotRequired[str]
