# write a small program that Converts Fahrenheit to Celsius

# Fahrenheit to Celsius formula:
#(°F - 32) x 5/9 = °C or in plain english, First subtract 32, then multiply by 5,
#then divide by 9.

# Celsius to Fahrenheit formula:
# (°C × 9/5) + 32 = °F or in plain English, Multiple by 9, then divide by 5, then add 32.

inp = input("Please Enter 'F' if you want to convert Fahreinheit to Celcious or 'C' if you want to convert Celcius to Fahreinheit ")

if inp.upper() == "F":
    f = float(input("Please enter Fahreinheit: "))
    c = round((((f - 32)*5)/9), 2)
    print(str(f) + " Fahreinheit are " + str(c) + " Grad Celcius")
         
elif inp.upper() == "C":
    c = float(input("Please enter Grad Celcius: "))
    f = round(((c*9)/5)+32, 2)
    print(str(c) + " Grad Celcisus are " + str(f) + " Fahreinheit")

else:
    print("Please enter C for Celcius or F for Fahreinheit")        
