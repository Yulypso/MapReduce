#!/.venv/bin/python3

import sys, numpy as np, pandas as pd

country_dict = dict()

for line in sys.stdin:
    line = line.strip()

    country, profit = line.split('\t', 1)

    if country not in country_dict:
        try:
            country_dict[str(country)] = float(profit)
        except ValueError:
            continue
    else:
        try:
            country_dict[str(country)] += float(profit)
        except ValueError:
            continue

for country in country_dict.keys():
    print(country, '\t', country_dict[country])


