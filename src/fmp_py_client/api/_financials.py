"""Financial statements API endpoints."""

from typing import Any

from fmp_py_client._types import JSONObject, Period
from fmp_py_client.models import (
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


class FinancialsMixin:
    """Financial statements endpoints."""

    async def income_statement(
        self,
        *,
        symbol: str | None = None,
        period: Period | None = None,
        limit: int | None = None,
    ) -> list[IncomeStatement]:
        """Get income statements."""
        return await self._request(  # type: ignore[attr-defined]
            "income-statement",
            params={"symbol": symbol, "period": period, "limit": limit},
        )

    async def balance_sheet_statement(
        self,
        *,
        symbol: str | None = None,
        period: Period | None = None,
        limit: int | None = None,
    ) -> list[BalanceSheetStatement]:
        """Get balance sheet statements."""
        return await self._request(  # type: ignore[attr-defined]
            "balance-sheet-statement",
            params={"symbol": symbol, "period": period, "limit": limit},
        )

    async def cash_flow_statement(
        self,
        *,
        symbol: str | None = None,
        period: Period | None = None,
        limit: int | None = None,
    ) -> list[CashFlowStatement]:
        """Get cash flow statements."""
        return await self._request(  # type: ignore[attr-defined]
            "cash-flow-statement",
            params={"symbol": symbol, "period": period, "limit": limit},
        )

    async def income_statement_ttm(
        self, *, symbol: str | None = None
    ) -> list[IncomeStatement]:
        """Get trailing twelve months income statement."""
        return await self._request(  # type: ignore[attr-defined]
            "income-statement-ttm",
            params={"symbol": symbol},
        )

    async def balance_sheet_statement_ttm(
        self, *, symbol: str | None = None
    ) -> list[BalanceSheetStatement]:
        """Get trailing twelve months balance sheet."""
        return await self._request(  # type: ignore[attr-defined]
            "balance-sheet-statement-ttm",
            params={"symbol": symbol},
        )

    async def cash_flow_statement_ttm(
        self, *, symbol: str | None = None
    ) -> list[CashFlowStatement]:
        """Get trailing twelve months cash flow statement."""
        return await self._request(  # type: ignore[attr-defined]
            "cash-flow-statement-ttm",
            params={"symbol": symbol},
        )

    async def latest_financial_statements(
        self,
        *,
        symbol: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> list[LatestFinancialStatement]:
        """Get latest financial statements across all companies."""
        return await self._request(  # type: ignore[attr-defined]
            "latest-financial-statements",
            params={"symbol": symbol, "page": page, "limit": limit},
        )

    async def income_statement_growth(
        self,
        *,
        symbol: str | None = None,
        period: Period | None = None,
        limit: int | None = None,
    ) -> list[IncomeStatementGrowth]:
        """Get income statement growth metrics."""
        return await self._request(  # type: ignore[attr-defined]
            "income-statement-growth",
            params={"symbol": symbol, "period": period, "limit": limit},
        )

    async def balance_sheet_statement_growth(
        self,
        *,
        symbol: str | None = None,
        period: Period | None = None,
        limit: int | None = None,
    ) -> list[BalanceSheetStatementGrowth]:
        """Get balance sheet growth metrics."""
        return await self._request(  # type: ignore[attr-defined]
            "balance-sheet-statement-growth",
            params={"symbol": symbol, "period": period, "limit": limit},
        )

    async def cash_flow_statement_growth(
        self,
        *,
        symbol: str | None = None,
        period: Period | None = None,
        limit: int | None = None,
    ) -> list[CashFlowStatementGrowth]:
        """Get cash flow statement growth metrics."""
        return await self._request(  # type: ignore[attr-defined]
            "cash-flow-statement-growth",
            params={"symbol": symbol, "period": period, "limit": limit},
        )

    async def financial_growth(
        self,
        *,
        symbol: str | None = None,
        period: Period | None = None,
        limit: int | None = None,
    ) -> list[FinancialGrowth]:
        """Get overall financial growth metrics."""
        return await self._request(  # type: ignore[attr-defined]
            "financial-growth",
            params={"symbol": symbol, "period": period, "limit": limit},
        )

    async def income_statement_as_reported(
        self,
        *,
        symbol: str | None = None,
    ) -> list[IncomeStatement]:
        """Get income statement as reported."""
        return await self._request(  # type: ignore[attr-defined]
            "income-statement-as-reported",
            params={"symbol": symbol},
        )

    async def balance_sheet_statement_as_reported(
        self,
        *,
        symbol: str | None = None,
    ) -> list[BalanceSheetStatement]:
        """Get balance sheet as reported."""
        return await self._request(  # type: ignore[attr-defined]
            "balance-sheet-statement-as-reported",
            params={"symbol": symbol},
        )

    async def cash_flow_statement_as_reported(
        self,
        *,
        symbol: str | None = None,
    ) -> list[CashFlowStatement]:
        """Get cash flow statement as reported."""
        return await self._request(  # type: ignore[attr-defined]
            "cash-flow-statement-as-reported",
            params={"symbol": symbol},
        )

    async def financial_statement_full_as_reported(
        self,
        *,
        symbol: str | None = None,
    ) -> list[JSONObject]:
        """Get full financial statement as reported."""
        return await self._request(  # type: ignore[attr-defined]
            "financial-statement-full-as-reported",
            params={"symbol": symbol},
        )

    async def financial_reports_dates(
        self, *, symbol: str | None = None
    ) -> list[FinancialReportDate]:
        """Get available financial report dates."""
        return await self._request(  # type: ignore[attr-defined]
            "financial-reports-dates",
            params={"symbol": symbol},
        )

    async def financial_reports_json(
        self,
        *,
        symbol: str | None = None,
    ) -> JSONObject:
        """Get financial reports in JSON format."""
        return await self._request(  # type: ignore[attr-defined]
            "financial-reports-json",
            params={"symbol": symbol},
        )

    async def revenue_product_segmentation(
        self,
        *,
        symbol: str | None = None,
    ) -> list[RevenueSegmentation]:
        """Get revenue product segmentation."""
        return await self._request(  # type: ignore[attr-defined]
            "revenue-product-segmentation",
            params={"symbol": symbol},
        )

    async def revenue_geographic_segmentation(
        self,
        *,
        symbol: str | None = None,
    ) -> list[RevenueSegmentation]:
        """Get revenue geographic segmentation."""
        return await self._request(  # type: ignore[attr-defined]
            "revenue-geographic-segmentation",
            params={"symbol": symbol},
        )

    async def income_statement_bulk(
        self,
        *,
        year: int | None = None,
        period: Period | None = None,
    ) -> list[IncomeStatement]:
        """Get bulk income statements."""
        return await self._request(  # type: ignore[attr-defined]
            "income-statement-bulk",
            params={"year": year, "period": period},
        )

    async def balance_sheet_statement_bulk(
        self,
        *,
        year: int | None = None,
        period: Period | None = None,
    ) -> list[BalanceSheetStatement]:
        """Get bulk balance sheet statements."""
        return await self._request(  # type: ignore[attr-defined]
            "balance-sheet-statement-bulk",
            params={"year": year, "period": period},
        )

    async def cash_flow_statement_bulk(
        self,
        *,
        year: int | None = None,
        period: Period | None = None,
    ) -> list[CashFlowStatement]:
        """Get bulk cash flow statements."""
        return await self._request(  # type: ignore[attr-defined]
            "cash-flow-statement-bulk",
            params={"year": year, "period": period},
        )

    async def financial_reports_xlsx(
        self,
        *,
        symbol: str | None = None,
    ) -> Any:
        """Get financial reports in XLSX format."""
        return await self._request(  # type: ignore[attr-defined]
            "financial-reports-xlsx",
            params={"symbol": symbol},
        )

    async def income_statement_growth_bulk(
        self,
        *,
        year: int | None = None,
        period: Period | None = None,
    ) -> list[IncomeStatementGrowth]:
        """Get bulk income statement growth data."""
        return await self._request(  # type: ignore[attr-defined]
            "income-statement-growth-bulk",
            params={"year": year, "period": period},
        )

    async def balance_sheet_statement_growth_bulk(
        self,
        *,
        year: int | None = None,
        period: Period | None = None,
    ) -> list[BalanceSheetStatementGrowth]:
        """Get bulk balance sheet statement growth data."""
        return await self._request(  # type: ignore[attr-defined]
            "balance-sheet-statement-growth-bulk",
            params={"year": year, "period": period},
        )

    async def cash_flow_statement_growth_bulk(
        self,
        *,
        year: int | None = None,
        period: Period | None = None,
    ) -> list[CashFlowStatementGrowth]:
        """Get bulk cash flow statement growth data."""
        return await self._request(  # type: ignore[attr-defined]
            "cash-flow-statement-growth-bulk",
            params={"year": year, "period": period},
        )
