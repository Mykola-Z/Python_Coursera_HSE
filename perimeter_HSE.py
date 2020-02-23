# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:37:52 2020

@author: mzly903
"""

c = []
for i in range(6):
    a = float(input())
    c.append(a)


def length(x1, y1, x2, y2):
    dist = ((x1-x2)**2+(y1-y2)**2)**0.5
    return dist

f = length(c[0], c[1], c[2], c[3])
s = length(c[2], c[3], c[4], c[5])
t = length(c[0], c[1], c[4], c[5])

print(f+s+t)
