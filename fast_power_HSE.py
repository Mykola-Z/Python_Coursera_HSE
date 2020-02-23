# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:54:38 2020

@author: mzly903
"""
import time

a = float(input())
n = float(input())


def fast_power(a, n):
    if n % 2 == 0:
        a = (a**2)**(n/2)
    else:
        a = a*a**(n-1)
    return a

print(fast_power(a, n))
