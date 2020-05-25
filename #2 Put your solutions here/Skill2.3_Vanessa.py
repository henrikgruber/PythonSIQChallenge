# Create 3 variables: mystring, myfloat and myint. 
# mystring should contain the word "hello.The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
# Finally, print all 3 variables by checking if mystring equals to "hello" then print it out. You then check if myfloat is really a float number and is equal to 10.0 - then you print it out (if both conditions are satisfied)
# And you do the same for int

mystring = input("Enter the word 'hello': ")

if mystring ==  "hello":
    myfloat = input("Enter the float number 10.0: ")
    try:
        myfloat = float(myfloat)
        if myfloat == 10.0:
            myint = input("Enter the integer number 20: ")
            try:
                myint = int(myint)
                if myint == 20:
                    print(mystring, myfloat, myint)
                else:
                    print("Error - the number you have entered is not equal to 20")
            except ValueError:
                print("Error - the numer you have entered is not an integer")
        else:
            print("Error - the number you have entered is not equal to 10.0")
    except ValueError:
        print("Error - the numer you have entered is not a float")
            

else:
    print("Error - you did not enter the word 'hello'")