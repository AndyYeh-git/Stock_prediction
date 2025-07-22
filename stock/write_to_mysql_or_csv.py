# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 12:16:03 2021

@author: User
"""

import requests
import pandas as pd
import os
#from sqlalchemy import create_engine

#engine = create_engine("mysql+pymysql://root:your_password@localhost:port/stock")
url = "https://api.finmindtrade.com/api/v4/data"
pd.set_option("display.max_rows", None, "display.max_columns", None, 'display.max_colwidth', None, 'display.width', 2000)

#dbConnection = engine.connect()

stock_num = list()
with open('stock_num.txt') as f:
    lines = f.readlines()
    for line in lines:
        stock_num.append(line.strip())
      
    
class Stock:
    def __init__(self, *stock_numbers):
        self.stock_numbers = stock_numbers    
    def scrape(self):

        for stock_number in self.stock_numbers:            
            parameter = {
                "dataset": "TaiwanStockPrice",
                "data_id": stock_number,
                "start_date": "2020-01-01",
                "end_date": "2025-07-15",
                "token": "your token here"
            }
            data = requests.get(url, params=parameter)
            data = data.json()
            data = pd.DataFrame(data['data'])            
            
            #data.to_csv(stock_number+'.csv', index=False)
            #data.to_sql(stock_number.lower(), engine, if_exists='append', index= False)            
            
        return data    

#stock = Stock("2303", "2330", "2337")
#stock = Stock("6131")
#stock.scrape()

os.makedirs('stocks', exist_ok=True)
#for i in range(500):
for i in range(1500, len(stock_num)):
    stock = Stock(stock_num[i])
    data = stock.scrape()
    data.to_csv('stocks/'+ stock_num[i] + '.csv', index=False)
#dbConnection.close()
