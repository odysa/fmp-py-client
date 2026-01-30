"""Response models for FMP API endpoints.

This module provides TypedDict definitions for all API response types,
enabling type safety and IDE autocomplete for API responses.
"""

from fmp_py_client.models.calendar import (
    Dividend,
    EarningsReport,
    EarningsTranscript,
    EarningsTranscriptDate,
    IPOCalendar,
    IPOProspectus,
    StockSplit,
)
from fmp_py_client.models.company import (
    CompanyNote,
    CompanyProfile,
    CompanyScreenerResult,
    CompensationBenchmark,
    EmployeeCount,
    Executive,
    ExecutiveCompensation,
    MarketCap,
    ShareFloat,
    StockPeer,
)
from fmp_py_client.models.crowdfunding import (
    CrowdfundingOffering,
    EquityOffering,
)
from fmp_py_client.models.economics import (
    Commodity,
    Cryptocurrency,
    EconomicCalendarEvent,
    EconomicIndicator,
    ExchangeHoliday,
    ExchangeMarketHours,
    ForexPair,
    MarketRiskPremium,
    TreasuryRate,
)
from fmp_py_client.models.esg import (
    COTAnalysis,
    COTReport,
    COTSymbol,
    ESGBenchmark,
    ESGDisclosure,
    ESGRating,
)
from fmp_py_client.models.etf import (
    ETFAssetExposure,
    ETFCountryWeighting,
    ETFHolding,
    ETFInfo,
    ETFSectorWeighting,
    FundDisclosure,
    FundDisclosureDate,
    FundHolder,
)
from fmp_py_client.models.financials import (
    BalanceSheetStatement,
    BalanceSheetStatementGrowth,
    CashFlowStatement,
    CashFlowStatementGrowth,
    FinancialGrowth,
    FinancialReportDate,
    IncomeStatement,
    IncomeStatementGrowth,
    LatestFinancialStatement,
    RevenueSegmentation,
)
from fmp_py_client.models.government import (
    GovernmentTrade,
)
from fmp_py_client.models.historical import (
    EODFull,
    EODLight,
    HistoricalChart,
)
from fmp_py_client.models.insider import (
    AcquisitionOwnership,
    IndustryOwnershipSummary,
    InsiderStatistics,
    InsiderTrade,
    InsiderTransactionType,
    InstitutionalHolderAnalytics,
    InstitutionalOwnership,
    InstitutionalOwnershipDate,
    SymbolPositionsSummary,
)
from fmp_py_client.models.market import (
    CIKEntry,
    DelistedCompany,
    HistoricalIndexConstituent,
    IndexConstituent,
    IndexInfo,
    StockListEntry,
    SymbolChange,
)
from fmp_py_client.models.mergers import (
    MergerAcquisition,
)
from fmp_py_client.models.metrics import (
    FinancialRatios,
    FinancialScores,
    KeyMetrics,
    OwnerEarnings,
)
from fmp_py_client.models.movers import (
    StockMover,
)
from fmp_py_client.models.news import (
    AnalystEstimates,
    FMPArticle,
    Grade,
    GradesConsensus,
    HistoricalGrade,
    NewsArticle,
    PriceTargetConsensus,
    PriceTargetSummary,
    RatingSnapshot,
)
from fmp_py_client.models.quotes import (
    AftermarketQuote,
    AftermarketTrade,
    PriceChange,
    ShortQuote,
    StockQuote,
)
from fmp_py_client.models.search import (
    CIKSearchResult,
    ExchangeVariant,
    SearchResult,
)
from fmp_py_client.models.sec import (
    IndustryClassification,
    SECCompanyProfile,
    SECFiling,
    SICCode,
)
from fmp_py_client.models.sector import (
    IndustryPE,
    IndustryPerformance,
    SectorPE,
    SectorPerformance,
)
from fmp_py_client.models.technical import (
    TechnicalIndicatorADX,
    TechnicalIndicatorMA,
    TechnicalIndicatorRSI,
    TechnicalIndicatorStdDev,
    TechnicalIndicatorWilliams,
)
from fmp_py_client.models.valuation import (
    CustomDCF,
    DCFValuation,
    EnterpriseValue,
)

__all__ = [
    # Calendar
    "Dividend",
    "EarningsReport",
    "EarningsTranscript",
    "EarningsTranscriptDate",
    "IPOCalendar",
    "IPOProspectus",
    "StockSplit",
    # Company
    "CompanyNote",
    "CompanyProfile",
    "CompanyScreenerResult",
    "CompensationBenchmark",
    "EmployeeCount",
    "Executive",
    "ExecutiveCompensation",
    "MarketCap",
    "ShareFloat",
    "StockPeer",
    # Crowdfunding
    "CrowdfundingOffering",
    "EquityOffering",
    # Economics
    "Commodity",
    "Cryptocurrency",
    "EconomicCalendarEvent",
    "EconomicIndicator",
    "ExchangeHoliday",
    "ExchangeMarketHours",
    "ForexPair",
    "MarketRiskPremium",
    "TreasuryRate",
    # ESG
    "COTAnalysis",
    "COTReport",
    "COTSymbol",
    "ESGBenchmark",
    "ESGDisclosure",
    "ESGRating",
    # ETF
    "ETFAssetExposure",
    "ETFCountryWeighting",
    "ETFHolding",
    "ETFInfo",
    "ETFSectorWeighting",
    "FundDisclosure",
    "FundDisclosureDate",
    "FundHolder",
    # Financials
    "BalanceSheetStatement",
    "BalanceSheetStatementGrowth",
    "CashFlowStatement",
    "CashFlowStatementGrowth",
    "FinancialGrowth",
    "FinancialReportDate",
    "IncomeStatement",
    "IncomeStatementGrowth",
    "LatestFinancialStatement",
    "RevenueSegmentation",
    # Government
    "GovernmentTrade",
    # Historical
    "EODFull",
    "EODLight",
    "HistoricalChart",
    # Insider
    "AcquisitionOwnership",
    "IndustryOwnershipSummary",
    "InsiderStatistics",
    "InsiderTrade",
    "InsiderTransactionType",
    "InstitutionalHolderAnalytics",
    "InstitutionalOwnership",
    "InstitutionalOwnershipDate",
    "SymbolPositionsSummary",
    # Market
    "CIKEntry",
    "DelistedCompany",
    "HistoricalIndexConstituent",
    "IndexConstituent",
    "IndexInfo",
    "StockListEntry",
    "SymbolChange",
    # Mergers
    "MergerAcquisition",
    # Metrics
    "FinancialRatios",
    "FinancialScores",
    "KeyMetrics",
    "OwnerEarnings",
    # Movers
    "StockMover",
    # News
    "AnalystEstimates",
    "FMPArticle",
    "Grade",
    "GradesConsensus",
    "HistoricalGrade",
    "NewsArticle",
    "PriceTargetConsensus",
    "PriceTargetSummary",
    "RatingSnapshot",
    # Quotes
    "AftermarketQuote",
    "AftermarketTrade",
    "PriceChange",
    "ShortQuote",
    "StockQuote",
    # Search
    "CIKSearchResult",
    "ExchangeVariant",
    "SearchResult",
    # SEC
    "IndustryClassification",
    "SECCompanyProfile",
    "SECFiling",
    "SICCode",
    # Sector
    "IndustryPE",
    "IndustryPerformance",
    "SectorPE",
    "SectorPerformance",
    # Technical
    "TechnicalIndicatorADX",
    "TechnicalIndicatorMA",
    "TechnicalIndicatorRSI",
    "TechnicalIndicatorStdDev",
    "TechnicalIndicatorWilliams",
    # Valuation
    "CustomDCF",
    "DCFValuation",
    "EnterpriseValue",
]
