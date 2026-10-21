prices = [120,100,140,200,80,300,450]

max_profit = 0
best_buy_day = 0
best_sell_day = 0

for buy in range(len(prices)):

    for sell in range(buy + 1, len(prices)):

        profit = prices[sell] - prices[buy]

        if profit > max_profit :
            max_profit = profit
            best_buy_day = buy
            best_sell_day = sell

# Print results
print("Best Buy Day:", best_buy_day, "Price:", prices[best_buy_day])
print("Best Sell Day:", best_sell_day, "Price:", prices[best_sell_day])
print("Maximum Profit:", max_profit)