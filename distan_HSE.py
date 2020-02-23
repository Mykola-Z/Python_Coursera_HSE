# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:30:10 2020

@author: mzly903
"""


def length(x1, y1, x2, y2):
    dist = ((x1-x2)**2+(y1-y2)**2)**0.5
    return dist

x1, y1 = float(input()), float(input())

x2, y2 = float(input()), float(input())

print(length(x1, y1, x2, y2))
