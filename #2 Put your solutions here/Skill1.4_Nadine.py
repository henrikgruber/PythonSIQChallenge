# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:35:19 2020

@author: nadine.spormann
"""

# 0 — Sunday   --> Rest: 3
# 1 — Monday   --> Rest: 4
# 2 — Tuesday  --> Rest: 5
# 3 — Wednesday--> Rest: 6
# 4 — Thursday --> Rest: 0
# 5 — Friday   --> Rest: 1
# 6 — Saturday --> Rest: 2
# January 1 was Thursday

list_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

k = input("Please enter any number between 1 and 365: ")
week_day = (int(k) % 7) - 1

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
