def print_trade_summary(symbol, quantity, price):
    total_cost = quantity * price
    print(f"Trade Summary: {quantity} shares of {symbol} at ${price} each.")
    print(f"Total Cost: ${total_cost}")

# Example
print_trade_summary("AAPL", 10, 189.45)
