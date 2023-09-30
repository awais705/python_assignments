import pandas as pd
df = pd.read_csv("./data/assignment_4_data.csv")
# print(df.head())
df['Date'] = pd.to_datetime(df['Date'])

# How much sale produced by each salesman
# new_df = df.groupby(["Revenue", "SalesRep"]).sum()["Units"]
# print(new_df)


# which salesman produced the best sale
new_df = df.groupby(["Revenue"]).sum()["SalesRep"]
print(new_df.iloc[1])
