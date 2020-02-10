# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:24:54 2020

@author: mzly903
"""
a = int(input())

if (a % 4 == 0 and a % 100 != 0) or (a % 4 == 0 and a % 400 == 0):
    print('YES')
else:
    print('NO')
