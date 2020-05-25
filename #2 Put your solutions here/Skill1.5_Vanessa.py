#Given a positive real number, print its first digit to the right of the decimal point

print("Enter the a decimal number")
a = float(input())

b = int((a*10) % 10)

print("The first decimal number is:", b)

