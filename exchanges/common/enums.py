from enum import Enum, auto


class Sides(Enum):
    SELL = "sell"
    BUY = "buy"


class OrderTypes(Enum):
    MARKET = "market"
    LIMIT = "limit"
