# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:57:27 2020

@author: mzly903
"""
a = float(input())
n = int(input())


def power(a, n):
    t = 1
    if n == 0:
        return t
    if a == 0:
        return 0
    i = 1
    if n >= 0:
        while(i <= n):
            t = t*a
            i += 1
    else:
        n = -n
        while(i <= n):
            t = t*(1/a)
            i += 1
        
    return t
print(power(a, n))
