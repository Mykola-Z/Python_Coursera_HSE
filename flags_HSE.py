# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:14:12 2020

@author: mzly903
"""

n = int(input())

top = "+___ " * n
mid = "|1 / "
thr = "|__\ " * n
fort = "|    " * n

for i in range(2, n+1):
    mid = mid + "|" + str(i) + r" / "

print(top, mid, thr, fort, sep="\n")
