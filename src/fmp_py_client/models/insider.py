"""Insider and institutional trading response types."""

from typing import NotRequired, TypedDict


class InsiderTrade(TypedDict):
    """Insider trade data."""

    symbol: str
    filingDate: str
    transactionDate: str
    reportingCik: str
    transactionType: str
    securitiesOwned: NotRequired[int]
    companyCik: NotRequired[str]
    reportingName: str
    typeOfOwner: NotRequired[str]
    acquistionOrDisposition: NotRequired[str]
    formType: NotRequired[str]
    securitiesTransacted: NotRequired[int]
    price: NotRequired[float]
    securityName: NotRequired[str]
    link: NotRequired[str]


class InsiderTransactionType(TypedDict):
    """Insider transaction type."""

    code: str
    description: str


class InsiderStatistics(TypedDict):
    """Insider trading statistics."""

    symbol: str
    cik: str
    year: int
    quarter: int
    purchases: NotRequired[int]
    sales: NotRequired[int]
    buySellRatio: NotRequired[float]
    totalBought: NotRequired[int]
    totalSold: NotRequired[int]
    averageBought: NotRequired[float]
    averageSold: NotRequired[float]
    pPurchases: NotRequired[int]
    sSales: NotRequired[int]


class AcquisitionOwnership(TypedDict):
    """Acquisition of beneficial ownership data."""

    symbol: str
    cik: str
    filingDate: str
    transactionDate: NotRequired[str]
    reportingName: str
    typeOfReportingPerson: NotRequired[str]
    percentOfClass: NotRequired[float]
    securitiesOwned: NotRequired[int]
    link: NotRequired[str]


class InstitutionalOwnership(TypedDict):
    """Institutional ownership data."""

    symbol: str
    cik: str
    date: str
    investorsHolding: NotRequired[int]
    lastInvestorsHolding: NotRequired[int]
    investorsHoldingChange: NotRequired[int]
    numberOf13Fshares: NotRequired[int]
    lastNumberOf13Fshares: NotRequired[int]
    numberOf13FsharesChange: NotRequired[int]
    totalInvested: NotRequired[float]
    lastTotalInvested: NotRequired[float]
    totalInvestedChange: NotRequired[float]
    ownershipPercent: NotRequired[float]
    lastOwnershipPercent: NotRequired[float]
    ownershipPercentChange: NotRequired[float]
    newPositions: NotRequired[int]
    lastNewPositions: NotRequired[int]
    closedPositions: NotRequired[int]
    lastClosedPositions: NotRequired[int]
    increasedPositions: NotRequired[int]
    lastIncreasedPositions: NotRequired[int]
    reducedPositions: NotRequired[int]
    lastReducedPositions: NotRequired[int]
    totalCalls: NotRequired[int]
    lastTotalCalls: NotRequired[int]
    totalCallsChange: NotRequired[int]
    totalPuts: NotRequired[int]
    lastTotalPuts: NotRequired[int]
    totalPutsChange: NotRequired[int]
    putCallRatio: NotRequired[float]
    lastPutCallRatio: NotRequired[float]
    putCallRatioChange: NotRequired[float]


class InstitutionalOwnershipDate(TypedDict):
    """Available institutional ownership dates."""

    cik: str
    year: int
    quarter: int


class InstitutionalHolderAnalytics(TypedDict):
    """Institutional holder analytics."""

    holder: str
    shares: int
    dateReported: str
    change: NotRequired[int]
    changePercentage: NotRequired[float]
    value: NotRequired[float]


class SymbolPositionsSummary(TypedDict):
    """Institutional symbol positions summary."""

    symbol: str
    cik: str
    date: str
    investorsHolding: NotRequired[int]
    totalInvested: NotRequired[float]


class IndustryOwnershipSummary(TypedDict):
    """Industry ownership summary."""

    industry: str
    totalInvested: float
    percentageOfPortfolio: float
