# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 19:59:07 2020

@author: mzly903
"""

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())


a = x1 + y1
b = x2 + y2

if (b % 2 == 0 and a % 2 == 0) or (b % 2 == 1 and a % 2 == 1):

    dif = y2 - y1
    if x1 - dif <= x2 <= x1+dif:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
