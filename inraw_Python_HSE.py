# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:08:10 2020

@author: mzly903
"""

b = int(input())
list_ = []
while b != 0:
    list_.append(b)
    b = int(input())
count = 0
list_.append(count)
counts = []
for i in range(1, len(list_)):
    if list_[i] == list_[i-1]:
        count += 1
    else:
        counts.append(count+1)
        count = 0

print(max(counts))
