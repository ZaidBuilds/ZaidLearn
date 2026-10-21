stock_data = [
    {"day": 1, "price": 100},
    {"day": 2, "price": 102},
    {"day": 3, "price": 105},
    {"day": 4, "price": 107},
    {"day": 5, "price": 110},
    {"day": 6, "price": 108},
    {"day": 7, "price": 115},
    {"day": 8, "price": 118},
    {"day": 9, "price": 120},
    {"day": 10, "price": 122},
]

window = 3  # number of days used for momentum calculation

cash = 1000   # starting capital
shares = 0    # number of shares owned

def get_avg_price(data, index, window):
    if index < window:
        return None
    last_prices = [data[i]["price"] for i in range(index - window, index)]
    return sum(last_prices) / window

# -----------------------------
# Trading Simulation
# -----------------------------
for i in range(len(stock_data)):
    current_day = stock_data[i]["day"]
    current_price = stock_data[i]["price"]

    avg_price = get_avg_price(stock_data, i, window)

    # Skip first days (not enough data)
    if avg_price is None:
        print(f"Day {current_day}: Not enough data for momentum")
        continue

    momentum = current_price - avg_price

    print(f"Day {current_day}: Price={current_price}, Avg={avg_price:.2f}, Momentum={momentum:.2f}")

    # Trading Rules
    if momentum > 3:
        # Strong momentum → Buy
        if cash >= current_price:
            shares_to_buy = cash // current_price
            shares += shares_to_buy
            cash -= shares_to_buy * current_price
            print(f"  BUY {shares_to_buy} shares at {current_price}")
    elif momentum < -3:
        # Negative momentum → Sell
        if shares > 0:
            cash += shares * current_price
            print(f"  SELL {shares} shares at {current_price}")
            shares = 0
    else:
        print("  HOLD")

# Final Portfolio Value
final_value = cash + shares * stock_data[-1]["price"]
print("\n----- FINAL PORTFOLIO VALUE -----")
print("Cash:", cash)
print("Shares:", shares)
print("Portfolio Value:", final_value)
