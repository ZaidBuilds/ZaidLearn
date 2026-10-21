symbol = ["AAPL","GOOG","MSFT"]
prices = [150, 1200, 200]

stock_dict = dict(zip(symbol, prices))

for stock, price in stock_dict.item():
    print(stock, price)
