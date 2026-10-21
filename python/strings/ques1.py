data = "AAPL100GOOG200MSFT300"

symbol = ""
number = ""

for ch in data:
    if ch.isalpha():  # Letter
        # If both symbol and number have values → previous item is complete
        if symbol and number:
            print(symbol, number)
            symbol = ""
            number = ""
        symbol += ch
    else:             # Digit
        number += ch

# Print last stock pair
print(symbol, number)
