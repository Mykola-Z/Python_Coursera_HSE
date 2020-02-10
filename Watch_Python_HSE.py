# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:35:59 2020

@author: mzly903
"""

minute = int(input())

days = minute // (60*24)
hours = (minute - days*(60*24))//60
minutes = (minute - days*(60*24) - hours*60)
print(hours, minutes)
