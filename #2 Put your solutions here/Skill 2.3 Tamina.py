# Create 3 variables: mystring, myfloat and myint. 
# mystring should contain the word "hello.The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
# Finally, print all 3 variables by checking if mystring equals to "hello" then print it out. You then check if myfloat is really a float number and is equal to 10.0 - then you print it out (if both conditions are satisfied)
# And you do the same for int

mystring = input ("Please enter a string ")
myfloat = input ("please enter a float number ")
myint = input ("Please enter an integer ")

try:
    val = str(mystring)
    if mystring == "Hello":
        print (mystring)
        break;
    else:
        print ("Error")

