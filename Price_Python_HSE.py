# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:49:11 2020

@author: mzly903
"""

uah = int(input())
kop = int(input())
n = int(input())

price_uah = n*uah + (n*kop) // 100
price_kop = (n*kop) % 100
print(price_uah, price_kop)
