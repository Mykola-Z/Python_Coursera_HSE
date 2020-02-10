# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 20:21:44 2020

@author: mzly903
"""

b = int(input())
list_ = []
while b != 0:
    list_.append(b)
    b = int(input())

loc_max = []

for i in range(1, len(list_)-1):
    if list_[i] > list_[i-1] and list_[i] > list_[i+1]:
        loc_max.append(i)
dist = []
if len(loc_max) >= 2:
    for j in range(1, len(loc_max)):
        add = loc_max[j] - loc_max[j-1]
        dist.append(add)
    print(min(dist))
else:
    print('0')
