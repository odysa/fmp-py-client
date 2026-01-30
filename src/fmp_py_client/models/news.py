"""News and analyst data response types."""

from typing import NotRequired, TypedDict


class NewsArticle(TypedDict):
    """News article data."""

    symbol: NotRequired[str]
    publishedDate: str
    publisher: NotRequired[str]
    title: str
    image: NotRequired[str]
    site: str
    text: str
    url: str


class FMPArticle(TypedDict):
    """FMP article data."""

    title: str
    date: str
    content: str
    tickers: NotRequired[str]
    image: NotRequired[str]
    link: str
    author: NotRequired[str]
    site: NotRequired[str]


class AnalystEstimates(TypedDict):
    """Analyst estimates data."""

    symbol: str
    date: str
    estimatedRevenueLow: NotRequired[int]
    estimatedRevenueHigh: NotRequired[int]
    estimatedRevenueAvg: NotRequired[int]
    estimatedEbitdaLow: NotRequired[int]
    estimatedEbitdaHigh: NotRequired[int]
    estimatedEbitdaAvg: NotRequired[int]
    estimatedEbitLow: NotRequired[int]
    estimatedEbitHigh: NotRequired[int]
    estimatedEbitAvg: NotRequired[int]
    estimatedNetIncomeLow: NotRequired[int]
    estimatedNetIncomeHigh: NotRequired[int]
    estimatedNetIncomeAvg: NotRequired[int]
    estimatedSgaExpenseLow: NotRequired[int]
    estimatedSgaExpenseHigh: NotRequired[int]
    estimatedSgaExpenseAvg: NotRequired[int]
    estimatedEpsAvg: NotRequired[float]
    estimatedEpsHigh: NotRequired[float]
    estimatedEpsLow: NotRequired[float]
    numberAnalystEstimatedRevenue: NotRequired[int]
    numberAnalystsEstimatedEps: NotRequired[int]


class RatingSnapshot(TypedDict):
    """Rating snapshot data."""

    symbol: str
    rating: str
    ratingScore: int
    ratingRecommendation: str
    ratingDetailsDCFScore: NotRequired[int]
    ratingDetailsDCFRecommendation: NotRequired[str]
    ratingDetailsROEScore: NotRequired[int]
    ratingDetailsROERecommendation: NotRequired[str]
    ratingDetailsROAScore: NotRequired[int]
    ratingDetailsROARecommendation: NotRequired[str]
    ratingDetailsDEScore: NotRequired[int]
    ratingDetailsDERecommendation: NotRequired[str]
    ratingDetailsPEScore: NotRequired[int]
    ratingDetailsPERecommendation: NotRequired[str]
    ratingDetailsPBScore: NotRequired[int]
    ratingDetailsPBRecommendation: NotRequired[str]


class PriceTargetSummary(TypedDict):
    """Price target summary data."""

    symbol: str
    lastMonth: NotRequired[int]
    lastMonthAvgPriceTarget: NotRequired[float]
    lastQuarter: NotRequired[int]
    lastQuarterAvgPriceTarget: NotRequired[float]
    lastYear: NotRequired[int]
    lastYearAvgPriceTarget: NotRequired[float]
    allTime: NotRequired[int]
    allTimeAvgPriceTarget: NotRequired[float]
    publishers: NotRequired[str]


class PriceTargetConsensus(TypedDict):
    """Price target consensus data."""

    symbol: str
    targetHigh: NotRequired[float]
    targetLow: NotRequired[float]
    targetConsensus: NotRequired[float]
    targetMedian: NotRequired[float]


class Grade(TypedDict):
    """Analyst grade data."""

    symbol: str
    date: str
    gradingCompany: str
    previousGrade: NotRequired[str]
    newGrade: str


class HistoricalGrade(TypedDict):
    """Historical analyst ratings count."""

    symbol: str
    date: str
    analystRatingsStrongBuy: int
    analystRatingsBuy: int
    analystRatingsHold: int
    analystRatingsSell: int
    analystRatingsStrongSell: int


class GradesConsensus(TypedDict):
    """Analyst grades consensus."""

    symbol: str
    strongBuy: int
    buy: int
    hold: int
    sell: int
    strongSell: int
    consensus: str
