"""Market movers response types."""

from typing import NotRequired, TypedDict


class StockMover(TypedDict):
    """Stock mover (gainer, loser, most active)."""

    symbol: str
    name: str
    change: float
    price: float
    changesPercentage: float
    exchange: NotRequired[str]
