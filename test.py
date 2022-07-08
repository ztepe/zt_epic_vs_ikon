
from nbformat import read

import datetime as dt
import pandas as pd
import matplotlib as mpl


import csv
with open('archive/annualsnow.csv', 'r') as annualsnow:
    reader = csv.reader(annualsnow)
    # for row in reader:
        # print(annualsnow_data()) # prints annual snow to confirm data is read correctly


import csv
with open('archive/skiresorts.csv', 'r') as resorts:
    reader = csv.reader(resorts)
    # for row in reader:
    #     print(row)

import csv
with open('archive/currentseason.csv', 'r') as archive:
    reader = csv.reader(archive)
   # for row in reader:
      #  print(row)

