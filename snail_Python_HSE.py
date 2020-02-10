# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:47:12 2020

@author: mzly903
"""

h = int(input())
up = int(input())
down = int(input())
where = 0
days = 0

while where < h:
    where += up
    if where < h:
        where -= down
    days += 1

print(days)
