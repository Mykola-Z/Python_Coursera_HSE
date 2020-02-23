# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:49:37 2020

@author: mzly903
"""

for i in range(10, 100):
    first = str(i)[0]
    sec = str(i)[1]
    if i == 2*int(first)*int(sec):
        print(i)
