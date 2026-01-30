"""Government trading response types."""

from typing import NotRequired, TypedDict


class GovernmentTrade(TypedDict):
    """Government (Senate/House) trade data."""

    symbol: NotRequired[str]
    disclosureDate: str
    transactionDate: str
    firstName: str
    lastName: str
    office: NotRequired[str]
    district: NotRequired[str]
    owner: NotRequired[str]
    assetDescription: str
    assetType: NotRequired[str]
    type: str
    amount: str
    comment: NotRequired[str]
    link: NotRequired[str]
    capitalGainsOver200USD: NotRequired[str]
