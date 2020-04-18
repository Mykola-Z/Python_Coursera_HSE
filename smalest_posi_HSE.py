# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:37:38 2020

@author: mzly903
"""

a = list(map(int, input().split()))

t = max(a)

for i in range(len(a)):
    if a[i] > 0 and a[i] < t:
        t = a[i]
print(t)
