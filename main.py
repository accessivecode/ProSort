import pandas as pd
from pathlib import Path

df = pd.read_csv("resources/UserRecords.txt")

df_fname_sorted = df.sort_values(by="first_name", ascending=False)

df_email_sorted = df.sort_values(by='email', key=lambda s: s.str.split('@').str[::-1])

filepath1 = Path('result/data_fname_ascending.csv')
filepath1.parent.mkdir(parents=True, exist_ok=True)
df_fname_sorted.to_csv(filepath1)

filepath2 = Path('result/data_emaildomain.csv')
filepath2.parent.mkdir(parents=True, exist_ok=True)
df_email_sorted.to_csv(filepath2)