stocks = [('AAPL', 150), ('GOOG', 1200), ('MSFT', 200)]

# menthod 1 

for stock in stocks:
    print(stock[0],stock[1])


# Method 2

for symbol, price in stocks:
    print(symbol,price)
    