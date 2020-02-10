# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 19:11:30 2020

@author: mzly903
"""

n = int(input())
m = int(input())
k = int(input())

if (k % m == 0 or k % n == 0) and (k <= m*n):
    print('YES')
else:
    print('NO')
