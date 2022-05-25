#!/usr/bin/env python3
from itertools import count
import time, datetime, sys
import pandas as pd
import os
import numpy as np

dir_path = os.path.realpath(__file__)

# Extracted from: https://www.nature.com/articles/s41599-020-0523-3#Sec7 [Supplementary information]
dj30_df = pd.read_csv(os.path.dirname(dir_path) + '/data/dj30.csv')
dj30_df.dropna(inplace=True)
dj30_df = dj30_df.loc[:,['Long Date','Close']]

counter = 0
dj30sum = 0
price_data = np.array([])
output = []
for i, row in dj30_df.iterrows():
    data = float(row['Close'])
    price_data = np.append(price_data, data)
    dj30sum += float(data)
    counter += 1
    date = row['Long Date']
    # print(i, dj30sum, flush = True)
    
    if len(price_data) >= 10:
        temp = np.convolve(price_data, np.ones(10), 'valid')/10
        print('10daysMA: ', temp[-1])
    
    if len(price_data) >= 40:
        temp = np.convolve(price_data, np.ones(40), 'valid')/40
        print('40daysMA: ', temp[-1])

    if len(price_data) > 40:
        ten_MA =  np.convolve(price_data, np.ones(10), 'valid')/10
        fourty_MA = np.convolve(price_data, np.ones(40), 'valid')/40
        if (ten_MA[-2] > fourty_MA[-2]) != (ten_MA[-1] > fourty_MA[-1]):
            if ten_MA[-1] > fourty_MA[-1]:
                
                output.append((date, 'buy'))
            else:
                output.append((date, 'sell'))

    time.sleep(1.0)
print(output)

