# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:04:37 2020

@author: nadine.spormann
"""

num1 = int(input("Please tell me any number that is not zero: "))
num2 = int(input("Please tell me another number that is not zero: "))
if num1 < 0 and num2 > 0:
    print("YES")
elif num1 > 0 and num2 < 0:
    print("YES")
else:
    print("NO")