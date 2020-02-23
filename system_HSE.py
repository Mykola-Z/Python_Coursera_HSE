# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:06:02 2020

@author: mzly903
"""

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if a != 0 and (d - c*b/a) != 0:
    y = (f - c*e/a)/(d - c*b/a)
    x = (e - b*y)/a

elif b != 0 and d != 0 and (c - d*a/b) != 0:
    x = (f - d*c)/(c - d*a/b)
    y = (f - c*x)/d
elif (b - d*a) != 0 and c != 0:
    y = (e - a*f/c) / (b - d*a)
    x = (f - d*y)/c
else:
    y = (e*c-a*f) / (c*b - a*d)
    x = (e - b*y) / a
print(x, y)
