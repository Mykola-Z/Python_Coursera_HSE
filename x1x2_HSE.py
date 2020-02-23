# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:50:07 2020

@author: mzly903
"""
a = float(input())
b = float(input())
c = float(input())

dis = b**2 - 4*a*c

if dis < 0:
    h = 1
else:
    x1 = (-b + dis**(0.5))/(2*a)
    x2 = (-b - dis**(0.5))/(2*a)
    if dis == 0:
        print(x1)
    else:
        f = [x1, x2]
        f = sorted(f)
        print(f[0], f[1])
