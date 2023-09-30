import pandas as pd
import re
df = pd.read_csv("./data/exercise_2_data.csv")
# print(df.head())

# Write a Pandas program to remove the duplicates from 'WHO region' column of World alcohol consumption dataset.
# df.drop_duplicates(subset=["WHO region"], inplace=True)
# print(df)


# Write a Pandas program to find out the alcohol consumption details in the year '1987' or '1989'
# from the world alcohol consumption dataset.
# new_df = df.loc[(df["Beverage Types"] != "Other") &
#                 (df["Year"].isin([1987, 1989]))]
# print(new_df)


# Write a Pandas program to find out the alcohol consumption details by
# the 'Americas' in the year '1985' from the world alcohol consumption dataset.
# new_df = df.loc[(df["WHO region"] == "Americas") & (df["Year"] == 1985)]
# print(new_df)


# Write a Pandas program to find out the alcohol consumption details in the
#  year '1986' where WHO region is 'Western Pacific' and country is 'VietNam' from the world
#  alcohol consumption dataset.
# new_df = df.loc[((df["WHO region"] == "Western Pacific") & (
#     df["Year"] == 1986) & (df["Country"] == "Viet Nam"))]
# print(new_df)


# Write a Pandas program to find out the alcohol consumption details in the year
# '1986' or '1989' where WHO region is 'Americas' from the world alcohol consumption dataset.
# new_df = df.loc[((df["WHO region"] == "Americas") & (
#     df["Year"].isin([1986, 1989])))]
# print(new_df)


# Write a Pandas program to find out the alcohol consumption details in the
# year '1986' or '1989' where WHO region is 'Americas' or 'Europe' from the world alcohol consumption dataset.
# new_df = df.loc[((df["WHO region"].isin(["Americas", "Europe"])) & (
#     df["Year"].isin([1986, 1989])))]
# print(new_df)


# Write a Pandas program to filter those records where WHO region
# contains "Ea" substring from world alcohol consumption dataset.
# new_df = df.loc[df["WHO region"].str.contains("Ea")]
# print(new_df)


# Write a Pandas program to filter those records where WHO region
#  matches with multiple values (Africa, Eastern Mediterranean, Europe) from world alcohol consumption dataset.
# new_df = df.loc[df["WHO region"].isin(
#     ["Africa", "Europe", "Eastern Mediterranean"])]
# print(new_df)


# Write a Pandas program to filter those records which not appears
# in a given list from world alcohol consumption dataset.
