print("weekly stock analysis analyzer")

prices = []

for day in range(1,8):
    price = float(input("enter price for day {day}:"))
    prices.append(price)

    average = sum(prices)/len(prices)

    print("\n------------summery------")
    print("prices entered:",prices)
    print("weekly average prices:",average)

