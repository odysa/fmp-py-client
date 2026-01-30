"""Crowdfunding and fundraising response types."""

from typing import NotRequired, TypedDict


class CrowdfundingOffering(TypedDict):
    """Crowdfunding offering data."""

    cik: str
    companyName: str
    date: str
    filingDate: str
    acceptedDate: str
    formType: NotRequired[str]
    formSignification: NotRequired[str]
    nameOfIssuer: NotRequired[str]
    legalStatusForm: NotRequired[str]
    jurisdictionOrganization: NotRequired[str]
    issuerStreet: NotRequired[str]
    issuerCity: NotRequired[str]
    issuerStateOrCountry: NotRequired[str]
    issuerZipCode: NotRequired[str]
    issuerWebsite: NotRequired[str]
    intermediaryCompanyName: NotRequired[str]
    intermediaryCommissionCik: NotRequired[str]
    intermediaryCommissionFileNumber: NotRequired[str]
    compensationAmount: NotRequired[str]
    financialInterest: NotRequired[str]
    securityOfferedType: NotRequired[str]
    securityOfferedOtherDescription: NotRequired[str]
    numberOfSecurityOffered: NotRequired[int]
    offeringPrice: NotRequired[float]
    offeringAmount: NotRequired[int]
    overSubscriptionAccepted: NotRequired[str]
    overSubscriptionAllocationType: NotRequired[str]
    maximumOfferingAmount: NotRequired[int]
    offeringDeadlineDate: NotRequired[str]
    currentNumberOfEmployees: NotRequired[int]


class EquityOffering(TypedDict):
    """Equity offering (fundraising) data."""

    cik: str
    companyName: str
    date: str
    filingDate: str
    acceptedDate: str
    formType: NotRequired[str]
    formSignification: NotRequired[str]
    entityName: NotRequired[str]
    issuerStreet: NotRequired[str]
    issuerCity: NotRequired[str]
    issuerStateOrCountry: NotRequired[str]
    issuerStateOrCountryDescription: NotRequired[str]
    issuerZipCode: NotRequired[str]
    issuerPhoneNumber: NotRequired[str]
    jurisdictionOfIncorporation: NotRequired[str]
    entityType: NotRequired[str]
    incorporatedWithinFiveYears: NotRequired[bool]
    yearOfIncorporation: NotRequired[str]
    industryGroupType: NotRequired[str]
    revenueRange: NotRequired[str]
    federalExemptionsExclusions: NotRequired[str]
    isAmendment: NotRequired[bool]
    dateOfFirstSale: NotRequired[str]
    durationOfOfferingIsMoreThanYear: NotRequired[bool]
    isBusinessCombinationTransaction: NotRequired[bool]
    minimumInvestmentAccepted: NotRequired[int]
    totalOfferingAmount: NotRequired[int]
    totalAmountSold: NotRequired[int]
    totalAmountRemaining: NotRequired[int]
    hasNonAccreditedInvestors: NotRequired[bool]
    totalNumberAlreadyInvested: NotRequired[int]
    salesCommissions: NotRequired[int]
    findersFees: NotRequired[int]
    grossProceedsUsed: NotRequired[int]
