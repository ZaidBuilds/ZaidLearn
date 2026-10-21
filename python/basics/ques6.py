buy = int(input("enter the buy value :"))
sell = int(input("enter the sell value :"))

roi = ((sell - buy) / buy) * 100

#print the roi 
print("Daily ROI",roi,"%")