current = int(input("current quantity: "))
buy = int(input("how many to buy: "))
sell = int(input("how many to sell: "))

new_total = current + buy - sell
print("new total",new_total)