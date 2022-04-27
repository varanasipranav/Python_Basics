# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:27:44 2022

@author: Pranav Varanasi
"""

l=int(input("enter the lower bound"))
u=int(input("enter the upper bound"))
u=20
for num in range (l,u+1,1):
    for i in range(2,num):
        if num%i==0:
            break
    else:
         print(num)