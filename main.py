from exchanges.common.enums import OrderTypes, Sides
from exchanges.okx_client.main import okx_client


def main():
    amount = "1"
    response = okx_client.traiding.place_order(
        "MEMEFI-USDT", "cash", Sides.SELL.value, OrderTypes.MARKET.value, amount
    )

    print(response["data"][0].get("sMsg"))


if __name__ == "__main__":
    main()
