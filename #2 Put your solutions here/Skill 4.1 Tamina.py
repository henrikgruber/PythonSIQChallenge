#Write a Python program to delete an existing item from the array# -*- coding: utf-8 -*-

array = [2, 8, 10, 12, 14]
#eingabe = int(input())
#array.append (eingabe)
x = input("Please enter the number you want to delete ")


if x in array:
    array.remove(x)
    print(x + " was removed from the array")
    print(array)
else:
    print(x + " is not an element of the array")


