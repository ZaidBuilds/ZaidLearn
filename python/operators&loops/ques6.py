bid_prices = range(90,101)
ask_prices = range(101,111)
volumes = [10,50,100]

print("-------BUY ORDERS-----")
for bid in bid_prices:
    for vol in volumes:
     print(f"placing BUY order at price {bid} for volume {vol}")

print("\n-------SELL ORDERS-------")
for ask in ask_prices:
    for vol in volumes:
        print(f"placing sell order at price {ask} for volume {vol}")