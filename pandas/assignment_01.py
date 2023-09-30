import pandas as pd
df = pd.read_csv("./data/assignment_data.csv")
# print(df.head())


# Write a Pandas program to get the first 3 rows of a given DataFrame.
# new_data = df.head(3)
# print(new_data)

# Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
# new_data = df[["name", "score"]]
# print(new_data)

# Write a Pandas program to select the specified columns and rows from a given data frame using loc and iloc.
# new_data = df.loc[:, ["name", "score"]]
# print(new_data)

# new_data = df.iloc[[1, 3, 5, 7]]
# print(new_data)


# Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
# new_data = df.loc[(df["attempts"] > 2)]
# print(new_data)


# Write a Pandas program to count the number of rows and columns of a DataFrame.
# print(df.shape)


# Write a Pandas program to select the rows where the score is missing
# new_data = df[df["score"].isnull()]
# print(new_data)


# Write a Pandas program to select the rows the score is between 15 and 20
# new_data = df.loc[((df["score"] >= 15) & (df["score"] <= 20))]
# print(new_data)


# Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and
#  score greater than 15.
# new_data = df.loc[((df["score"] > 15) & (df["attempts"] < 2))]
# print(new_data)


# Write a Pandas program to change the score in row 'd' to 11.5.
# df.loc[4, "score"] = 11.5
# print(df)


# Write a Pandas program to calculate the sum of the examination attempts by the students.
# new_data = df["attempts"].sum()
# print(new_data)


# Write a Pandas program to calculate the mean of all students' scores
# new_data = df["score"].mean()
# print(new_data)


# Write a Pandas program to append a new row to data frame with given values for each column.
#  Now delete the new row
# new_row = {"name": "Awais", "score": 6, "attempts": 2, "qualify": "no"}
# df.loc[len(df)] = new_row
# print(df)

# df.drop((len(df)-1), axis=0, inplace=True)
# print(df)

# Write a Pandas program to sort the DataFrame first by 'name' in descending order,
# then by 'score' in ascending order.

# df.sort_values(by=["name", "score"], ascending=[False, True], inplace=True)
# print(df)


# Write a Pandas program to replace the 'qualify' column contains the values 'yes'
# and 'no' with True and False.

# filtr = (df["qualify"] == "yes")
# df.loc[filtr, "qualify"] = True

# filtr = (df["qualify"] == "no")
# df.loc[filtr, "qualify"] = False
# print(df)


# Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame.
# filtr3 = (df["name"] == "James")
# df.loc[filtr3, "name"] = "Suresh"

# print(df)

# Write a Pandas program to delete the 'attempts' column from the DataFrame.
# df.drop("attempts", axis=1, inplace=True)
# print(df)

# Write a Pandas program to insert a new column in existing DataFrame.
# total_col = len(df.columns)
# df.insert(total_col, "Custom", "")
# print(df)


# Write a Pandas program to iterate over rows in a DataFrame.


# Display all columns
# print(list(df.columns))

# Rename Column
# df.rename(columns={"qualify": "Qualify"}, inplace=True)
# print(list(df.columns))


# Write a Pandas program to replace all the NaN values with Zero's in a column of a dataframe.
# filtr5 = (df["score"].isnull())
# df.loc[filtr5, "score"] = 0

# print(df["score"])


# Drop multiple columns
# df.drop(columns=["name", "score"], inplace=True)
# print(df)


# Drop rows and then reset the index
# df.drop(labels=[1, 3, 5], inplace=True)
# print(df.reset_index())


# Remove duplicates
# df.drop_duplicates(subset=["qualify"], inplace=True)
# print(df)
