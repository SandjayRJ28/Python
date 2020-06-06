#Nummers kan opgeslagen worden in variabelen
pi = 3,14159
print(pi)

#Met Python kan je ook rekenen
Eerste_nummer = 9
Tweede_nummer = 5
print(Eerste_nummer + Tweede_nummer)
print(Eerste_nummer - Tweede_nummer)
print(Eerste_nummer * Tweede_nummer)
print(Eerste_nummer / Tweede_nummer)
print(Eerste_nummer ** Tweede_nummer)

#Om een number uit te laten printen moet je eerst converten naar een string
dagen_in_juni = 30
print(str(dagen_in_juni) + " dagen in Juni")

#Nummers kunnen opslagen worden als strings. Nummers die opgeslagen worden als strings worden ook gezien als een string
Derde_nummer =  "2"
Vierde_nummer = "6"
print(Derde_nummer + Vierde_nummer)

#Input funtie zal altijd een string terug geven
Vijfde_nummer = input("Voer hier uw eerste nummer in")
Zesde_nummer = input("Voer hier uw tweede nummer in")
print(Vijfde_nummer + Zesde_nummer)

#Een string die nummers bevat moet eerst convert worden naar nummers voordat je gaat rekenen
Zevende_nummer = input("Voer hier uw eerste nummer in")
Achste_nummer = input("Voer hier uw tweede nummer in")
print(int(Zevende_nummer) + int(Achste_nummer))
print(float(Zevende_nummer) + float(Achste_nummer))