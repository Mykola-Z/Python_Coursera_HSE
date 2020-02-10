# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 09:44:45 2020

@author: mzly903
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
f = int(input())

l = [a, b, c]

l_max = max(l)

l.remove(l_max)

bri = [d, f]

if min(bri) >= min(l) and max(bri) >= max(l):
    print('YES')
else:
    print('NO')
