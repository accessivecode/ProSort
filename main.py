
'''
This project is to read csv file,
sort by first name
and sort by email domain name.

pandas library is used to achieve these requirements.
'''


import pandas as pd
from pathlib import Path


#method to sort data by first name in descending order.
def sort_fname(df):
    df_fname_sorted = df.sort_values(by="first_name", ascending=False)
    return df_fname_sorted


#method to sort data by email-domain name
def sort_email(df):
    df_email_sorted = df.sort_values(by='email', key=lambda s: s.str.split('@').str[::-1])
    return df_email_sorted


def main():

    #loading the csv data in dataframe
    df = pd.read_csv("resources/UserRecords.txt")


    df_sort1 = sort_fname(df)      #sorting data by firstname in descending order

    # storing data in to csv file
    filepath1 = Path('result/data_fname_ascending.csv')
    filepath1.parent.mkdir(parents=True, exist_ok=True)  # making directory with given file name.
    df_sort1.to_csv(filepath1)  # creating data frames to csv file with given path.


    df_sort2 = sort_email(df)      #sorting data by email-domain name

    #storing data in to csv file
    filepath2 = Path('result/data_emaildomain.csv')
    filepath2.parent.mkdir(parents=True, exist_ok=True)   # making directory with given name.
    df_sort2.to_csv(filepath2) # creating data frames to csv file with given path.



if __name__=="__main__":
    main()