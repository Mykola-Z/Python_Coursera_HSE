# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:37:19 2020

@author: mzly903
"""

n = int(input())
t = 0
for i in range(n):
    a = int(input())
    if a == 0:
        t += 1
print(t)
