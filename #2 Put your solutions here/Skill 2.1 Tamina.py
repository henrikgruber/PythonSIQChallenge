# write a program that reads a float numbers and then you check if the number is < 100 - if yes, you print "Your number is smaller than 100" - otherwise, you print is higher than 100
# in addition, try to check if someone enters non-numeric character - display an error message
# example: input: 10.7 
# output: Your number is smaller 100
# example: input: abc
# output: Error - you have to enter float number


a = input ("Enter a number: ")
try:
    val = int(a)
    if a <= 100:
        print ("Your number is smaller than! 100")
    else:
        print ("Your number is higher than 100")
except ValueError:
    try:
        val = float(a)
        print("Input is a float  number. Please enter an integer. Number = ", val)
    except ValueError:
        print("You have to enter a number.")
