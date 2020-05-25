#Given two non-zero integers, print "YES" if exactly one of them is positive and print "NO" otherwise.

a = int(input("Enter an integer that does not equal 0: "))
b = int(input("Enter another integer that does not equal 0: "))

if a == 0 or b ==0:
    print("You are not allowed to enter 0")
elif a > 0 and b > 0:
    print("NO")
elif a < 0 and b < 0:
    print("NO")
else:
    print("YES")