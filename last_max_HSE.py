# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:50:36 2020

@author: mzly903
"""

b = []
for i in range(5):
    a = int(input())
    b.append(a)

flip = b[::-1]
i = 0
elem = -1000
while elem != max(b):
    elem = flip[i]
    i += 1
print(ma, 6 - i)
