# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:44:54 2020

@author: mzly903
"""
a = int(input())
b = list(map(int, input().split()))
x = int(input())
l = b[0]
k = abs(x-b[0])
for i in range(len(b)):
    if abs(x-b[i]) < k:
        k = abs(x-b[i])
        l = b[i]
print(l)
