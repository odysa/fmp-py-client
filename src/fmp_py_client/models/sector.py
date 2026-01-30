"""Sector and industry performance response types."""

from typing import NotRequired, TypedDict


class SectorPerformance(TypedDict):
    """Sector performance data."""

    sector: str
    changesPercentage: float
    date: NotRequired[str]


class IndustryPerformance(TypedDict):
    """Industry performance data."""

    industry: str
    changesPercentage: float
    date: NotRequired[str]


class SectorPE(TypedDict):
    """Sector P/E ratio data."""

    date: str
    sector: str
    pe: float


class IndustryPE(TypedDict):
    """Industry P/E ratio data."""

    date: str
    industry: str
    pe: float
