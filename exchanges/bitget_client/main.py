from typing import Protocol, TypeVar

from pybitget import Client
from pybitget.enums import ORDER_SIDES

from core.settings import config

client = Client(config.BITGET_KEY, config.BITGET_SECRET, config.BITGET_PASS)


class UseInt(Protocol):

    def __int__(self) -> int: ...


T = TypeVar("T", bound=UseInt)


def place_order(coin: str, q: T, side: str = "sell") -> dict:

    result = client.spot_place_order(coin, q, side, "market", "normal")

    return result
