#!/.venv/bin/python3

import sys, numpy as np, pandas as pd

total_profit_mean = 0
nb_country = 0

for line in sys.stdin:
    line = line.strip()

    country, profit = line.split('\t', 1)

    try:
        total_profit_mean += float(profit)
        nb_country += 1
    except ValueError:
        continue

total_profit_mean = total_profit_mean/nb_country

print('Total profit mean:', '\t', total_profit_mean)


