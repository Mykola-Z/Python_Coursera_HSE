# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:26:57 2020

@author: mzly903
"""

a = int(input())

for i in range(10**(a)-1, 10**(a-1)-1, -2):
    print(i, end=" ")
