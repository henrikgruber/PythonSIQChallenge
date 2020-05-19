# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:13:42 2020

@author: nadine.spormann
"""

i = [1, 3, 5, 7, 9]
appendix = int(input("Please enter an element to append to the list: "))
i.append(appendix)
print(i)
print("The new array length is " + str(len(i)))