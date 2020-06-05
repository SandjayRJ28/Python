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

#String formatting
output = "Hallo, " + V_naam + " " + A_naam
output = "Hallo, {} {} ".format(V_naam, A_naam)
output = "Hallo, {0} {1} ".format(V_naam, A_naam)

#Deze formatting is alleen in Python 3 beschikbaar
output = f'Hallo,  {V_naam} {A_naam}'

#String formatting Part 2
V2_naam = "Sandjay"
A2_naam = "Jethoe"
output = "Hallo, " + V2_naam + " " + A2_naam
output2 = "Hallo, {} {} ".format(V2_naam, A2_naam)
output3 = "Hallo, {0}, {1} ".format(V2_naam, A2_naam)
output4 = f'Hallo,  {V2_naam} {A2_naam}'
print(output)
print(output2)
print(output3)
print(output4)