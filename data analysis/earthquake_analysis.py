import csv
import pandas as pd

df = pd.read_csv('data/earthquake.csv', index_col='earthquake_id')
pd.set_option('display.max_columns', 10)

print(df.head())
