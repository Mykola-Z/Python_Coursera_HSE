# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:35:25 2020

@author: mzly903
"""


def sum_sq(a):
    b = 0
    for i in range(a+1):
        b = b + i*i
    print(b)

a = int(input())
sum_sq(a)
