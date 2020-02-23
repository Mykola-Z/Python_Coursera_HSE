# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:03:40 2020

@author: mzly903
"""

x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())


def IsPointInCircle(x, y, xc, yc, r):

    all_points = (x-xc)**2 + (y-yc)**2
    return (all_points <= r**2)

if IsPointInCircle(x, y, xc, yc, r):
    print("YES")
else:
    print("NO")
