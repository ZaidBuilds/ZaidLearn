import pandas as pd # import pandas 

# load the csv file
# support file name is 'stock.csv'
df = pd.read_csv("stock.csv")

# calculate daily percentage change of closing price 

df["daily_return_%"] = df["Close"].pct_change()*100

# print the dataframe with new columne
print(df)
