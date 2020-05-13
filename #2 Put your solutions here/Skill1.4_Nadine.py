# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:35:19 2020

@author: nadine.spormann
"""

# 0 — Sunday   --> Index: 3
# 1 — Monday   --> Index: 4
# 2 — Tuesday  --> Index: 5
# 3 — Wednesday--> Index: 6
# 4 — Thursday --> Index: 0
# 5 — Friday   --> Index: 1
# 6 — Saturday --> Index: 2
# January 1 was Thursday

list_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

k = input("Please enter any number between 1 and 365: ")
week_day = int(k) % 7

if week_day == 0:
    print(4)
elif week_day == 1:
    print(5)
elif week_day == 2:
    print(6)
elif week_day == 3:
    print(0)
elif week_day == 4:
    print(1)
elif week_day == 5:
    print(2)
else: 
    print(3)