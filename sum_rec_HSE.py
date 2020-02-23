# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:43:05 2020

@author: mzly903
"""
a = int(input())
b = int(input())


def sumy(a, b):
    a += 1
    if b != 0:
        b -= 1
        sumy(a, b)
    else:
        print(a-1)

sumy(a, b)
