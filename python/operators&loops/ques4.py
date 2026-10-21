import time
import random

current_price = 200
threshold_price = 150

while current_price > threshold_price:
    print("checking price... current price:",current_price)

    current_price -=random.randint(1,10)

    time.sleep(10)

    print("threshold exceeded! current price:",current_price)