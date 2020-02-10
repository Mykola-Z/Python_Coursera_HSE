# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:44:42 2020

@author: mzly903
"""

times = int(input('Enter '))

first = '   _~_    '
second = '  (o o)    ' 
third = ' /  V  \   '
fourth = '/(  _  )\   '
fifth = '  ^^ ^^   ' 


print(first[0:10]*times, second[:10]*times, third[:10]*times, fourth[:10]*times, fifth[:10]*times, sep = ' \n')
