# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:23:17 2020

@author: mzly903
"""

n = int(input())
a = [0, 1]

for i in range(2, n+1):
    fibo = a[i-2] + a[i-1]
    a.append(fibo)

print(a[n])
