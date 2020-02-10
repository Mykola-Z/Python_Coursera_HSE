# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:49:54 2020

@author: mzly903
"""

a = int(input())

b = int(input())

c = int(input())
l = [a, b, c]

if len(set(l)) == len(l):
    print('0')
elif len(set(l)) == 2:
    print('2')
else:
    print('3')
