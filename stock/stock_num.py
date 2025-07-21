# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 23:51:19 2021

@author: User
"""

import twstock

stocks = twstock.codes
print("Total stocks:", len(stocks))

f = open("stock_num.txt", "w")

codes = 0
for code in sorted(stocks):
    if len(code) <= 5:
        print(code, stocks[code].name)
        codes += 1
        f.write(code)
        f.write("\n")
#     print(code, stocks[code].name)

print("Total codes:", codes)

f.close()