# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 19:18:19 2020

@author: mzly903
"""

n = input()

if 2 <= int(n[-1]) <= 4 and n[-2:] not in ['12', '13', '14']:
    print(n, 'korovy')
elif n[-1] == '1' and n[-2:] != '11':
    print(n, 'korova')
else:
    print(n, 'korov')
