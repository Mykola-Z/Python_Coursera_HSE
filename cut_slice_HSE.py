# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:21:44 2020

@author: mzly903
"""

a = input()

b = a[::-1]

s = a.find('h')
e = b.find('h')

if len(a) != len(a[:s]+a[-e:len(a)]):
    print((a[:s]+a[-e:len(a)]))
