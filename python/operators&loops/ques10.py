# Hypothetical prices for 15 days
prices = [100, 102, 103, 108, 110, 111, 120, 118, 119, 124, 130, 128, 135, 140, 150]

last_recorded_price = prices[0]  # starting price

print("Last Recorded Price:", last_recorded_price)

for day in range(1, len(prices)):
    
    current_price = prices[day]

    # Calculate percentage increase
    increase_percentage = ((current_price - last_recorded_price) / last_recorded_price) * 100

    if increase_percentage >= 5:
        print(f"Sell Order Triggered on Day {day+1}: Price = {current_price}, Gain = {increase_percentage:.2f}%")
        
        # update last recorded price after selling
        last_recorded_price = current_price

    # If no 5% gain, just update last price slowly over time
    else:
        last_recorded_price = current_price
