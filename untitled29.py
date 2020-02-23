# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:21:46 2020

@author: mzly903
"""

def val(a, n):
    if n % 2 == 0:
        a = a*a
        return val(a*a, n/2)
    if n % 2 != 0:
        a = a*a
        while ()
        return val(a, n-1)

print(val(1,3))
