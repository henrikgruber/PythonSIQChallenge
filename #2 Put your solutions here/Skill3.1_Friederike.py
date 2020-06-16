#Given the two integers, print the least of them.
#Example input
#3
#7
#Example output
#3


# Read an integer:
# a = int(input())
# Print a value:
# print(a)

a=int(input("Bitte gebe eine ganze positive Zahl ein."))
b=int(input("Bitte gebe eine weitere positive Zahl ein."))

if a < b:
    print(a)
else:
    print(b)