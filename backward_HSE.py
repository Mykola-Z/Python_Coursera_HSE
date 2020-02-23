# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:41:15 2020

@author: mzly903
"""


def a():
    f = int(input())
    if f != 0:
        a()
    print(f)

a()
