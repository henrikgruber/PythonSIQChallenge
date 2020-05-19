# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:44:00 2020

@author: nadine.spormann
"""

mystring = "Hello"
myfloat = 10.0
myint = 20

# Check mystring:
if mystring == "Hello":
    print(mystring)
else:
    print("Variable mystring does not contain \"Hello\"")
    
# Check myfloat:
if isinstance(myfloat, float) and myfloat == 10.0:
    print(myfloat)
else:
    print("Variable myfloat is not a float or not 10.0")
    
# Check myint:
if isinstance(myint, int) and myint == 20:
    print(myint)
else:
    print("Variable myint is not an int or not 20")
    