# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:35:28 2022

@author: Pranav Varanasi
"""


def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

res=recur_factorial(5)
print(res)