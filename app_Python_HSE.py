# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:57:35 2020

@author: mzly903
"""

x = int(input())
y = int(input())

dif = y - x + 1

if (x-1) % dif == 0 and y % dif == 0:
    print('YES')
else:
    print('NO')
