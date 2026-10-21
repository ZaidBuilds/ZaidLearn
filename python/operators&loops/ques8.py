
import numpy as np

# Step 1: Create a numpy array of 20 prices
prices = np.array([
    120, 122, 125, 128, 127,
    130, 135, 137, 140, 138,
    142, 145, 148, 150, 152,
    155, 157, 160, 162, 165
])

window = 5  # rolling window size
rolling_averages = []  # to store results

# Step 2: Loop through valid window positions
for i in range(len(prices) - window + 1):
    window_values = prices[i : i + window]  # slicing
    avg = np.mean(window_values)            # numpy mean
    rolling_averages.append(avg)

# Step 3: Print results
print("Rolling 5-day averages:")
for avg in rolling_averages:
    print(avg)
