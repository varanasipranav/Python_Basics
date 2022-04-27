# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 14:27:11 2022

@author: Pranav Varanasi
"""

t1=0
t2=1
n=int(input("enter the number"))
while n>0:
    t3=t1+t2;
    t1=t2
    t2=t3
    print(t3)
    n=n-1

    
    