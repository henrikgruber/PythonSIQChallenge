# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:53:54 2020

@author: nadine.spormann
"""

num1 = int(input("Please tell me any number: "))
num2 = int(input("Please tell me another number: "))
if num1 < num2:
    print("The number " + str(num1) + " is the least one")
elif num1 > num2:
    print("The number " + str(num2) + " is the least one")
else:
    print("The two given numbers are equal")

