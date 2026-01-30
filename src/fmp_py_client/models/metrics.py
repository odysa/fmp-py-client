"""Financial metrics and ratios response types."""

from typing import NotRequired, TypedDict


class KeyMetrics(TypedDict):
    """Key financial metrics."""

    symbol: str
    date: str
    calendarYear: NotRequired[str]
    period: str
    revenuePerShare: NotRequired[float]
    netIncomePerShare: NotRequired[float]
    operatingCashFlowPerShare: NotRequired[float]
    freeCashFlowPerShare: NotRequired[float]
    cashPerShare: NotRequired[float]
    bookValuePerShare: NotRequired[float]
    tangibleBookValuePerShare: NotRequired[float]
    shareholdersEquityPerShare: NotRequired[float]
    interestDebtPerShare: NotRequired[float]
    marketCap: NotRequired[int]
    enterpriseValue: NotRequired[int]
    peRatio: NotRequired[float]
    priceToSalesRatio: NotRequired[float]
    pocfratio: NotRequired[float]
    pfcfRatio: NotRequired[float]
    pbRatio: NotRequired[float]
    ptbRatio: NotRequired[float]
    evToSales: NotRequired[float]
    enterpriseValueOverEBITDA: NotRequired[float]
    evToOperatingCashFlow: NotRequired[float]
    evToFreeCashFlow: NotRequired[float]
    earningsYield: NotRequired[float]
    freeCashFlowYield: NotRequired[float]
    debtToEquity: NotRequired[float]
    debtToAssets: NotRequired[float]
    netDebtToEBITDA: NotRequired[float]
    currentRatio: NotRequired[float]
    interestCoverage: NotRequired[float]
    incomeQuality: NotRequired[float]
    dividendYield: NotRequired[float]
    payoutRatio: NotRequired[float]
    salesGeneralAndAdministrativeToRevenue: NotRequired[float]
    researchAndDdevelopementToRevenue: NotRequired[float]
    intangiblesToTotalAssets: NotRequired[float]
    capexToOperatingCashFlow: NotRequired[float]
    capexToRevenue: NotRequired[float]
    capexToDepreciation: NotRequired[float]
    stockBasedCompensationToRevenue: NotRequired[float]
    grahamNumber: NotRequired[float]
    roic: NotRequired[float]
    returnOnTangibleAssets: NotRequired[float]
    grahamNetNet: NotRequired[float]
    workingCapital: NotRequired[int]
    tangibleAssetValue: NotRequired[int]
    netCurrentAssetValue: NotRequired[int]
    investedCapital: NotRequired[int]
    averageReceivables: NotRequired[int]
    averagePayables: NotRequired[int]
    averageInventory: NotRequired[int]
    daysSalesOutstanding: NotRequired[float]
    daysPayablesOutstanding: NotRequired[float]
    daysOfInventoryOnHand: NotRequired[float]
    receivablesTurnover: NotRequired[float]
    payablesTurnover: NotRequired[float]
    inventoryTurnover: NotRequired[float]
    roe: NotRequired[float]
    capexPerShare: NotRequired[float]


class FinancialRatios(TypedDict):
    """Financial ratios."""

    symbol: str
    date: str
    calendarYear: NotRequired[str]
    period: str
    currentRatio: NotRequired[float]
    quickRatio: NotRequired[float]
    cashRatio: NotRequired[float]
    daysOfSalesOutstanding: NotRequired[float]
    daysOfInventoryOutstanding: NotRequired[float]
    operatingCycle: NotRequired[float]
    daysOfPayablesOutstanding: NotRequired[float]
    cashConversionCycle: NotRequired[float]
    grossProfitMargin: NotRequired[float]
    operatingProfitMargin: NotRequired[float]
    pretaxProfitMargin: NotRequired[float]
    netProfitMargin: NotRequired[float]
    effectiveTaxRate: NotRequired[float]
    returnOnAssets: NotRequired[float]
    returnOnEquity: NotRequired[float]
    returnOnCapitalEmployed: NotRequired[float]
    netIncomePerEBT: NotRequired[float]
    ebtPerEbit: NotRequired[float]
    ebitPerRevenue: NotRequired[float]
    debtRatio: NotRequired[float]
    debtEquityRatio: NotRequired[float]
    longTermDebtToCapitalization: NotRequired[float]
    totalDebtToCapitalization: NotRequired[float]
    interestCoverage: NotRequired[float]
    cashFlowToDebtRatio: NotRequired[float]
    companyEquityMultiplier: NotRequired[float]
    receivablesTurnover: NotRequired[float]
    payablesTurnover: NotRequired[float]
    inventoryTurnover: NotRequired[float]
    fixedAssetTurnover: NotRequired[float]
    assetTurnover: NotRequired[float]
    operatingCashFlowPerShare: NotRequired[float]
    freeCashFlowPerShare: NotRequired[float]
    cashPerShare: NotRequired[float]
    payoutRatio: NotRequired[float]
    operatingCashFlowSalesRatio: NotRequired[float]
    freeCashFlowOperatingCashFlowRatio: NotRequired[float]
    cashFlowCoverageRatios: NotRequired[float]
    shortTermCoverageRatios: NotRequired[float]
    capitalExpenditureCoverageRatio: NotRequired[float]
    dividendPaidAndCapexCoverageRatio: NotRequired[float]
    dividendPayoutRatio: NotRequired[float]
    priceBookValueRatio: NotRequired[float]
    priceToBookRatio: NotRequired[float]
    priceToSalesRatio: NotRequired[float]
    priceEarningsRatio: NotRequired[float]
    priceToFreeCashFlowsRatio: NotRequired[float]
    priceToOperatingCashFlowsRatio: NotRequired[float]
    priceCashFlowRatio: NotRequired[float]
    priceEarningsToGrowthRatio: NotRequired[float]
    priceSalesRatio: NotRequired[float]
    dividendYield: NotRequired[float]
    enterpriseValueMultiple: NotRequired[float]
    priceFairValue: NotRequired[float]


class FinancialScores(TypedDict):
    """Financial scores (Altman Z-Score, Piotroski, etc.)."""

    symbol: str
    altmanZScore: NotRequired[float]
    piotroskiScore: NotRequired[int]
    workingCapital: NotRequired[int]
    totalAssets: NotRequired[int]
    retainedEarnings: NotRequired[int]
    ebit: NotRequired[int]
    marketCap: NotRequired[float]
    totalLiabilities: NotRequired[int]
    revenue: NotRequired[int]


class OwnerEarnings(TypedDict):
    """Owner earnings data."""

    symbol: str
    date: str
    calendarYear: NotRequired[str]
    period: str
    averagePPE: NotRequired[float]
    maintenanceCapex: NotRequired[int]
    ownersEarnings: NotRequired[int]
    growthCapex: NotRequired[int]
    ownersEarningsPerShare: NotRequired[float]
