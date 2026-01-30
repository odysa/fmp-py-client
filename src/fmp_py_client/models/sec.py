"""SEC filing response types."""

from typing import NotRequired, TypedDict


class SECFiling(TypedDict):
    """SEC filing data."""

    symbol: str
    cik: str
    type: str
    link: str
    finalLink: NotRequired[str]
    acceptedDate: str
    filingDate: str


class SECCompanyProfile(TypedDict):
    """SEC company profile."""

    symbol: str
    cik: str
    companyName: str
    formType: NotRequired[str]
    sicCode: NotRequired[str]
    sicDescription: NotRequired[str]
    sicGroup: NotRequired[str]
    businessAddress: NotRequired[str]
    mailingAddress: NotRequired[str]
    phoneNumber: NotRequired[str]
    stateLocation: NotRequired[str]
    stateOfIncorporation: NotRequired[str]
    fiscalYearEnd: NotRequired[str]


class SICCode(TypedDict):
    """Standard Industrial Classification code."""

    sicCode: str
    industry: str
    title: str


class IndustryClassification(TypedDict):
    """Industry classification."""

    symbol: str
    name: str
    sicCode: str
    industryTitle: str
    businessAddress: NotRequired[str]
    phoneNumber: NotRequired[str]
