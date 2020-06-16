#Given three integers. Determine how many of them are equal to each other. The program must print one of the numbers: 3 (if all are same), 2 (if two of them are equal to each other and the third one is different) or 0 (if all numbers are different).

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a == b and a == c:
    print("3 - all numbers are the same")
    
elif a != b and a != c and b != c:
    print("1 - all numbers are different")
    
else:
    print("2 - two numbers are equal")