# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:45:32 2020

@author: mzly903
"""

a = int(input())

b = int(a**0.5)

c = int((a-b*b)**0.5)


d = int((a-b*b-c*c)**0.5)

e = int((a-b*b-c*c-d*d)**0.5)

ans = [b, c, d, e]

for i in range(len(ans)):
    if ans[i] != 0:
        print(ans[i])
