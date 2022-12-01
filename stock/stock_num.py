# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 23:51:19 2021

@author: User
"""

import requests
from bs4 import BeautifulSoup

r = requests.get('https://tw.stock.yahoo.com/h/kimosel.php')

soup = BeautifulSoup(r.text, "lxml")

tables = soup.find_all("table")[3]

tables2 = soup.find_all("table")[5]

tds = tables.find_all(["td"])

tags = tables2.find_all(["a"])
stock_num = list()
for link in tags:
    stock_num.append(link.get('href')[18:22])

names = tuple(td.getText().strip() for td in tds)
stock_types = list()
for i in range(2, 16):
    stock_types.append(names[i])
for i in range(17, 30):
    stock_types.append(names[i])
stock_types.append(names[34])
    
#print(stock_types)
class Stock_types:
    def __init__(self, *stock_types):
        self.stock_types = stock_types
    def scrape_num(self):
        for stock_type in self.stock_types:
            r = requests.get('https://tw.stock.yahoo.com/h/kimosel.php?tse=1&cat='+stock_type+'&form=menu&form_id=stock_id&form_name=stock_name&domain=0')

            soup = BeautifulSoup(r.text, "lxml")

            tables = soup.find_all("table")[5]
            tags = tables.find_all(["a"])
            num = list()
            for link in tags:
                number = link.get('href')[18:23].strip("'")
                num.append(number)
                
            #print(num)
        
        return num
    

for i in range(len(stock_types)):
    stock = Stock_types(stock_types[i])    
    stock_num = stock_num + stock.scrape_num()
    
#print(len(stock_num))
#print(stock_num)
f = open("stock_num.txt", "w")
for line in stock_num:
    f.write(line)
    f.write("\n")
f.close()