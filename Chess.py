# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:50:32 2020

@author: mzly903
"""

x = int(input())
y = int(input())
x2 = int(input())
y2 = int(input())

if x-1 <= x2 <= x+1 and y-1 <= y2 <= y+1:
    print('YES')
else:
    print('NO')
