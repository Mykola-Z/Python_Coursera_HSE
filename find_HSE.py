# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:04:32 2020

@author: mzly903
"""

a = input()
b = []
i = 0

while a.find('f', i) != -1:
    b.append(a.find('f', i))
    i += 1

b = set(b)
b = list(b)
if len(b) == 1:
    print(b[0])
elif len(b) > 1:
    print(b[0], b[-1])
