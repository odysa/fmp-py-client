"""ESG and sustainability response types."""

from typing import NotRequired, TypedDict


class ESGDisclosure(TypedDict):
    """ESG disclosure data."""

    symbol: str
    cik: str
    date: str
    environmentalScore: NotRequired[float]
    socialScore: NotRequired[float]
    governanceScore: NotRequired[float]
    ESGScore: NotRequired[float]
    companyName: NotRequired[str]
    industry: NotRequired[str]
    formType: NotRequired[str]
    acceptedDate: NotRequired[str]
    url: NotRequired[str]


class ESGRating(TypedDict):
    """ESG rating data."""

    symbol: str
    cik: str
    companyName: str
    industry: NotRequired[str]
    year: int
    ESGRiskRating: NotRequired[str]
    environmentalScore: NotRequired[float]
    socialScore: NotRequired[float]
    governanceScore: NotRequired[float]


class ESGBenchmark(TypedDict):
    """ESG benchmark by sector."""

    sector: str
    averageEnvironmentalScore: float
    averageSocialScore: float
    averageGovernanceScore: float
    year: int


class COTReport(TypedDict):
    """Commitment of Traders report."""

    symbol: str
    name: str
    sector: str
    currentLongMarketSituation: NotRequired[float]
    currentShortMarketSituation: NotRequired[float]
    date: str


class COTAnalysis(TypedDict):
    """Commitment of Traders analysis."""

    symbol: str
    name: str
    sector: str
    currentLongMarketSituation: NotRequired[float]
    currentShortMarketSituation: NotRequired[float]
    netPosition: NotRequired[float]
    date: str


class COTSymbol(TypedDict):
    """Commitment of Traders symbol."""

    tradingSymbol: str
    shortName: str
