# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:56:14 2020

@author: mzly903
"""

a = abs(int(input()))

b = abs(int(input()))

c = abs(int(input()))

triang = [a, b, c]

hipo = max(triang)

check = 0
i = 0
sides = triang
while check != hipo:

    check = triang[i]

    if check == hipo:
        del sides[i]
    i = i+1

condition = (sides[0]**2+sides[1]**2)

if hipo > sum(sides) and :
    print('impossible')
elif hipo > condition**2:
    print('impossible')
elif hipo < condition**2:
    print('impossible')
else:
    print('rectangular')
