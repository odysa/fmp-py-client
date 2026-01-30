"""Economics and market timing response types."""

from typing import NotRequired, TypedDict


class TreasuryRate(TypedDict):
    """US Treasury rates."""

    date: str
    month1: NotRequired[float]
    month2: NotRequired[float]
    month3: NotRequired[float]
    month6: NotRequired[float]
    year1: NotRequired[float]
    year2: NotRequired[float]
    year3: NotRequired[float]
    year5: NotRequired[float]
    year7: NotRequired[float]
    year10: NotRequired[float]
    year20: NotRequired[float]
    year30: NotRequired[float]


class EconomicIndicator(TypedDict):
    """Economic indicator data."""

    date: str
    value: float


class EconomicCalendarEvent(TypedDict):
    """Economic calendar event."""

    date: str
    country: str
    event: str
    currency: NotRequired[str]
    previous: NotRequired[float]
    estimate: NotRequired[float]
    actual: NotRequired[float]
    change: NotRequired[float]
    impact: NotRequired[str]
    changePercentage: NotRequired[float]


class MarketRiskPremium(TypedDict):
    """Market risk premium by country."""

    country: str
    continent: NotRequired[str]
    countryRiskPremium: float
    totalEquityRiskPremium: float


class Commodity(TypedDict):
    """Commodity info."""

    symbol: str
    name: str
    currency: NotRequired[str]
    stockExchange: NotRequired[str]
    exchangeShortName: NotRequired[str]


class ForexPair(TypedDict):
    """Forex currency pair."""

    symbol: str
    name: str
    currency: NotRequired[str]
    stockExchange: NotRequired[str]
    exchangeShortName: NotRequired[str]


class Cryptocurrency(TypedDict):
    """Cryptocurrency info."""

    symbol: str
    name: str
    currency: NotRequired[str]
    stockExchange: NotRequired[str]
    exchangeShortName: NotRequired[str]


class ExchangeMarketHours(TypedDict):
    """Exchange market hours."""

    stockExchange: str
    stockMarketHours: NotRequired[dict]
    stockMarketHolidays: NotRequired[list]
    isTheStockMarketOpen: bool
    isTheEuronextMarketOpen: NotRequired[bool]
    isTheForexMarketOpen: NotRequired[bool]
    isTheCryptoMarketOpen: NotRequired[bool]


class ExchangeHoliday(TypedDict):
    """Exchange holiday."""

    year: int
    date: str
    name: str
    exchange: str
