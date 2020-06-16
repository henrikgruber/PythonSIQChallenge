# write a program that reads a float numbers and then you check if the number is < 100 - if yes, you print "Your number is smaller than 100" - otherwise, you print is higher than 100
# in addition, try to check if someone enters non-numeric character - display an error message
# example: input: 10.7
# output: Your number is smaller 100
# example: input: abc
# output: Error - you have to enter float number


try:
    number = float(input("Bitte gebe eine beliebge Zahl ein."))

    if number < 100:
        print("Deine Zahl ist kleiner als 100")
    elif number > 100:
        print("Deine Zahl ist größer als 100")
    elif number == 100:
        print("Deine Zahl ist 100")

except ValueError:\
    print("Dies ist keine Zahl!")








