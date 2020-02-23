# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:58:21 2020

@author: mzly903
"""

a = input()

b = a.find('f')
if b == -1:
    print(-2)
elif a.find('f', b) == -1:
    print(-1)
else:
    print(a.find('f', b+1))
