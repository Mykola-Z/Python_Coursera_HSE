# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:18:48 2020

@author: mzly903
"""

n = int(input())
count = 0
for i in range(1, n):

    if str(i) == str(i)[::-1]:

        count = count + 1

print(count)
