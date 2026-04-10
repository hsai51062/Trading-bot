from binance.client import Client

API_KEY = "xMG4gNpNLtcs1Cf9qgzMwbIVEEbWfSksF3iXFM8mQBo4gZppRbbb9spVGfZriJnG"
API_SECRET = "I67g7xFBVMCciPeggV2BV4JG6LiMl8EuLY67oErhFtwTKaSPLnLsUSbKEYG5Vzah"

client = Client(API_KEY, API_SECRET)

client.FUTURES_URL = "https://demo-fapi.binance.com/fapi"

try:
    order = client.futures_create_order(
        symbol="BTCUSDT",
        side="BUY",
        type="MARKET",
        quantity=0.002
    )

    print("Order placed successfully:")
    print(order)

except Exception as e:
    print("Error placing order:")
    print(e)