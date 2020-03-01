#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
import os
import numpy as np
import pandas as pd
import csv

os.chdir("C:/Users/saksh/Desktop/Rotman/TD hackathon/hackathon_data/company_prices_returns")
curr_path = os.getcwd()
files = os.listdir(curr_path)
csv_files = [f for f in files if f[-3:] == 'csv']


# In[18]:


len(csv_files)


# In[12]:


final = pd.DataFrame(columns=['Ticker', 'Date', 'Close', 'Returns'])
for items in csv_files:
    company=pd.read_csv(items)
    date=company['Date']
    close=company['Close']
    returns=company['Returns']
    ticker = items.strip('_adj_close.csv')
    price_returns_temp = pd.DataFrame(
    {'Ticker': ticker,
     'Date': date,
     'Close': close,
     'Returns': returns})
    final=pd.concat([final,price_returns_temp])


# In[17]:


final.Ticker.unique()


# In[15]:


len(final['Ticker'])


# In[14]:


final


# In[37]:


#create a list of dates where transcripts were released
import pandas as pd
import wrds
conn = wrds.Connection(wrds_username='sakshamg')

import numpy as np
from scipy import stats


# In[ ]:


'''Data Dictionary


oiadp- Operating Income After Depreciation
at-total assets
txp- Income Taxes Payable
dp- depreciation and amortization
EBIT- earnings before tax
amort-
sic-

'''


# In[39]:


funda = conn.raw_sql("""
                   select distinct tic,sich, avg(at) as Total_Assets
                from compa.funda where
                  (consol='C' and indfmt='INDL' and datafmt='STD' and popsrc='D') and
                      2000< fyear and 2018>fyear
                      group by tic,sich
                      """) 


# In[40]:


funda.shape


# In[41]:


funda=funda[funda['tic'].isin(final.Ticker)]


# In[42]:


funda.shape


# In[43]:


funda.head()


# In[100]:


final1=final.merge(funda,left_on="Ticker",right_on="tic",how="left")


# In[101]:


final1.shape


# In[102]:


final1=final1.drop_duplicates()


# In[103]:


final1.shape


# In[105]:


final1.tail()


# In[133]:


final2=final1.dropna()


# In[134]:


final2.head()


# In[135]:


final2['Date']=pd.to_datetime(final2['Date'])


# In[165]:


final2lag1=final2.copy()


# In[166]:


final2.head()


# In[173]:


from datetime import timedelta
final2lag1["Date"] = final2lag1["Date"] + timedelta(days=1)


# In[ ]:





# In[174]:


final2lag1=final2lag1.rename(columns={'Returns':'Returns_lag1'})


# In[175]:


final2lag1=final2lag1[['Ticker','Date','Returns_lag1']]


# In[176]:


final2lag1.head()


# In[177]:



final2lag=pd.merge(final2,final2lag1,on=['Ticker','Date'])


# In[178]:


final2lag.head()


# In[179]:


final2lag5=final2.copy()
final2lag5["Date"] = final2lag5["Date"] + timedelta(days=5)
final2lag5=final2lag5.rename(columns={'Returns':'Returns_lag5'})
final2lag5=final2lag5[['Ticker','Date','Returns_lag5']]
final2lag5.head()


# In[180]:



final2lag=pd.merge(final2lag,final2lag5,on=['Ticker','Date'])


# In[181]:


final2lag.head()


# In[182]:


final2lag2=final2.copy()
final2lag2["Date"] = final2lag2["Date"] + timedelta(days=2)
final2lag2=final2lag2.rename(columns={'Returns':'Returns_lag2'})
final2lag2=final2lag2[['Ticker','Date','Returns_lag2']]
final2lag2.head()


# In[185]:


final2lag=pd.merge(final2lag,final2lag2,on=['Ticker','Date'])


# In[187]:


final2lag.head()


# In[188]:


final2lead1=final2.copy()
final2lead1["Date"] = final2lead1["Date"] - timedelta(days=1)
final2lead1=final2lead1.rename(columns={'Returns':'Returns_lead1'})
final2lead1=final2lead1[['Ticker','Date','Returns_lead1']]
final2lead1.head()


# In[189]:


final2lag=pd.merge(final2lag,final2lead1,on=['Ticker','Date'])


# In[190]:


final2lag.head()


# In[191]:


final2lead2=final2.copy()
final2lead2["Date"] = final2lead2["Date"] - timedelta(days=2)
final2lead2=final2lead2.rename(columns={'Returns':'Returns_lead2'})
final2lead2=final2lead2[['Ticker','Date','Returns_lead2']]
final2lead2.head()


# In[192]:


final2lag=pd.merge(final2lag,final2lead2,on=['Ticker','Date'])


# In[193]:


final2lag.head()


# In[194]:


final2lead5=final2.copy()
final2lead5["Date"] = final2lead5["Date"] - timedelta(days=5)
final2lead5=final2lead5.rename(columns={'Returns':'Returns_lead5'})
final2lead5=final2lead5[['Ticker','Date','Returns_lead5']]
final2lead5.head()


# In[195]:


final2lag=pd.merge(final2lag,final2lead5,on=['Ticker','Date'])


# In[196]:


final2lag.head()


# In[197]:


#final2lag1.to_csv("leadlag.csv")


# In[ ]:




