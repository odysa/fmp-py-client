"""Calendar-related response types (dividends, splits, earnings, IPO)."""

from typing import NotRequired, TypedDict


class Dividend(TypedDict):
    """Dividend data."""

    symbol: str
    date: str
    recordDate: NotRequired[str | None]
    paymentDate: NotRequired[str | None]
    declarationDate: NotRequired[str | None]
    adjDividend: NotRequired[float]
    dividend: float
    # yield is a reserved word, API returns it as 'yield'


class StockSplit(TypedDict):
    """Stock split data."""

    symbol: str
    date: str
    numerator: int
    denominator: int


class EarningsReport(TypedDict):
    """Earnings report data."""

    symbol: str
    date: str
    epsActual: NotRequired[float | None]
    epsEstimated: NotRequired[float | None]
    revenueActual: NotRequired[int | None]
    revenueEstimated: NotRequired[int | None]
    time: NotRequired[str]
    updatedFromDate: NotRequired[str]


class EarningsTranscript(TypedDict):
    """Earnings call transcript."""

    symbol: str
    quarter: int
    year: int
    date: str
    content: str


class EarningsTranscriptDate(TypedDict):
    """Available earnings transcript dates."""

    symbol: str
    quarter: int
    year: int
    date: str


class IPOCalendar(TypedDict):
    """IPO calendar data."""

    symbol: NotRequired[str]
    date: str
    company: str
    exchange: NotRequired[str]
    actions: NotRequired[str]
    shares: NotRequired[int]
    priceRange: NotRequired[str]
    marketCap: NotRequired[int]


class IPOProspectus(TypedDict):
    """IPO prospectus data."""

    symbol: str
    cik: str
    form: str
    filingDate: str
    acceptedDate: str
    effectivenessDate: NotRequired[str]
    url: str
    pricePublicPerShare: NotRequired[float]
    pricePublicTotal: NotRequired[int]
    discountsAndCommissionsPerShare: NotRequired[float]
    discountsAndCommissionsTotal: NotRequired[int]
    proceedsBeforeExpensesPerShare: NotRequired[float]
    proceedsBeforeExpensesTotal: NotRequired[int]
