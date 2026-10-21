text = "Buy 50 AAPL and sell 30 GOOG"

words = text.split()

for i in range(len(words)):
    if words[i].lower() == "buy" or words[i].lower() =="sell":
        action = words[i].capitalize()
        quantity = words[i+1]
        symbol = words[i+2].upper()

        print(action,quantity,symbol)
        
