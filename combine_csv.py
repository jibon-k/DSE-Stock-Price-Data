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

# combine all the dataframes
combined_df1 = pd.concat([dic[i] for i in range(0, 11)])
combined_df2 = pd.concat([dic[i] for i in range(11, 22)])

# export the combined dataframe as csv
combined_df1.to_csv('1999-2009.csv', index=False)
combined_df2.to_csv('2010-2020.csv', index=False)
