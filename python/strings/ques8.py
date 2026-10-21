data = "High: 100, Low: 90, Open: 95, Close: 98"

parts = data.split(",")

for part in parts:
    label, value = part.split(",")
    value = int(value.strip())

    if value > 95:
        print(value)