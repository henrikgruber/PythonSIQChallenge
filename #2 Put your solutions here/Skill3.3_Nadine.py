# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:08:53 2020

@author: nadine.spormann
"""

num1 = int(input("Please tell me any number: "))
num2 = int(input("Please tell me another number: "))
num3 = int(input("Please tell me a third number: "))
if num1 == num2 == num3:
    print(str(3) + " - all numbers are equal")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print(str(2) + " - two numbers are equal")
else:
    print(str(0) + " - all numbers are different")
    