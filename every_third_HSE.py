# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:49:14 2020

@author: mzly903
"""

a = input()

letters = (
    "" if i % 3 == 0 else char
    for i, char in enumerate(a, 0)
)
b = ''.join(letters)
print(b)
