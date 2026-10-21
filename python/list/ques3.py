stocks = ["AAPL","GOOG","NFLX","MSFT"]

stocks[stocks.index("GOOG")] = "GOOGL"
stocks.remove("NFLX")

print(stocks)

