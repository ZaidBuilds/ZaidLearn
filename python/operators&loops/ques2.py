# 30 days of prices
prices = [120, 125, 118, 130, 128, 135, 140, 138, 142, 145,
          150, 148, 149, 151, 155, 160, 158, 162, 165, 170,
          168, 172, 175, 174, 178, 180, 185, 188, 190, 195]

# step 1 calculate a 30-day moving average 

moving_average = sum(prices) / len(prices)

current_price = prices[15]

if current_price > moving_average:
    print("buy signal")
else:
    print("sell signal")