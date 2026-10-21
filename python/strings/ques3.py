data = "AAPL","GOOG","MSFT","TSLA"

symbols = data.split(",")

for symbol in symbols:
    reversed_symbol = ""
    for ch in symbol:
        reversed_symbol = ch + reversed_symbol
        print(symbol,reversed_symbol)