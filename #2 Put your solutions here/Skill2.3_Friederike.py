# Create 3 variables: mystring, myfloat and myint.
# mystring should contain the word "hello.The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
# Finally, print all 3 variables by checking if mystring equals to "hello" then print it out. You then check if myfloat is really a float number and is equal to 10.0 - then you print it out (if both conditions are satisfied)
# And you do the same for int

mystring = "Hello"
myfloat= "string"
myint= 20

# mystring
if (type(mystring) is str) == True:
    print(mystring)
elif (type(mystring) is str) != True:
    print("No string")

# myfloat
if (type(myfloat)is float) == True:
    print(myfloat)
elif (type(myfloat)) != True:
    print("No float")

#myint
if (type(myint)is int) == True:
    print(myint)
elif (type(myint)is int) != True:
    print("No int")