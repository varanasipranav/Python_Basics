# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:03:42 2022

@author: Pranav Varanasi
"""
f1=input("enter the file 1 name")
f2=input("enter the file 2 name")
fr=open(f1,'r+') 
fw=open(f2,'r+') 
fr.write("hello my name is pranav")
for line in fr:
    fw.write(line)
    