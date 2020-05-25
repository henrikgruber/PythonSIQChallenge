# This program finds the number of day of week for K-th day of year

print("Enter the day of the year:")
K = int(input())

a = (K % 7) + 3


if a == 0:
    print("This day is a Sunday")

if a == 1:
     print("This day is a Monday")
     
if a == 2:
     print("This day is a Tuesday")     
     
if a == 3:
     print("This day is a Wednesday")
     
if a == 4:
     print("This day is a Thursday")

if a == 5:
     print("This day is a Friday")
     
if a == 6:
     print("This day is a Saturday")
     
     