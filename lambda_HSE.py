# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 23:04:23 2020

@author: mzly903
"""

points = [(1, 1),
          (5, 1),
          (10, 10)
          ]

points.sort(key=lambda p:p[0]**2+p[1]**2)
print(*points)

x = [1, 5, 2, 3]

y = list(map(lambda x: x**2, x))

print(*y)

print(' '.join(map(lambda x: str(x**2), range(1, 101))))

def traditionalSqr(x):
    return x**2

lambdaSqr = lambda x: x**2
print(traditionalSqr(3))
print(lambdaSqr(3))