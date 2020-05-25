#Write a Python program to append a new item to the end of the array

# Once added, print the total length of the array together with the new array

#Original array: array('i', [1, 3, 5, 7, 9])                       

#Sample Output:
#Enter an element to append to the list: 11  # -*- coding: utf-8 -*-

number = int(input("Please enter a number "))
array = [2,4,6,9]
if number not in array:
    array.append(number)    
    print(array)
    print(len(array))
else:
    print("The number already exists.")