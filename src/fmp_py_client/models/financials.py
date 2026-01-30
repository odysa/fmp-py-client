"""Financial statement response types."""

from typing import Any, NotRequired, TypedDict


class IncomeStatement(TypedDict):
    """Income statement data."""

    date: str
    symbol: str
    reportedCurrency: str
    cik: NotRequired[str]
    filingDate: NotRequired[str]
    acceptedDate: NotRequired[str]
    calendarYear: NotRequired[str]
    period: str
    revenue: int
    costOfRevenue: int
    grossProfit: int
    grossProfitRatio: float
    researchAndDevelopmentExpenses: NotRequired[int]
    generalAndAdministrativeExpenses: NotRequired[int]
    sellingAndMarketingExpenses: NotRequired[int]
    sellingGeneralAndAdministrativeExpenses: NotRequired[int]
    otherExpenses: NotRequired[int]
    operatingExpenses: int
    costAndExpenses: int
    interestIncome: NotRequired[int]
    interestExpense: NotRequired[int]
    depreciationAndAmortization: NotRequired[int]
    ebitda: int
    ebitdaratio: float
    operatingIncome: int
    operatingIncomeRatio: float
    totalOtherIncomeExpensesNet: NotRequired[int]
    incomeBeforeTax: int
    incomeBeforeTaxRatio: NotRequired[float]
    incomeTaxExpense: int
    netIncome: int
    netIncomeRatio: float
    eps: float
    epsdiluted: float
    weightedAverageShsOut: int
    weightedAverageShsOutDil: int
    link: NotRequired[str]
    finalLink: NotRequired[str]


class BalanceSheetStatement(TypedDict):
    """Balance sheet statement data."""

    date: str
    symbol: str
    reportedCurrency: str
    cik: NotRequired[str]
    filingDate: NotRequired[str]
    acceptedDate: NotRequired[str]
    calendarYear: NotRequired[str]
    period: str
    cashAndCashEquivalents: int
    shortTermInvestments: NotRequired[int]
    cashAndShortTermInvestments: int
    netReceivables: NotRequired[int]
    inventory: NotRequired[int]
    otherCurrentAssets: NotRequired[int]
    totalCurrentAssets: int
    propertyPlantEquipmentNet: NotRequired[int]
    goodwill: NotRequired[int]
    intangibleAssets: NotRequired[int]
    goodwillAndIntangibleAssets: NotRequired[int]
    longTermInvestments: NotRequired[int]
    taxAssets: NotRequired[int]
    otherNonCurrentAssets: NotRequired[int]
    totalNonCurrentAssets: int
    otherAssets: NotRequired[int]
    totalAssets: int
    accountPayables: NotRequired[int]
    shortTermDebt: NotRequired[int]
    taxPayables: NotRequired[int]
    deferredRevenue: NotRequired[int]
    otherCurrentLiabilities: NotRequired[int]
    totalCurrentLiabilities: int
    longTermDebt: NotRequired[int]
    deferredRevenueNonCurrent: NotRequired[int]
    deferredTaxLiabilitiesNonCurrent: NotRequired[int]
    otherNonCurrentLiabilities: NotRequired[int]
    totalNonCurrentLiabilities: int
    otherLiabilities: NotRequired[int]
    capitalLeaseObligations: NotRequired[int]
    totalLiabilities: int
    preferredStock: NotRequired[int]
    commonStock: NotRequired[int]
    retainedEarnings: int
    accumulatedOtherComprehensiveIncomeLoss: NotRequired[int]
    othertotalStockholdersEquity: NotRequired[int]
    totalStockholdersEquity: int
    totalEquity: int
    totalLiabilitiesAndStockholdersEquity: int
    minorityInterest: NotRequired[int]
    totalLiabilitiesAndTotalEquity: int
    totalInvestments: NotRequired[int]
    totalDebt: int
    netDebt: int
    link: NotRequired[str]
    finalLink: NotRequired[str]


class CashFlowStatement(TypedDict):
    """Cash flow statement data."""

    date: str
    symbol: str
    reportedCurrency: str
    cik: NotRequired[str]
    filingDate: NotRequired[str]
    acceptedDate: NotRequired[str]
    calendarYear: NotRequired[str]
    period: str
    netIncome: int
    depreciationAndAmortization: NotRequired[int]
    deferredIncomeTax: NotRequired[int]
    stockBasedCompensation: NotRequired[int]
    changeInWorkingCapital: NotRequired[int]
    accountsReceivables: NotRequired[int]
    inventory: NotRequired[int]
    accountsPayables: NotRequired[int]
    otherWorkingCapital: NotRequired[int]
    otherNonCashItems: NotRequired[int]
    netCashProvidedByOperatingActivities: int
    investmentsInPropertyPlantAndEquipment: NotRequired[int]
    acquisitionsNet: NotRequired[int]
    purchasesOfInvestments: NotRequired[int]
    salesMaturitiesOfInvestments: NotRequired[int]
    otherInvestingActivites: NotRequired[int]
    netCashUsedForInvestingActivites: int
    debtRepayment: NotRequired[int]
    commonStockIssued: NotRequired[int]
    commonStockRepurchased: NotRequired[int]
    dividendsPaid: NotRequired[int]
    otherFinancingActivites: NotRequired[int]
    netCashUsedProvidedByFinancingActivities: int
    effectOfForexChangesOnCash: NotRequired[int]
    netChangeInCash: int
    cashAtEndOfPeriod: int
    cashAtBeginningOfPeriod: int
    operatingCashFlow: int
    capitalExpenditure: int
    freeCashFlow: int
    link: NotRequired[str]
    finalLink: NotRequired[str]


class IncomeStatementGrowth(TypedDict):
    """Income statement growth metrics."""

    date: str
    symbol: str
    period: str
    calendarYear: NotRequired[str]
    growthRevenue: NotRequired[float]
    growthCostOfRevenue: NotRequired[float]
    growthGrossProfit: NotRequired[float]
    growthGrossProfitRatio: NotRequired[float]
    growthResearchAndDevelopmentExpenses: NotRequired[float]
    growthGeneralAndAdministrativeExpenses: NotRequired[float]
    growthSellingAndMarketingExpenses: NotRequired[float]
    growthOtherExpenses: NotRequired[float]
    growthOperatingExpenses: NotRequired[float]
    growthCostAndExpenses: NotRequired[float]
    growthInterestExpense: NotRequired[float]
    growthDepreciationAndAmortization: NotRequired[float]
    growthEBITDA: NotRequired[float]
    growthEBITDARatio: NotRequired[float]
    growthOperatingIncome: NotRequired[float]
    growthOperatingIncomeRatio: NotRequired[float]
    growthTotalOtherIncomeExpensesNet: NotRequired[float]
    growthIncomeBeforeTax: NotRequired[float]
    growthIncomeBeforeTaxRatio: NotRequired[float]
    growthIncomeTaxExpense: NotRequired[float]
    growthNetIncome: NotRequired[float]
    growthNetIncomeRatio: NotRequired[float]
    growthEPS: NotRequired[float]
    growthEPSDiluted: NotRequired[float]
    growthWeightedAverageShsOut: NotRequired[float]
    growthWeightedAverageShsOutDil: NotRequired[float]


class BalanceSheetStatementGrowth(TypedDict):
    """Balance sheet statement growth metrics."""

    date: str
    symbol: str
    period: str
    calendarYear: NotRequired[str]
    growthCashAndCashEquivalents: NotRequired[float]
    growthShortTermInvestments: NotRequired[float]
    growthCashAndShortTermInvestments: NotRequired[float]
    growthNetReceivables: NotRequired[float]
    growthInventory: NotRequired[float]
    growthOtherCurrentAssets: NotRequired[float]
    growthTotalCurrentAssets: NotRequired[float]
    growthPropertyPlantEquipmentNet: NotRequired[float]
    growthGoodwill: NotRequired[float]
    growthIntangibleAssets: NotRequired[float]
    growthGoodwillAndIntangibleAssets: NotRequired[float]
    growthLongTermInvestments: NotRequired[float]
    growthTaxAssets: NotRequired[float]
    growthOtherNonCurrentAssets: NotRequired[float]
    growthTotalNonCurrentAssets: NotRequired[float]
    growthOtherAssets: NotRequired[float]
    growthTotalAssets: NotRequired[float]
    growthAccountPayables: NotRequired[float]
    growthShortTermDebt: NotRequired[float]
    growthTaxPayables: NotRequired[float]
    growthDeferredRevenue: NotRequired[float]
    growthOtherCurrentLiabilities: NotRequired[float]
    growthTotalCurrentLiabilities: NotRequired[float]
    growthLongTermDebt: NotRequired[float]
    growthDeferredRevenueNonCurrent: NotRequired[float]
    growthDeferredTaxLiabilitiesNonCurrent: NotRequired[float]
    growthOtherNonCurrentLiabilities: NotRequired[float]
    growthTotalNonCurrentLiabilities: NotRequired[float]
    growthOtherLiabilities: NotRequired[float]
    growthTotalLiabilities: NotRequired[float]
    growthCommonStock: NotRequired[float]
    growthRetainedEarnings: NotRequired[float]
    growthAccumulatedOtherComprehensiveIncomeLoss: NotRequired[float]
    growthOthertotalStockholdersEquity: NotRequired[float]
    growthTotalStockholdersEquity: NotRequired[float]
    growthTotalLiabilitiesAndStockholdersEquity: NotRequired[float]
    growthTotalInvestments: NotRequired[float]
    growthTotalDebt: NotRequired[float]
    growthNetDebt: NotRequired[float]


class CashFlowStatementGrowth(TypedDict):
    """Cash flow statement growth metrics."""

    date: str
    symbol: str
    period: str
    calendarYear: NotRequired[str]
    growthNetIncome: NotRequired[float]
    growthDepreciationAndAmortization: NotRequired[float]
    growthDeferredIncomeTax: NotRequired[float]
    growthStockBasedCompensation: NotRequired[float]
    growthChangeInWorkingCapital: NotRequired[float]
    growthAccountsReceivables: NotRequired[float]
    growthInventory: NotRequired[float]
    growthAccountsPayables: NotRequired[float]
    growthOtherWorkingCapital: NotRequired[float]
    growthOtherNonCashItems: NotRequired[float]
    growthNetCashProvidedByOperatingActivites: NotRequired[float]
    growthInvestmentsInPropertyPlantAndEquipment: NotRequired[float]
    growthAcquisitionsNet: NotRequired[float]
    growthPurchasesOfInvestments: NotRequired[float]
    growthSalesMaturitiesOfInvestments: NotRequired[float]
    growthOtherInvestingActivites: NotRequired[float]
    growthNetCashUsedForInvestingActivites: NotRequired[float]
    growthDebtRepayment: NotRequired[float]
    growthCommonStockIssued: NotRequired[float]
    growthCommonStockRepurchased: NotRequired[float]
    growthDividendsPaid: NotRequired[float]
    growthOtherFinancingActivites: NotRequired[float]
    growthNetCashUsedProvidedByFinancingActivities: NotRequired[float]
    growthEffectOfForexChangesOnCash: NotRequired[float]
    growthNetChangeInCash: NotRequired[float]
    growthCashAtEndOfPeriod: NotRequired[float]
    growthCashAtBeginningOfPeriod: NotRequired[float]
    growthOperatingCashFlow: NotRequired[float]
    growthCapitalExpenditure: NotRequired[float]
    growthFreeCashFlow: NotRequired[float]


class FinancialGrowth(TypedDict):
    """Overall financial growth metrics."""

    symbol: str
    date: str
    period: str
    calendarYear: NotRequired[str]
    revenueGrowth: NotRequired[float]
    grossProfitGrowth: NotRequired[float]
    ebitgrowth: NotRequired[float]
    operatingIncomeGrowth: NotRequired[float]
    netIncomeGrowth: NotRequired[float]
    epsgrowth: NotRequired[float]
    epsdilutedGrowth: NotRequired[float]
    weightedAverageSharesGrowth: NotRequired[float]
    weightedAverageSharesDilutedGrowth: NotRequired[float]
    dividendsperShareGrowth: NotRequired[float]
    operatingCashFlowGrowth: NotRequired[float]
    freeCashFlowGrowth: NotRequired[float]
    tenYRevenueGrowthPerShare: NotRequired[float]
    fiveYRevenueGrowthPerShare: NotRequired[float]
    threeYRevenueGrowthPerShare: NotRequired[float]
    tenYOperatingCFGrowthPerShare: NotRequired[float]
    fiveYOperatingCFGrowthPerShare: NotRequired[float]
    threeYOperatingCFGrowthPerShare: NotRequired[float]
    tenYNetIncomeGrowthPerShare: NotRequired[float]
    fiveYNetIncomeGrowthPerShare: NotRequired[float]
    threeYNetIncomeGrowthPerShare: NotRequired[float]
    tenYShareholdersEquityGrowthPerShare: NotRequired[float]
    fiveYShareholdersEquityGrowthPerShare: NotRequired[float]
    threeYShareholdersEquityGrowthPerShare: NotRequired[float]
    tenYDividendperShareGrowthPerShare: NotRequired[float]
    fiveYDividendperShareGrowthPerShare: NotRequired[float]
    threeYDividendperShareGrowthPerShare: NotRequired[float]
    receivablesGrowth: NotRequired[float]
    inventoryGrowth: NotRequired[float]
    assetGrowth: NotRequired[float]
    bookValueperShareGrowth: NotRequired[float]
    debtGrowth: NotRequired[float]
    rdexpenseGrowth: NotRequired[float]
    sgaexpensesGrowth: NotRequired[float]


class LatestFinancialStatement(TypedDict):
    """Latest financial statement info."""

    symbol: str
    date: str
    period: str
    filingDate: str


class FinancialReportDate(TypedDict):
    """Available financial report dates."""

    symbol: str
    date: str
    period: str
    linkXlsx: NotRequired[str]
    linkJson: NotRequired[str]


class RevenueSegmentation(TypedDict):
    """Revenue segmentation data (product or geographic)."""

    date: str
    # Dynamic keys based on product/region names
    # Using Any to allow dynamic keys
