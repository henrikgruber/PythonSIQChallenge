# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:03:13 2020

@author: nadine.spormann
"""


mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: " + mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: " + str(myfloat))
if isinstance(myint, int) and myint == 20:
    print("Integer: " + str(myint))