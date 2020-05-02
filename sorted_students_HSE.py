# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 23:55:27 2020

@author: mzly903
"""

file = open('input.txt', 'r', encoding='utf8')
p = []
i = 0
for student in file:
    data = list(student.strip().split(' '))
    p.append((data[0], data[1], data[3]))
p = sorted(p)
fout = open('output.txt', 'w', encoding='utf8')
for i in range(len(p)):
    write = p[i][0] + ' ' + p[i][1] + ' ' + p[i][2]
    print(write, file=fout)
fout.close()
