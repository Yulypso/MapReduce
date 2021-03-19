#!/.venv/bin/python3

import sys, numpy as np, pandas as pd

for line in sys.stdin:
    line = line.strip()

    country, total_profit = line.split('\t', 1)
    print(country, '\t', total_profit)
       


    