stocks = [
    {"name": "AAPL", "open": 150, "close": 155},
    {"name": "TSLA", "open": 200, "close": 195},
    {"name": "MSFT", "open": 300, "close": 310},
]
for stock in stocks:
    open_price = stock["open"]
    close_price = stock["close"]
    name = stock["name"]

    gain_loss = close_price - open_price

    print(f"{name}: gain/loss = {gain_loss}")
    