#Variablen defineren gaat heel makkelijk heeft het een naam en waarde het its done
Voor_naam = "Sandjay"
print(Voor_naam)

#Je kan stringe combineren met +
Achter_naam = "Jethoe"
print(Voor_naam + Achter_naam)
print("Hallo" + Voor_naam + "" + Achter_naam)

#Je kan functies gebruiken om je string aan te passen
zin = "Ik kan eindelijke een beetje Pyhton"
print(zin.upper())
print(zin.lower())
print(zin.capitalize())
print(zin.count("a"))

#De functies helpen on om de tekste een opmaak te geven om het op te slaan naar bestanden,Databases of om aan gebruikers te laten zien.
print("Hallo" + Voor_naam.capitalize() + " \n" + Achter_naam.capitalize())

#verschillende string oefeningen met tab voor autocomplete
print(Voor_naam + Achter_naam)
print("Hallo, " + Voor_naam + " " + Achter_naam)

#input geven via de console
V_naam = input("Vul hier jou naam is ")
A_naam = input("Vul hier jou Achternaam in ")
print("Hallo, " + V_naam.capitalize() + " " + A_naam.capitalize())