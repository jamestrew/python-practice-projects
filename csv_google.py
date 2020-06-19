# intro to csv
# analsysi of Google stocks

import csv

path = "google_stock_data.csv"
dataset = [line.strip().split(",")for line in open(path)]

print(dataset[0])
print(dataset[1])


