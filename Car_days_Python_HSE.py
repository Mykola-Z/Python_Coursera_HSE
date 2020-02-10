# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:37:53 2020

@author: mzly903
"""

day_km = int(input())

m = int(input())

print(int(m/day_km) + (m % day_km > 0))
