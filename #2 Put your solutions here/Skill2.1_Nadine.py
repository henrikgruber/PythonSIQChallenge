# -*- coding: utf-8 -*-
"""
Created on Thu May 14 08:48:26 2020

@author: nadine.spormann
"""

try:
    number = float(input("Please enter any number: "))   
    if number < 100:
        print("Your number is smaller than 100")
    elif number > 100:
        print("Your number is higher than 100")
    elif number == 100:
        print("Your number is equal to 100")
except ValueError:
    print("Error - you have to enter float number")
    