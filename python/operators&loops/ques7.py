prices = [
    120,122,125,128,130,132,135,137,140,142,
    145,147,149,150,152,155,157,160,162,165,
    167,170,172,175,177,178,180,182,185,187,
    188,190,192,194,195,197,198,200,202,205,
    207,209,210,212,214,215,217,220,222,225
]

ma_30 = sum(prices[-30:]) / 30
ma_50 = sum(prices) / 50

current_price = prices[10]

#print data for understanding 

print("current prices:",current_price)
print("30-day ma:",ma_30)
print("50-day ma:",ma_50)

if current_price > ma_30 and current_price > ma_50:
    print("strong buy")

elif current_price > ma_30:
    print("Hold")

else:
    print("sell")