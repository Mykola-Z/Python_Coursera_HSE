# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:05:40 2020

@author: mzly903
"""

t = 0
def only_sq(t):
    a = int(input())
    t = 0
    if a != 0:
        t += 1
        only_sq(t)
    if int(a**0.5)*a**0.5 == a and a != 0:
        r = 3
        print(a)
    if t != 1:
        print(t)
only_sq(t)
