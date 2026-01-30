"""ETF and fund response types."""

from typing import NotRequired, TypedDict


class ETFHolding(TypedDict):
    """ETF holding data."""

    asset: str
    name: NotRequired[str]
    sharesNumber: int
    weightPercentage: float
    marketValue: NotRequired[float]


class ETFInfo(TypedDict):
    """ETF information."""

    symbol: str
    name: str
    description: NotRequired[str]
    assetClass: NotRequired[str]
    domicile: NotRequired[str]
    etfCompany: NotRequired[str]
    expenseRatio: NotRequired[float]
    inceptionDate: NotRequired[str]
    website: NotRequired[str]
    isin: NotRequired[str]
    cusip: NotRequired[str]
    nav: NotRequired[float]
    navCurrency: NotRequired[str]
    aum: NotRequired[int]
    avgVolume: NotRequired[int]
    holdingsCount: NotRequired[int]


class ETFCountryWeighting(TypedDict):
    """ETF country allocation."""

    country: str
    weightPercentage: float


class ETFAssetExposure(TypedDict):
    """ETF asset class exposure."""

    assetClass: str
    weightPercentage: float


class ETFSectorWeighting(TypedDict):
    """ETF sector weighting."""

    sector: str
    weightPercentage: float


class FundHolder(TypedDict):
    """Fund holder info."""

    holder: str
    shares: int
    dateReported: str
    change: NotRequired[int]
    weightPercentage: NotRequired[float]


class FundDisclosure(TypedDict):
    """Fund disclosure data."""

    symbol: str
    cik: str
    date: str
    shares: int
    value: float
    weightPercentage: NotRequired[float]


class FundDisclosureDate(TypedDict):
    """Fund disclosure available dates."""

    symbol: str
    year: int
    quarter: int
