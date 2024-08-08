import pandas as pd

df = pd.read_csv("stock_analysis.csv")

df2 = df.copy()
df2["unwanted"] = df["Open"] * df["Close"]
# print(df2.head())

df2.to_csv("stock_analysis2.csv", index=False)

# import re

# # Original list
# tickers = ["HSI", "GDAXI", "GSPTSE", "399001.SZ", "000001.SS", "J203.JO", "NYA"]

# # Define the regex pattern to match .SZ, .SS, and JO
# pattern = re.compile(r'\.(SZ|SS|JO)$')

# # Filter the list
# filtered_tickers = [ticker for ticker in tickers if not pattern.search(ticker)]

# print(filtered_tickers)
