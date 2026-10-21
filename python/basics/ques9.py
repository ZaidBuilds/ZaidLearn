# break even price is that when you sell something and after selling when you pay all of your profit into it get it 
qty = int(input(" enter the quantity: "))
cost = int(input("enter the cost you pay: "))
fees = int(input("enter the fees you pay for it:"))

breakeven = (cost + fees) / qty

print("breakeven price",breakeven)