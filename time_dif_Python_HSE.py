# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:31:58 2020

@author: mzly903
"""

h1 = int(input())
m1 = int(input())
s1 = int(input())

h2 = int(input())
m2 = int(input())
s2 = int(input())


sec = s2-s1
minutes = (m2-m1)*60
hours = (h2-h1)*60*60

secs = hours + minutes + sec

print(secs)
