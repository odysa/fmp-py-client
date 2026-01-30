"""Quote and price response types."""

from typing import NotRequired, TypedDict


class StockQuote(TypedDict):
    """Real-time stock quote data."""

    symbol: str
    name: str
    price: float
    change: float
    changesPercentage: float
    volume: int
    dayLow: float
    dayHigh: float
    yearHigh: float
    yearLow: float
    marketCap: int
    priceAvg50: float
    priceAvg200: float
    exchange: str
    open: float
    previousClose: float
    eps: NotRequired[float | None]
    pe: NotRequired[float | None]
    earningsAnnouncement: NotRequired[str | None]
    sharesOutstanding: NotRequired[int]
    avgVolume: int
    timestamp: int


class ShortQuote(TypedDict):
    """Abbreviated quote data."""

    symbol: str
    price: float
    change: float
    volume: int


class AftermarketQuote(TypedDict):
    """After-hours trading quote."""

    symbol: str
    bidSize: int
    bidPrice: float
    askSize: int
    askPrice: float
    volume: int
    timestamp: int


class AftermarketTrade(TypedDict):
    """After-hours trade data."""

    symbol: str
    price: float
    size: int
    timestamp: int


class PriceChange(TypedDict):
    """Stock price change over various time periods."""

    symbol: str
    oneDay: NotRequired[float]
    fiveDay: NotRequired[float]
    oneMonth: NotRequired[float]
    threeMonth: NotRequired[float]
    sixMonth: NotRequired[float]
    ytd: NotRequired[float]
    oneYear: NotRequired[float]
    threeYear: NotRequired[float]
    fiveYear: NotRequired[float]
    tenYear: NotRequired[float]
    max: NotRequired[float]
