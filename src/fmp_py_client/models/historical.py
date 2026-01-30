"""Historical price data response types."""

from typing import NotRequired, TypedDict


class EODLight(TypedDict):
    """Light end-of-day price data."""

    symbol: str
    date: str
    price: float
    volume: int


class EODFull(TypedDict):
    """Full end-of-day price data."""

    symbol: str
    date: str
    open: float
    high: float
    low: float
    close: float
    adjClose: NotRequired[float]
    volume: int
    unadjustedVolume: NotRequired[int]
    change: NotRequired[float]
    changePercent: NotRequired[float]
    vwap: NotRequired[float]
    label: NotRequired[str]
    changeOverTime: NotRequired[float]


class HistoricalChart(TypedDict):
    """Historical chart data (intraday)."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
