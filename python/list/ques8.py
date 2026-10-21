prices = [180, 220, 150, 300]

for i, price in enumerate(prices):
    if price < 200:
        prices[i] = price * 1.05
        print("Modified index:", i)

print(prices)
