# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:22:22 2020

@author: mzly903
"""

a = int(input())
b = int(input())

if a < b:
    for i in range(a, b+1):
        print(i, end=' ')
else:
    for j in range(a, b-1, -1):
        print(j, end=' ')
