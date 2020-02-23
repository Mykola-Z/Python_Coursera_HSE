# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:30:23 2020

@author: mzly903
"""

a = input()

b = a[::-1]

s = a.find('h')
e = -b.find('h')

print(a[:s+1]+a[(s+1):(e-1)]+a[(s+1):(e-1)]+a[(e-1):])
