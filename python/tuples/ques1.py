market_data = {}

data_stream = [
    ("AAPL", 180, 1000),
    ("AAPL", 182, 1200),
    ("AAPL", 181, 900),
    ("AAPL", 185, 1500),
    ("GOOG", 2700, 500),
    ("GOOG", 2720, 600)
]

for symbol, price, volume in data_stream:
    if symbol not in market_data:
        market_data[symbol] = []

    market_data[symbol].append((price, volume))

    market_data[symbol] = market_data[symbol][-3:]

print(market_data)
