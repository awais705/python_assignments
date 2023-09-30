import pandas as pd
df = pd.read_csv("./data/assignment_3_data.csv")
# print(df.head())

# findout how many schools we have in the file
# new_df = df.groupby(["school_code"]).count()["class"]
# print(new_df)

# find out the number of class we have in each school
# new_df = df.groupby(["school_code", "class"]).count()["S.no"]
# print(new_df)


# find out the avg, min and max age of students of each school.
# new_df = df.groupby(['school_code']).agg({"age": ['min', 'max', 'mean']})
# print(new_df)
