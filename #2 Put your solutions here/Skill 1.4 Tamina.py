# -*- coding: utf-8 -*-
# Days of week are numbered as: 0 — Sunday, 1 — Monday, 2 — Tuesday, ..., 6 — Saturday. An integer K in the range 1 to 365 is given. Find the number of day of week for K-th day of year provided that in this year January 1 was Thursday.

day = int(input("Please enter a number "))
rest = int(0)
week = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]

if day in range(365):
    rest = day % 7
    print (week[rest])
else:
    print ("Number out of range. Enter da number between 1-365")
    
    



