# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:57:32 2020

@author: mzly903
"""


def IsPointinSquare(x, y):
    if (abs(x)+abs(y) <= 1):
        return True
    else:
        return False
x, y = float(input()), float(input())

if IsPointinSquare(x, y):
    print("YES")
else:
    print("No")
