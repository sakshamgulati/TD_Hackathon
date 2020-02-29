# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:42:29 2020

@author: Karan Babariya
"""

import os, json
import pandas as pd
from datetime import datetime

path_to_json = 'E:/TD -Rise of Data/hackathon_data/hackathon_data/company_transcripts'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
print(json_files)  # for me this prints ['foo.json']


call_df = pd.DataFrame()
calls_list = []
# we need both the json and an index number so use enumerate()
for index, js in enumerate(json_files):
    ticker = js.strip('.json')
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        for call_id in json_text['title'].keys():
            call_body = ' | '.join(map(str, json_text['body'][call_id]))
            call_date = datetime.utcfromtimestamp(
                    json_text['date'][call_id]/1000).strftime(
                            "%A, %B %d, %R")
            calls_list.append([ticker, call_id, 
                                           json_text['title'][call_id], 
                                           call_date,
                                           call_body])

blob = pd.DataFrame(calls_list, 
                    columns=['ticker', 'call_id', 'title', 'date', 'body'])

