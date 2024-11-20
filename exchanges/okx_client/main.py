from okx import AccountClient, FundingClient, PublicDataClient, TradingClient

from core.settings import config


class OKXClient:

    "Pair example: BTC-USDT"

    def __init__(self, key: str, secret: str, password: str) -> None:
        self._key = key
        self._secret = secret
        self._password = password

    @property
    def public(self):
        return PublicDataClient(self._key, self._secret, self._password)

    @property
    def account(self):
        return AccountClient(self._key, self._secret, self._password)

    @property
    def funding(self):
        return FundingClient(self._key, self._secret, self._password)

    @property
    def traiding(self):
        return TradingClient(self._key, self._secret, self._password)


okx_client = OKXClient(config.OKX_KEY, config.OKX_SECRET, config.OKX_PASS)
