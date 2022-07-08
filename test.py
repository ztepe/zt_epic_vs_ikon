
from nbformat import read

import datetime as dt
import pandas as pd
import matplotlib as mpl

df = pd.read_csv('archive/annualsnow.csv')

resort = df[(df["Resort"] == 'Alta')]

print(resort)

# import csv
# with open('archive/annualsnow.csv', 'r') as annualsnow:
#     reader = csv.reader(annualsnow)
#     # for row in reader:
#         # print(annualsnow_data()) # prints annual snow to confirm data is read correctly

# location = pd.read_csv("Location"[annualsnow])
# for col in reader:
#     print(annualsnow)

# import csv
# with open('archive/skiresorts.csv', 'r') as resorts:
#     reader = csv.reader(resorts)
#     # for row in reader:
#     #     print(row)

# import csv
# with open('archive/currentseason.csv', 'r') as archive:
#     reader = csv.reader(archive)
#    # for row in reader:
#       #  print(row)

# avgbase = "Average Base Depth"(annualsnow)
#     for col in reader
#         print(avgbase)