# Imports
import pandas as pd
from os import listdir  # for listing the files of a directory


# List of all the csv files
all_csv = sorted(listdir("csv"))

# List of hte headers for the columns of the dataframes
headers = ["trading_code", "date", "openning_price", "high", "low",
           "closing_price", "volume"]


def make_dataframe(file):
    # creates dataframe from csv and adds headers
    df = pd.read_csv(file, names=headers)
    return df


dic = {}    # empty dictionary for saving the dataframes

for n, csv in enumerate(all_csv):   # enumerate the list of csv
    # create dictionary of dataframes as the values and the indices as keys.
    dic[n] = make_dataframe(f'csv/{csv}')

# combine all the dataframes to one
combined_df = pd.concat([dic[i] for i in range(len(dic))])

# export the combined dataframe as csv
combined_df.to_csv('combined.csv', index=False)
