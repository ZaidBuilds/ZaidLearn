print("Moving Average Crossover Strategy")
print("This strategy buys when short MA crosses above long MA and sells when short MA crosses below.")

data = [
("2021-01-01", 100),
("2021-01-02", 102),
("2021-01-03", 104),
("2021-01-04", 101),
("2021-01-05", 105),
("2021-01-06", 107),
("2021-01-07", 110),
("2021-01-08", 108),
("2021-01-09", 106),
("2021-01-10", 104),
("2021-01-11", 103),
("2021-01-12", 102),
("2021-01-13", 101),
("2021-01-14", 105),
("2021-01-15", 108),
("2021-01-16", 110),
("2021-01-17", 112),
("2021-01-18", 115),
("2021-01-19", 117),
("2021-01-20", 120),
]

prices = [price for date, price in data]
dates = [date for date, price in data]

print("Data loaded. Total days:", len(data))

# Step 3: Calculate Moving Averages

short_window = 5
long_window = 10

short_ma = []
long_ma = []

# Calculate 5-day MA
for i in range(len(prices)):
    if i < short_window - 1:
        short_ma.append(None)
    else:
        window_prices = prices[i - short_window + 1 : i + 1]
        avg = sum(window_prices) / short_window
        short_ma.append(avg)

# Calculate 10-day MA
for i in range(len(prices)):
    if i < long_window - 1:
        long_ma.append(None)
    else:
        window_prices = prices[i - long_window + 1 : i + 1]
        avg = sum(window_prices) / long_window
        long_ma.append(avg)

print("Short MA:", short_ma)
print("Long MA:", long_ma)
