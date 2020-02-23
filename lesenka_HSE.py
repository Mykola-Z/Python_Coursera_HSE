# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:40:29 2020

@author: mzly903
"""

n = int(input())
for i in range(1, n+1):
    t = ''
    for j in range(1, i+1):
        t += str(j)
    print(t)
