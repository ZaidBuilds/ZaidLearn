data = "Buy100AAPLSell200GOOG"

word = ""
result = []

# Step 1: Break string into words: Buy, 100, AAPL, Sell, 200, GOOG
for ch in data:
    if ch.isalpha() and word != "" and word[-1].isdigit():
        result.append(word)
        word = ""

    if ch.isdigit() and word != "" and word[-1].isalpha():
        result.append(word)
        word = ""

    word += ch

# Add last word
result.append(word)

# Step 2: Now result = ["Buy", "100", "AAPL", "Sell", "200", "GOOG"]
# Group every 3 items and print
for i in range(0, len(result), 3):
    print(result[i], result[i+1], result[i+2])
