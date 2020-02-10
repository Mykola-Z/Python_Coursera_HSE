# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:16:55 2020

@author: mzly903
"""

secs = int(input())

days = secs//(60*60*24)
hours = (secs - days*(60*60*24))//(60*60)
minutes = (secs - days*(60*60*24) - hours*60*60)//(60)
sec = secs - days*(60*60*24) - hours*60*60 - minutes*60

if len(str(sec)) == 1:
    sec = '0' + str(sec)
if len(str(minutes)) == 1:
    minutes = '0' + str(minutes)
print(hours, minutes, sec, sep=':')
