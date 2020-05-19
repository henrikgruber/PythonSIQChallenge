# -*- coding: utf-8 -*-
"""
Created on Thu May 14 08:48:26 2020

@author: nadine.spormann
"""

number = float(input("Please enter any positive real number: "))
import math
first_after_dot = math.floor((number * 10) % 10)
print(first_after_dot)