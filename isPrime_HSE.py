# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:22:22 2020

@author: mzly903
"""


def isPrime(a):
    t = int(a**0.5)

    r = 11
    if a < 100:
        t = a-2
    if a == 2 or a == 3 or a == 5 or a == 7:
        print("YES")
    elif a % 2 == 0 or a % 3 == 0 or a % 5 == 0 or a % 7 == 0:
        print("NO")
    else:
        for i in range(7, t+1, 2):
            if a % i == 0:
                print("NO")
                r = 11
                break
            else:
                r = 12
        if r == 12:
            print("YES")
k = int(input())
isPrime(k)
