#Given two non-zero integers, print "YES" if exactly one of them is positive and print "NO" otherwise.# -*- coding: utf-8 -*-

x = int( input ("Please enter a number: "))
y = int (input  ("Please enter another number: "))
if (x > 0) and (y < 0):
    print ("YES")
elif (x < 0) and (y > 0):
    print ("YES")
else: 
    print ('No')
    