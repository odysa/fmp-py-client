"""Technical indicator response types."""

from typing import NotRequired, TypedDict


class TechnicalIndicatorMA(TypedDict):
    """Moving average indicator data (SMA, EMA, WMA, DEMA, TEMA)."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    sma: NotRequired[float]
    ema: NotRequired[float]
    wma: NotRequired[float]
    dema: NotRequired[float]
    tema: NotRequired[float]


class TechnicalIndicatorRSI(TypedDict):
    """RSI indicator data."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    rsi: float


class TechnicalIndicatorStdDev(TypedDict):
    """Standard deviation indicator data."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    standardDeviation: float


class TechnicalIndicatorWilliams(TypedDict):
    """Williams %R indicator data."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    williams: float


class TechnicalIndicatorADX(TypedDict):
    """ADX indicator data."""

    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    adx: float
