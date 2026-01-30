"""Company profile and data response types."""

from typing import NotRequired, TypedDict


class CompanyProfile(TypedDict):
    """Full company profile data."""

    symbol: str
    price: float
    marketCap: int
    beta: NotRequired[float | None]
    lastDiv: NotRequired[float]
    range: NotRequired[str]
    changes: NotRequired[float]
    changesPercentage: NotRequired[float]
    volume: NotRequired[int]
    avgVolume: NotRequired[int]
    companyName: str
    currency: NotRequired[str]
    cik: NotRequired[str | None]
    isin: NotRequired[str | None]
    cusip: NotRequired[str | None]
    exchangeFullName: NotRequired[str]
    exchange: str
    industry: NotRequired[str]
    website: NotRequired[str]
    description: NotRequired[str]
    ceo: NotRequired[str | None]
    sector: NotRequired[str]
    country: NotRequired[str]
    fullTimeEmployees: NotRequired[int | None]
    phone: NotRequired[str | None]
    address: NotRequired[str | None]
    city: NotRequired[str | None]
    state: NotRequired[str | None]
    zip: NotRequired[str | None]
    image: NotRequired[str]
    ipoDate: NotRequired[str | None]
    defaultImage: NotRequired[bool]
    isEtf: NotRequired[bool]
    isActivelyTrading: NotRequired[bool]
    isAdr: NotRequired[bool]
    isFund: NotRequired[bool]
    dcf: NotRequired[float | None]
    dcfDiff: NotRequired[float | None]


class Executive(TypedDict):
    """Company executive information."""

    title: str
    name: str
    pay: NotRequired[float | None]
    currencyPay: NotRequired[str]
    gender: NotRequired[str | None]
    yearBorn: NotRequired[int | None]
    titleSince: NotRequired[str | None]


class ExecutiveCompensation(TypedDict):
    """Executive compensation data."""

    cik: str
    symbol: str
    companyName: str
    filingDate: str
    acceptedDate: str
    nameAndPosition: str
    year: int
    salary: int
    bonus: int
    stockAward: int
    optionAward: int
    incentivePlanCompensation: int
    allOtherCompensation: int
    total: int
    link: str


class CompensationBenchmark(TypedDict):
    """Industry compensation benchmark."""

    industry: str
    averageCompensation: float
    medianCompensation: float
    year: int


class EmployeeCount(TypedDict):
    """Company employee count."""

    symbol: str
    cik: str
    acceptanceTime: str
    periodOfReport: str
    companyName: str
    formType: str
    filingDate: str
    employeeCount: int
    source: str


class MarketCap(TypedDict):
    """Market capitalization data."""

    symbol: str
    date: str
    marketCap: float


class ShareFloat(TypedDict):
    """Shares float data."""

    symbol: str
    date: str
    freeFloat: float
    floatShares: int
    outstandingShares: int
    source: NotRequired[str]


class StockPeer(TypedDict):
    """Stock peer comparison."""

    symbol: str
    companyName: str
    price: float
    mktCap: int


class CompanyNote(TypedDict):
    """Company notes from SEC filings."""

    cik: str
    symbol: str
    title: str
    exchange: str


class CompanyScreenerResult(TypedDict):
    """Company screener result."""

    symbol: str
    companyName: str
    marketCap: NotRequired[int]
    sector: NotRequired[str]
    industry: NotRequired[str]
    beta: NotRequired[float | None]
    price: NotRequired[float]
    lastAnnualDividend: NotRequired[float | None]
    volume: NotRequired[int]
    exchange: NotRequired[str]
    exchangeShortName: NotRequired[str]
    country: NotRequired[str]
    isEtf: NotRequired[bool]
    isFund: NotRequired[bool]
    isActivelyTrading: NotRequired[bool]
