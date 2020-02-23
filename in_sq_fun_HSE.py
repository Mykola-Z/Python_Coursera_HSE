# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:50:55 2020

@author: mzly903
"""


def IsPointinSquare(x, y):
    if (x <= 1 and x >= -1):
        if (y <= 1 and y >= -1):
            return True
        else:
            return False
    else:
        return False
x, y = float(input()), float(input())

if IsPointinSquare(x, y):
    print("YES")
else:
    print("No")
