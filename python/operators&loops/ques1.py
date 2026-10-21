prices = [120, 118, 115, 110, 112, 111]   # example prices

# We create a counter to track how many days in a row prices drop
drop_count = 0

# We loop from 1 to the end because we compare current day with previous day
for i in range(1, len(prices)):

    # Check if today's price is lower than yesterday's price
    if prices[i] < prices[i - 1]:
        drop_count += 1      # Add to drop streak
    else:
        drop_count = 0       # Reset if price does NOT drop

    # If drop_count reaches 3, it means 4 consecutive falling values (3 drops)
    if drop_count >= 3:
        print("Consecutive price drop detected!")
        break
else:
    print("No consecutive 3-day drop found.")
