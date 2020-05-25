#Given the two integers, print the least of them.

a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

if a < b:
    print("The lower number is: ", a)
elif a > b:
    print("The lower number is: ", b)
else:
    print(a, "equals", b)