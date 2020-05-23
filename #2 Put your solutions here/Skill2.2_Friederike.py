# write a small program that Converts Fahrenheit to Celsius

# Fahrenheit to Celsius formula:
#(°F - 32) x 5/9 = °C or in plain english, First subtract 32, then multiply by 5,
#then divide by 9.

# Celsius to Fahrenheit formula:
# (°C × 9/5) + 32 = °F or in plain English, Multiple by 9, then divide by 5, then add 32.

FinC=input("Möchtest du Fahrenheit in Celsius umrechnen?")
if FinC == "Ja":
    Fahrenheit= float(input("Sag mir die Gradzahl in Fahrenheit:"))
    FinCelsius= ((Fahrenheit-32)* 5/9)
    print("Das sind", FinCelsius, "Grad in Celsius.")
elif FinC == "Nein":
    CinF= input('Möchtest du Celsius in Fahrenheit umrechen?')
    if CinF == "Ja":
        Celsius= float(input("Sag mir die Gradzahl in Celsius:"))
        CinFahrenheit= ((Celsius* 9/5)+32)
        print("Das sind", CinFahrenheit, "Grad in Fahrenheit.")
    elif CinF == "Nein":
        print("Dann kann man dir auch nicht helfen!")


