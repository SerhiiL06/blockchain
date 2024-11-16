from exchanges.okx_client.main import okx_client
from exchanges.common.enums import Sides, OrderTypes


def main():
    response = okx_client.traiding.place_order(
        "BTC-USDT", "cash", Sides.SELL.value, OrderTypes.MARKET.value, "1"
    )

    print(response["data"][0].get("sMsg"))


if __name__ == "__main__":
    main()
