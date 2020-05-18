# Aufgabe 1.4 17.05


k=input("Sage mir für den wievielten Tag des Jahres ich dir den Wochentag nennen soll?")
Wochentagzahl= (int(k) + int(3)) %7

if Wochentagzahl == 1:
    print("Montag")

elif Wochentagzahl == 2:
    print("Dienstag")

elif Wochentagzahl == 0:
    print("Sonntag")

elif Wochentagzahl == 4:
    print("Donnerstag")

elif Wochentagzahl == 5:
    print("Freitag")

elif Wochentagzahl == 6:
    print("Samstag")

elif Wochentagzahl == 3:
    print("Mittwoch")
