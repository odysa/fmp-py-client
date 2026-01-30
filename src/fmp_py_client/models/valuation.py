"""Valuation and DCF response types."""

from typing import NotRequired, TypedDict


class DCFValuation(TypedDict):
    """Discounted cash flow valuation."""

    symbol: str
    date: str
    dcf: float
    stockPrice: NotRequired[float]


class CustomDCF(TypedDict):
    """Custom DCF valuation with detailed inputs."""

    symbol: str
    date: str
    dcf: float
    stockPrice: NotRequired[float]
    revenue: NotRequired[int]
    revenueGrowth: NotRequired[float]
    ebitda: NotRequired[int]
    ebitdaMargin: NotRequired[float]
    ebit: NotRequired[int]
    ebitMargin: NotRequired[float]
    depreciation: NotRequired[int]
    totalCash: NotRequired[int]
    receivables: NotRequired[int]
    inventories: NotRequired[int]
    payable: NotRequired[int]
    capitalExpenditure: NotRequired[int]
    price: NotRequired[float]
    beta: NotRequired[float]
    dilutedSharesOutstanding: NotRequired[int]
    costOfDebt: NotRequired[float]
    taxRate: NotRequired[float]
    afterTaxCostOfDebt: NotRequired[float]
    riskFreeRate: NotRequired[float]
    marketRiskPremium: NotRequired[float]
    costOfEquity: NotRequired[float]
    totalDebt: NotRequired[int]
    totalEquity: NotRequired[int]
    totalCapital: NotRequired[int]
    debtWeighting: NotRequired[float]
    equityWeighting: NotRequired[float]
    wacc: NotRequired[float]
    terminalValue: NotRequired[int]
    presentTerminalValue: NotRequired[int]
    enterpriseValue: NotRequired[int]
    netDebt: NotRequired[int]
    equityValue: NotRequired[int]
    equityValuePerShare: NotRequired[float]
    freeCashFlowT1: NotRequired[int]


class EnterpriseValue(TypedDict):
    """Enterprise value data."""

    symbol: str
    date: str
    stockPrice: float
    numberOfShares: int
    marketCapitalization: int
    minusCashAndCashEquivalents: int
    addTotalDebt: int
    enterpriseValue: int
