# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:35:44 2020

@author: mzly903
"""

def isprime(a):
    if a == 2 or a == 3: return True
    if a < 2 or a%2 == 0: return False
    if a < 9: return True
    if a%3 == 0: return False
    i = 5
    while a**(0.5) >= i:
        if (a % i == 0 or a % (i + 2) == 0) : 
            return False
        i = i + 6
highest_prime_palindrome = 2
for j in range(10000, 100000):
    j += 1
    for g in range(10000, 100000):
        g += 1
        if isprime(g) and isprime(j):
            primes = g*j
            if primes > highest_prime_palindrome and str(primes) == str(primes)[::-1]:
                highest_prime_palindrome = primes

print(highest_prime_palindrome)