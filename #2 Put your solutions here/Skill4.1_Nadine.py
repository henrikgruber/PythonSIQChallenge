# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:19:08 2020

@author: nadine.spormann
"""

i = [1, 3, 5, 7, 9, 11]
print(i)
del_position = int(input("Which list element (position) would you like to delete? Position: "))
del i[del_position - 1]
print(i)