from datetime import datetime

#Functie om de huidige datum en tijd te printen
def print_tijd(taak_naam):
    print(taak_naam)
    print(datetime.now())
    print()

#funtie oefeningen: Timestamps printen om te kijken hoe lang het duur op een sectie van je code te laten draaien

voornaam = "Sandjay"
print_tijd("voornaam geprint ")

for x in range(0,10):
        print(x)
print_tijd("loop is klaar ")


#funtie krijg initialen
def krijg_initiaal(naam):
    initiaal = naam[0:1].upper()
    return initiaal

#iemand zijn naam vragen en initialen weergeven
voornaam = input("Voor je voornaam in: ")
voornaam_initiaal = krijg_initiaal(voornaam)

tussenvoegsel = input("Wat is je tussenvoegsel: ")
tussenvoegsel_initiaal = krijg_initiaal(tussenvoegsel)

achternaam = input("Wat is je achternaam: ")
achternaam_initiaal = krijg_initiaal(achternaam)

print("Je initialen zijn: " + voornaam_initiaal + tussenvoegsel_initiaal + achternaam_initiaal)


#funtie krijg initialen
def krijg_initiaal1(naam1, force_hoofdletter=True):
    if force_hoofdletter:
        initiaal1 = naam1[0:1].upper()
    else:
        intiaal1 = naam1[0:1]
    return initiaal1

#iemand zijn naam vragen en initialen weergeven via naam notaties
voornaam1 = input("Voor je voornaam in: ")
voornaam_initiaal1 = krijg_initiaal1(force_hoofdletter=False, naam1=voornaam1)

print("Je initialen zijn: " + voornaam_initiaal)