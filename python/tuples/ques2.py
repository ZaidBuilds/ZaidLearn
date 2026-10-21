transactions = [
    ("AAPL", "buy", 100),
    ("AAPL", "sell", 50),
    ("GOOG", "sell", 30),
    ("MSFT", "buy", 20),
    ("GOOG", "sell", 10)
]

sell_symbols = set()

for symbol, tx_type, amount in transactions:
 if tx_type == "sell":
  sell_symbols.add(symbol)


print(sell_symbols)

 