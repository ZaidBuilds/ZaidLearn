raw_data = [" 3,000 ", " $5,500", "  10,200$ ", "2,50,000", "$ 1,00,000 "]


cleaned_data = []

for item in raw_data:
    value = item.strip()
    value = value.replace("$", "")
    value = value.replace(",", "")
    number = int(value)
    cleaned_data.append(number)

    print(cleaned_data)
