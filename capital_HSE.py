# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:41:30 2020

@author: mzly903
"""

a = input()

s = a.find('h')
e = a.rfind('h')

text = a[(s+1):e].replace("h", 'H')
print(a[:s+1] + text + a[e:])
