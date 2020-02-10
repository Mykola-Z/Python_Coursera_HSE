# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:53:33 2020

@author: mzly903
"""
matches = []

len_mat = []

all_points = []

lefts = []

rights = []
for i in range(3):
    l = int(input())
    r = int(input())
    matches.append(l)
    matches.append(r)
    lefts.append(l)
    rights.append(r)
    for j in range(l, r):
        all_points.append(j)

x = {1: [lefts[0], rights[0]]}

x[2] = [lefts[1], rights[1]]
x[3] = [lefts[2], rights[2]]

x = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

keys = []
indexes = []
for t in list(x)[0:3]:
    indexes.append(x[t])
    keys.append(t)

all_points = list(set(all_points))

min_value = min(all_points)
max_value = max(all_points)

check = 0
for t in range(min_value, max_value + 1):
    if t not in all_points:

        check = 1


if check == 0:
    print(check)
else:

    cond1 = False
    cond2 = False
    if indexes[1][1]+indexes[0][1] - indexes[0][0] >= indexes[2][0]:
        cond1 = True
    if indexes[0][1]+indexes[2][1] - indexes[2][0] >= indexes[1][0]:
        cond2 = True
    if (cond1 and cond2):
        print(min([keys[0], keys[2]]))
    elif cond1:
        print(keys[0])
    elif cond2:
        print(keys[2])
    else:
        print(-1)
