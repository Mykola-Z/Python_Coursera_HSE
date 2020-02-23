# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:45:14 2020

@author: mzly903
"""


def xor(x, y):
    f = x + y
    if f == 1:
        print(1)
    else:
        print(0)
x, y = int(input()), int(input())
xor(x, y)
