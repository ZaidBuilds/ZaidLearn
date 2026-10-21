data = "20210101\n200\n20210102\n250\n20210103\n300"

lines = data.split("\n")

for i in range(0, len(lines),2):
    data = lines[i]
    prices = lines[i + 1]
    print(data, prices)
    