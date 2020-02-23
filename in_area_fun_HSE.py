# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:28:27 2020

@author: mzly903
"""
a = float(input())
b = float(input())


def IsPointInArea(x, y):
    all_points = (x+1)**2 + (y-1)**2
    if y < 0 and all_points >= 4 and x <= -y and x >= 0.5*y - 1:
        print("YES")
    elif y > 0 and all_points <= 4 and x >= -y and x <= 0.5*y - 1:
        print("YES")
    else:
        print("NO")

IsPointInArea(a, b)
