# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 16:38:16 2020

@author: Karan Babariya
"""
import os
import pandas as pd
import datetime
from datetime import time

base_time = time(13, 0 ,0)
blob = pd.read_csv('E:/TD -Rise of Data/TD_Hackathon/src/blob.csv', nrows=100)
blob['date'] = pd.to_datetime(blob['date'])
exls = pd.read_csv('E:/TD -Rise of Data/TD_Hackathon/src/price_returns_df.csv', nrows=100)
exls['Date'] = pd.to_datetime(exls['Date'])
exls.rename(columns={'Date': 'date', 'Ticker': 'ticker'}, inplace=True)
exls['dates_only'] = [d.date() for d in exls['date']]
x = []
for d in blob['date']:
    if (d.time() > base_time):
        exls_date = (d + datetime.timedelta(days=1)).date()
        x.append(exls.loc[exls['dates_only'] == exls_date]['Returns'].values[0])
    else:
        x.append(exls.loc[exls['dates_only'] == d.date()]['Returns'].values[0])
        
                 


print('Stop here!')
exls['date']
