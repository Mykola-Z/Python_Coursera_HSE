# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:13:38 2020

@author: mzly903
"""


def au():
    a = int(input())
    if a == 0:
        return 0
    return a + au()
print(au())
