# This program converts Fahrenheit to Celsius

print("What would you like to convert?")
print("Enter 1 for Fahrenheit to Celsius")
print("Enter 2 for Celsius to Fahrenheit")

choice = int(input())

if choice == 1:
    fahrenheit = input("Please enter the temperature in Fahrenheit:")
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
        print(fahrenheit,"°F equals",round(celsius,2), "°C")
    except ValueError:
        print("Error - you have to enter float number")

elif choice == 2:
    celsius = input("Please enter the temperature in Celsius:")
    try:
        celsius = float(celsius)
        fahrenheit = (celsius * 9/5) + 32
        print(celsius,"°C equals",round(fahrenheit,2), "°F")
    except ValueError:
        print("Error - you have to enter float number")
        
elif choice != 1 or choice != 2:
    print("Please enter 1 or 2, to convert the temperature")