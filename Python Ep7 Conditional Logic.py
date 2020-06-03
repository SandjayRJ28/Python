#Het is nodig om je code een skill te geven om andere acties te nemen gebasseerd op conditions
prijs = 5
if prijs >= 0.50:
       belasting = .05
       print(belasting)
else:
        tax = 0
        print(belasting)

#andere manier van conditioneel schrijven
prijs1 = 6
if prijs1 >= 3.00:
        belasting2 = 29.00
else:
        belasting2 = 1.00
print(belasting2)

#Pas op als je strings gaat vergelijken omdat ze het letterlijk overneme maar als je een ectra string functie erbij plaats
land = "NEDERLAND"
if land.lower() == "nederland":
      print("Hey je bent een Nederlander")
else:
      print("Je bent niet van Nederland")

#Oefening 1 Condionteel IF statements
verkoopprijs = input("Wat heb je voor dit product betaald ")

verkoopprijs = float(verkoopprijs)
if verkoopprijs >= 2.00:
        BTW = .20
else:
        BTW = 0
print("De BTW waarde is: " + str(BTW))

#oefening 2 If statements
herkomst = input("Voer in de land van herkomst: ")
if herkomst.lower() == "nederland":
    print("Je houd vast wel van games :smugface:")
else:
    print("Hey je komt ook niet uit Nederland!")

#Meerdere condities in een IF statement Oefening
Provincie = input("In welke Provincie woon je? ")
BTW1 = 0

if Provincie == "Noord-Brabant":
    BTW1 = 50
elif Provincie == "Drenthe":
    BTW1 = 50
elif Provincie == "Gelderland":
    BTW1 = 20
else:
    BTW = 0
print(BTW1)

#If statement met een OR
Provincie1 = input("In welke Provincie woon je? ")
BTW2 = 0
if Provincie1 == "Noord-Brabant" or Provincie == "Drenthe":
    BTW2 = 50
elif Provincie1 == "Gelderland":
    BTW2 = 20
else:
    BTW2 = 0
print(BTW2)

#If statement met een (IN) om in een list te kijken om te vergelijken
Provincie2 = input("In welke Provincie woon je? ")
BTW3 = 0

if Provincie2 in("Noord-Brabant", "Drenthe", "Zeeland"):
    BTW3 = 50
elif Provincie2 == "Gelderland":
    BTW3 = 20
else:
    BTW3 = 0
print(BTW3)

#Nested If statement oefening
Land3 = input("Welke land kom je vandaan? ")
BTW3 = 0

if Land3.lower() == "Nederland":
    Provincie2 = input("In welke Provincie woon je? ")
    if Provincie3 in("Noord-Brabant",  "Drenthe", "Zeeland"):
        BTW4 = 50
    elif Provincie3 == "Gelderland":
        BTW4 = 20
    else:
        BTW4 = 0
else:
    BTW4 = 0
print(BTW4)