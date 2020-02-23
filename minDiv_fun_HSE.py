# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:53:33 2020

@author: mzly903
"""


def MinDivisor(a):
    t = int(a**0.5)
    r = 11
    if a < 100:
        t = a
    if a % 2 == 0:
        print(2)
    elif a % 3 == 0:
        print(3)
    elif a % 5 == 0:
        print(5)
    elif a % 7 == 0:
        print(7)
    else:
        for i in range(11, t+1):
            if a % i == 0:
                print(i)
                r = 11
                break
            else:
                r = 12
        if r == 12:
            print(a)
a = int(input())

MinDivisor(a)
