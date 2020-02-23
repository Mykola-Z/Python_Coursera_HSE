# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:34:11 2020

@author: mzly903
"""

n = int(input())
m = int(input())

if max(n, m) % min(n, m) != 0:
    t = int(min(m, n)/2)+1
    h = 2
    while(h == 2):
        t -= 1
        if (n % t == 0) and (m % t == 0):
            print(int(n/t), int(m/t))
            h = 1
else:
    print(int(n/min(m, n)), int(m/min(m, n)))
