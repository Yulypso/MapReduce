#!/.venv/bin/python3

import sys, numpy as np, pandas as pd

df = pd.read_csv('sales.csv', skiprows=9)
df = df.drop(['Region', 'Item Type', 'Sales Channel', 'Order Priority',
       'Order Date', 'Order ID', 'Ship Date', 'Units Sold', 'Unit Price',
       'Unit Cost', 'Total Revenue', 'Total Cost'], axis=1)
       
for i in range(int(df.shape[0])):
    print(df.iloc[i,0], '\t', df.iloc[i,1].replace('\\',''))


    