# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:23:17 2020

@author: nadine.spormann
"""

degree_F = float(input("Please enter the current temperature in Fahrenheit: "))
degree_C = ((degree_F - 32) * 5) /9
print("This corresponds to a temperature of " + str(degree_C) + " degrees Celcius")

degree_C = float(input("Please enter the current temperature in Celsius: "))
degree_F = ((degree_C * 9) / 5) + 32
print("This corresponds to a temperature of " + str(degree_F) + " degrees Fahrenheit")
