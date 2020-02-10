# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:17:55 2020

@author: mzly903
"""

a = int(input())

b = int(input())

c = int(input())
f = 0
li = [a, b, c]
for i in range(0, len(li)):
    if li[i] % 2 == 0:
        for j in range(0, len(li)):
            if li[j] % 2 == 1:
                f = 'ok'
if f == 'ok':
    print('YES')
else:
    print('NO')
